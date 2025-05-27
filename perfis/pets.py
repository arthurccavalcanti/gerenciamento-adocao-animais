import armazenamento_json as armazenamento
from perfis.adotantes import validar_idade as validar_idade

def crud_pets(tipo_operacao: str):
    while True:
        print("DESEJA VISUALIZAR OS DADOS ANTES DA OPERAÇÃO?")
        print("1 - SIM")
        print("2 - NÃO")
        deseja_listar = input(">>> ")
        if deseja_listar == "1":
            listar_pets()
            break
        elif deseja_listar == "2":
            break
        else:
            print("Opção inválida.")    
    
    if tipo_operacao == "criar":
        print("CRIAÇÃO DE PET")
        return adicionar_pet()
    elif tipo_operacao == "editar":
        print("EDIÇÃO DE PET")
        return atualizar_pet()
    elif tipo_operacao == "deletar":
        print("DELEÇÃO DE PET")
        return deletar_pet()
    elif tipo_operacao == "ler":
        print("LEITURA DE PET")
        return ler_pet()
    else:
        return "Operação inválida. Tente novamente."

def adicionar_pet():
    pets = {}
    pets_json = armazenamento.carregar_arquivo('pets.json')
    
    if not pets_json:
        pets_json = []
    
    pets['id'] = gerar_novo_id(pets_json)

    while True:
        print("TIPO DO PET:")
        print("1 - Canino")
        print("2 - Felino")
        tipo_opcao = input(">>> ")
        if tipo_opcao == "1":
            pets['tipo'] = 'canino'
            break
        elif tipo_opcao == "2":
            pets['tipo'] = 'felino'
            break
        else:
            print("Opção inválida. Tente novamente.")

    pets['nome'] = input("DIGITE O NOME DO PET:\n>>> ")
    while True:
        idade = input("Digite a idade do PET:\n>>> ")
        if not validar_idade(idade):
            print("Idade inválida!\n")
            continue
        pets['idade'] = int(idade)
        break

    while True:
        print("SEXO:")
        print("1 - Macho")
        print("2 - Fêmea")
        sexo_opcao = input(">>> ")
        if sexo_opcao == "1":
            pets['sexo'] = 'M'
            break
        elif sexo_opcao == "2":
            pets['sexo'] = 'F'
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
            pets['personalidade'] = opcoes_personalidade[personalidade_opcao]
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
            pets['historico'] = opcoes_historico[historico_opcao]
            break
        else:
            print("Opção inválida. Tente novamente.")

    pets['raca'] = input("DIGITE A RAÇA:\n>>> ")
    pets['cor'] = input("DIGITE A COR PREDOMINANTE:\n>>> ")

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
            pets['porte'] = opcoes_porte[porte_opcao]
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
    while True:
        id_pet = int(input("DIGITE A ID DO PET:\n"))
        try:
            id_pet = int(id_pet)
            pet = armazenamento.ler_entrada(id_pet, 'id', 'pets.json')     
            if pet is None:                                               
                while True:
                    print("DESEJA LISTAR AS IDS DISPONÍVEIS?")
                    print("1 - SIM")
                    print("2 - NÃO")
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
            print("A ID FORNECIDA DEVE SER UM NÚMERO. TENTE NOVAMENTE.")
            continue

def atualizar_pet():                   
    pet_antigo = ler_pet()[1]  
    novo_pet = pet_antigo.copy()

    while True:
        print(f"\nAtualizando pet: {novo_pet['nome']} (ID: {novo_pet['id']})")
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
            novo_pet['tipo'] = "canino" if tipo_opcao == "1" else "felino" if tipo_opcao == "2" else pet_antigo['tipo']
            print(f"Tipo atualizado para: {novo_pet['tipo']}")
        elif opcao == "2":
            novo_nome = input(f"Novo nome (atual: {pet_antigo['nome']}):\n>>> ")
            if novo_nome.strip():
                novo_pet['nome'] = novo_nome
                print(f"Nome atualizado para: {novo_pet['nome']}")
        elif opcao == "3":
            nova_idade = input(f"Nova idade (atual: {pet_antigo['idade']}):\n>>> ")
            if nova_idade.strip():
                novo_pet['idade'] = nova_idade
                print(f"Idade atualizada para: {novo_pet['idade']}")
        elif opcao == "4":
            print("SEXO:")
            print("1 - Macho")
            print("2 - Fêmea")
            sexo_opcao = input(">>> ")
            if sexo_opcao == "1":
                novo_pet['sexo'] = "M"
            elif sexo_opcao == "2":
                novo_pet['sexo'] = "F"
            print(f"Sexo atualizado para: {novo_pet['sexo']}")
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
            novo_pet['personalidade'] = opcoes_personalidade.get(personalidade_opcao, pet_antigo['personalidade'])
            print(f"Personalidade atualizada para: {novo_pet['personalidade']}")
        elif opcao == "6":
            print("HISTÓRICO VETERINÁRIO/VACINAL:")
            print("1 - Tudo em dia")
            print("2 - Faltando")
            historico_opcao = input(">>> ")
            opcoes_historico = {
                "1": "Tudo em dia",
                "2": "Faltando"
            }
            novo_pet['historico'] = opcoes_historico.get(historico_opcao, pet_antigo['historico'])
            print(f"Histórico atualizado para: {novo_pet['historico']}")
        elif opcao == "7":
            nova_raca = input(f"Nova raça (atual: {pet_antigo['raca']}):\n>>> ")
            if nova_raca.strip():
                novo_pet['raca'] = nova_raca
                print(f"Raça atualizada para: {novo_pet['raca']}")
        elif opcao == "8":
            nova_cor = input(f"Nova cor predominante (atual: {pet_antigo['cor']}):\n>>> ")
            if nova_cor.strip():
                novo_pet['cor'] = nova_cor
                print(f"Cor atualizada para: {novo_pet['cor']}")
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
            novo_pet['porte'] = opcoes_porte.get(porte_opcao, pet_antigo['porte'])
            print(f"Porte atualizado para: {novo_pet['porte']}")
        else:
            print("Opção inválida.")

        continuar = input("Deseja continuar editando este pet? (s/n)\n>>> ").lower()
        while True:
            if continuar == 'n':
                print("Finalizando edição do pet.")
                if not armazenamento.editar_entrada(int(pet_antigo['id']), 'id', novo_pet, 'pets.json'):
                    return ('atualizar', (pet_antigo, novo_pet))
                return f"Erro ao atualizar pet com a id {pet_antigo['id']}. Tente novamente."
            elif continuar == 's':
                break
            else:
                print("Opção inválida.")

def deletar_pet():
    pet_excluido = ler_pet()[1]  

    print(f"Deletando pet:\n {pet_excluido}")
    if armazenamento.deletar_entrada(int(pet_excluido['id']), 'id', 'pets.json'):
        return ('deletar', pet_excluido)
    return f"Erro ao deletar pet com a id {pet_excluido['id']}. Tente novamente."

def listar_pets():

    pets = armazenamento.carregar_arquivo('pets.json')
    if not pets:
        print("Erro ao carregar o arquivo 'pets.json' para listar. Tente novamente.")
    else:
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
            print(f"Porte: {pet['porte']}\n")
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
