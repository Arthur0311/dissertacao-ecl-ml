r"""Exportação de tabelas e figuras para os documentos em LaTeX.

Os arquivos são gravados em ``<documento>/tabelas`` e ``<documento>/figuras``, em que
``documento`` é ``"projeto"`` ou ``"dissertacao"``, e incluídos no texto por
``\tabelagerada{nome}`` e ``\includegraphics``. A formatação (título APA, fonte de
10 pt, nota de fonte) vem de ``latex/ppgcont.sty``. Reexecutar o pipeline regenera os
artefatos; nunca editar esses arquivos à mão.
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

RAIZ_REPOSITORIO = Path(__file__).resolve().parents[3]
DOCUMENTOS = ("projeto", "dissertacao")

_ESCAPES = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}
_FIM_DE_LINHA = " " + "\\" * 2


def escapar_latex(texto: object) -> str:
    """Escapa caracteres especiais do LaTeX em um texto."""
    return "".join(_ESCAPES.get(c, c) for c in str(texto))


def _celula(valor: object, casas: int) -> str:
    if isinstance(valor, float):
        return "--" if pd.isna(valor) else f"{valor:.{casas}f}".replace(".", ",")
    return escapar_latex(valor)


def _pasta(documento: str, tipo: str) -> Path:
    if documento not in DOCUMENTOS:
        raise ValueError(f"documento deve ser um de {DOCUMENTOS}, recebido {documento!r}")
    return RAIZ_REPOSITORIO / documento / tipo


def tabela_latex(
    df: pd.DataFrame,
    legenda: str,
    rotulo: str,
    casas: int = 3,
    fonte: str = "Elaborada pelo autor.",
    nota: str | None = None,
) -> str:
    """Converte um DataFrame em tabela no padrão APA do PPGCONT (decimal com vírgula)."""
    colunas = "l" + "r" * max(df.shape[1] - 1, 0)
    cabecalho = " & ".join(rf"\textbf{{{escapar_latex(c)}}}" for c in df.columns)
    linhas = [
        r"\begin{table}[htbp]",
        rf"\caption{{{escapar_latex(legenda)}}}",
        rf"\label{{tab:{rotulo}}}",
        rf"\begin{{tabular*}}{{\textwidth}}{{@{{\extracolsep{{\fill}}}}{colunas}}}",
        r"\toprule",
        cabecalho + _FIM_DE_LINHA,
        r"\midrule",
    ]
    for _, linha in df.iterrows():
        linhas.append(" & ".join(_celula(v, casas) for v in linha) + _FIM_DE_LINHA)
    linhas += [r"\bottomrule", r"\end{tabular*}"]
    if nota:
        linhas.append(rf"\nota{{{escapar_latex(nota)}}}")
    linhas += [rf"\fonte{{{escapar_latex(fonte)}}}", r"\end{table}", ""]
    return "\n".join(linhas)


def salvar_tabela(
    df: pd.DataFrame,
    nome: str,
    legenda: str,
    documento: str = "dissertacao",
    casas: int = 3,
    fonte: str = "Elaborada pelo autor.",
    nota: str | None = None,
    pasta: Path | None = None,
) -> Path:
    """Grava ``<documento>/tabelas/<nome>.tex``; o rótulo no texto é ``tab:<nome>``."""
    destino = (pasta or _pasta(documento, "tabelas")) / f"{nome}.tex"
    destino.parent.mkdir(parents=True, exist_ok=True)
    conteudo = tabela_latex(df, legenda, nome, casas, fonte, nota)
    destino.write_text(conteudo, encoding="utf-8", newline="\n")
    return destino


def salvar_figura(
    fig, nome: str, documento: str = "dissertacao", pasta: Path | None = None
) -> Path:
    """Grava uma figura do matplotlib como PDF vetorial em ``<documento>/figuras``."""
    destino = (pasta or _pasta(documento, "figuras")) / f"{nome}.pdf"
    destino.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(destino, bbox_inches="tight")
    return destino
