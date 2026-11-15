"""Relatórios previstos na proposta v5: contrastes H1–H4 e C1, calibração e ECL sintética.

Previstos e não implementados: log-loss e Brier, intercepto e inclinação de calibração
com intervalos, erro frente à PD verdadeira do DGP, frequência de transferência
negativa, erro-padrão de Monte Carlo dos contrastes pareados, desvio da ECL sintética,
critério de adequação (adequada, inadequada, inconclusiva), fronteira de utilidade,
custo operacional e regra de seleção com arrependimento.
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
