"""Interfaces de PD: logística regularizada e gradient boosting; EBM é extensão histórica.

V3 compara local, agrupado, transferido sem adaptação e adaptado. O chamador deve
definir explicitamente a população de treino; ainda não há executor desses regimes.
"""
from __future__ import annotations
from typing import Literal

Algorithm = Literal["logistic", "gbm", "ebm"]


def make_model(algorithm: Algorithm, **params):
    """Fábrica de estimadores com interface scikit-learn (fit/predict_proba)."""
    raise NotImplementedError


def fit_global(X, y, algorithm: Algorithm = "logistic", **params):
    """Previsto: ajustar na origem ou em origem+destino, conforme população fornecida; nunca no teste."""
    raise NotImplementedError


def fit_local(X, y, groups, algorithm: Algorithm = "logistic", *, min_events: int = 50, **params):
    """Interface local legada; min_events=50 é ilustrativo e deve ser revisto por precisão/viabilidade."""
    raise NotImplementedError
