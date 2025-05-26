from interface import cli_interface
from perfis import adotantes, pets, voluntarios
from match import match_pet, match_voluntario


def main():

    while True:

        '''
        No menu principal, o usuário deve escolher entre mexer nos dados (CRUD), fazer match com os dados, ou encerrar o programa.
        A função deve retornar o tipo de operação a ser realizada ('CRUD', ou 'match').

        A função deve receber e validar as escolhas do usuário, permitindo que o usuário volte atrás para fazer novas escolhas.
        Se o usuário quiser encerrar o programa, a função retorna 'sair'.
        '''
        operacao = cli_interface.exibir_menu()


        '''
        A função do menu CRUD pergunta ao usuário o tipo de perfil a ser modificado ('adotante', 'pet', ou 'voluntario').
        O menu deve exibir também as opções de CRUD (criar, ler, atualizar, deletar), validar a escolha e permitir ao usuário voltar atrás para escolher uma nova operação.
        Se o usuário escolher voltar para o menu principal, a função deve retornar False.

        Quando o usuário confirmar a escolha, a função retorna o tipo de operação a ser realizada e o perfil a ser acessado num tupla (tipo_operacao, perfil).
        As escolhas possíveis para tipos de operação são 'criar', 'ler', 'editar' e 'deletar'.
        As escolhas possíveis para perfis são 'adotante', 'pet' e 'voluntario'.
        
        Por exemplo, uma saída possível da função é ('ler', 'adotante').        
        '''
        while operacao == 'CRUD':
            escolha_usuario = cli_interface.exibir_menu_crud()
            if not escolha_usuario:
                break

            '''
            A função de cada perfil recebe a operação a ser feita (criar, deletar, atualizar, ler), realiza a operação e retorna o resultado.
            A função também deve dar ao usuário a opção de visualizar todas as entradas.
            '''
            tipo_operacao, perfil = escolha_usuario
            if perfil == 'pet':
                resultado_crud = pets.crud_pet(tipo_operacao)
            elif perfil == 'voluntario':
                resultado_crud = voluntarios.crud_voluntario(tipo_operacao)
            elif perfil == 'adotante':
                resultado_crud = adotantes.crud_adotante(tipo_operacao)
            else:
                print("Perfil inválido.")
                continue
            '''
            A função de exibição recebe e mostra o resultado ao usuário, além de perguntar se o usuário deseja fazer mais uma operação.
            Se sim, a função retorna True. Se não, a função retorna False.
            '''
        if not cli_interface.exibir_resultado(resultado_crud, 'crud'):   
            print("Voltando ao menu principal...")
            break

        '''
        A funçao do menu de match deve perguntar ao usuário qual tipo de match ele deseja fazer (melhores matches de um pet ou de um voluntário).
        O menu tambem deve dar ao usuário a opção de voltar ao menu principal. Se o usuário escolher voltar para o menu principal, a função deve retornar False.
        A função do menu deve validar e retornar a escolha do usuário.
        '''
        while operacao == 'match':
            escolha_usuario = cli_interface.exibir_menu_match()
            if not escolha_usuario:
                break
            '''
            A funçao de match pede ao usuário para escolher um pet ou um voluntário (a depender do tipo de match escolhido).
            Com os dados, a função calcula e retorna os melhores matches.
            A função também deve dar ao usuário a opção de visualizar todas as entradas.
            '''
            if escolha_usuario == 'pets':
                resultado_match = match_pet.match_pets()
            elif escolha_usuario == 'voluntario':
                resultado_match = match_voluntario.match_voluntario()
            else: 
                print("Opção inválida.")
                continue
            ''' 
            A função de exibição recebe e mostra o resultado ao usuário, além de perguntar se o usuário deseja fazer mais uma operação.
            Se sim, a função retorna True. Se não, a função retorna False.
            '''
            if not cli_interface.exibir_resultado(resultado_match, 'match'):
                print("Voltando ao menu principal...")
                break
  

        if operacao == 'sair':
            print("Encerrando o programa. Até mais!")
            break
