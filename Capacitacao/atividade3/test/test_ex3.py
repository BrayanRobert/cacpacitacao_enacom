from atividade3.ex3 import Elevador

def test_entra():
    elevador = Elevador(5, 10)
    elevador.set_pessoas_presentes(2)
    elevador.entra()
    assert elevador.get_pessoas_presentes() == 3

def test_sai():
    elevador = Elevador(5, 10)
    elevador.set_pessoas_presentes(3)
    elevador.sai()
    assert elevador.get_pessoas_presentes() == 2

def test_sobe():
    elevador = Elevador(5, 10)
    elevador.set_andar_atual(3)
    elevador.sobe()
    assert elevador.get_andar_atual() == 4

def test_desce():
    elevador = Elevador(5, 10)
    elevador.set_andar_atual(3)
    elevador.desce()
    assert elevador.get_andar_atual() == 2

def test_set_andar_atual():
    elevador = Elevador(5, 10)
    elevador.set_andar_atual(5)
    assert elevador.get_andar_atual() == 5

def test_set_total_andares():
    elevador = Elevador(5, 10)
    elevador.set_total_andares(12)
    assert elevador.get_total_andares() == 12

def test_set_capacidade():
    elevador = Elevador(5, 10)
    elevador.set_capacidade(7)
    assert elevador.get_capacidade() == 7

def test_set_pessoas_presentes():
    elevador = Elevador(5, 10)
    elevador.set_pessoas_presentes(3)
    assert elevador.get_pessoas_presentes() == 3