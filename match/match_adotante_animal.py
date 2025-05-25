import sys
import os
import pprint

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from armazenamento import armazenamento_json as armazenamento


def mapear_idade_para_faixa(idade):
    if idade <= 3:
        return 'filhote'
    elif 4 <= idade <= 9:
        return 'adulto'
    else:
        return 'idoso'


def encontrar_matches(pet):
    possiveis_adotantes = armazenamento.carregar_arquivo('adotantes.json')
    compatibilidades = []

    for adotante in possiveis_adotantes:
        compatibilidade_counter = 0
        testes = 0
        preferencias = adotante.get('preferencias', {})

        if pet['porte'] == preferencias.get('porte'):
            compatibilidade_counter += 1
        testes += 1

        if pet.get('personalidade', '').lower() in [t.lower() for t in preferencias.get('temperamento', [])]:
            compatibilidade_counter += 1
        testes += 1

        if pet['sexo'].lower() == preferencias.get('sexo', '').lower():
            compatibilidade_counter += 1
        testes += 1

        faixa_pet = mapear_idade_para_faixa(pet['idade'])
        if faixa_pet == preferencias.get('faixa_etaria'):
            compatibilidade_counter += 1
        testes += 1

        if pet['tipo'] == preferencias.get('tipo'):
            compatibilidade_counter += 1
        testes += 1

        if not pet.get('exige_experiencia', False) or preferencias.get('experiencia', False):
            compatibilidade_counter += 1
        testes += 1

        compatibilidade_em_porcentagem = (compatibilidade_counter / testes) * 100

        compatibilidades.append({
            'adotante': adotante,
            'compatibilidade': round(compatibilidade_em_porcentagem, 2)
        })

    return sorted(compatibilidades, key=lambda d: d['compatibilidade'], reverse=True)


def encontrar_matches_para_adotante(adotante):
    pets_disponiveis = armazenamento.carregar_arquivo('pets.json')
    compatibilidades = []
    preferencias = adotante.get('preferencias', {})

    for pet in pets_disponiveis:
        compatibilidade_counter = 0
        testes = 0

        if pet['porte'] == preferencias.get('porte'):
            compatibilidade_counter += 1
        testes += 1

        if pet.get('personalidade', '').lower() in [t.lower() for t in preferencias.get('temperamento', [])]:
            compatibilidade_counter += 1
        testes += 1

        if pet['sexo'].lower() == preferencias.get('sexo', '').lower():
            compatibilidade_counter += 1
        testes += 1

        faixa_pet = mapear_idade_para_faixa(pet['idade'])
        if faixa_pet == preferencias.get('faixa_etaria'):
            compatibilidade_counter += 1
        testes += 1

        if pet['tipo'] == preferencias.get('tipo'):
            compatibilidade_counter += 1
        testes += 1

        if not pet.get('exige_experiencia', False) or preferencias.get('experiencia', False):
            compatibilidade_counter += 1
        testes += 1

        compatibilidade_em_porcentagem = (compatibilidade_counter / testes) * 100

        compatibilidades.append({
            'pet': pet,
            'compatibilidade': round(compatibilidade_em_porcentagem, 2)
        })

    return sorted(compatibilidades, key=lambda d: d['compatibilidade'], reverse=True)


def visualizar_pets():
    pets = armazenamento.carregar_arquivo('pets.json')
    print("\n📋 Lista de Pets Disponíveis:\n")
    pprint.pprint(pets)


def visualizar_adotantes():
    adotantes = armazenamento.carregar_arquivo('adotantes.json')
    print("\n📋 Lista de Adotantes Registrados:\n")
    pprint.pprint(adotantes)


def ver_matches():
    try:
        id_pet = int(input("Digite a ID do pet para visualizar os melhores matches: \n"))
    except ValueError:
        print("❌ Entrada inválida. Use um número inteiro.")
        return

    pet = armazenamento.ler_entrada(id_pet, 'id', 'pets.json')

    if not pet:
        print("❌ Pet não encontrado. Verifique o ID e tente novamente.")
        return

    matches = encontrar_matches(pet)
    top_matches = matches[:10]

    print("\n🔍 Melhores Matches:\n")
    for match in top_matches:
        pprint.pprint(match)


def ver_matches_para_adotante():
    cpf = input("Digite o CPF do adotante para visualizar os melhores matches: \n")

    adotante = armazenamento.ler_entrada(cpf, 'id', 'adotantes.json')

    if not adotante:
        print("❌ Adotante não encontrado. Verifique o CPF e tente novamente.")
        return

    matches = encontrar_matches_para_adotante(adotante)
    top_matches = matches[:10]

    print("\n🔍 Melhores Matches para o Adotante:\n")
    for match in top_matches:
        pprint.pprint(match)


def menu():
    while True:
        print("\n========= MENU =========")
        print("1. Visualizar todos os pets")
        print("2. Ver melhores matches de um pet")
        print("3. Visualizar todos os adotantes")
        print("4. Ver melhores matches de um adotante")
        print("5. Sair")
        print("=========================")

        opcao = input("Escolha uma opção (1/2/3/4/5): ")

        if opcao == '1':
            visualizar_pets()
        elif opcao == '2':
            ver_matches()
        elif opcao == '3':
            visualizar_adotantes()
        elif opcao == '4':
            ver_matches_para_adotante()
        elif opcao == '5':
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
