agenda = {
    "Ana": "1111-1111",
    "Bruno": "2222-2222"
}

# ADICIONAR CONTATO
nome = input("Digite o nome para adicionar: ")
telefone = input("Digite o telefone: ")
agenda[nome] = telefone

print("Agenda após adicionar:", agenda)

# ATUALIZAR CONTATO
nome_att = input("Digite o nome para atualizar: ")

if nome_att in agenda:
    novo_tel = input("Digite o novo telefone: ")
    agenda[nome_att] = novo_tel
    print("Atualizado!")
else:
    print("Contato não encontrado")