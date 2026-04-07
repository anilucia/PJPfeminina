#Crie uma função que receba um nome como parâmetro e exiba a mensagem:'Bem-vindo, NOME' 
def boas_vindas(nome):
    print("Bem-vindo," , nome)
nome = input("Digite seu nome: ")
boas_vindas(nome)