"""Perda esperada por contrato (12 meses) e extensão multiperíodo (soma descontada das perdas marginais)."""
from __future__ import annotations
import numpy as np


def ecl_12m(pd_12m: np.ndarray, lgd: np.ndarray, ead: np.ndarray) -> np.ndarray:
    """ECL = PD × LGD × EAD, elemento a elemento."""
    pd_12m, lgd, ead = (np.asarray(a, dtype=float) for a in (pd_12m, lgd, ead))
    if not ((0 <= pd_12m) & (pd_12m <= 1)).all():
        raise ValueError("PD fora de [0, 1]")
    if not ((0 <= lgd) & (lgd <= 1)).all():
        raise ValueError("LGD fora de [0, 1]")
    return pd_12m * lgd * ead


def ecl_lifetime(marginal_pd, lgd, ead, discount_factors):
    """Soma ao longo do prazo esperado de PD marginal × LGD × EAD × fator de desconto."""
    raise NotImplementedError
