def ler_dados(habitantes: dict) -> None:
    for i in range(len(habitantes)):
        print(f"Habitante {i+1}:")
        habitantes[i]["sexo"] = input("Sexo (M ou F): ")
        habitantes[i]["olhos"] = input("Cor dos olhos (A - Azuis, C - Castanhos ou V - Verdes): ")
        habitantes[i]["cabelos"] = input("Cor dos cabelos (B - Brancos, L - Louros, P - Pretos ou C - Castanhos): ")
        habitantes[i]["idade"] = int(input("Idade: "))
    print("Dados lidos com sucesso!")

def media_idade_olhos_castanhos_cabelos_pretos(habitantes: dict) -> float:
    soma_idades = 0
    qtde_pessoas = 0
    for h in habitantes:
        if h["olhos"] == "C" and h["cabelos"] == "P":
            soma_idades += h["idade"]
            qtde_pessoas += 1
    if qtde_pessoas == 0:
        return 0
    else:
        return soma_idades/qtde_pessoas

def menor_idade_cabelos_brancos(habitantes: dict) -> int:
    menor_idade = float("inf")
    for h in habitantes:
        if h["cabelos"] == "B" and h["idade"] < menor_idade:
            menor_idade = h["idade"]
    if menor_idade == float("inf"):
        return 0
    else:
        return menor_idade

def maior_idade(habitantes: dict) -> int:
    maior_idade = 0
    for h in habitantes:
        if h["idade"] > maior_idade:
            maior_idade = h["idade"]
    return maior_idade

def qtde_mulheres_18_35_olhos_verdes_cabelos_castanhos(habitantes: dict) -> int:
    qtde_mulheres = 0
    for h in habitantes:
        if h["sexo"] == "F" and h["idade"] >= 18 and h["idade"] <= 35 and h["olhos"] == "V" and h["cabelos"] == "C":
            qtde_mulheres += 1
    return qtde_mulheres


habitantes = [
    {"sexo": "", "olhos": "", "cabelos": "", "idade": 0} for i in range(10)
]

ler_dados(habitantes)

print(f"Média de idade das pessoas com olhos castanhos e cabelos pretos: {media_idade_olhos_castanhos_cabelos_pretos(habitantes)}")

print(f"Menor idade de quem possui cabelos brancos: {menor_idade_cabelos_brancos(habitantes)}")

print(f"Maior idade entre os habitantes: {maior_idade(habitantes)}")

print(f"Quantidade de mulheres entre 18 e 35 anos com olhos verdes e cabelos castanhos: {qtde_mulheres_18_35_olhos_verdes_cabelos_castanhos(habitantes)}")
