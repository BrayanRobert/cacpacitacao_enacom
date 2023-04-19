def soma_matrizes(m1: list, m2: list) -> list:
    m3 = []
    for i in range(2):
        linha = []
        for j in range(2):
            valor = m1[i][j] + m2[i][j]
            linha.append(valor)
        m3.append(linha)
    return m3

def subtrai_matrizes(m1: list, m2: list) -> list:
    m3 = []
    for i in range(2):
        linha = []
        for j in range(2):
            valor = m2[i][j] - m1[i][j]
            linha.append(valor)
        m3.append(linha)
    return m3

def adiciona_constante(m: list, constante: int) -> list:
    for i in range(2):
        for j in range(2):
            m[i][j] += constante
    return m

def imprime_matriz(m: list) -> list:
    for linha in m:
        print(linha)

# lê a primeira matriz
m1 = []
print("Digite os valores da primeira matriz:")
for i in range(2):
    linha = []
    for j in range(2):
        valor = float(input(f"Digite o valor de A[{i}][{j}]: "))
        linha.append(valor)
    m1.append(linha)

# lê a segunda matriz
m2 = []
print("\nDigite os valores da segunda matriz:")
for i in range(2):
    linha = []
    for j in range(2):
        valor = float(input(f"Digite o valor de B[{i}][{j}]: "))
        linha.append(valor)
    m2.append(linha)

# loop principal
while True:
    print("\nEscolha uma opção:")
    print("1 - Somar as duas matrizes")
    print("2 - Subtrair a primeira matriz da segunda")
    print("3 - Adicionar uma constante às duas matrizes")
    print("4 - Imprimir as matrizes")
    print("0 - Sair")
    opcao = int(input("> "))

    if opcao == 0:
        break

    if opcao == 1:
        m3 = soma_matrizes(m1, m2)
        print("\nResultado da soma:")
        imprime_matriz(m3)

    elif opcao == 2:
        m3 = subtrai_matrizes(m1, m2)
        print("\nResultado da subtração:")
        imprime_matriz(m3)

    elif opcao == 3:
        constante = float(input("\nDigite a constante a ser adicionada: "))
        m1 = adiciona_constante(m1, constante)
        m2 = adiciona_constante(m2, constante)
        print("\nAs duas matrizes foram atualizadas.")

    elif opcao == 4:
        print("\nMatriz A:")
        imprime_matriz(m1)
        print("\nMatriz B:")
        imprime_matriz(m2)

    else:
        print("\nOpção inválida. Tente novamente.")
