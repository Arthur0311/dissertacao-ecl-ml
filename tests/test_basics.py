import numpy as np
import pytest

from ecl_suficiencia.ecl_engine import ecl_12m
from ecl_suficiencia.local_recalibration import shrinkage_weight
from ecl_suficiencia.regulatory_floors import dias_para_faixa
from ecl_suficiencia.sufficiency import complement, sufficiency_ratio
from ecl_suficiencia.reporting import relative_loss_error


def test_ecl_12m_elementwise():
    out = ecl_12m([0.02, 0.10], [0.5, 0.4], [1000.0, 500.0])
    assert np.allclose(out, [10.0, 20.0])


def test_ecl_rejects_invalid_pd():
    with pytest.raises(ValueError):
        ecl_12m([1.2], [0.5], [100.0])


def test_shrinkage_weight_bounds():
    assert shrinkage_weight(0) == 0.0
    assert 0.0 < shrinkage_weight(50) < 1.0
    assert shrinkage_weight(50) == pytest.approx(0.5)


def test_floor_bands():
    assert dias_para_faixa(0) == "0-14"
    assert dias_para_faixa(45) == "31-60"
    assert dias_para_faixa(120) == ">90"


def test_sufficiency():
    assert complement(120.0, 100.0) == 20.0
    assert complement(80.0, 100.0) == 0.0
    assert sufficiency_ratio(120.0, 100.0) == pytest.approx(1.2)


def test_relative_loss_error():
    assert relative_loss_error(100.0, 110.0) == pytest.approx(0.10)


def test_tabela_latex_escapa_e_usa_virgula(tmp_path):
    import pandas as pd

    from ecl_suficiencia.reporting.latex import salvar_tabela

    df = pd.DataFrame({"modelo_R1": ["a&b"], "erro": [0.1234]})
    caminho = salvar_tabela(df, "teste", "Erro (%)", pasta=tmp_path)
    texto = caminho.read_text(encoding="utf-8")
    assert r"modelo\_R1" in texto and r"a\&b" in texto
    assert "0,123" in texto and r"\label{tab:teste}" in texto
