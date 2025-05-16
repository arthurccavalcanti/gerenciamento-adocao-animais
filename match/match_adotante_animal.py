import pprint
from armazenamento import armazenamento_json as armazenamento

'''
ALGORTIMO PARA ENCONTRAR UM PAR ANIMAL-ADOTANTE
'''

'''
A funçao de match pede ao usuário para escolher um pet, calcula e retorna os melhores matches.
A função também deve dar ao usuário a opção de visualizar todas as entradas.
'''

# ESBOÇO
def main():

    visualizar = input("Deseja visualizar todos os pets? 's'/'n'\n")

    if visualizar == 's':
        pprint.pprint(armazenamento.carregar_arquivo('pets.json'))
    
    id_pet_escolhido = input("Digite a ID do pet para visualizar os melhores matches: \n")

    pet_escolhido = armazenamento.ler_entrada(id_pet_escolhido, 'id', 'pets.json')

    possiveis_matches = encontrar_matches(pet_escolhido)

    melhores_dez_matches = possiveis_matches[:9]

    return melhores_dez_matches

# ESBOÇO
def encontrar_matches(pet):

    possiveis_adotantes = armazenamento.carregar_arquivo('adotantes.json')
    compatibilidades = []

    for adotante in possiveis_adotantes:

        compatibilidade_adotante = {'adotante':adotante, 'compatibilidade':0}
        compatibilidade_counter = 0
        testes = 0

        # testes de compatibilidade
        if pet['porte'] == adotante['preferencia_porte']:
            compatibilidade_counter += 1
        testes += 1
        if pet['temperamento'] == adotante['personalidade']:
            compatibilidade_counter += 1
        testes += 1
        # ...

        compatibilidade_em_porcentagem = (compatibilidade_counter / testes) * 100
        compatibilidade_adotante['compatibilidade'] = compatibilidade_em_porcentagem
        compatibilidades.append(compatibilidade_adotante)

    return sorted(compatibilidades, key=lambda dicionario: dicionario['compatibilidade'])

