"""Aproximação estática da ECL sintética (proposta v5, seção 7) e interface multiperíodo pendente.

PD12 não é ECL integral: interpretação requer LGD/EAD, horizonte, cenários e desconto
compatíveis. Perdas decorrentes de defaults em 12 meses podem ocorrer além desse prazo.
"""
from __future__ import annotations
import numpy as np


def ecl_12m(pd_12m: np.ndarray, lgd: np.ndarray, ead: np.ndarray) -> np.ndarray:
    """Produto PD12 × LGD × EAD (LP12); não aplica cenários ou desconto por conta própria."""
    pd_12m, lgd, ead = (np.asarray(a, dtype=float) for a in (pd_12m, lgd, ead))
    if not ((0 <= pd_12m) & (pd_12m <= 1)).all():
        raise ValueError("PD fora de [0, 1]")
    if not ((0 <= lgd) & (lgd <= 1)).all():
        raise ValueError("LGD fora de [0, 1]")
    return pd_12m * lgd * ead


def ecl_lifetime(marginal_pd, lgd, ead, discount_factors):
    """Soma ao longo do prazo esperado de PD marginal × LGD × EAD × fator de desconto."""
    raise NotImplementedError
