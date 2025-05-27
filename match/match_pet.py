import pprint
import armazenamento_json as armazenamento
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def match_pets():
    while True:
        print("\n========= MENU DE MATCH (PETS) =========")
        print("1. Visualizar todos os pets")
        print("2. Ver melhores matches de um pet")
        print("3. Visualizar todos os adotantes")
        print("4. Ver melhores matches de um adotante")
        print("5. Sair")
        print("=========================")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            visualizar_pets()
        elif opcao == '2':
            return ver_matches_pet()
        elif opcao == '3':
            visualizar_adotantes()
        elif opcao == '4':
            return ver_matches_adotante()
        elif opcao == '5':
            print("Saindo do menu de match. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

 # ---------------------------------------------------------------         

def ver_matches_pet():
    try:
        id_pet = int(input("Digite a ID do pet para visualizar os melhores matches: \n"))
    except ValueError:
        print("❌ Entrada inválida. Use um número inteiro.")
        return

    pet = armazenamento.ler_entrada(id_pet, 'id', 'pets.json')
    if pet is None:
        return f"❌ Pet com ID {id_pet} não encontrado. Verifique o ID e tente novamente."

    return encontrar_matches_pet(pet)


def ver_matches_adotante():
    cpf = input("Digite o CPF do adotante para visualizar os melhores matches: \n")

    adotante = armazenamento.ler_entrada(int(cpf), 'CPF', 'adotantes.json')

    if adotante is None:
        return f"❌ Adotante com CPF {cpf} não encontrado. Verifique o CPF e tente novamente."

    return encontrar_matches_adotante(adotante)


# --------------------------------------------------------------------

def encontrar_matches_pet(pet):

    possiveis_adotantes = armazenamento.carregar_arquivo('adotantes.json')

    if possiveis_adotantes is None:
        return f"Erro ao encontrar matches para pet {pet}\n Não conseguimos abrir o arquivo adotantes.json. Tente novamente."
    elif not possiveis_adotantes:
        return f"Não foi possível encontrar matches para o pet {pet}\n O arquivo adotantes.json não contém entradas."

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



def encontrar_matches_adotante(adotante):

    pets_disponiveis = armazenamento.carregar_arquivo('pets.json')

    if pets_disponiveis is None:
        return f"Erro ao encontrar matches para adotante {adotante}\n Não conseguimos abrir o arquivo pets.json. Tente novamente."
    elif not pets_disponiveis:
        return f"Não foi possível encontrar matches para o adotante {adotante}\n O arquivo pets.json não contém entradas."

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


# -------------------------------------------------------

def mapear_idade_para_faixa(idade):
    if idade <= 3:
        return 'filhote'
    elif 4 <= idade <= 9:
        return 'adulto'
    else:
        return 'idoso'

def visualizar_pets():
    pets = armazenamento.carregar_arquivo('pets.json')
    if pets is None:
        print("Erro ao abrir arquivo pets.json para visualizar no menu de match.")
    elif not pets:
        print("Oops, parece que não há entradas no arquivo pets.json")
    else:
        print("\n📋 Lista de Pets Disponíveis:\n")
        for pet in pets:
            print('-' * 40)
            pprint.pprint(pet)


def visualizar_adotantes():
    adotantes = armazenamento.carregar_arquivo('adotantes.json')
    if adotantes is None:
        print("Erro ao abrir arquivo adotantes.json para visualizar no menu de match.")
    elif not adotantes:
        print("Oops, parece que não há entradas no arquivo adotantes.json")
    else:
        print("\n--- 📋 Lista de Adotantes Registrados ---\n")
        for adotante in adotantes:
            print('-' * 40)
            pprint.pprint(adotantes)
