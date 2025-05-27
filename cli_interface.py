import pprint

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
        print("3. Voltar ao menu principal")
        escolha = input("Escolha uma opção: ")

        opcoes = {
            '1': 'pet',
            '2': 'adotante',
            '3': False
        }

        if escolha in opcoes:
            return opcoes[escolha]
        else:
            print("Opção inválida. Tente novamente.")



def exibir_resultado(resultado, tipo):
    print(f"\n--- RESULTADO ({tipo.upper()}) ---")
    if tipo == 'crud':
        if isinstance(resultado, tuple):
            operacao, dados = resultado
            if operacao == 'ler':
                print("Aqui estão os dados que você pediu:")
                print(dados)
            elif operacao == 'criar':
                print("Você salvou:")
                print(dados)
            elif operacao == 'editar':
                dados_antigos, dados_novos = dados
                print("Você editou:")
                print("Dados alterados: ", dados_antigos)
                print("Dados novos: ", dados_novos)
            elif operacao == 'deletar':
                print("Você exclui com sucesso estes dados:")
                print(dados)
        else:
            print("Houve um erro com a sua operação: ")
            print(resultado)
    elif tipo == 'match':
        print("\n🔍 Melhores Matches:\n")
        for match in resultado:
            pprint.pprint(resultado)

    while True:
        escolha = input("Deseja realizar outra operação? (s/n): ").lower()
        if escolha == 's':
            return True
        elif escolha == 'n':
            return False
        else:
            print("Escolha inválida. Digite 's' ou 'n'.")
