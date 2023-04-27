class Televisao:
    def __init__(self) -> None:
        self.volume = 50
        self.canal = 1

    def aumentar_volume(self) -> None:
        if self.volume < 100:
            self.volume += 1

    def diminuir_volume(self) -> None:
        if self.volume > 0:
            self.volume -= 1

    def trocar_canal(self, canal: int) -> None:
        self.canal = canal

    def aumentar_canal(self) -> None:
        self.canal += 1

    def diminuir_canal(self) -> None:
        self.canal -= 1


class ControleRemoto:
    def __init__(self, televisao: object) -> None:
        self.televisao = televisao

    def aumentar_volume(self) -> None:
        self.televisao.aumentar_volume()

    def diminuir_volume(self) -> None:
        self.televisao.diminuir_volume()

    def trocar_canal(self, canal: int) -> None:
        self.televisao.trocar_canal(canal)

    def aumentar_canal(self) -> None:
        self.televisao.aumentar_canal()

    def diminuir_canal(self) -> None:
        self.televisao.diminuir_canal()

    def consultar_volume(self) -> int:
        return self.televisao.volume

    def consultar_canal(self) -> int:
        return self.televisao.canal

tv = Televisao()
controle = ControleRemoto(tv)

controle.aumentar_volume() 
controle.aumentar_canal() 
controle.trocar_canal(5) 
print(controle.consultar_volume()) 
print(controle.consultar_canal())
