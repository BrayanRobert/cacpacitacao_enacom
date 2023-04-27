class Agenda:
    def __init__(self) -> None:
        self.__pessoas = [None]*10

    def armazenar_pessoa(self, pessoa: str) -> None:
        for i in range(10):
            if self.__pessoas[i] is None:
                self.__pessoas[i] = pessoa
                break

    def remover_pessoa(self, nome: str) -> None:
        for i in range(10):
            if self.__pessoas[i] is not None and self.__pessoas[i].get_nome() == nome:
                self.__pessoas[i] = None
                break

    def buscar_pessoa(self, posicao: int) -> int:
        if posicao >= 0 and posicao < 10:
            return self.__pessoas[posicao]
        else:
            return None

    def imprimir_agenda(self) -> None:
        for i in range(10):
            if self.__pessoas[i] is not None:
                print(f"Posição: {i} - {self.__pessoas[i].imprimir_dados()}")
            else:
                print(f"Posição: {i} - Vazia")

    def imprimir_pessoa(self, posicao: int) -> None:
        if posicao >= 0 and posicao < 10 and self.__pessoas[posicao] is not None:
            print(f"Posição: {posicao} - {self.__pessoas[posicao].imprimir_dados()}")
        else:
            print("Posição inválida ou vazia")
