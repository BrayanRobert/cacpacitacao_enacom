def identifica_numeros_pares_e_impares() -> None:
    numeros = []
    for i in range(6):
        num = int(input(f"Digite o {i+1}º número: "))
        numeros.append(num)
    
    pares = []
    impares = []
    
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    
    print(f"Números pares: {pares}")
    print(f"Soma dos números pares: {sum(pares)}")
    print(f"Números ímpares: {impares}")
    print(f"Quantidade de números ímpares: {len(impares)}")

identifica_numeros_pares_e_impares()
