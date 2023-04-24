class Pessoa:
    def __init__(self, nome: str, idade: int, altura: float) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, novo_nome: str) -> None:
        self.__nome = novo_nome

    def get_idade(self) -> int:
        return self.__idade

    def set_idade(self, nova_idade: int) -> None:
        self.__idade = nova_idade

    def get_altura(self) -> float:
        return self.__altura

    def set_altura(self, nova_altura: float) -> None:
        self.__altura = nova_altura

    def imprimir_dados(self) -> None:
        print(f"Nome: {self.__nome}, Idade: {self.__idade}, Altura: {self.__altura}")
