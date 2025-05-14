import json
import os

arquivo = os.path.join(os.path.dirname(__file__), 'pets.json')

# Carrega a lista de pets do arquivo
def carregarPets():
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump([], f, indent=4)
        return []
    with open(arquivo, 'r') as f:
        return json.load(f)

def seusPets(responsavel):
    pets = carregarPets()
    pets_responsavel = [pet for pet in pets if pet.get('responsavel') == responsavel]
    return pets_responsavel

def listarPets():
    pets = carregarPets()
    if pets:
        print("=" * 50)
        print("LISTA DE PETS:\n")
        for pet in pets:
            print("*" * 50)
            print(f"ID: {pet['id']}, TIPO: {pet['tipo']}, NOME: {pet['nome']}, IDADE: {pet['idade']}, SEXO: {pet['sexo']}, "
                  f"PERSONALIDADE: {pet['personalidade']}, HISTÓRICO: {pet['historico']}, RAÇA: {pet['raca']}, "
                  f"COR: {pet['cor']}, PORTE: {pet['porte']}")
            print("*" * 50)
        print("=" * 50)
    else:
        print("NENHUM PET CADASTRADO.")

def listarSeusPets(responsavel):
    pets = seusPets(responsavel)
    if pets:
        print("=" * 50)
        print(f"PETS DO RESPONSÁVEL: {responsavel.upper()}\n")
        for pet in pets:
            print("*" * 50)
            print(f"ID: {pet['id']}, TIPO: {pet['tipo']}, NOME: {pet['nome']}, IDADE: {pet['idade']}, SEXO: {pet['sexo']}, "
                  f"PERSONALIDADE: {pet['personalidade']}, HISTÓRICO: {pet['historico']}, RAÇA: {pet['raca']}, "
                  f"COR: {pet['cor']}, PORTE: {pet['porte']}")
            print("*" * 50)
        print("=" * 50)
    else:
        print("Você não possui pets cadastrados.")

def deletarPet(responsavel):
    pets = seusPets(responsavel)
    if not pets:
        print("Você não possui pets cadastrados.")
        return

    listarSeusPets(responsavel)

    while True:
        id_escolhido = input("Digite o ID do pet que deseja deletar: ")
        try:
            id_escolhido = int(id_escolhido)
        except ValueError:
            print("ID inválido. Use apenas números.")
            continue

        todos_pets = carregarPets()
        encontrado = False
        for pet in todos_pets:
            if pet['id'] == id_escolhido:
                encontrado = True
                if pet['responsavel'] == responsavel:
                    todos_pets.remove(pet)
                    with open(arquivo, 'w') as f:
                        json.dump(todos_pets, f, indent=4, ensure_ascii=False)
                    print("Pet deletado com sucesso.")
                    return
                else:
                    print("Você não tem permissão para deletar este pet.")
                    return
        if not encontrado:
            print("Pet com esse ID não foi encontrado.")
