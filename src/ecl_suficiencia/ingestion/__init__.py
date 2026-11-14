"""Ingestão: leitura de posições mensais por contrato, cadastro de tomadores, séries macro e níveis mínimos.

Fontes previstas: core banking, histórico do documento 3040 (SCR), BCB/SGS, BCB/Focus, IBGE/SIDRA.
"""
from __future__ import annotations
import pandas as pd


def load_contract_month(path: str) -> pd.DataFrame:
    """Interface prevista; esquema final conforme data_dictionary/README.md.

    Exigir identificação pseudonimizada de contrato/tomador, domínio, data-base,
    disponibilidade, seguimento e evento. C1–C5 é condicional à comparação regulatória.
    Pseudonimização não comprova anonimização nem autorização de uso.
    """
    raise NotImplementedError


def load_macro(path: str, *, use_focus: bool = True) -> pd.DataFrame:
    """Carrega séries macro realizadas (defasadas pelo calendário de divulgação) e expectativas Focus por data de referência."""
    raise NotImplementedError


def load_regulatory_floors(path: str) -> pd.DataFrame:
    """Previsto: carregar regras por vigência, carteira, atraso, componente e condições especiais."""
    raise NotImplementedError
