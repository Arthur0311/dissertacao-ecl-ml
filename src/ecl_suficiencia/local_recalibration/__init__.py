"""Regime híbrido: recalibração logística por carteira do logit da PD global, com encolhimento para (0, 1).

logit(PD_ic) = a_c + b_c · logit(PD_global(X_i)) + s_c(t)
"""
from __future__ import annotations
import numpy as np


def shrinkage_weight(n_events: int, k: float = 50.0) -> float:
    """Peso do ajuste local w = n / (n + k). Com poucos eventos, a carteira herda o modelo global."""
    if n_events < 0:
        raise ValueError("n_events deve ser não negativo")
    return n_events / (n_events + k)


def recalibrate_by_group(logit_global: np.ndarray, y: np.ndarray, groups: np.ndarray, *, k: float = 50.0):
    """Estima (a_c, b_c) por carteira e os encolhe para (0, 1) com peso `shrinkage_weight`. Retorna dict carteira -> (a, b)."""
    raise NotImplementedError
