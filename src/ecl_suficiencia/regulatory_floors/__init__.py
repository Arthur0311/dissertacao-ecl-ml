"""Provisão pelos níveis mínimos da metodologia simplificada (Res. BCB 309/2023): percentual por carteira C1–C5 e faixa de atraso."""
from __future__ import annotations
import pandas as pd

ATRASO_FAIXAS = [(0, 14), (15, 30), (31, 60), (61, 90)]


def dias_para_faixa(dias_atraso: int) -> str:
    """Mapeia dias de atraso para a faixa do Anexo II (operações não inadimplidas)."""
    for lo, hi in ATRASO_FAIXAS:
        if lo <= dias_atraso <= hi:
            return f"{lo}-{hi}"
    return ">90"


def minimum_provision(positions: pd.DataFrame, floors: pd.DataFrame) -> pd.DataFrame:
    """Aplica os percentuais vigentes à data a cada operação e agrega por carteira e período."""
    raise NotImplementedError
