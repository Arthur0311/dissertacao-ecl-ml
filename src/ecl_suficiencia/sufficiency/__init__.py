"""Avaliação de suficiência: razão perda estimada / mínimo, parcela complementar e defasagem temporal."""
from __future__ import annotations
import numpy as np


def complement(ecl_estimated: float, minimum_provision: float) -> float:
    """Parcela complementar a registrar de forma segregada: max(0, ECL estimada − provisão mínima)."""
    return max(0.0, float(ecl_estimated) - float(minimum_provision))


def sufficiency_ratio(ecl_estimated: float, minimum_provision: float) -> float:
    """Razão entre perda esperada estimada e provisão mínima (1 = exatamente suficiente)."""
    if minimum_provision <= 0:
        return np.inf if ecl_estimated > 0 else 1.0
    return float(ecl_estimated) / float(minimum_provision)


def lead_time_months(ecl_series, minimum_series, events_series):
    """Defasagem, em meses, entre a elevação da ECL estimada e a elevação da provisão mínima antes dos eventos observados."""
    raise NotImplementedError
