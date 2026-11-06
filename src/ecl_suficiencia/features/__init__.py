"""Variáveis explicativas observáveis na data-base (operação, histórico de pagamento, tomador, carteira)."""
from __future__ import annotations
import pandas as pd


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """Constrói variáveis sem usar informação posterior à data-base (controle de vazamento)."""
    raise NotImplementedError
