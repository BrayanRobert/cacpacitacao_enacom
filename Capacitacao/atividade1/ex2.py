salario_atual = int(input('Qual seu salário atual? '))
tempo_servico = int(input('Quantos anos você trabalha na empresa? '))

if salario_atual < 500:
    reajuste = 0.25
elif salario_atual >= 500 and salario_atual < 1000:
    reajuste = 0.20
elif salario_atual >= 1000 and salario_atual < 1500:
    reajuste = 0.15
elif salario_atual >= 1500 and salario_atual < 2000:
    reajuste = 0.10
elif salario_atual > 2000:
    reajuste = 0

if tempo_servico < 1:
    bonus = 0
elif tempo_servico >= 1 and tempo_servico <= 3:
    bonus = 100
elif tempo_servico >= 4 and tempo_servico <= 6:
    bonus = 200
elif tempo_servico >= 7 and tempo_servico <= 10:
    bonus = 300
elif tempo_servico > 10:
    bonus = 500

if reajuste == 0:
    print(f'Você não ganhou reajuste de salário! permanece {salario_atual}')
    print(f'Você ganhou {bonus} por {tempo_servico} de tempo de serviço!')
    print(f'Você ganhou ao todo: {salario_atual + bonus}')
else:
    print(f'Você ganhou {salario_atual*reajuste} de reajuste no salário')
    print(f'Você ganhou {bonus} por {tempo_servico} de tempo de serviço!')
    print(f'Você ganhou ao todo: {salario_atual + bonus + (salario_atual*reajuste)}')