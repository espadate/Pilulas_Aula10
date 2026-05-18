"""
Exercício 1 - Semáforo
Função: acao_semaforo(cor: str) -> str
"""

def acao_semaforo(cor: str) -> str:
    if cor == "vermelho":
        return "Pare"
    elif cor == "amarelo":
        return "Atenção"
    elif cor == "verde":
        return "Siga"
    else:
        return "Cor inválida"


def test_vermelho_deve_retornar_pare():
    assert acao_semaforo("vermelho") == "Pare"


def test_amarelo_deve_retornar_atencao():
    assert acao_semaforo("amarelo") == "Atenção"


def test_verde_deve_retornar_siga():
    assert acao_semaforo("verde") == "Siga"


def test_cor_invalida():
    assert acao_semaforo("azul") == "Cor inválida"
