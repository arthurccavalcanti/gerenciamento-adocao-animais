import pprint
import armazenamento_json as armazenamento


def match_voluntario():

    while True:
        print("\n========= MENU DE MATCH (VOLUNTÁRIOS) =========")
        print("1. Visualizar todos os voluntários")
        print("2. Ver melhores matches de um voluntário")
        print("3. Sair")
        print("=========================")

        opcao = input("Escolha uma opção (1/2/3): ")

        if opcao == '1':
            visualizar_voluntarios()
        elif opcao == '2':
            print("AINDA ESTAMOS TRABALHANDO NESTE RECURSO... TENTE MAIS TARDE")
            #ver_matches_voluntarios()
        elif opcao == '3':
            print("Saindo do menu de match. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


def visualizar_voluntarios():
    voluntarios = armazenamento.carregar_arquivo('voluntarios.json')
    if voluntarios is None:
        print("Erro ao abrir arquivo voluntarios.json para visualizar no menu de match.")
    elif not voluntarios:
        print("Oops, parece que não há entradas no arquivo voluntarios.json")
    else:
        print("\n====📋 Lista de Voluntários Disponíveis ====\n")
        pprint.pprint(voluntarios)


def ver_matches_voluntario():
    try:
        cpf_voluntario = int(input("Digite o CPF do voluntário para visualizar os melhores matches: \n"))
    except ValueError:
        print("❌ Entrada inválida. Use um número inteiro.")
        return

    voluntario = armazenamento.ler_entrada(cpf_voluntario, 'CPF', 'voluntarios.json')
    if voluntario is None:
        return f"❌ Voluntário com CPF {cpf_voluntario} não encontrado. Verifique o CPF e tente novamente."
    elif not voluntario:
        return "Oops, parece que não há entradas no arquivo voluntarios.json"
    return encontrar_matches_voluntario(voluntario)
     

def encontrar_matches_voluntario(voluntario):

    possiveis_adotantes = armazenamento.carregar_arquivo('adotantes.json')

    if possiveis_adotantes is None:
        return f"Erro ao encontrar matches para voluntario {voluntario}\n Não conseguimos abrir o arquivo adotantes.json. Tente novamente."
    elif not possiveis_adotantes:
        return f"Não foi possível encontrar matches para o voluntário {voluntario}\n O arquivo adotantes.json não contém entradas."

    compatibilidades = []

    for adotante in possiveis_adotantes:
        compatibilidade_counter = 0
        testes = 0
        
        '''
        preferencias = adotante.get('preferencias', {})
        if pet['porte'] == preferencias.get('porte'):
            compatibilidade_counter += 1
        testes += 1 

        distancia_max = 5       # maxima distancia de 5km


        if adotante['sexo'] == voluntario['sexo']:
            compatibilidade_counter += 1
        testes += 1

        if distancia_total(adotante['endereco'], voluntario['endereco']) < distancia_max:
            compatibilidade_counter += 1
        testes += 1
        '''
        
        compatibilidade_em_porcentagem = (compatibilidade_counter / testes) * 100


        compatibilidades.append({
            'adotante': adotante,
            'compatibilidade': round(compatibilidade_em_porcentagem, 2)
        })

    return sorted(compatibilidades, key=lambda d: d['compatibilidade'], reverse=True)








