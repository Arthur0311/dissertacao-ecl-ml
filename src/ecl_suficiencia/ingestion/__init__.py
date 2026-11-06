"""Ingestão: leitura de posições mensais por contrato, cadastro de tomadores, séries macro e níveis mínimos.

Fontes previstas: core banking, histórico do documento 3040 (SCR), BCB/SGS, BCB/Focus, IBGE/SIDRA.
"""
from __future__ import annotations
import pandas as pd


def load_contract_month(path: str) -> pd.DataFrame:
    """Carrega a base contrato-mês já anonimizada. Colunas mínimas: id_contrato, instituicao, carteira,
    data_base, saldo_devedor, dias_atraso, carteira_regulatoria (C1–C5), evento_default_12m."""
    raise NotImplementedError


def load_macro(path: str, *, use_focus: bool = True) -> pd.DataFrame:
    """Carrega séries macro realizadas (defasadas pelo calendário de divulgação) e expectativas Focus por data de referência."""
    raise NotImplementedError


def load_regulatory_floors(path: str) -> pd.DataFrame:
    """Carrega os percentuais dos níveis mínimos vigentes por data, carteira C1–C5 e faixa de atraso."""
    raise NotImplementedError
