"""Consolida e deduplica as exportações BibTeX do WoS (Q1–Q6).

Lê literature/raw/Q*.bib (sem alterá-los) e grava em literature/processed/:
  - wos_consolidado.xlsx   uma linha por registro exportado (com duplicatas entre consultas)
  - wos_deduplicado.xlsx   uma linha por registro único, com todas as consultas de origem
  - registros_unicos.jsonl mesma base, com resumo, para a triagem de título/resumo

Deduplicação: 1) identificador WoS (UT); 2) DOI normalizado; 3) título normalizado + ano.
Os filtros de elegibilidade do protocolo (tipo, idioma, período) NÃO removem linhas aqui:
viram a coluna `filtro_protocolo`, para que a exclusão fique documentada na triagem.

Uso: python literature/scripts/consolidar_wos.py
"""
from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from datetime import datetime
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
RAW = RAIZ / "raw"
PROC = RAIZ / "processed"
ANO_MIN, ANO_MAX = 2009, 2026


def ler_bib(caminho: Path) -> list[dict]:
    texto = caminho.read_text(encoding="utf-8-sig")
    registros = []
    for m in re.finditer(r"^@(\w+)\{\s*([^,\s]+),", texto, flags=re.M):
        i, prof, campos = m.end(), 1, {}
        # percorre o corpo do registro respeitando chaves aninhadas
        while i < len(texto) and prof > 0:
            c = re.compile(r"\s*([\w-]+)\s*=\s*\{").match(texto, i)
            if not c:
                if texto[i] == "}":
                    prof -= 1
                i += 1
                continue
            j, p = c.end(), 1
            while p:
                ch = texto[j]
                p += (ch == "{") - (ch == "}")
                j += 1
            valor = re.sub(r"\s+", " ", texto[c.end(): j - 1]).strip()
            campos[c.group(1).lower()] = valor.replace("\\&", "&").replace("\\%", "%").replace("\\_", "_")
            i = j
            if texto[i: i + 1] == ",":
                i += 1
        campos["entrada"] = m.group(1).lower()
        campos["id_wos"] = m.group(2)
        registros.append(campos)
    return registros


def norm_doi(doi: str | None) -> str:
    if not doi:
        return ""
    return re.sub(r"^https?://(dx\.)?doi\.org/", "", doi.strip().lower())


def norm_titulo(t: str | None) -> str:
    t = unicodedata.normalize("NFKD", (t or "").lower())
    return re.sub(r"[^a-z0-9]+", " ", t).strip()


def filtro_protocolo(r: dict) -> str:
    tipo = r.get("type", "")
    if "Article" not in tipo:
        return f"E1 tipo documental ({tipo})"
    if r.get("language", "") != "English":
        return f"E2 idioma ({r.get('language', '')})"
    ano = int(r["year"]) if r.get("year", "").isdigit() else None
    if ano is None or not (ANO_MIN <= ano <= ANO_MAX):
        return f"E3 fora do período {ANO_MIN}-{ANO_MAX} ({r.get('year', 's/ano')})"
    return ""


def main() -> None:
    linhas, execucoes = [], []
    for arq in sorted(RAW.glob("Q*.bib")):
        q = arq.stem
        regs = ler_bib(arq)
        execucoes.append({
            "id_execucao": f"{q}-E01", "query": q, "arquivo_raw": f"literature/raw/{arq.name}",
            "registros_bib": len(regs),
            "modificado_em": datetime.fromtimestamp(arq.stat().st_mtime).isoformat(timespec="seconds"),
            "sha256": hashlib.sha256(arq.read_bytes()).hexdigest(),
        })
        xls = arq.with_suffix(".xls")
        if xls.exists():
            execucoes.append({
                "id_execucao": f"{q}-E01", "query": q, "arquivo_raw": f"literature/raw/{xls.name}",
                "registros_bib": None,
                "modificado_em": datetime.fromtimestamp(xls.stat().st_mtime).isoformat(timespec="seconds"),
                "sha256": hashlib.sha256(xls.read_bytes()).hexdigest(),
            })
        for r in regs:
            linhas.append({
                "query_origem": q, "id_execucao": f"{q}-E01", "arquivo_raw": arq.name,
                "id_wos": r["id_wos"], "doi": norm_doi(r.get("doi")), "titulo": r.get("title", ""),
                "autores": r.get("author", "").replace(" and ", "; "), "ano": r.get("year", ""),
                "periodico_evento": r.get("journal") or r.get("booktitle", ""),
                "tipo": r.get("type", ""), "idioma": r.get("language", ""),
                "palavras_chave": r.get("keywords", ""), "resumo": r.get("abstract", ""),
                "citacoes_wos": r.get("times-cited", ""), "filtro_protocolo": filtro_protocolo(r),
            })
    bruto = pd.DataFrame(linhas)

    # chave de deduplicação em cascata: UT -> DOI -> título+ano
    chave: dict[str, str] = {}
    grupos = []
    for _, r in bruto.iterrows():
        cands = [f"ut:{r.id_wos}"]
        if r.doi:
            cands.append(f"doi:{r.doi}")
        if norm_titulo(r.titulo):
            cands.append(f"ti:{norm_titulo(r.titulo)}|{r.ano}")
        g = next((chave[c] for c in cands if c in chave), cands[0])
        for c in cands:
            chave.setdefault(c, g)
        grupos.append(g)
    bruto["grupo"] = grupos
    ordem = {g: i for i, g in enumerate(dict.fromkeys(grupos), start=1)}
    bruto["id_registro"] = bruto["grupo"].map(lambda g: f"R{ordem[g]:04d}")

    agreg = bruto.groupby("id_registro", sort=True).agg(
        queries_origem=("query_origem", lambda s: "; ".join(sorted(set(s)))),
        ids_execucao=("id_execucao", lambda s: "; ".join(sorted(set(s)))),
        arquivo_raw=("arquivo_raw", lambda s: "; ".join(sorted(set(s)))),
        ids_wos=("id_wos", lambda s: "; ".join(dict.fromkeys(s))),
    )
    unico = bruto.drop_duplicates("id_registro").set_index("id_registro").drop(
        columns=["query_origem", "id_execucao", "arquivo_raw", "grupo", "id_wos"]).join(agreg).reset_index()

    PROC.mkdir(exist_ok=True)
    bruto.drop(columns="grupo").to_excel(PROC / "wos_consolidado.xlsx", index=False)
    unico.to_excel(PROC / "wos_deduplicado.xlsx", index=False)
    unico.to_json(PROC / "registros_unicos.jsonl", orient="records", lines=True, force_ascii=False)
    pd.DataFrame(execucoes).to_csv(PROC / "execucoes_raw.csv", index=False)

    print("registros exportados:", len(bruto), "| únicos:", len(unico), "| duplicatas:", len(bruto) - len(unico))
    print("grupos unidos por DOI/título (UT distintos):", int((unico.ids_wos.str.contains(";")).sum()))
    print(bruto.groupby("query_origem").size().to_string())
    print(unico.filtro_protocolo.str[:2].value_counts().to_string())
    print("elegíveis por consulta de origem:")
    print(unico[unico.filtro_protocolo == ""].queries_origem.value_counts().to_string())


if __name__ == "__main__":
    main()
