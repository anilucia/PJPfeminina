#5. Solicite ao usuário que informe dois números e depois exiba qual número é maior ou se são iguais.

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

if a > b:
    print("O primeiro número é maior")
elif b > a:
    print("O segundo número é maior")
else:
    print("Os números são iguais")