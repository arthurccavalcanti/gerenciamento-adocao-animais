import pprint
from armazenamento import armazenamento_json as armazenamento

'''
ALGORITMO PARA ENCONTRAR VOLUNTARIOS PARA UM PAR ADOTANTE-ANIMAL
'''

'''
A funçao de match pede ao usuário para escolher um voluntário.
Com os dados, a função calcula e retorna os melhores matches.
'''

# ESBOÇO
def main():

    visualizar = input("Deseja visualizar todos os voluntários? 's'/'n'\n")

    if visualizar == 's':
        pprint.pprint(armazenamento.carregar_arquivo('voluntarios.json'))
    
    cpf_voluntario_escolhido = input("Digite o CPF do voluntário para visualizar os melhores matches: \n")

    voluntario_escolhido = armazenamento.ler_entrada(cpf_voluntario_escolhido, 'cpf', 'voluntarios.json')

    possiveis_matches = encontrar_matches(voluntario_escolhido)

    melhores_dez_matches = possiveis_matches[:9]

    return melhores_dez_matches


# ESBOÇO
def encontrar_matches(voluntario):

    possiveis_adotantes = armazenamento.carregar_arquivo('adotantes.json')
    compatibilidades = []

    for adotante in possiveis_adotantes:

        compatibilidade_adotante = {'adotante':adotante, 'compatibilidade':0}
        compatibilidade_counter = 0
        testes = 0
        
        distancia_max = 5       # maxima distancia de 5km

        # testes de compatibilidade
        if adotante['sexo'] == voluntario['sexo']:
            compatibilidade_counter += 1
        testes += 1
        if distancia_total(adotante['endereco'], voluntario['endereco']) < distancia_max:
            compatibilidade_counter += 1
        testes += 1
        # ...

        compatibilidade_em_porcentagem = (compatibilidade_counter / testes) * 100
        compatibilidade_adotante['compatibilidade'] = compatibilidade_em_porcentagem
        compatibilidades.append(compatibilidade_adotante)

    return sorted(compatibilidades, key=lambda dicionario: dicionario['compatibilidade'])

# ESBOÇO
def distancia_total(cep1, cep2):

    # procurar biblioteca para calcular aproximação de distancia entre dois ceps
    return