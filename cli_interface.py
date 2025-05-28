def exibir_ascii_logo():
    logo = r"""
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
         \_)))\   (   `._  .:Y)__)
          '''  \   `-._.'`---^_)))
                `-._ )))
    """
    print(logo)

def exibir_menu():
    exibir_ascii_logo()
    print("\n---- MENU PRINCIPAL ----\n")
    print("1. Gerenciar dados (CRUD)")
    print("2. Fazer match")
    print("3. Sair")
    
    while True:
        escolha = input("Escolha uma opção: ").strip()
        if escolha == '1':
            return 'CRUD'
        elif escolha == '2':
            return 'match'
        elif escolha == '3':
            return 'sair'
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

def exibir_menu_crud():
    ascii_animal = r"""
      / \__ 
     (    @\___      
    /          O     
   /    (_____/      
  /_____/    U       
    """
    print(ascii_animal)
    print("\n---- MENU CRUD ----  \n")
    print("1. Adotante")
    print("2. Pet")
    print("3. Voluntário")
    print("4. Voltar ao menu principal")
    
    while True:
        escolha = input("Escolha o perfil a ser gerenciado: ").strip()
        if escolha == '1':
            return escolher_operacao('adotante')
        elif escolha == '2':
            return escolher_operacao('pet')
        elif escolha == '3':
            return escolher_operacao('voluntario')
        elif escolha == '4':
            return None
        else:
            print("Opção inválida. Por favor, escolha 1, 2, 3 ou 4.")

def escolher_operacao(perfil):
    print("\n---- OPERAÇÕES DISPONÍVEIS ----\n")
    print(f"1. Criar {perfil.capitalize()}")
    print(f"2. Ler {perfil.capitalize()}s")
    print(f"3. Editar {perfil.capitalize()}")
    print(f"4. Deletar {perfil.capitalize()}")
    print("5. Voltar para o Menu")
    
    while True:
        escolha = input("Escolha a operação desejada: ").strip()
        if escolha == '1':
            return ('criar ' + perfil, perfil)
        elif escolha == '2':
            return ('ler ' + perfil + 's', perfil)
        elif escolha == '3':
            return ('editar ' + perfil, perfil)
        elif escolha == '4':
            return ('deletar ' + perfil, perfil)
        elif escolha == '5':
            return None
        else:
            print("Opção inválida. Por favor, escolha de 1 a 5.")

def exibir_menu_match():
    ascii_coracoes = r"""
   ___     ___
  (o o)   (o o)
 (  V  ) (  V  )
/--m-m- /--m-m-
    """
    print(ascii_coracoes)
    print("\n---- MENU DE MATCH ----\n")
    print("1. Fazer match com Pets")
    print("2. Fazer match com Voluntários")
    print("3. Voltar ao menu principal")
    
    while True:
        escolha = input("Escolha a opção de match: ").strip()
        if escolha == '1':
            return 'pets'
        elif escolha == '2':
            return 'voluntarios'
        elif escolha == '3':
            return None
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
