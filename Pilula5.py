"""
Exercício 5 - Aplicar cupom
Função: aplicar_cupom(codigo_cupom: str, valor_compra: float) -> float
"""

def aplicar_cupom(codigo_cupom: str, valor_compra: float) -> float:
    codigo = codigo_cupom.upper()

    if codigo == "CUPOM10":
        return 0.10
    elif codigo == "CUPOM25" and valor_compra > 100.0:
        return 0.25
    elif codigo == "DESCONTOVIP" and valor_compra > 500.0:
        return 0.35
    else:
        return 0.0


def test_cupom10_qualquer_valor():
    assert aplicar_cupom("CUPOM10", 50.0) == 0.10


def test_cupom10_minusculo():
    assert aplicar_cupom("cupom10", 50.0) == 0.10


def test_cupom25_funciona_acima_de_100():
    assert aplicar_cupom("CUPOM25", 150.0) == 0.25


def test_cupom25_nao_funciona_ate_100():
    assert aplicar_cupom("CUPOM25", 100.0) == 0.0
    assert aplicar_cupom("CUPOM25", 50.0) == 0.0


def test_descontovip_funciona_acima_de_500():
    assert aplicar_cupom("DESCONTOVIP", 600.0) == 0.35


def test_descontovip_nao_funciona_ate_500():
    assert aplicar_cupom("DESCONTOVIP", 500.0) == 0.0
    assert aplicar_cupom("DESCONTOVIP", 300.0) == 0.0


def test_cupom_invalido():
    assert aplicar_cupom("CUPOM_FALSO", 1000.0) == 0.0
