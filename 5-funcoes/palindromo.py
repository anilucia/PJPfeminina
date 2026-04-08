#Crie uma função que receba uma palavra e verifique se ela é um palíndromo
def palindromo(palavra):
    if palavra == palavra[::-1]:
        print("É palíndromo")
    else:
        print("Não é palíndromo")
palavra = input("Digite uma palavra: ")
palindromo(palavra)