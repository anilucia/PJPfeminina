fruta1 = input("Digite uma fruta: ")
fruta2 = input("Digite outra fruta: ")
fruta3 = input("Digite mais uma fruta: ")

tupla = (fruta1, fruta2, fruta3)

busca = input("Digite uma fruta para buscar: ")

if busca in tupla:
    print("Está na tupla")
else:
    print("Não está na tupla")