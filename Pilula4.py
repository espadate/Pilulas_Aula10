"""
Exercício 4 - Cálculo de bônus
Função: calcular_bonus(salario_base: float, avaliacao: str) -> float
"""

def calcular_bonus(salario_base: float, avaliacao: str) -> float:
    if salario_base < 0:
        return 0.0

    if avaliacao == "Excelente":
        return salario_base * 0.20
    elif avaliacao == "Bom":
        return salario_base * 0.10
    elif avaliacao == "Regular":
        return salario_base * 0.02
    else:
        return 0.0


def test_bonus_excelente():
    assert calcular_bonus(1000.0, "Excelente") == 200.0


def test_bonus_bom():
    assert calcular_bonus(1000.0, "Bom") == 100.0


def test_bonus_regular():
    assert calcular_bonus(1000.0, "Regular") == 20.0


def test_avaliacao_ruim_ou_invalida():
    assert calcular_bonus(1000.0, "Ruim") == 0.0
    assert calcular_bonus(1000.0, "Mais ou Menos") == 0.0


def test_salario_negativo():
    assert calcular_bonus(-1000.0, "Excelente") == 0.0
