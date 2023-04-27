altura = float(input('Qual sua altura? '))
peso = float(input('Qual o seu peso? '))
imc = peso/(altura*altura)

if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc >= 18.6 and imc <= 24.9:
    print('Você está saudável!')
elif imc >= 25.0 and imc <= 29.9:
    print('Você está com peso em excesso!')
elif imc >= 30.0 and imc <= 34.9:
    print('Você está com obesidade grau I!')
elif imc >= 35.0 and imc <= 39.9:
    print('Você está com obesidade grau II!')
elif imc >= 40:
    print('Você está com obesidade grau III!')