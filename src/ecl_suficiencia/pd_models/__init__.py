"""Modelos de probabilidade de inadimplência: regressão logística regularizada (referência), gradient boosting e EBM."""
from __future__ import annotations
from typing import Literal

Algorithm = Literal["logistic", "gbm", "ebm"]


def make_model(algorithm: Algorithm, **params):
    """Fábrica de estimadores com interface scikit-learn (fit/predict_proba)."""
    raise NotImplementedError


def fit_global(X, y, algorithm: Algorithm = "logistic", **params):
    """Modelo global: treinado com todas as carteiras, sem identificadores de grupo e sem variáveis macro."""
    raise NotImplementedError


def fit_local(X, y, groups, algorithm: Algorithm = "logistic", *, min_events: int = 50, **params):
    """Modelos locais: um por carteira com ao menos `min_events` eventos."""
    raise NotImplementedError
