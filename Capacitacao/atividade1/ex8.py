from num2words import num2words

total = 0

for i in range(1000):
    numero = i+1
    num_ptbr = num2words(numero, lang='pt-br')
    quantidade = len(num_ptbr)
    total += quantidade

print(total)