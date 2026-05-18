"""
Exercício 2 - Cálculo de frete
Função: calcular_frete(peso_kg: float) -> float
"""

def calcular_frete(peso_kg: float) -> float:
    if peso_kg <= 0:
        return 0.0
    elif peso_kg <= 1:
        return 5.0
    elif peso_kg <= 5:
        return 10.0
    else:
        return 18.0


def test_peso_zero_ou_negativo():
    assert calcular_frete(0) == 0.0
    assert calcular_frete(-10) == 0.0


def test_peso_ate_um_kg():
    assert calcular_frete(1.0) == 5.0
    assert calcular_frete(0.5) == 5.0


def test_peso_acima_de_um_ate_cinco_kg():
    assert calcular_frete(1.01) == 10.0
    assert calcular_frete(5.0) == 10.0


def test_peso_acima_de_cinco_kg():
    assert calcular_frete(5.01) == 18.0
    assert calcular_frete(10) == 18.0
