"""Relatórios: calibração (intercepto e inclinação), log-loss, erro relativo de perdas, TOST, Diebold–Mariano e explicabilidade."""
from __future__ import annotations
import numpy as np


def calibration_intercept_slope(y: np.ndarray, p: np.ndarray) -> tuple[float, float]:
    """Regressão logística de y sobre logit(p); retorna (intercepto, inclinação). Ideal: (0, 1)."""
    raise NotImplementedError


def relative_loss_error(observed_loss: float, estimated_loss: float) -> float:
    """Erro relativo de perdas agregadas: (estimada − observada) / observada."""
    if observed_loss == 0:
        raise ZeroDivisionError("perda observada nula")
    return (float(estimated_loss) - float(observed_loss)) / float(observed_loss)
