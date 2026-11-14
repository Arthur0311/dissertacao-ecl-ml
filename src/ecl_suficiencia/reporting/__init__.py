"""Relatórios previstos na proposta v4: contrastes H1–H4 e C1, calibração e viés monetário.

Previstos e não implementados: intercepto e inclinação de calibração com intervalos,
viés monetário em pontos-base, critério de adequação (adequada, inadequada,
inconclusiva) e fronteira de utilidade. Erro de perdas monetárias requer perdas
realizadas comparáveis; o viés monetário usa apenas a ocorrência do evento.
"""
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
