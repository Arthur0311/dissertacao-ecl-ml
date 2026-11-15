"""Interface histórica de recalibração e auxiliar heurístico de encolhimento.

O regime R4 da proposta v5 atualiza o modelo da origem com intercepto e, quando
suportado, inclinação estimados no desenvolvimento do destino, com regularização;
sem eventos locais, retorna a R3 ou a uma atualização por prior documentado. O peso n/(n+k) não implementa essa estimação nem um modelo bayesiano.
"""
from __future__ import annotations
import numpy as np


def shrinkage_weight(n_events: int, k: float = 50.0) -> float:
    """Peso heurístico w = n/(n+k); k=50 é ilustrativo, não limiar validado de viabilidade."""
    if n_events < 0:
        raise ValueError("n_events deve ser não negativo")
    return n_events / (n_events + k)


def recalibrate_by_group(logit_global: np.ndarray, y: np.ndarray, groups: np.ndarray, *, k: float = 50.0):
    """Estima (a_c, b_c) por carteira e os encolhe para (0, 1) com peso `shrinkage_weight`. Retorna dict carteira -> (a, b)."""
    raise NotImplementedError
