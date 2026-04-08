#Crie uma função que receba um número e informe se ele é PAR ou ÍMPAR. 
def par_ou_impar(numero):
    if numero % 2 == 0:
         print("Par")
    else:
        print("Ímpar")
num = int(input("Digite um número: "))  
resultado = par_ou_impar(num)

