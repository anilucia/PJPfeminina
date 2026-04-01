n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))
n4 = int(input("Digite mais um número: "))

tupla = (n1, n2, n3, n4)

busca = int(input("Digite um número para contar: "))

quantidade = tupla.count(busca)

print("Aparece", quantidade, "vez(es)")