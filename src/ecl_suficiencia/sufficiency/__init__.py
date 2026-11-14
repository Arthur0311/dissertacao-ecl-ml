"""Diferenças experimentais entre perda modelada e referência de provisão.

Nomes históricos preservados; os auxiliares não determinam suficiência contábil,
conformidade, autorização de redução ou lançamento obrigatório.
"""
from __future__ import annotations
import numpy as np


def complement(ecl_estimated: float, minimum_provision: float) -> float:
    """Diferença experimental positiva: max(0, estimativa − referência); não é lançamento exigido."""
    return max(0.0, float(ecl_estimated) - float(minimum_provision))


def sufficiency_ratio(ecl_estimated: float, minimum_provision: float) -> float:
    """Razão estimativa/referência; 1 indica igualdade aritmética, sem conclusão de suficiência."""
    if minimum_provision <= 0:
        return np.inf if ecl_estimated > 0 else 1.0
    return float(ecl_estimated) / float(minimum_provision)


def lead_time_months(ecl_series, minimum_series, events_series):
    """Defasagem, em meses, entre a elevação da ECL estimada e a elevação da provisão mínima antes dos eventos observados."""
    raise NotImplementedError
