from problema_2.app import Coluna, Quadro, Tarefa
from pytest import fixture
from faker import Faker

fake = Faker()

@fixture(scope="function")
def quadro():
    # Inicio do Setup
    print("Estou montando o quadro")
    # Fim do Setup
    
    yield Quadro()
    
    # Inicio do Teardown
    print("Estou desmontando o quadro")
    # Fim do Teardown

@fixture(scope="function")
def quadro_com_coluna(quadro):
    quadro.inserir_coluna(Coluna(fake.pystr()))
    return quadro

def test_nao_deve_existir_nenhuma_coluna_no_quadro(quadro):
    quantidade_de_colunas = len(quadro.colunas)
    assert quantidade_de_colunas == 0 


def test_quando_inserir_uma_coluna_deve_existir_uma_coluna(quadro):
    quadro.inserir_coluna(Coluna(nome='A fazer'))
    assert len(quadro.colunas) == 1


def test_quando_inserir_a_coluna_a_fazer_deve_estar_no_quadro(quadro):
    quadro.inserir_coluna(Coluna(nome='A fazer'))
    assert quadro.colunas[0].nome == "A fazer"


def test_quando_inserir_uma_tarefa_no_quadro_ela_deve_estar_na_primeira_coluna(quadro_com_coluna):
    quadro_com_coluna.inserir_tarefa(Tarefa(nome='Dormir'))
    assert len(quadro_com_coluna.colunas[0].tarefas) == 1

def test_quando_inserir_duas_tarefas_no_quadro_ela_deve_estar_na_primeira_coluna(quadro_com_coluna):
    quadro_com_coluna.inserir_tarefa(Tarefa(nome='Dormir'))
    quadro_com_coluna.inserir_tarefa(Tarefa(nome='Comer'))
    assert len(quadro_com_coluna.colunas[0].tarefas) == 2
