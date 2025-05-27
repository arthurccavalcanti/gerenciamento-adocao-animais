import cli_interface
from perfis import adotantes, pets, voluntarios
from match import match_pet, match_voluntario


def main():

    while True:
        operacao = cli_interface.exibir_menu()

        while operacao == 'CRUD':
            escolha_usuario = cli_interface.exibir_menu_crud()
            if not escolha_usuario:
                break

            tipo_operacao, perfil = escolha_usuario
            if perfil == 'pet':
                resultado_crud = pets.crud_pets(tipo_operacao)
            elif perfil == 'voluntario':
                resultado_crud = voluntarios.crud_voluntarios(tipo_operacao)
            elif perfil == 'adotante':
                resultado_crud = adotantes.crud_adotantes(tipo_operacao)

            if not cli_interface.exibir_resultado(resultado_crud, 'crud'):   
                print("Voltando ao menu principal...\n")
                break

        while operacao == 'match':
            escolha_usuario = cli_interface.exibir_menu_match()
            if not escolha_usuario:
                break

            if escolha_usuario == 'pets':
                resultado_match = match_pet.match_pets()
            elif escolha_usuario == 'voluntarios':
                resultado_match = match_voluntario.match_voluntario()

            if not cli_interface.exibir_resultado(resultado_match, 'match'):
                print("Voltando ao menu principal...\n")
                break
  
        if operacao == 'sair':
            print("Encerrando o programa. Até mais! =)\n")
            break



if __name__ == "__main__":
    main()