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

    while True:
        print("TIPO DO PET:")
        print("1 - Canino")
        print("2 - Felino")
        tipo_opcao = input(">>> ")
        if tipo_opcao == "1":
            tipo = "canino"
            break
        elif tipo_opcao == "2":
            tipo = "felino"
            break
        else:
            print("Opção inválida. Tente novamente.")

    nome = input("DIGITE O NOME DO PET:\n>>> ")
    idade = input("DIGITE A IDADE DO PET:\n>>> ")

    while True:
        print("SEXO:")
        print("1 - Macho")
        print("2 - Fêmea")
        sexo_opcao = input(">>> ")
        if sexo_opcao == "1":
            sexo = "M"
            break
        elif sexo_opcao == "2":
            sexo = "F"
            break
        else:
            print("Opção inválida. Tente novamente.")

    opcoes_personalidade = {
        "1": "Brincalhão",
        "2": "Calmo",
        "3": "Protetor",
        "4": "Dócil"
    }
    while True:
        print("PERSONALIDADE:")
        for k, v in opcoes_personalidade.items():
            print(f"{k} - {v}")
        personalidade_opcao = input(">>> ")
        if personalidade_opcao in opcoes_personalidade:
            personalidade = opcoes_personalidade[personalidade_opcao]
            break
        else:
            print("Opção inválida. Tente novamente.")

    opcoes_historico = {
        "1": "Tudo em dia",
        "2": "Faltando"
    }
    while True:
        print("HISTÓRICO VETERINÁRIO/VACINAL:")
        for k, v in opcoes_historico.items():
            print(f"{k} - {v}")
        historico_opcao = input(">>> ")
        if historico_opcao in opcoes_historico:
            historico = opcoes_historico[historico_opcao]
            break
        else:
            print("Opção inválida. Tente novamente.")

    raca = input("DIGITE A RAÇA:\n>>> ")
    cor = input("DIGITE A COR PREDOMINANTE:\n>>> ")

    opcoes_porte = {
        "1": "pequeno",
        "2": "médio",
        "3": "grande"
    }
    while True:
        print("PORTE:")
        for k, v in opcoes_porte.items():
            print(f"{k} - {v}")
        porte_opcao = input(">>> ")
        if porte_opcao in opcoes_porte:
            porte = opcoes_porte[porte_opcao]
            break
        else:
            print("Opção inválida. Tente novamente.")

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

def filtrar_pets():
    pets = carregar_pets()
    if not pets:
        print("Nenhum pet cadastrado para filtrar.")
        return

    filtros = {}

    def menu_filtrar():
        while True:
            print("\nESCOLHA UM CRITÉRIO PARA FILTRAR:")
            print("1 - Tipo (canino/felino)")
            print("2 - Sexo (M/F)")
            print("3 - Porte (pequeno/médio/grande)")
            print("4 - Personalidade")
            print("5 - Histórico Veterinário/Vacinal")
            print("6 - Raça")
            print("7 - Cor")
            print("0 - Finalizar filtros")
            opcao = input(">>> ")
            if opcao in {"0", "1", "2", "3", "4", "5", "6", "7"}:
                return opcao
            else:
                print("Opção inválida. Tente novamente.")

    while True:
        opcao = menu_filtrar()
        if opcao == "0":
            break

        elif opcao == "1":
            while True:
                print("TIPO:")
                print("1 - Canino")
                print("2 - Felino")
                escolha = input(">>> ")
                if escolha == "1":
                    filtros["tipo"] = "canino"
                    break
                elif escolha == "2":
                    filtros["tipo"] = "felino"
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "2":
            while True:
                print("SEXO:")
                print("1 - Macho")
                print("2 - Fêmea")
                escolha = input(">>> ")
                if escolha == "1":
                    filtros["sexo"] = "M"
                    break
                elif escolha == "2":
                    filtros["sexo"] = "F"
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "3":
            while True:
                print("PORTE:")
                print("1 - Pequeno")
                print("2 - Médio")
                print("3 - Grande")
                escolha = input(">>> ")
                opcoes = {"1": "pequeno", "2": "médio", "3": "grande"}
                if escolha in opcoes:
                    filtros["porte"] = opcoes[escolha]
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "4":
            while True:
                print("PERSONALIDADE:")
                print("1 - Brincalhão")
                print("2 - Calmo")
                print("3 - Protetor")
                print("4 - Dócil")
                escolha = input(">>> ")
                opcoes = {
                    "1": "Brincalhão",
                    "2": "Calmo",
                    "3": "Protetor",
                    "4": "Dócil"
                }
                if escolha in opcoes:
                    filtros["personalidade"] = opcoes[escolha]
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "5":
            while True:
                print("HISTÓRICO VETERINÁRIO/VACINAL:")
                print("1 - Tudo em dia")
                print("2 - Faltando")
                escolha = input(">>> ")
                opcoes = {"1": "Tudo em dia", "2": "Faltando"}
                if escolha in opcoes:
                    filtros["historico"] = opcoes[escolha]
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "6":
            valor = input("Digite a raça:\n>>> ").strip().lower()
            if valor:
                filtros["raca"] = valor
            else:
                print("Raça não pode ser vazia.")

        elif opcao == "7":
            valor = input("Digite a cor:\n>>> ").strip().lower()
            if valor:
                filtros["cor"] = valor
            else:
                print("Cor não pode ser vazia.")

        else:
            print("Opção inválida. Tente novamente.")

        while True:
            continuar = input("Deseja adicionar mais um filtro? (s/n)\n>>> ").lower()
            if continuar in ('s', 'n'):
                break
            else:
                print("Digite 's' para sim ou 'n' para não.")
        if continuar != 's':
            break

    if filtros:
        print("\n=== FILTROS APLICADOS ===")
        for chave, valor in filtros.items():
            print(f"{chave.capitalize()}: {valor}")
        print("=" * 50)

    pets_filtrados = pets
    for chave, valor in filtros.items():
        pets_filtrados = [
            p for p in pets_filtrados
            if p.get(chave, '').strip().lower() == valor.strip().lower()
        ]

    if not pets_filtrados:
        print("\nNenhum pet encontrado com os filtros fornecidos.")
    else:
        print("\n=== PETS FILTRADOS ===")
        for pet in pets_filtrados:
            print("-" * 50)
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
        print("=" * 50)

def main():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1 - Adicionar pet")
        print("2 - Listar pets")
        print("3 - Atualizar pet")
        print("4 - Deletar pet")
        print("5 - Filtrar pet por característica")
        print("6 - Sair")
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
            filtrar_pets()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()