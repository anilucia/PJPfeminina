#2. Solicite ao usuário que informe a sua idade e depois exiba se é maior ou menor de idade.

while True:
    idade = int(input("Digite a sua idade:"))
    if idade >= 18:
        print("Maior de idade")
    else:
        print("Menor de idade")
        
    finalizar = input("Deseja parar? (s/n)")
    if finalizar.lower() == 's':
        break
    