"""LGD segmentada por modalidade e garantia (com tratamento de censura) e EAD contratual."""
from __future__ import annotations


def segmented_lgd(recoveries, *, maturity_months: int = 24):
    """LGD por segmento a partir de fluxos de recuperação maturados por ao menos `maturity_months`."""
    raise NotImplementedError


def contractual_ead(positions):
    """EAD a partir do saldo contábil e dos fluxos contratuais, com ajuste para limites rotativos."""
    raise NotImplementedError
