#Crie uma função que receba uma string e retorne a quantidade de caracteres que ela possui.
def tamanho(texto):
    return len(texto)
texto = input("Digite uma palavra: ")
print("Quantidade de caracteres:", tamanho(texto))