#Crie uma função que receba uma lista de números e retorne a média dos valores.
def media(lista):
    return sum(lista) / len(lista)
numeros = []
for i in range(3):
    n = int(input("Digite um número: "))
    numeros.append(n)
print("Média:", media(numeros))