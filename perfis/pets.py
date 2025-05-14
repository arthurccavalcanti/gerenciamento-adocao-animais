from armazenamento import armazenamento_json as armazenamento


def gerar_novo_id(animais_json):
    if not animais_json:
        return 1
    return max(pet['id'] for pet in animais_json) + 1


def adicionar_pet():
    pets = {}
    animais_json = armazenamento.carregar_arquivo('animais.json')
    
    pets['id'] = gerar_novo_id(animais_json)

    print("TIPO DO PET:")
    print("1 - Canino")
    print("2 - Felino")
    tipo_opcao = input(">>> ")
    pets['tipo'] = "canino" if tipo_opcao == "1" else "felino" if tipo_opcao == "2" else "não especificado"

    pets['nome'] = input("NOME DO PET:\n>>> ")
    pets['idade'] = input("IDADE:\n>>> ")

    print("SEXO:")
    print("1 - Macho")
    print("2 - Fêmea")
    sexo_opcao = input(">>> ")
    pets['sexo'] = "M" if sexo_opcao == "1" else "F" if sexo_opcao == "2" else "Não especificado"

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
    pets['personalidade'] = opcoes_personalidade.get(personalidade_opcao, "não especificado")

    print("HISTÓRICO VETERINÁRIO/VACINAL:")
    print("1 - Tudo em dia")
    print("2 - Faltando")
    historico_opcao = input(">>> ")
    opcoes_historico = {
        "1": "Tudo em dia",
        "2": "Faltando"
    }
    pets['historico'] = opcoes_historico.get(historico_opcao, "não especificado")

    pets['raca'] = input("RAÇA:\n>>> ")
    pets['cor'] = input("COR PREDOMINANTE:\n>>> ")

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
    pets['porte'] = opcoes_porte.get(porte_opcao, "não especificado")

    armazenamento.criar_entrada(pets, 'animais.json')
    print("PET ADICIONADO COM SUCESSO!\n")

    return 0


def atualizar_pet(id_pet):

    pet = armazenamento.ler_entrada(id_pet, 'id', 'animais.json')

    if pet == 2:
        print("O ID fornecido não corresponde a nenhuma animal.")
        return 2

    novo_nome = input("NOVO NOME:\n>>> ")
    nova_idade = input("NOVA IDADE:\n>>> ")

    print("NOVO SEXO:")
    print("1 - Macho")
    print("2 - Fêmea")
    sexo_opcao = input(">>> ")
    novo_sexo = "M" if sexo_opcao == "1" else "F" if sexo_opcao == "2" else "não especificado"

    print("NOVA PERSONALIDADE:")
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
    nova_personalidade = opcoes_personalidade.get(personalidade_opcao, "não especificado")

    print("NOVO HISTÓRICO VETERINÁRIO/VACINAL:")
    print("1 - Tudo em dia")
    print("2 - Faltando")
    historico_opcao = input(">>> ")
    opcoes_historico = {
        "1": "Tudo em dia",
        "2": "Faltando"
    }
    novo_historico = opcoes_historico.get(historico_opcao, "não especificado")

    nova_raca = input("NOVA RAÇA:\n>>> ")
    nova_cor = input("NOVA COR PREDOMINANTE:\n>>> ")

    print("NOVO PORTE:")
    print("1 - Pequeno")
    print("2 - Médio")
    print("3 - Grande")
    porte_opcao = input(">>> ")
    opcoes_porte = {
        "1": "pequeno",
        "2": "médio",
        "3": "grande"
    }
    novo_porte = opcoes_porte.get(porte_opcao, "não especificado")


    pet['nome'] = novo_nome
    pet['idade'] = nova_idade
    pet['sexo'] = novo_sexo
    pet['personalidade'] = nova_personalidade
    pet['historico'] = novo_historico
    pet['raca'] = nova_raca
    pet['cor'] = nova_cor
    pet['porte'] = novo_porte

    armazenamento.editar_entrada(id_pet, 'id', pet, 'animais.json')
    print("✅ PET ATUALIZADO COM SUCESSO!\n")
    
    return 0



def seusPets(responsavel):
    pets = armazenamento.carregar_arquivo('animais.json')
    pets_responsavel = [pet for pet in pets if pet.get('responsavel') == responsavel]
    return pets_responsavel


def listarSeusPets(responsavel):
    pets = seusPets(responsavel)
    if pets:
        print("=" * 50)
        print(f"PETS DO RESPONSÁVEL: {responsavel.upper()}\n")
        for pet in pets:
            print("*" * 50)
            print(f"ID: {pet['id']}, TIPO: {pet['tipo']}, NOME: {pet['nome']}, IDADE: {pet['idade']}, SEXO: {pet['sexo']}, "
                  f"PERSONALIDADE: {pet['personalidade']}, HISTÓRICO: {pet['historico']}, RAÇA: {pet['raca']}, "
                  f"COR: {pet['cor']}, PORTE: {pet['porte']}")
            print("*" * 50)
        print("=" * 50)
    else:
        print("Você não possui pets cadastrados.")


def listarPets():
    pets = armazenamento.carregar_arquivo('animais.json')
    if pets:
        print("=" * 50)
        print("LISTA DE PETS:\n")
        for pet in pets:
            print("*" * 50)
            print(f"ID: {pet['id']}, TIPO: {pet['tipo']}, NOME: {pet['nome']}, IDADE: {pet['idade']}, SEXO: {pet['sexo']}, "
                  f"PERSONALIDADE: {pet['personalidade']}, HISTÓRICO: {pet['historico']}, RAÇA: {pet['raca']}, "
                  f"COR: {pet['cor']}, PORTE: {pet['porte']}")
            print("*" * 50)
        print("=" * 50)
    else:
        print("NENHUM PET CADASTRADO.")


def deletarPet(responsavel):
    pets = seusPets(responsavel)
    if not pets:
        print("Você não possui pets cadastrados.")
        return

    listarSeusPets(responsavel)

    while True:
        id_escolhido = input("Digite o ID do pet que deseja deletar: ")
        try:
            id_escolhido = int(id_escolhido)
        except ValueError:
            print("ID inválido. Use apenas números.")
            continue

        pet = armazenamento.ler_entrada(id_escolhido, 'id', 'animais.json')

        if pet == 2:
            print("Pet com esse ID não foi encontrado.\n")
            continuar = print(input("Deseja continuar? 's/'n' \n"))
            if continuar == 'n':
                break

        if pet[responsavel] == responsavel:
            armazenamento.deletar_entrada(id_escolhido, 'id', 'animais.json')
            print(f"O pet de ID {id_escolhido} foi deletado.")
            return 0
        else:
            print("Você não tem permissão para deletar este pet.")
            return 1
