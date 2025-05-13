import json
import os
from time import sleep

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
            print("Arquivo JSON corrompido. Redefinindo...")
            return []

def salvar_pets(pets):
    with open(arquivo, 'w') as f:
        json.dump(pets, f, indent=4, ensure_ascii=False)

def gerar_novo_id(pets):
    if not pets:
        return 1
    return max(pet['id'] for pet in pets) + 1

def menu_inicial():
    print("=")
    print(" ---->>> BEM VINDO AO SISTEMA ADOÇÃO DE PETS <<<---- ")
    print("          1 - VER PETS ")
    print("          2 - ...")
    print("          3 - SAIR  ")
    print("=")

def adicionar_pet():
    pets = carregar_pets()
    novo_id = gerar_novo_id(pets)

    print("TIPO DO PET:")
    print("1 - Canino")
    print("2 - Felino")
    tipo_opcao = input(">>> ")
    tipo = "canino" if tipo_opcao == "1" else "felino" if tipo_opcao == "2" else "não especificado"

    nome = input("NOME DO PET:\n>>> ")
    idade = input("IDADE:\n>>> ")

    print("SEXO:")
    print("1 - Macho")
    print("2 - Fêmea")
    sexo_opcao = input(">>> ")
    sexo = "M" if sexo_opcao == "1" else "F" if sexo_opcao == "2" else "Não especificado"

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

    raca = input("RAÇA:\n>>> ")
    cor = input("COR PREDOMINANTE:\n>>> ")

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

    pets.append({
        'id': novo_id,
        'tipo': tipo,
        'nome': nome,
        'idade': idade,
        'sexo': sexo,
        'personalidade': personalidade,
        'historico': historico,
        'raca': raca,
        'cor': cor,
        'porte': porte
    })

    salvar_pets(pets)
    print("PET ADICIONADO COM SUCESSO!\n")

def atualizar_pet(id_pet):
    pets = carregar_pets()
    pet_encontrado = None

    for pet in pets:
        if pet['id'] == id_pet:
            pet_encontrado = pet
            break

    if not pet_encontrado:
        print(" PET NÃO ENCONTRADO.")
        return

    novo_nome = input("NOVO NOME:\n>>> ")
    nova_idade = input("NOVA IDADE:\n>>> ")

    print("NOVO SEXO:")
    print("1 - Macho")
    print("2 - Fêmea")
    sexo_opcao = input(">>> ")
    novo_sexo = "M" if sexo_opcao == "1" else "F" if sexo_opcao == "2" else "Não especificado"

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


    pet_encontrado['nome'] = novo_nome
    pet_encontrado['idade'] = nova_idade
    pet_encontrado['sexo'] = novo_sexo
    pet_encontrado['personalidade'] = nova_personalidade
    pet_encontrado['historico'] = novo_historico
    pet_encontrado['raca'] = nova_raca
    pet_encontrado['cor'] = nova_cor
    pet_encontrado['porte'] = novo_porte

    salvar_pets(pets)
    print("✅ PET ATUALIZADO COM SUCESSO!\n")



