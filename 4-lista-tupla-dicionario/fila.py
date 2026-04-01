fila = ["Ana", "Bruno"]

# adicionar 2 nomes
n1 = input("Digite um nome: ")
n2 = input("Digite outro nome: ")
fila.extend([n1, n2])

print("Fila atual:", fila)

# cliente prioritário
prioritario = input("Digite nome prioritário: ")
fila.insert(1, prioritario)

print("Fila com prioridade:", fila)

# atender (remover o primeiro)
atendido = fila.pop(0)

print("Atendido:", atendido)
print("Fila final:", fila)