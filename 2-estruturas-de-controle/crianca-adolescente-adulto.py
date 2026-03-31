#3. Solicite ao usuário que informe a sua idade e depois classifique.

idade = int(input("Digite sua idade: "))

if idade <= 11:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")