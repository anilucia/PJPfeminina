notas = []

for i in range(3):
    n = float(input("Digite uma nota: "))
    notas.append(n)

media = sum(notas) / len(notas)
print("Média inicial:", media)

menor = min(notas)
indice = notas.index(menor)

nova = float(input("Digite uma nova nota para substituir a menor: "))
notas[indice] = nova

notas.sort()

media_nova = sum(notas) / len(notas)

print("Lista final:", notas)
print("Nova média:", media_nova)