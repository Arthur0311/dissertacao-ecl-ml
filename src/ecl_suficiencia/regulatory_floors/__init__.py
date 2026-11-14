"""Interface para regras da Res. BCB 352/2023 e alterações por data e ativo.

O auxiliar de faixas é incompleto para cálculo normativo: não cobre todos os períodos,
componentes e exceções. A Res. BCB 309/2023 é referência histórica revogada.
"""
from __future__ import annotations
import pandas as pd

ATRASO_FAIXAS = [(0, 14), (15, 30), (31, 60), (61, 90)]


def dias_para_faixa(dias_atraso: int) -> str:
    """Agrupa faixas básicas; >90 reúne atrasos que exigem detalhamento normativo adicional."""
    for lo, hi in ATRASO_FAIXAS:
        if lo <= dias_atraso <= hi:
            return f"{lo}-{hi}"
    return ">90"


def minimum_provision(positions: pd.DataFrame, floors: pd.DataFrame) -> pd.DataFrame:
    """Previsto: aplicar regras por ativo/data, incluindo componentes e exceções; ainda não implementado."""
    raise NotImplementedError
