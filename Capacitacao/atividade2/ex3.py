def gera_matriz() -> None:
    matriz = []
    
    for i in range(10):
        linha = []
        for j in range(10):
            if i < j:
                valor = 2 * i + 7 * j - 2
            elif i == j:
                valor = 3 * i ** 2 - 1
            else:
                valor = 4 * i ** 3 - 5 * j ** 2 + 1
            linha.append(valor)
        matriz.append(linha)
    
    for linha in matriz:
        print(linha)

gera_matriz()
