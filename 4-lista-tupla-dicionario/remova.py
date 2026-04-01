lista = []

for i in range(4):
    numero = int(input("Digite um número: "))
    lista.append(numero)

print("Lista:", lista)
print("Tamanho antes:", len(lista))

alvo = int(input("Digite um número para remover: "))

if alvo in lista:
    lista.remove(alvo)
    print("Removido!")
else:
    print("Número não está na lista")

print("Lista final:", lista)
print("Tamanho depois:", len(lista))