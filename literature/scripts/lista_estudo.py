"""Gera a lista de estudo: os artigos incluídos na triagem, ordenados por prioridade de leitura
(pontos da segunda leitura; desempate por citações/ano), em literature/analysis/:

  - lista_estudo_versionada.xlsx   sem os resumos do WoS; vai para o Git
  - lista_estudo_priorizada.xlsx   com os resumos; cópia de trabalho, fora do Git (.gitignore).
                                   Não é sobrescrita se já existir (preserva `lido` e `anotacoes`);
                                   use --refazer-local para gerar de novo.

Uso: python literature/scripts/lista_estudo.py [--refazer-local]
"""
import sys
from pathlib import Path

import pandas as pd
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

RAIZ = Path(__file__).resolve().parents[1]
PROC = RAIZ / "processed"
ANO_REF = 2026
FAIXAS = [(85, "1 - Ler primeiro (íntegra)"), (75, "2 - Ler na íntegra"),
          (55, "3 - Leitura dirigida (método e resultados)"), (0, "4 - Só resumo; citar se couber")]
CORES = {"1": "C6E0B4", "2": "E2EFDA", "3": "FFF2CC", "4": "F2F2F2"}


def faixa(p: int) -> str:
    return next(nome for corte, nome in FAIXAS if p >= corte)


def grava(out: pd.DataFrame, duv: pd.DataFrame, destino: Path) -> None:
    with pd.ExcelWriter(destino, engine="openpyxl") as w:
        out.to_excel(w, index=False, sheet_name="Lista de estudo")
        duv.to_excel(w, index=False, sheet_name="Duvidas resolvidas")
        ws = w.sheets["Lista de estudo"]
        for i, larg in enumerate([7, 26, 8, 20, 6, 50, 28, 26, 55, 28, 9, 30, 10, 11, 7, 35, 90], start=1):
            ws.column_dimensions[get_column_letter(i)].width = larg
        for c in ws[1]:
            c.font = Font(bold=True)
        for linha in ws.iter_rows(min_row=2):
            cor = PatternFill("solid", start_color=CORES[str(linha[1].value)[0]])
            for c in linha:
                c.alignment = Alignment(wrap_text=True, vertical="top")
            for c in linha[:3]:
                c.fill = cor
            if linha[11].value:
                linha[11].hyperlink = linha[11].value
                linha[11].font = Font(color="0563C1", underline="single")
        ws.freeze_panes = "G2"
        ws.auto_filter.ref = ws.dimensions
        w2 = w.sheets["Duvidas resolvidas"]
        for i, larg in enumerate([11, 12, 6, 60, 110], start=1):
            w2.column_dimensions[get_column_letter(i)].width = larg
        for linha in w2.iter_rows(min_row=2):
            for c in linha:
                c.alignment = Alignment(wrap_text=True, vertical="top")


def main() -> None:
    t = pd.read_excel(PROC / "triagem_estudos.xlsx", sheet_name="Registros")
    s = pd.read_csv(PROC / "segunda_leitura.csv").fillna("")
    u = pd.read_json(PROC / "registros_unicos.jsonl", lines=True)[["id_registro", "citacoes_wos", "resumo"]]
    d = t[t.decisao_titulo_resumo == "incluir"].merge(s, on="id_registro", validate="one_to_one").merge(u, on="id_registro")
    d["cit"] = pd.to_numeric(d.citacoes_wos, errors="coerce").fillna(0).astype(int)
    d["cit_ano"] = (d.cit / (ANO_REF - d.ano + 1)).round(1)
    d = d.sort_values(["pontos", "cit_ano"], ascending=False).reset_index(drop=True)
    d["faixa"] = d.pontos.map(faixa)
    d["link"] = d.doi.map(lambda x: f"https://doi.org/{x}" if isinstance(x, str) and x else "")
    out = pd.DataFrame({
        "ordem": d.index + 1, "faixa": d.faixa, "pontos": d.pontos, "categoria": d.categoria_evidencia,
        "ano": d.ano, "titulo": d.titulo, "autores": d.autores, "periodico": d.periodico_evento,
        "o_que_aproveitar": d.o_que_aproveitar, "eixos": d.eixos, "citacoes_wos": d.cit,
        "link_doi": d.link, "consultas": d.queries_origem, "id_registro": d.id_registro,
        "lido": "", "anotacoes": "",
    })
    duv = t[t.observacoes.fillna("").str.startswith("[Dúvida resolvida")][
        ["id_registro", "decisao_titulo_resumo", "ano", "titulo", "observacoes"]]

    pasta = RAIZ / "analysis"
    grava(out, duv, pasta / "lista_estudo_versionada.xlsx")
    local = pasta / "lista_estudo_priorizada.xlsx"
    if local.exists() and "--refazer-local" not in sys.argv:
        print("cópia local preservada:", local.name)
    else:
        grava(out.assign(resumo=d.resumo), duv, local)
    destino = pasta / "lista_estudo_versionada.xlsx"
    print(len(out), "artigos em", destino)
    print(out.faixa.value_counts().sort_index().to_string())
    print(pd.crosstab(out.faixa, out.categoria).to_string())


if __name__ == "__main__":
    main()
