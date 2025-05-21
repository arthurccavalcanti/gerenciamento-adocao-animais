

# A FAZER:
'''
No menu principal, o usuário deve escolher entre mexer nos dados (CRUD), fazer match com os dados, ou encerrar o programa.
A função deve retornar o tipo de operação a ser realizada ('CRUD', ou 'match').

A função deve receber e validar as escolhas do usuário, permitindo que o usuário volte atrás para fazer novas escolhas.
Se o usuário quiser encerrar o programa, a função retorna 'sair'.
'''
def exibir_menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1  Gerenciar dados (CRUD)")
        print("2 Fazer match")
        print("3  Sair")
        
        escolha = input("Escolha uma opção (1-3): ").strip()
        
        if escolha == '1':
            return 'CRUD'
        elif escolha == '2':
            return 'match'
        elif escolha == '3':
            return 'sair'
        else:
            print("Opção inválida. Tente novamente.")

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
    while True:
        print("\n=== MENU CRUD ===")
        print("1  Criar")
        print("2Ler")
        print("3  Editar")
        print("4  Deletar")
        print("5 Voltar ao menu principal")
        
        operacao = input("Escolha a operação (1-5): ").strip()

        if operacao == '5':
            return False

        operacoes = {'1': 'criar', '2': 'ler', '3': 'editar', '4': 'deletar'}

        if operacao in operacoes:
            tipo_operacao = operacoes[operacao]
            
            print("\nEscolha o perfil:")
            print("1  Adotante")
            print("2 Pet")
            print("3  Voluntário")
            print("4  Voltar")
            
            perfil = input("Escolha o perfil (1-4): ").strip()

            perfis = {'1': 'adotante', '2': 'pet', '3': 'voluntario'}

            if perfil == '4':
                continue  # volta ao menu de operação

            if perfil in perfis:
                return (tipo_operacao, perfis[perfil])
            else:
                print("Perfil inválido.")
        else:
            print("Operação inválida.")
# -----------------------------------------------------

# A FAZER:
'''
A função de exibir recebe e mostra o resultado ao usuário, além de perguntar se o usuário deseja fazer mais uma operação.
Se sim, a função retorna True. Se não, a função retorna False.

O tipo de resultado a ser exibido pode ser um match ('match') ou uma operação de CRUD  ('crud').
'''
def exibir_resultado(resultado, tipo):
    print("\n=== RESULTADO DA OPERAÇÃO ===")
    print(resultado)

    while True:
        escolha = input(f"Deseja realizar mais uma operação de {tipo}? (s/n): ").lower().strip()
        if escolha == 's':
            return True
        elif escolha == 'n':
            return False
        else:
            print("Escolha inválida, responda com 's' ou 'n'.")


def exibir_menu_match():
    while True:
        print("\n=== MENU DE MATCH ===")
        print("1  Ver melhores matches de pets")
        print("2 Ver melhores matches de voluntários")
        print("3 Voltar ao menu principal")
        
        escolha = input("Escolha uma opção (1-3): ").strip()

        if escolha == '1':
            return 'pets'
        elif escolha == '2':
            return 'voluntario'
        elif escolha == '3':
            return False
        else:
            print(" Opção inválida.")

if __name__ == "__main__":
    main()