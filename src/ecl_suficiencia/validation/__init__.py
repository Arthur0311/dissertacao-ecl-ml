"""Validação temporal: desenvolvimento, validação cronológica interna e teste futuro, com maturação e embargo."""
from __future__ import annotations
from dataclasses import dataclass
import pandas as pd


@dataclass(frozen=True)
class TemporalSplit:
    train_end: pd.Timestamp
    test_start: pd.Timestamp
    test_end: pd.Timestamp


def out_of_time_split(df: pd.DataFrame, *, test_months: int = 12, horizon_months: int = 12) -> TemporalSplit:
    """Previsto: reservar datas-base futuras com rótulos maturados e embargo coerente com o horizonte.

    Não reservar simplesmente os últimos registros se faltar acompanhamento futuro.
    """
    raise NotImplementedError


def expanding_window_folds(df: pd.DataFrame, *, n_folds: int, horizon_months: int = 12):
    """Gera dobras de validação progressiva; toda transformação deve ser ajustada apenas no treino de cada dobra."""
    raise NotImplementedError
