import re
from armazenamento import armazenamento_json as armazenamento

def validar_contato():
    print("A FAZER...")


def validar_cpf(cpf):
    if re.match(r"^\d{11}$", cpf):  
        return True
    return False


def validar_idade(idade):
    return idade.isdigit() and int(idade) > 0



def listar_adotantes_por_cpf():
    cpf = int(input("Digite o CPF do adotante: \n"))
    adotante = armazenamento.ler_entrada(cpf, 'CPF', "adotantes.json")
    if isinstance(adotante, dict):
        print(adotante)



def cadastrar_adotante():
    while True:
        cpf = input("Digite o CPF (somente números, 11 dígitos): \n")
        if not validar_cpf(cpf):
            print("CPF inválido! Certifique-se de que está no formato correto (11 dígitos).\n")
            continue

        nome = input("Digite o nome completo: \n")
        idade = int(input("Digite a idade: \n"))
        if not validar_idade(idade):
            print("Idade inválida! Certifique-se que a idade é um número.\n")
            continue

        profissao = input("Digite a profissão: \n")
        endereco = input("Digite o endereço: \n")

        contato = int(input("Contato (somente números): "))
        if not validar_contato(contato):
            print("Contato inválido! Deve conter apenas números.")
            continue

        adotante = {
            "id": cpf,
            "nome": nome,
            "idade": idade,
            "profissao": profissao,
            "endereco": endereco,
            "contato": contato
        }

        armazenamento.criar_entrada(adotante, "adotantes.json")
        break

def atualizar_adotante():
    cpf = input("Digite o CPF do adotante: ")
    novos_dados = {
        "nome": input("Novo nome: "),
        "idade": input("Nova idade: "),
        "profissao": input("Nova profissão: "),
        "endereco": input("Novo endereço: "),
        "contato": input("Novo contato: ")
    }

    editar_entrada(cpf, novos_dados, "json-test.json")


def excluir_adotante():
    cpf = input("Digite o CPF do adotante a excluir: ")
    deletar_entrada(cpf, "json-test.json")


def menu():
    adotantes = carregar_dados()

    while True:
        print("\n===== MENU =====")
        print("1. Cadastrar adotante")
        print("2. Listar adotantes")
        print("3. Atualizar adotante")
        print("4. Excluir adotante")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_adotante(adotantes)
        elif opcao == "2":
            listar_adotantes_por_cpf(adotantes)
        elif opcao == "3":
            atualizar_adotante(adotantes)
        elif opcao == "4":
            excluir_adotante(adotantes)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if _name_ == "_main_":
    menu()