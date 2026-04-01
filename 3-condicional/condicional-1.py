#Peça para o aluno digitar a idade de uma pessoa e o programa deve classificar:
# 0–12 → Criança
# 13–17 → Adolescente
# 18–59 → Adulto
# 60+ → Idoso

idade = int(input("Digite sua idade: "))
if idade >= 0 and idade <= 12: 
    print(" Você ainda é criança!")
elif idade >= 13 and idade <= 17:
    print("Você é adolescente!") 
elif idade >= 18 and idade <= 59:
    print("Você é adulto!")
else:
    print("Você é idoso!")       