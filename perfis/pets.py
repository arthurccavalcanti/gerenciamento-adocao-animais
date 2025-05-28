import armazenamento_json as armazenamento

def crud_pets(tipo_operacao: str):
    while True:
        print("Deseja visualizar os dados de pets antes da operação?")
        print("1 - Sim")
        print("2 - Não")
        deseja_listar = input(">>> ")
        if deseja_listar == "1":
            listar_pets()
            break
        elif deseja_listar == "2":
            break
        else:
            print("Opção inválida.")    
    
    if tipo_operacao == "criar":
        print("--- CRIAÇÃO DE PET ---")
        return adicionar_pet()
    elif tipo_operacao == "editar":
        print("--- EDIÇÃO DE PET ---")
        return atualizar_pet()
    elif tipo_operacao == "deletar":
        print("--- DELEÇÃO DE PET ---")
        return deletar_pet()
    elif tipo_operacao == "ler":
        print("--- LEITURA DE PET ---")
        resultado = ler_pet()
        if resultado is None:
            return "Não foi possível realizar a leitura. Nenhum pet cadastrado."
        return resultado
    else:
        return "Operação inválida. Tente novamente."

def adicionar_pet():
    pets = {}
    pets_json = armazenamento.carregar_arquivo('pets.json')
    
    if not pets_json:
        pets_json = []
    
    pets['ID'] = gerar_novo_id(pets_json)

    while True:
        print("TIPO DO PET:")
        print("1 - Canino")
        print("2 - Felino")
        tipo_opcao = input(">>> ")
        if tipo_opcao == "1":
            pets['Tipo'] = 'canino'
            break
        elif tipo_opcao == "2":
            pets['Tipo'] = 'felino'
            break
        else:
            print("Opção inválida. Tente novamente.")

    pets['Nome'] = input("Digite o nome do pet:\n>>> ")
    while True:
        idade = input("Digite a idade do pet:\n>>> ")
        try:
            pets['Idade'] = int(idade)
            break
        except ValueError:
            print("Idade inválida! Tem que ser um número inteiro\n")

    while True:
        print("SEXO:")
        print("1 - Macho")
        print("2 - Fêmea")
        sexo_opcao = input(">>> ")
        if sexo_opcao == "1":
            pets['Sexo'] = 'M'
            break
        elif sexo_opcao == "2":
            pets['Sexo'] = 'F'
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
            pets['Personalidade'] = opcoes_personalidade[personalidade_opcao]
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
            pets['Histórico'] = opcoes_historico[historico_opcao]
            break
        else:
            print("Opção inválida. Tente novamente.")

    pets['Raça'] = input("DIGITE A RAÇA:\n>>> ")
    pets['Cor'] = input("DIGITE A COR PREDOMINANTE:\n>>> ")

    opcoes_porte = {
        "1": "pequeno",
        "2": "médio",
        "3": "grande"
    }
    while True:
        print("PORTE:\n")
        for k, v in opcoes_porte.items():
            print(f"{k} - {v}")
        porte_opcao = input(">>> ")
        if porte_opcao in opcoes_porte:
            pets['Porte'] = opcoes_porte[porte_opcao]
            break
        else:
            print("Opção inválida. Tente novamente.")

    if armazenamento.criar_entrada(pets, 'pets.json'):
        return ('criar', pets)
    return f"Erro ao criar pet:\n {pets}.\n Tente novamente."

def gerar_novo_id(pets_json):
    if not pets_json:  
        return 1
    try:
        return max(int(pet['id']) for pet in pets_json) + 1
    except (KeyError, ValueError):
        
        return len(pets_json) + 1

def ler_pet():
    pets = listar_pets()
    
    if not pets:
        print("Não há pets cadastrados.")
        return None

    while True:
        id_pet = int(input("Digite a ID do pet: "))
        try:
            id_pet = int(id_pet)
            pet = armazenamento.ler_entrada(id_pet, 'ID', 'pets.json')     
            if pet is None:                                               
                while True:
                    print("Deseja listar as IDs disponíveis?")
                    print("1 - Sim")
                    print("2 - Não")
                    deseja_listar = input(">>> ")
                    if deseja_listar == "1":
                        listar_pets()
                        break
                    elif deseja_listar == "2":
                        break
                    else:
                        print("Opção inválida.")            
            else:
                return ('ler', pet)
        except ValueError:
            print("A ID fornecida deve ser um número. Tente novamente.")
            continue

def atualizar_pet():                   
    pet_antigo = ler_pet()[1]  
    novo_pet = pet_antigo.copy()

    while True:
        print(f"\nAtualizando pet: {novo_pet['Nome']} (ID: {novo_pet['ID']})")
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
        opcao = input(">>> ")

        if opcao == "1":
            print("TIPO DO PET:")
            print("1 - Canino")
            print("2 - Felino")
            tipo_opcao = input(">>> ")
            novo_pet['Tipo'] = "canino" if tipo_opcao == "1" else "felino" if tipo_opcao == "2" else pet_antigo['Tipo']
            print(f"Tipo atualizado para: {novo_pet['Tipo']}")
        elif opcao == "2":
            novo_nome = input(f"Novo nome (atual: {pet_antigo['Nome']}):\n>>> ")
            if novo_nome.strip():
                novo_pet['Nome'] = novo_nome
                print(f"Nome atualizado para: {novo_pet['Nome']}")
        elif opcao == "3":
            nova_idade = input(f"Nova idade (atual: {pet_antigo['Idade']}):\n>>> ")
            if nova_idade.strip():
                novo_pet['Idade'] = nova_idade
                print(f"Idade atualizada para: {novo_pet['Idade']}")
        elif opcao == "4":
            print("SEXO:")
            print("1 - Macho")
            print("2 - Fêmea")
            sexo_opcao = input(">>> ")
            if sexo_opcao == "1":
                novo_pet['Sexo'] = "M"
            elif sexo_opcao == "2":
                novo_pet['Sexo'] = "F"
            print(f"Sexo atualizado para: {novo_pet['Sexo']}")
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
            novo_pet['Personalidade'] = opcoes_personalidade.get(personalidade_opcao, pet_antigo['Personalidade'])
            print(f"Personalidade atualizada para: {novo_pet['Personalidade']}")
        elif opcao == "6":
            print("HISTÓRICO VETERINÁRIO/VACINAL:")
            print("1 - Tudo em dia")
            print("2 - Faltando")
            historico_opcao = input(">>> ")
            opcoes_historico = {
                "1": "Tudo em dia",
                "2": "Faltando"
            }
            novo_pet['Histórico'] = opcoes_historico.get(historico_opcao, pet_antigo['Histórico'])
            print(f"Histórico atualizado para: {novo_pet['Histórico']}")
        elif opcao == "7":
            nova_raca = input(f"Nova raça (atual: {pet_antigo['Raça']}):\n>>> ")
            if nova_raca.strip():
                novo_pet['Raça'] = nova_raca
                print(f"Raça atualizada para: {novo_pet['Raça']}")
        elif opcao == "8":
            nova_cor = input(f"Nova cor predominante (atual: {pet_antigo['Cor']}):\n>>> ")
            if nova_cor.strip():
                novo_pet['Cor'] = nova_cor
                print(f"Cor atualizada para: {novo_pet['Cor']}")
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
            novo_pet['Porte'] = opcoes_porte.get(porte_opcao, pet_antigo['Porte'])
            print(f"Porte atualizado para: {novo_pet['Porte']}")
        else:
            print("Opção inválida.")

        continuar = input("Deseja continuar editando este pet? (s/n)\n>>> ").lower()
        while True:
            if continuar == 'n':
                print("Finalizando edição do pet.")
                if armazenamento.editar_entrada(int(pet_antigo['ID']), 'ID', novo_pet, 'pets.json'):
                    return ('atualizar', (pet_antigo, novo_pet))
                return f"Erro ao atualizar pet com a id {pet_antigo['ID']}. Tente novamente."
            elif continuar == 's':
                break
            else:
                print("Opção inválida.")

def deletar_pet():
    pet_excluido = ler_pet()[1]  

    print(f"Deletando pet:\n {pet_excluido}")
    if armazenamento.deletar_entrada(int(pet_excluido['ID']), 'ID', 'pets.json'):
        return ('deletar', pet_excluido)
    return f"Erro ao deletar pet com a id {pet_excluido['ID']}. Tente novamente."

def listar_pets():

    pets = armazenamento.carregar_arquivo('pets.json')

    if pets is None:
        print(f"Erro ao listar pets: não foi possível criar o arquivo pets.json")
    elif not pets:
        print("Oops. Parece que não há pets registrados.")
    else:
        print("="*50)
        print("LISTA DE PETS:")
        for pet in pets:
            print("-"*50)
            print(f"ID: {pet['ID']}")
            print(f"Tipo: {pet['Tipo']}")
            print(f"Nome: {pet['Nome']}")
            print(f"Idade: {pet['Idade']}")
            print(f"Sexo: {pet['Sexo']}")
            print(f"Personalidade: {pet['Personalidade']}")
            print(f"Histórico: {pet['Histórico']}")
            print(f"Raça: {pet['Raça']}")
            print(f"Cor: {pet['Cor']}")
            print(f"Porte: {pet['Porte']}\n")
        print("="*50)

def filtrar_pets():
    pets = armazenamento.carregar_arquivo('pets.json')

    if not pets: 
        return "Erro ao criar o arquivo 'pets.json'. Tente novamente."
    
    filtros = {}

    while True:
        opcao = menu_filtrar()
        if opcao == "1":
            while True:
                print("TIPO:")
                print("1 - Canino")
                print("2 - Felino")
                escolha = input(">>> ")
                if escolha == "1":
                    filtros["Tipo"] = "canino"
                    break
                elif escolha == "2":
                    filtros["Tipo"] = "felino"
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
                    filtros["Sexo"] = "M"
                    break
                elif escolha == "2":
                    filtros["Sexo"] = "F"
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
            if str(p.get(chave, '')).strip().lower() == str(valor).strip().lower()
        ]
    
    if not pets_filtrados:
        print("\nNenhum pet encontrado com os filtros fornecidos.")
    else:
        print("\n=== PETS FILTRADOS ===")
        for pet in pets_filtrados:
            print(f"ID: {pet['ID']}")
            print(f"Tipo: {pet['Tipo']}")
            print(f"Nome: {pet['Nome']}")
            print(f"Idade: {pet['Idade']}")
            print(f"Sexo: {pet['Sexo']}")
            print(f"Personalidade: {pet['Personalidade']}")
            print(f"Histórico: {pet['Histórico']}")
            print(f"Raça: {pet['Raça']}")
            print(f"Cor: {pet['Cor']}")
            print(f"Porte: {pet['Porte']}")
        print("=" * 50)

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
        opcao = input(">>> ")
        if opcao in ["1", "2", "3", "4", "5", "6", "7"]:
            return opcao
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    crud_pets()
