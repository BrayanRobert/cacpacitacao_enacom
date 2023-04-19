def conta_valores_maiores_que_10() -> None:
    matriz = []
    contador = 0
    
    for i in range(5):
        linha = []
        for j in range(5):
            valor = int(input(f"Digite o valor da posição [{i}][{j}]: "))
            linha.append(valor)
            if valor > 10:
                contador += 1
        matriz.append(linha)
    
    print(f"A matriz é: {matriz}")
    print(f"A quantidade de valores maiores que 10 é: {contador}")

conta_valores_maiores_que_10()
