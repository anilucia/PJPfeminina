#1. Solicite ao usuário que informe um número e depois exiba se o número é positivo, negativo ou zero.

while True:
    numero = int(input("Digite um número: "))
    if numero > 0:
            print("Número positivo")
    else:
        if numero == 0:
            print("Número é igual a zero")
        else:
            print("Número negativo")
    
