"""Validação temporal: divisão fora do tempo, janela expansiva e embargo entre horizontes."""
from __future__ import annotations
from dataclasses import dataclass
import pandas as pd


@dataclass(frozen=True)
class TemporalSplit:
    train_end: pd.Timestamp
    test_start: pd.Timestamp
    test_end: pd.Timestamp


def out_of_time_split(df: pd.DataFrame, *, test_months: int = 12, horizon_months: int = 12) -> TemporalSplit:
    """Reserva os últimos `test_months` como teste fora do tempo e aplica embargo de `horizon_months` entre treino e teste."""
    raise NotImplementedError


def expanding_window_folds(df: pd.DataFrame, *, n_folds: int, horizon_months: int = 12):
    """Gera dobras de validação progressiva; toda transformação deve ser ajustada apenas no treino de cada dobra."""
    raise NotImplementedError
