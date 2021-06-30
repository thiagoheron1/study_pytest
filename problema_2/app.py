from dataclasses import dataclass

@dataclass
class Tarefa:
    nome: str


class Coluna:

    def __init__(self, nome) -> None:
        self.nome = nome
        self.tarefas = []

    def inserir_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    

class Quadro:

    def __init__(self) -> None:
        self.colunas = []
    
    def inserir_coluna(self, coluna):
        self.colunas.append(coluna)

    def inserir_tarefa(self, tarefa):
        self.colunas[0].inserir_tarefa(tarefa)