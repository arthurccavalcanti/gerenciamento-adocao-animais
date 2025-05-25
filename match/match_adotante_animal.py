import pprint
from armazenamento import armazenamento_json as armazenamento

'''
O programa de match pede ao usuário para escolher um pet.
Com os dados do pet, calcula e retorna os melhores matches.
A função também dá ao usuário a opção de visualizar todas as entradas.
'''

def main():
    visualizar = input("Deseja visualizar todos os pets? ('s' para sim / qualquer outra tecla para não):\n").lower()

    if visualizar == 's':
        pprint.pprint(armazenamento.carregar_arquivo('pets.json'))

    id_pet_escolhido = input("Digite a ID do pet para visualizar os melhores matches:\n")

    pet_escolhido = armazenamento.ler_entrada(id_pet_escolhido, 'id', 'pets.json')

    if not pet_escolhido:
        print("Pet não encontrado. Verifique o ID e tente novamente.")
        return

    possiveis_matches = encontrar_matches(pet_escolhido)

    melhores_dez_matches = possiveis_matches[:10]

    pprint.pprint(melhores_dez_matches)


def encontrar_matches(pet):
    possiveis_adotantes = armazenamento.carregar_arquivo('adotantes.json')
    compatibilidades = []

    for adotante in possiveis_adotantes:
        compatibilidade_counter = 0
        total_criterios = 0

        if pet['porte'] == adotante['preferencia_porte']:
            compatibilidade_counter += 1
        total_criterios += 1

        if pet['temperamento'] == adotante['temperamento']:
            compatibilidade_counter += 1
        total_criterios += 1

        if pet['sexo'] == adotante['preferencia_sexo']:
            compatibilidade_counter += 1
        total_criterios += 1

        if pet['idade'] in adotante['faixa_etaria_aceita']:
            compatibilidade_counter += 1
        total_criterios += 1

        if pet['tipo'] == adotante['preferencia_tipo']:
            compatibilidade_counter += 1
        total_criterios += 1

        if not pet['exige_experiencia'] or adotante['tem_experiencia']:
            compatibilidade_counter += 1
        total_criterios += 1

        compatibilidade_em_porcentagem = (compatibilidade_counter / total_criterios) * 100

        compatibilidades.append({
            'adotante': adotante,
            'compatibilidade': compatibilidade_em_porcentagem
        })

    
    return sorted(compatibilidades, key=lambda d: d['compatibilidade'], reverse=True)