"""Ingestão: base sintética, agregados públicos e séries macroeconômicas.

Na proposta v5 não se leem microdados de instituições. Fontes previstas: saídas do
simulador, agregados do SCR.data e séries públicas (BCB/SGS e previsões históricas
datadas). As assinaturas abaixo são legadas e serão revistas.
"""
from __future__ import annotations
import pandas as pd


def load_contract_month(path: str) -> pd.DataFrame:
    """Interface prevista; esquema final conforme data_dictionary/README.md.

    Na v5, lê contrato–mês da base sintética, com identificadores fictícios, domínio,
    data-base, seguimento e evento. Nunca lê a tabela de verdade do simulador.
    """
    raise NotImplementedError


def load_macro(path: str, *, use_focus: bool = True) -> pd.DataFrame:
    """Carrega séries macro realizadas (defasadas pelo calendário de divulgação) e expectativas Focus por data de referência."""
    raise NotImplementedError


def load_regulatory_floors(path: str) -> pd.DataFrame:
    """Previsto: carregar regras por vigência, carteira, atraso, componente e condições especiais."""
    raise NotImplementedError
