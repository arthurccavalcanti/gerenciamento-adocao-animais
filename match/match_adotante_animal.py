import pprint
from armazenamento import armazenamento_json as armazenamento

'''
O programa de match pede ao usuário para escolher um pet.
Com os dados do pet, calcula e retorna os melhores matches.
A função também deve dar ao usuário a opção de visualizar todas as entradas.
'''

def main():

    visualizar = input("Deseja visualizar todos os pets? 's'/'n'\n").lower()

    if visualizar == 's':
        pprint.pprint(armazenamento.carregar_arquivo('pets.json'))
    
    id_pet_escolhido = input("Digite a ID do pet para visualizar os melhores matches: \n")

    pet_escolhido = armazenamento.ler_entrada(id_pet_escolhido, 'id', 'pets.json')

    if pet_escolhido == 1 or pet_escolhido == 2:
        return f"Pet não encontrado. Verifique o ID {id_pet_escolhido} e tente novamente."

    possiveis_matches = encontrar_matches(pet_escolhido)

    melhores_dez_matches = possiveis_matches[:9]

    return melhores_dez_matches


def encontrar_matches(pet):

    possiveis_adotantes = armazenamento.carregar_arquivo('adotantes.json')
    compatibilidades = []

    for adotante in possiveis_adotantes:

        compatibilidade_adotante = {'adotante':adotante, 'compatibilidade':0}
        compatibilidade_counter = 0
        testes = 0

        if pet['porte'] == adotante['preferencia_porte']:
            compatibilidade_counter += 1
        testes += 1
        if pet['temperamento'] == adotante['temperamento']:
            compatibilidade_counter += 1
        testes += 1
        if pet['sexo'] == adotante['preferencia_sexo']:
            compatibilidade_counter += 1
        testes += 1
        if pet['idade'] in adotante['faixa_etaria_aceita']:
            compatibilidade_counter += 1
        testes += 1
        if pet['tipo'] == adotante['preferencia_tipo']:
            compatibilidade_counter += 1
        testes += 1
        if not pet['exige_experiencia'] or adotante['tem_experiencia']:
            pontos_em_comum += 1
        total_criterios += 1
        # ...

        compatibilidade_em_porcentagem = (compatibilidade_counter / testes) * 100
        compatibilidade_adotante['compatibilidade'] = compatibilidade_em_porcentagem
        compatibilidades.append(compatibilidade_adotante)

    return sorted(compatibilidades, key=lambda dicionario: dicionario['compatibilidade'])

