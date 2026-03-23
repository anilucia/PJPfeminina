
'''Solicite ao usuário que informe o saldo da sua conta e o valor que será depositado; ambos os valores devem ser 
do tipo FLOAT. Utilize atribuição += para adicionar o deposito ao saldo da conta e exiba o novo saldo na tela. '''

# saldo_conta = float(input("Digite o valor da conta "))
# saldo_conta += float(input("Digite o valor do deposito "))
# print(f'O saldo da sua conta é : R$ {saldo_conta}')


'''Solicite ao usuário que informe um orçamento (float) e um gasto (float). Utilize atribuição -= para descontar o gasto do orçamento.'''

# orcamento = float(input("Informe seu orcamento "))
# orcamento -= float(input("Informe um gasto "))
# print("O orcamento com deconto do gasto é:", orcamento)


'''Solicite ao usuário que informe o estoque no início do dia (int) e a quantidade vendida ao final do dia (int). 
Atualize a quantidade utilizando atribuição -= para mostrar o estoque final.'''

# estoque = float(input("Digite o estoque do inicio do dia: "))
# estoque -= float(input("Digite a quantidade vendida do final do dia: "))
# print("O estoque do final do dia é:", estoque)


'''Solicite ao usuário que informe um número (int) e multiplique por 3 utilizando atribuição *=.'''

# numero = int(input("Digite um número: "))
# numero *= 3
# print("O resultado é:", numero)


'''Solicite ao usuário que informe uma quantidade de horas e converta para dias utilizando /= 24.'''

# horas = float(input("Digite a quantidade de horas: "))
# horas /=24
# print("Isso equivale a", horas, "dias")


'''Solicite ao usuário que informe minutos (int) e transforme em horas inteiras utilizando //= 60.'''

# minutos = int(input("Digite minutos: "))
# minutos //=60
# print("Isso equivale a", minutos, "hora")


'''Solicite ao usuário que informe uma quantidade de segundos e depois transforme em minutos inteiros utilizando //=60.'''

# segundos = int(input("Digite segundos: "))
# segundos //=60
# print("Isso equivale a", segundos, "minuto")


'''Solicite um número (int), aplique n %= 2 e exiba o valor na tela. Se o resultado for 0, o número é par; se o resultado for 1, o número é ímpar.'''

# n = int(input("Digite um numero: "))
# if n % 2 == 0:
#  print("Par")
# else:
#  print("impar")


'''Solicite um valor de estoque (int), subtraia as vendas utilizando -= e depois a reposição do estoque utilizando +=, por fim, aplique %= 6.''' 

# est = int(input("Digite o valor do estoque: "))
# vendas = int(input("Digite o total de vendas: "))
# est -= vendas
# reposição = int(input("Digite o valor de reposição: "))
# est += reposição
# est %= 6
# print("Valor final: ", est)


'''Solicite ao usuário que informe os tempos em segundos (int). Converta para minutos inteiros com //= e depois use %= para obter segundos restantes.'''

# segundos = int(input("Digite o tempo em segundos: "))
# minutos = segundos // 60
# segundos_restantes = segundos % 60
# print("Isso equivale a", minutos, "minutos e", segundos_restantes, "segundos")


'''Solicite ao usuário uma distância em metros e depois converta para km inteiros com //= 1000, guarde os metros restantes utilizando %= (utilize outra variável).'''

metros = int(input("Digite a distância em metros: "))
km = metros // 1000
metros_restantes = metros % 1000
print("Isso equivale a", km, "km e", metros_restantes, "metros")