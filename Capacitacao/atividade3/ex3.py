class Elevador:
    def __init__(self, capacidade: int, total_andares: int) -> None:
        self.__andar_atual = 0
        self.__total_andares = total_andares
        self.__capacidade = capacidade
        self.__pessoas_presentes = 0

    def entra(self) -> None:
        if self.__pessoas_presentes < self.__capacidade:
            self.__pessoas_presentes += 1
        else:
            print("Elevador cheio, não é possível entrar mais pessoas.")

    def sai(self) -> None:
        if self.__pessoas_presentes > 0:
            self.__pessoas_presentes -= 1
        else:
            print("Elevador vazio, não é possível sair mais pessoas.")

    def sobe(self) -> None:
        if self.__andar_atual < self.__total_andares:
            self.__andar_atual += 1
        else:
            print("O elevador já está no último andar.")

    def desce(self) -> None:
        if self.__andar_atual > 0:
            self.__andar_atual -= 1
        else:
            print("O elevador já está no térreo.")

    def set_andar_atual(self, andar: int) -> None:
        if andar < 0 or andar > self.__total_andares:
            print("Andar inválido.")
        else:
            self.__andar_atual = andar

    def get_andar_atual(self) -> int:
        return self.__andar_atual

    def set_total_andares(self, total_andares: int) -> None:
        if total_andares <= 0:
            print("Total de andares inválido.")
        else:
            self.__total_andares = total_andares

    def get_total_andares(self) -> int:
        return self.__total_andares

    def set_capacidade(self, capacidade: int) -> None:
        if capacidade <= 0:
            print("Capacidade inválida.")
        else:
            self.__capacidade = capacidade

    def get_capacidade(self) -> int:
        return self.__capacidade

    def set_pessoas_presentes(self, pessoas_presentes: int) -> None:
        if pessoas_presentes < 0 or pessoas_presentes > self.__capacidade:
            print("Número de pessoas inválido.")
        else:
            self.__pessoas_presentes = pessoas_presentes

    def get_pessoas_presentes(self) -> int:
        return self.__pessoas_presentes
