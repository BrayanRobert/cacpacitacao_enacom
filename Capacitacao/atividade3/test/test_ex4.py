from atividade3.ex4 import *

def test_aumentar_volume():
    televisao = Televisao()
    televisao.aumentar_volume()
    assert televisao.volume == 51

def test_diminuir_volume():
    televisao = Televisao()
    televisao.diminuir_volume()
    assert televisao.volume == 49

def test_trocar_canal():
    televisao = Televisao()
    televisao.trocar_canal(5)
    assert televisao.canal == 5

def test_aumentar_canal():
    televisao = Televisao()
    televisao.aumentar_canal()
    assert televisao.canal == 2

def test_diminuir_canal():
    televisao = Televisao()
    televisao.diminuir_canal()
    assert televisao.canal == 1

# Teste da classe ControleRemoto
def test_aumentar_volume_controle():
    televisao = Televisao()
    controle = ControleRemoto(televisao)
    controle.aumentar_volume()
    assert controle.consultar_volume() == 51

def test_diminuir_volume_controle():
    televisao = Televisao()
    controle = ControleRemoto(televisao)
    controle.diminuir_volume()
    assert controle.consultar_volume() == 49

def test_trocar_canal_controle():
    televisao = Televisao()
    controle = ControleRemoto(televisao)
    controle.trocar_canal(5)
    assert controle.consultar_canal() == 5

def test_aumentar_canal_controle():
    televisao = Televisao()
    controle = ControleRemoto(televisao)
    controle.aumentar_canal()
    assert controle.consultar_canal() == 2

def test_diminuir_canal_controle():
    televisao = Televisao()
    controle = ControleRemoto(televisao)
    controle.diminuir_canal()
    assert controle.consultar_canal() == 1