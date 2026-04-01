nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

aluno = {
    "nome": nome,
    "idade": idade
}

nota = float(input("Digite a nota: "))
aluno["nota"] = nota

print("Antes:", aluno)

nova_nota = float(input("Digite a nova nota: "))
aluno["nota"] = nova_nota

print("Depois:", aluno)