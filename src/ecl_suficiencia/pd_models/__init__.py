"""Interfaces de PD: logística regularizada e gradient boosting; EBM é extensão histórica.

A proposta v5 compara cinco regimes: R0 referência simples, R1 local, R2 agrupado,
R3 transferido e R4 transferido com recalibração. R1–R4 usam logística regularizada e
gradient boosting quando a arquitetura comportar. Reponderação por importância é
extensão condicionada ao piloto. O chamador define explicitamente a população de
treino; ainda não há executor desses regimes nem interface para R0.
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
