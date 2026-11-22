"""Grava a triagem de título/resumo em literature/processed/triagem_estudos.xlsx.

Entradas:
  - literature/processed/registros_unicos.jsonl      (de consolidar_wos.py)
  - literature/processed/wos_consolidado.xlsx        (origens por consulta)
  - literature/processed/decisoes_titulo_resumo.csv  (uma linha por registro elegível lido)

Registros barrados pelos filtros do protocolo (tipo, idioma, período) entram como excluídos
com o motivo E1/E2/E3. Os demais recebem a decisão registrada no CSV.

Uso: python literature/scripts/aplicar_triagem.py
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd
from openpyxl import load_workbook

PROC = Path(__file__).resolve().parents[1] / "processed"
DATA_BUSCA = "2026-11-18"
REVISOR = "Claude (IA), duas leituras; conferência humana por amostra pendente"

MOTIVOS = {
    "E4": "E4 artigo retratado",
    "M1": "M1 fora do domínio (sem crédito/PD nem contribuição metodológica geral)",
    "M2": "M2 crédito sem pertinência aos eixos da revisão",
    "M3": "M3 contábil/regulatório sem modelagem ou estimação de PD/ECL",
    "M4": "M4 aplicação de outro domínio sem contribuição metodológica transferível",
    "M5": "M5 somente fraude, seguros ou outro risco não creditício",
    "M6": "M6 informação insuficiente e sem indício de pertinência",
    "M7": "M7 segunda leitura: ligação insuficiente com os eixos da revisão",
}


def main() -> None:
    unico = pd.read_json(PROC / "registros_unicos.jsonl", lines=True)
    bruto = pd.read_excel(PROC / "wos_consolidado.xlsx")
    dec = pd.read_csv(PROC / "decisoes_titulo_resumo.csv").fillna("")
    d = unico.merge(dec, on="id_registro", how="left", validate="one_to_one").fillna("")

    eleg = d.filtro_protocolo == ""
    assert (d[eleg].decisao != "").all(), "há registro elegível sem decisão"
    assert (d[~eleg].decisao == "").all(), "decisão em registro barrado por filtro"

    d.loc[~eleg, "decisao"] = "excluir"
    d["motivo_txt"] = d.motivo.map(MOTIVOS).fillna("")
    d.loc[~eleg, "motivo_txt"] = d.loc[~eleg, "filtro_protocolo"]
    d.loc[d.decisao != "excluir", "motivo_txt"] = ""
    d["obs"] = d.justificativa
    d.loc[d.revisao.astype(str).str.lower() == "true", "obs"] = "[Revisão: usar para rastreamento] " + d.obs
    d.loc[~eleg & d.filtro_protocolo.str.startswith("E3"), "obs"] = (
        "Fora do período candidato; não lido. Recuperável como exceção metodológica antiga, se pertinente.")

    # segunda leitura (opcional): resolve as dúvidas e corrige categorias
    seg = PROC / "segunda_leitura.csv"
    if seg.exists():
        s = pd.read_csv(seg).fillna("").set_index("id_registro")
        for i, r in d[d.id_registro.isin(s.index)].iterrows():
            x = s.loc[r.id_registro]
            era_duvida = r.decisao == "duvida"
            d.loc[i, "categoria"] = x.categoria
            if era_duvida:
                d.loc[i, "decisao"] = x.decisao
                d.loc[i, "obs"] = f"[Dúvida resolvida na 2ª leitura: {x.decisao}] {x.o_que_aproveitar} | 1ª leitura: {r.obs}"
                if x.decisao == "excluir":
                    d.loc[i, "motivo_txt"] = "M7 segunda leitura: ligação insuficiente com os eixos da revisão"
                    d.loc[i, "categoria"] = ""

    wb = load_workbook(PROC / "triagem_estudos.xlsx")
    ws = wb["Registros"]
    cab = [c.value for c in ws[1]]
    ws.delete_rows(2, ws.max_row)
    for r in d.itertuples():
        linha = dict(
            id_registro=r.id_registro, doi=r.doi, titulo=r.titulo, autores=r.autores, ano=r.ano,
            periodico_evento=r.periodico_evento, queries_origem=r.queries_origem, arquivo_raw=r.arquivo_raw,
            decisao_titulo_resumo=r.decisao, motivo_exclusao_titulo_resumo=r.motivo_txt,
            categoria_evidencia=r.categoria, observacoes=r.obs, data_busca=DATA_BUSCA,
            classificacao_tematica=r.temas, id_wos=r.ids_wos, ids_execucao=r.ids_execucao,
            revisor=REVISOR if eleg[r.Index] else "Regra do protocolo (filtro automático)",
            data_decisao=DATA_BUSCA,
        )
        ws.append([linha.get(c, "") or None for c in cab])

    wo = wb["Origens"]
    cabo = [c.value for c in wo[1]]
    wo.delete_rows(2, wo.max_row)
    for r in bruto.fillna("").itertuples():
        linha = dict(id_registro=r.id_registro, id_execucao=r.id_execucao, query_origem=r.query_origem,
                     data_busca=DATA_BUSCA, arquivo_raw=r.arquivo_raw, id_wos_original=r.id_wos,
                     doi_original=r.doi)
        wo.append([linha.get(c, "") or None for c in cabo])
    wb.save(PROC / "triagem_estudos.xlsx")

    print("registros:", len(d))
    print(d.decisao.value_counts().to_string())
    print(d[d.decisao == "excluir"].motivo_txt.str[:2].value_counts().sort_index().to_string())
    print(pd.crosstab(d[d.decisao != "excluir"].categoria, d[d.decisao != "excluir"].decisao).to_string())


if __name__ == "__main__":
    main()
