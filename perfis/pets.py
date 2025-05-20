import json
import os

arquivo = os.path.join(os.path.dirname(__file__), 'pets.json')

def carregar_pets():
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump([], f, indent=4)

    with open(arquivo, 'r') as f:
        try:
            conteudo = f.read().strip()
            if not conteudo:
                return []
            return json.loads(conteudo)
        except json.JSONDecodeError:
            print("⚠️ Arquivo JSON corrompido. Redefinindo...")
            return []

def salvar_pets(pets):
    with open(arquivo, 'w') as f:
        json.dump(pets, f, indent=4, ensure_ascii=False)

def gerar_novo_id(pets):
    if not pets:
        return 1
    return max(pet['id'] for pet in pets) + 1

def adicionar_pet():
    pets = carregar_pets()
    novo_id = gerar_novo_id(pets)

    print("TIPO DO PET:")
    print("1 - Canino")
    print("2 - Felino")
    tipo_opcao = input(">>> ")
    tipo = "canino" if tipo_opcao == "1" else "felino" if tipo_opcao == "2" else "não especificado"

    nome = input("DIGITE O NOME DO PET:\n>>> ")
    idade = input("DIGITE A IDADE DO PET:\n>>> ")

    print("SEXO:")
    print("1 - Macho")
    print("2 - Fêmea")
    sexo_opcao = input(">>> ")
    sexo = "M" if sexo_opcao == "1" else "F" if sexo_opcao == "2" else "não especificado"

    print("PERSONALIDADE:")
    print("1 - Brincalhão")
    print("2 - Calmo")
    print("3 - Protetor")
    print("4 - Dócil")
    personalidade_opcao = input(">>> ")
    opcoes_personalidade = {
        "1": "Brincalhão",
        "2": "Calmo",
        "3": "Protetor",
        "4": "Dócil"
    }
    personalidade = opcoes_personalidade.get(personalidade_opcao, "não especificado")

    print("HISTÓRICO VETERINÁRIO/VACINAL:")
    print("1 - Tudo em dia")
    print("2 - Faltando")
    historico_opcao = input(">>> ")
    opcoes_historico = {
        "1": "Tudo em dia",
        "2": "Faltando"
    }
    historico = opcoes_historico.get(historico_opcao, "não especificado")

    raca = input("DIGITE A RAÇA:\n>>> ")
    cor = input("DIGITE A COR PREDOMINANTE:\n>>> ")

    print("PORTE:")
    print("1 - Pequeno")
    print("2 - Médio")
    print("3 - Grande")
    porte_opcao = input(">>> ")
    opcoes_porte = {
        "1": "pequeno",
        "2": "médio",
        "3": "grande"
    }
    porte = opcoes_porte.get(porte_opcao, "não especificado")

    pet_novo = {
        "id": novo_id,
        "tipo": tipo,
        "nome": nome,
        "idade": idade,
        "sexo": sexo,
        "personalidade": personalidade,
        "historico": historico,
        "raca": raca,
        "cor": cor,
        "porte": porte
    }

    pets.append(pet_novo)
    salvar_pets(pets)

    print("PET ADICIONADO COM SUCESSO!")

def atualizar_pet():
    pets = carregar_pets()

    if not pets:
        print("Nenhum pet cadastrado para atualizar.")
        return

    try:
        id_atualizar = int(input("DIGITE O ID DO PET A SER ATUALIZADO:\n>>> "))
    except ValueError:
        print("ID inválido. Deve ser um número.")
        return

    pet = next((p for p in pets if p['id'] == id_atualizar), None)

    if pet is None:
        print("Pet com esse ID não encontrado.")
        return

    while True:
        print(f"\nAtualizando pet: {pet['nome']} (ID {pet['id']})")
        print("Escolha o campo para atualizar:")
        print("1 - Tipo (Canino/Felino)")
        print("2 - Nome")
        print("3 - Idade")
        print("4 - Sexo (M/F)")
        print("5 - Personalidade")
        print("6 - Histórico Veterinário/Vacinal")
        print("7 - Raça")
        print("8 - Cor Predominante")
        print("9 - Porte")
        print("0 - Sair da atualização")

        opcao = input(">>> ")

        if opcao == "0":
            print("Saindo da atualização.")
            break

        if opcao == "1":
            print("TIPO DO PET:")
            print("1 - Canino")
            print("2 - Felino")
            tipo_opcao = input(">>> ")
            pet['tipo'] = "canino" if tipo_opcao == "1" else "felino" if tipo_opcao == "2" else pet['tipo']
            print(f"Tipo atualizado para: {pet['tipo']}")
        elif opcao == "2":
            novo_nome = input(f"Novo nome (atual: {pet['nome']}):\n>>> ")
            if novo_nome.strip():
                pet['nome'] = novo_nome
                print(f"Nome atualizado para: {pet['nome']}")
        elif opcao == "3":
            nova_idade = input(f"Nova idade (atual: {pet['idade']}):\n>>> ")
            if nova_idade.strip():
                pet['idade'] = nova_idade
                print(f"Idade atualizada para: {pet['idade']}")
        elif opcao == "4":
            print("SEXO:")
            print("1 - Macho")
            print("2 - Fêmea")
            sexo_opcao = input(">>> ")
            if sexo_opcao == "1":
                pet['sexo'] = "M"
            elif sexo_opcao == "2":
                pet['sexo'] = "F"
            print(f"Sexo atualizado para: {pet['sexo']}")
        elif opcao == "5":
            print("PERSONALIDADE:")
            print("1 - Brincalhão")
            print("2 - Calmo")
            print("3 - Protetor")
            print("4 - Dócil")
            personalidade_opcao = input(">>> ")
            opcoes_personalidade = {
                "1": "Brincalhão",
                "2": "Calmo",
                "3": "Protetor",
                "4": "Dócil"
            }
            pet['personalidade'] = opcoes_personalidade.get(personalidade_opcao, pet['personalidade'])
            print(f"Personalidade atualizada para: {pet['personalidade']}")
        elif opcao == "6":
            print("HISTÓRICO VETERINÁRIO/VACINAL:")
            print("1 - Tudo em dia")
            print("2 - Faltando")
            historico_opcao = input(">>> ")
            opcoes_historico = {
                "1": "Tudo em dia",
                "2": "Faltando"
            }
            pet['historico'] = opcoes_historico.get(historico_opcao, pet['historico'])
            print(f"Histórico atualizado para: {pet['historico']}")
        elif opcao == "7":
            nova_raca = input(f"Nova raça (atual: {pet['raca']}):\n>>> ")
            if nova_raca.strip():
                pet['raca'] = nova_raca
                print(f"Raça atualizada para: {pet['raca']}")
        elif opcao == "8":
            nova_cor = input(f"Nova cor predominante (atual: {pet['cor']}):\n>>> ")
            if nova_cor.strip():
                pet['cor'] = nova_cor
                print(f"Cor atualizada para: {pet['cor']}")
        elif opcao == "9":
            print("PORTE:")
            print("1 - Pequeno")
            print("2 - Médio")
            print("3 - Grande")
            porte_opcao = input(">>> ")
            opcoes_porte = {
                "1": "pequeno",
                "2": "médio",
                "3": "grande"
            }
            pet['porte'] = opcoes_porte.get(porte_opcao, pet['porte'])
            print(f"Porte atualizado para: {pet['porte']}")
        else:
            print("Opção inválida.")

        salvar_pets(pets)

        continuar = input("Deseja continuar editando esse pet? (s/n)\n>>> ").lower()
        if continuar != 's':
            print("Finalizando edição do pet.")
            break

def listar_pets():
    pets = carregar_pets()
    if not pets:
        print("Nenhum pet cadastrado.")
        return
    print("="*50)
    print("LISTA DE PETS:")
    for pet in pets:
        print("-"*50)
        print(f"ID: {pet['id']}")
        print(f"Tipo: {pet['tipo']}")
        print(f"Nome: {pet['nome']}")
        print(f"Idade: {pet['idade']}")
        print(f"Sexo: {pet['sexo']}")
        print(f"Personalidade: {pet['personalidade']}")
        print(f"Histórico: {pet['historico']}")
        print(f"Raça: {pet['raca']}")
        print(f"Cor: {pet['cor']}")
        print(f"Porte: {pet['porte']}")
    print("="*50)

def deletar_pet():
    pets = carregar_pets()
    if not pets:
        print("Nenhum pet cadastrado para deletar.")
        return

    try:
        id_deletar = int(input("Digite o ID do pet que deseja deletar:\n>>> "))
    except ValueError:
        print("ID inválido.")
        return

    pet = next((p for p in pets if p['id'] == id_deletar), None)

    if pet is None:
        print("Pet com esse ID não encontrado.")
        return

    pets.remove(pet)
    salvar_pets(pets)
    print(f"Pet {pet['nome']} (ID {pet['id']}) deletado com sucesso!")

def main():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1 - Adicionar pet")
        print("2 - Listar pets")
        print("3 - Atualizar pet")
        print("4 - Deletar pet")
        print("5 - Sair")
        opcao = input("Escolha uma opção:\n>>> ")

        if opcao == "1":
            adicionar_pet()
        elif opcao == "2":
            listar_pets()
        elif opcao == "3":
            atualizar_pet()
        elif opcao == "4":
            deletar_pet()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
