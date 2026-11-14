"""LGD segmentada por modalidade e garantia (com tratamento de censura) e EAD contratual."""
from __future__ import annotations


def segmented_lgd(recoveries, *, maturity_months: int = 24):
    """Interface prevista de LGD por segmento; maturação e censura dependem da carteira.

    O padrão histórico de 24 meses é ilustrativo, não garantia de recuperação completa.
    """
    raise NotImplementedError


def contractual_ead(positions):
    """EAD a partir do saldo contábil e dos fluxos contratuais, com ajuste para limites rotativos."""
    raise NotImplementedError
