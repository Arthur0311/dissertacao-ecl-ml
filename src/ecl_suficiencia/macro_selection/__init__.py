"""Componente macroeconômico prospectivo s_c(t): configurações M0 (sem macro), M1 (uniforme), M2 (por carteira), M3 (direto no modelo)."""
from __future__ import annotations
import pandas as pd


def fit_macro_component(residual_by_portfolio_period: pd.DataFrame, macro: pd.DataFrame, *, mode: str = "M2", alpha: float = 1.0, l1_ratio: float = 0.5):
    """Ajusta, por Elastic Net, o deslocamento de log-odds por carteira-período em função de indicadores e defasagens,
    apenas dentro da janela de treino. Retorna um objeto com `predict(portfolio, period)`."""
    raise NotImplementedError
