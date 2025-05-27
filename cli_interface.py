import pprint

def exibir_menu():
    while True:
        gato = r"""
        (`.
         ) )
        ( (
         \ \
          \ \
        .-'  `-.
       /        `.
      (      )    `-._ ,    _
       )   ,'         (.\--'(
       \  (         ) /      \
        \  \_(     / (    <6 (6
         \_)))\   (   `._  .:Y)__
          '''  \   `-._.'`---^_)))
                `-._ )))                                
                """
        print(gato)
        print("\n---- MENU PRINCIPAL ----\n")
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
        cachorro = r"""
      / \__ 
     (    @\___  
    /          O 
   /    (_____/      
  /_____/    U 
                    """
        print(cachorro)
        print("\n---- MENU CRUD ----\n")
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

            print("\n---- OPERAÇÕES DISPONÍVEIS ----\n")
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
        coelho = r"""

                     /\    .-" /
                    /  ; .'  .' 
                   :   :/  .'   
                    \  ;-.'     
       .--''''--..__/     `.    
     .'           .'    `o  \   
    /                    `   ;  
   :                  \      :  
 .-;        -.         `.__.-'  
:  ;          \     ,   ;       
'._:           ;   :   (        
    \/  .__    ;    \   `-.     
 ;     "-,/_..--"`-..__)    
     '""--.._:
                """
        print(coelho)
        print("\n---- MENU MATCH ----\n")
        print("1. Melhores matches para um pet")
        print("2. Melhores matches para um voluntário")
        print("3. Voltar ao menu principal")
        escolha = input("Escolha uma opção: ")

        opcoes = {
            '1': 'pets',
            '2': 'voluntarios',
            '3': False
        }

        if escolha in opcoes:
            return opcoes[escolha]
        print("Opção indisponível. Tente novamente.")



def exibir_resultado(resultado, tipo):
    corujas = r"""
   ___     ___
  (o o)   (o o)
 (  V  ) (  V  ) 
/--m-m- /--m-m-
                """
    print(corujas)
    if tipo == 'crud':
        if isinstance(resultado, tuple):
            print(f"\n===== RESULTADO ({tipo.upper()}) =====\n")
            operacao, dados = resultado
            if operacao == 'ler':
                print("\n---Aqui estão os dados que você pediu:")
                print(dados)
            elif operacao == 'criar':
                print("\n---Você salvou:")
                print(dados)
            elif operacao == 'editar':
                dados_antigos, dados_novos = dados
                print("\n---Você editou:")
                print("Dados alterados: ", dados_antigos)
                print("Dados novos: ", dados_novos)
            elif operacao == 'deletar':
                print("\n---Você exclui com sucesso estes dados:")
                print(dados)
        else:
            print("\nHouve um erro com a sua operação: ")
            print(resultado)
    elif tipo == 'match':
        if resultado is not None and isinstance(resultado, list):
            print("\n===== 🔍 MELHORES MATCHES =====\n")
            for i, match in enumerate(resultado[:4]):
                print(f"{i+1}º Match --------------\n")
                pprint.pprint(match,'\n')
        else:
            print("\nHouve um erro ao fazer o match:")
            print(resultado)

    while True:
        escolha = input("\nDeseja realizar outra operação? (s/n): ").lower()
        if escolha == 's':
            return True
        elif escolha == 'n':
            return False
        else:
            print("Escolha inválida. Digite 's' ou 'n'.")
