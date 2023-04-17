a = int(input("Escreva um número: "))
b = int(input("Escreva outro número: "))

count = 0

for num in range(a, b + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            count += 1

print(f"Existem {count} números primos entre {a} e {b}")
