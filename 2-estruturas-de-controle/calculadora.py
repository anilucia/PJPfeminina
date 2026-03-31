#6. Faça uma calculadora simples contendo as operações: soma, subtração, divisão e multiplicação. Solicite ao usuário que informe dois número e que informe também a operação que deseja realizar (+, -, /, *) e depois exiba o resultado.

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
op = input("Digite a operação (+, -, *, /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b != 0:
        print(a / b)
    else:
        print("Não pode dividir por zero")
else:
    print("Operação inválida")