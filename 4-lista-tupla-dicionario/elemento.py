lista = []

for i in range(3):
    numero = int(input("Digite um número: "))
    lista.append(numero)

lista[2] = lista[0] + lista[1]

print("Lista final:", lista)