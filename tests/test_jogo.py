from pytest import mark
from problema_1.jogo import brincadeira

"""
O teste é formado por três etapadas (GWT):
1 - Given - Dado
2 - When - Quando
3 - Then - Então


Existe outra também denominada AAA
- Arange - Arranje 
- Act - Acione
- Assert - Teste

TDD -  Kent Beck - One Step Test

"Brincadeira" - SUT - System Under Test
Learning PyTest - Foguete na Capa - Brian Oclan

Ver a aula 128 do Setup

xUnit Patterns - Gerard Mezaros
4 steps
- Setup -> Dado
- Exercise -> Quando
- Verify -> Então
- Teardown -> Desmonta tudo antes que seja tarde

Ver sobre a live de mocks, fakes live 76

Melhorando testes unitarios live 80
"""


def test_quando_brincadeira_receber_1_entao_deve_retornar_1():
    # TDD -  Kent Beck - One Step Test
    entrada = 1 # Given
    esperado = 1 

    resultado = brincadeira(entrada) # When
    assert resultado == esperado # Then


def test_quando_brincadeira_receber_2_entao_deve_retornar_2():
    # TDD -  Kent Beck - One Step Test
    assert brincadeira(2) == 2


def test_quando_brincadeira_receber_3_entao_deve_retornar_queijo():
    # TDD -  Kent Beck - One Step Test
    assert brincadeira(3) == "queijo"


@mark.goiabada
def test_quando_brincadeira_receber_5_entao_deve_retornar_goiabada():
    # TDD -  Kent Beck - One Step Test
    assert brincadeira(5) == "goiabada"

@mark.goiabada
def test_quando_brincadeira_receber_10_entao_deve_retornar_goiabada():
    # TDD -  Kent Beck - One Step Test
    assert brincadeira(5) == "goiabada"

@mark.goiabada
def test_quando_brincadeira_receber_20_entao_deve_retornar_goiabada():
    # TDD -  Kent Beck - One Step Test
    assert brincadeira(5) == "goiabada"

@mark.parametrize(
    "entrada",
    [5, 10, 20, 25, 35]

)
def test_brincadeira_deve_retornar_goiabada_com_multiplos_de_5(entrada):
    assert brincadeira(5) == "goiabada"

@mark.parametrize(
    "entrada",
    [3, 6, 9, 12, 18]

)
def test_brincadeira_deve_retornar_queijo_com_multiplos_de_3(entrada):
    assert brincadeira(5) == "queijo"


@mark.parametrizado
@mark.parametrize(
    "entrada, esperado",
    [(1,1), (2,2), (3, 'queijo'), (4,4), (5, 'goiabada')]

)
def test_brincadeira_deve_retornar_valor_esperado(entrada, esperado):
    assert brincadeira(entrada) == esperado


def test_xfail_windows():
    assert brincadeira(20) == "goiabada"


@mark.xfail
def test_xfail_2():
    assert brincadeira(20) != "goiabada"
    