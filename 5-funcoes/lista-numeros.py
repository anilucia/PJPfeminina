#Crie uma função que receba uma lista de números e retorne o maior número da lista. 
def maior(lista):
    return max(lista)
numeros = []
for i in range(3):
    n = int(input("Digite um número: "))
    numeros.append(n)
print("Maior número:", maior(numeros))  
