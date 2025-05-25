import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from perfis import pets
from perfis import voluntarios
from perfis import adotantes
from armazenamento import armazenamento_json as armazenamento

def main():
    while True:
        operacao = exibir_menu()

        if operacao == 'sair':
            print("Encerrando o programa. Até mais!")
            break

        elif operacao == 'CRUD':
            while True:
                escolha_usuario = exibir_menu_crud()

                if not escolha_usuario:
                    break

                tipo_operacao, perfil = escolha_usuario

                if perfil == 'pet':
                    resultado = crud_pet(tipo_operacao)
                elif perfil == 'voluntario':
                    resultado = crud_voluntario(tipo_operacao)
                elif perfil == 'adotante':
                    resultado = crud_adotante(tipo_operacao)
                else:
                    print("Perfil inválido.")
                    continue

                if not exibir_resultado(resultado, 'crud'):
                    print("Voltando ao menu principal...")
                    break

        elif operacao == 'match':
            while True:
                escolha_usuario = exibir_menu_match()

                if not escolha_usuario:
                    break

                if escolha_usuario == 'pets':
                    resultado = match_pets()
                elif escolha_usuario == 'adotante':
                    resultado = match_adotante()
                elif escolha_usuario == 'listar_pets':
                    resultado = pets.listar_pets()
                elif escolha_usuario == 'listar_adotantes':
                    resultado = adotantes.listar_adotantes()
                else:
                    print("Opção inválida.")
                    continue

                if not exibir_resultado(resultado, 'match'):
                    print("Voltando ao menu principal...")
                    break

        else:
            print("Opção inválida no menu principal.")




def exibir_menu():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Gerenciar dados (CRUD)")
        print("2. Fazer match")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            return 'CRUD'
        elif escolha == '2':
            return 'match'
        elif escolha == '3':
            return 'sair'
        else:
            print("Opção inválida. Tente novamente.")

def exibir_menu_crud():
    while True:
        print("\n--- MENU CRUD ---")
        print("1. Adotante")
        print("2. Pet")
        print("3. Voluntário")
        print("4. Voltar ao menu principal")
        perfil_opcao = input("Escolha o perfil a ser gerenciado: ")

        perfis = {'1': 'adotante', '2': 'pet', '3': 'voluntario'}

        if perfil_opcao == '4':
            return False
        elif perfil_opcao in perfis:
            perfil = perfis[perfil_opcao]

            print("\nOperações disponíveis:")
            print("1. Criar")
            print("2. Ler")
            print("3. Editar")
            print("4. Deletar")
            print("5. Voltar")

            operacao_opcao = input("Escolha a operação desejada: ")
            operacoes = {'1': 'criar', '2': 'ler', '3': 'editar', '4': 'deletar'}

            if operacao_opcao == '5':
                continue
            elif operacao_opcao in operacoes:
                tipo_operacao = operacoes[operacao_opcao]
                return (tipo_operacao, perfil)
            else:
                print("Operação inválida.")
        else:
            print("Perfil inválido.")

def exibir_menu_match():
    while True:
        print("\n--- MENU MATCH ---")
        print("1. Ver melhores matches para um pet")
        print("2. Ver melhores matches para um adotante")
        print("3. Listar todos os pets")
        print("4. Listar todos os adotantes")
        print("5. Voltar ao menu principal")
        escolha = input("Escolha uma opção: ")

        opcoes = {
            '1': 'pets',
            '2': 'adotante',
            '3': 'listar_pets',
            '4': 'listar_adotantes',
            '5': False
        }

        if escolha in opcoes:
            return opcoes[escolha]
        else:
            print("Opção inválida. Tente novamente.")



def crud_pet(operacao):
    if operacao == 'criar':
        return pets.adicionar_pet()
    elif operacao == 'ler':
        return pets.listar_pets()
    elif operacao == 'editar':
        return pets.atualizar_pet()
    elif operacao == 'deletar':
        return pets.deletar_pet()
    else:
        return "Operação inválida para pet."



def crud_voluntario(operacao):
    if operacao == 'criar':
        return voluntarios.criar_voluntario()
    elif operacao == 'ler':
        return voluntarios.listar_voluntarios()
    elif operacao == 'editar':
        return "Em desenvolvimento..."
    elif operacao == 'deletar':
        return "Em desenvolvimento..."
    else:
        return "Operação inválida para voluntários."



def crud_adotante(operacao):
    if operacao == 'criar':
        return adotantes.cadastrar_adotante()
    elif operacao == 'ler':
        return adotantes.listar_adotantes()
    elif operacao == 'editar':
        return adotantes.atualizar_adotante()
    elif operacao == 'deletar':
        return adotantes.excluir_adotante()
    else:
        return "Operação inválida para adotantes."


def match_pets():
    try:
        id_pet = int(input("Digite a ID do pet para visualizar os melhores matches: "))
    except ValueError:
        return "❌ Entrada inválida. Use um número inteiro."

    pet = armazenamento.ler_entrada(id_pet, 'id', 'pets.json')

    if not pet:
        return "❌ Pet não encontrado. Verifique o ID e tente novamente."

    adotantes_lista = armazenamento.carregar_arquivo('adotantes.json')
    if not adotantes_lista:
        return "❌ Nenhum adotante cadastrado."

    matches = encontrar_matches(pet, adotantes_lista)
    return matches[:10]

def match_adotante():
    cpf = input("Digite o CPF do adotante para visualizar os melhores matches: ")
    adotante = armazenamento.ler_entrada(cpf, 'id', 'adotantes.json')

    if not adotante:
        return "❌ Adotante não encontrado. Verifique o CPF e tente novamente."

    pets_lista = armazenamento.carregar_arquivo('pets.json')
    if not pets_lista:
        return "❌ Nenhum pet disponível."

    matches = encontrar_matches_para_adotante(adotante, pets_lista)
    return matches[:10]

def mapear_idade_para_faixa(idade):
    if idade <= 3:
        return 'filhote'
    elif 4 <= idade <= 9:
        return 'adulto'
    else:
        return 'idoso'

def encontrar_matches(pet, adotantes_lista):
    compatibilidades = []

    for adotante in adotantes_lista:
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

def encontrar_matches_para_adotante(adotante, pets_lista):
    compatibilidades = []
    preferencias = adotante.get('preferencias', {})

    for pet in pets_lista:
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



def exibir_resultado(resultado, tipo):
    print(f"\n--- RESULTADO ({tipo.upper()}) ---")
    if isinstance(resultado, list):
        for item in resultado:
            print(item)
    else:
        print(resultado)

    while True:
        escolha = input("Deseja realizar outra operação? (s/n): ").lower()
        if escolha == 's':
            return True
        elif escolha == 'n':
            return False
        else:
            print("Escolha inválida. Digite 's' ou 'n'.")



if __name__ == "__main__":
    main()
