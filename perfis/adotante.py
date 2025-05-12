'''
CRUD DE ADOTANTES
'''
def cadastrar_adotante(lista):
    adotante = {
        "cpf": input("CPF: "),
        "nome": input("Nome completo: "),
        "idade": int(input("Idade: ")),
        "profissao": input("Profissão: "),
        "endereco": input("Endereço: "),
        "tipo_preferido": input("Tipo (felino/canino): "),
        "idade_preferida": int(input("Idade preferida do animal: ")),
        "sexo_preferido": input("Sexo preferido (macho/fêmea): "),
        "personalidade_preferida": input("Personalidade preferida: "),
        "contato": input("Contato: ")
    }
    lista.append(adotante)
    print("Adotante cadastrado com sucesso!")

def listar_adotantes(lista):
    for adotante in lista:
        print(adotante)

def atualizar_adotante(lista, cpf):
    for adotante in lista:
        if adotante["cpf"] == cpf:
            adotante["nome"] = input("Novo nome: ")
            # repetir para os demais campos...
            print("Adotante atualizado!")
            return
    print("CPF não encontrado.")

def excluir_adotante(lista, cpf):
    for adotante in lista:
        if adotante["cpf"] == cpf:
            lista.remove(adotante)
            print("Adotante removido.")
            return
    print("CPF não encontrado.")