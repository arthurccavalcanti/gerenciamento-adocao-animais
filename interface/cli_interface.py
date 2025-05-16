

# A FAZER:
'''
No menu principal, o usuário deve escolher entre mexer nos dados (CRUD), fazer match com os dados, ou encerrar o programa.
A função deve retornar o tipo de operação a ser realizada ('CRUD', ou 'match').

A função deve receber e validar as escolhas do usuário, permitindo que o usuário volte atrás para fazer novas escolhas.
Se o usuário quiser encerrar o programa, a função retorna 'sair'.
'''
def exibir_menu():
    print("=")
    print(" ---->>> BEM VINDO AO SISTEMA ADOÇÃO DE PETS <<<---- ")
    print("          1 - VER PETS ")
    print("          2 - ...")
    print("          3 - SAIR  ")
    print("=")

    return

# -----------------------------------------------------

# A FAZER:
'''
A função do menu CRUD pergunta ao usuário o tipo de perfil a ser modificado ('adotante', 'pet', ou 'voluntario').
O menu deve exibir as opções de CRUD (criar, ler, atualizar, deletar), validar a escolha e permitir ao usuário voltar atrás para escolher uma nova operação.
Se o usuário escolher voltar para o menu principal, a função deve retornar False.

Quando o usuário confirmar a escolha, a função retorna o tipo de operação a ser realizada e o perfil a ser acessado num tupla (tipo_operacao, perfil).
As escolhas possíveis para tipos de operação são 'criar', 'ler', 'editar' e 'deletar'.
As escolhas possíveis para perfis são 'adotante', 'pet' e 'voluntario'.
        
Por exemplo, uma saída possível da função é ('ler', 'adotante').        
'''
def exibir_menu_crud():
    return


# -----------------------------------------------------

# A FAZER:
'''
A função de exibir recebe e mostra o resultado ao usuário, além de perguntar se o usuário deseja fazer mais uma operação.
Se sim, a função retorna True. Se não, a função retorna False.

O tipo de resultado a ser exibido pode ser um match ('match') ou uma operação de CRUD  ('crud').
'''
def exibir_resultado(resultado = None, tipo_resultado = None):
    return
