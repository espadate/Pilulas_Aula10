"""
Exercício 3 - Converter nota para conceito
Função: converter_nota_para_conceito(nota: float) -> str
"""

def converter_nota_para_conceito(nota: float) -> str:
    if nota < 0 or nota > 10:
        return "Nota inválida"
    elif nota >= 9.0:
        return "A"
    elif nota >= 7.0:
        return "B"
    elif nota >= 5.0:
        return "C"
    elif nota >= 3.0:
        return "D"
    else:
        return "F"


def test_nota_invalida():
    assert converter_nota_para_conceito(-1) == "Nota inválida"
    assert converter_nota_para_conceito(10.1) == "Nota inválida"


def test_conceito_a():
    assert converter_nota_para_conceito(9.0) == "A"
    assert converter_nota_para_conceito(10.0) == "A"


def test_conceito_b():
    assert converter_nota_para_conceito(7.0) == "B"
    assert converter_nota_para_conceito(8.9) == "B"


def test_conceito_c():
    assert converter_nota_para_conceito(5.0) == "C"
    assert converter_nota_para_conceito(6.9) == "C"


def test_conceito_d():
    assert converter_nota_para_conceito(3.0) == "D"
    assert converter_nota_para_conceito(4.9) == "D"


def test_conceito_f():
    assert converter_nota_para_conceito(0) == "F"
    assert converter_nota_para_conceito(2.9) == "F"
