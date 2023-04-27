from atividade3.ex2 import Agenda

def test_armazenar_pessoa():
    agenda = Agenda()
    pessoa = "João"
    agenda.armazenar_pessoa(pessoa)
    assert agenda.buscar_pessoa(0) == pessoa

def test_remover_pessoa():
    agenda = Agenda()
    pessoa1 = "João"
    pessoa2 = "Maria"
    agenda.armazenar_pessoa(pessoa1)
    agenda.armazenar_pessoa(pessoa2)
    agenda.remover_pessoa(pessoa1)
    assert agenda.buscar_pessoa(0) == None
    assert agenda.buscar_pessoa(1) == pessoa2

def test_buscar_pessoa():
    agenda = Agenda()
    pessoa1 = "João"
    pessoa2 = "Maria"
    agenda.armazenar_pessoa(pessoa1)
    agenda.armazenar_pessoa(pessoa2)
    assert agenda.buscar_pessoa(0) == pessoa1
    assert agenda.buscar_pessoa(1) == pessoa2
    assert agenda.buscar_pessoa(2) == None

def test_imprimir_agenda(capfd):
    agenda = Agenda()
    pessoa1 = "João"
    pessoa2 = "Maria"
    agenda.armazenar_pessoa(pessoa1)
    agenda.armazenar_pessoa(pessoa2)
    agenda.imprimir_agenda()
    out, _ = capfd.readouterr()
    expected_output = "Posição: 0 - João\nPosição: 1 - Maria\nPosição: 2 - Vazia\nPosição: 3 - Vazia\nPosição: 4 - Vazia\nPosição: 5 - Vazia\nPosição: 6 - Vazia\nPosição: 7 - Vazia\nPosição: 8 - Vazia\nPosição: 9 - Vazia\n"
    assert out == expected_output

def test_imprimir_pessoa(capfd):
    agenda = Agenda()
    pessoa = "João"
    agenda.armazenar_pessoa(pessoa)
    agenda.imprimir_pessoa(0)
    out, _ = capfd.readouterr()
    expected_output = "Posição: 0 - João\n"
    assert out == expected_output