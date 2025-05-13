import json
import re


CAMINHO_ARQUIVO = "adotantes.json"


def carregar_dados():
    try:
        with open(CAMINHO_ARQUIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def salvar_dados(adotantes):
    with open(CAMINHO_ARQUIVO, "w") as f:
        json.dump(adotantes, f, indent=4)


def validar_cpf(cpf):
    if re.match(r"^\d{11}$", cpf):  
        return True
    return False


def validar_idade(idade):
    return idade.isdigit() and int(idade) > 0


def validar_contato(contato):
    return contato.isdigit()


def cadastrar_adotante(adotantes):
    while True:
        cpf = input("CPF (somente números, 11 dígitos): ")
        if not validar_cpf(cpf):
            print("CPF inválido! Certifique-se de que está no formato correto (11 dígitos).")
            continue

        nome = input("Nome completo: ")
        idade = input("Idade: ")
        if not validar_idade(idade):
            print("Idade inválida! Deve ser um número.")
            continue

        profissao = input("Profissão: ")
        endereco = input("Endereço: ")

        contato = input("Contato (somente números): ")
        if not validar_contato(contato):
            print("Contato inválido! Deve conter apenas números.")
            continue

        adotante = {
            "cpf": cpf,
            "nome": nome,
            "idade": int(idade),
            "profissao": profissao,
            "endereco": endereco,
            "contato": contato
        }

        adotantes.append(adotante)
        salvar_dados(adotantes)
        print("Adotante cadastrado com sucesso!")
        break


def listar_adotantes(adotantes):
    if not adotantes:
        print("Nenhum adotante cadastrado.")
    else:
        for adotante in adotantes:
            print(f"Nome: {adotante['nome']}, CPF: {adotante['cpf']}, Profissão: {adotante['profissao']}")


def atualizar_adotante(adotantes):
    cpf = input("Informe o CPF do adotante a ser atualizado: ")
    for adotante in adotantes:
        if adotante['cpf'] == cpf:
            adotante["nome"] = input("Novo nome: ")
            adotante["idade"] = input("Nova idade: ")
            if not validar_idade(adotante["idade"]):
                print("Idade inválida! Deve ser um número inteiro positivo.")
                return

            adotante["profissao"] = input("Nova profissão: ")
            adotante["endereco"] = input("Novo endereço: ")
            adotante["contato"] = input("Novo contato (somente números): ")
            if not validar_contato(adotante["contato"]):
                print("Contato inválido! Deve conter apenas números.")
                return

            salvar_dados(adotantes)
            print("Adotante atualizado com sucesso!")
            return
    print("Adotante não encontrado!")


def excluir_adotante(adotantes):
    cpf = input("Informe o CPF do adotante a ser excluído: ")
    for adotante in adotantes:
        if adotante['cpf'] == cpf:
            adotantes.remove(adotante)
            salvar_dados(adotantes)
            print("Adotante excluído com sucesso!")
            return
    print("Adotante não encontrado!")


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
            listar_adotantes(adotantes)
        elif opcao == "3":
            atualizar_adotante(adotantes)
        elif opcao == "4":
            excluir_adotante(adotantes)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()
