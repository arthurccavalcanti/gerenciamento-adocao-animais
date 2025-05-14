import json
import os

arquivo = os.path.join(os.path.dirname(__file__), 'pets.json')

def carregar_pets():
  if not os.path.exists(arquivo):
    with open(arquivo, 'w') as f:
      json.dump([], f, indent=4)
      return []
    
  with open(arquivo, 'r') as f:
    return json.load(f)


def listar_pets():
    pets = carregar_pets()

    if pets:
        print("=" * 50)
        print("LISTA DE Pets:")
        print("-" * 50)
        for pet in pets:
            print("*" * 50)
            print(f"ID: {pet['id']}, TIPO: {pet['tipo']}, NOME: {pet['nome']}, IDADE: {pet['idade']}, SEXO: {pet['sexo']}, PERSONALIDADE: {pet['personalidade']}, HISTÓRICO: {pet['historico']}, RAÇA: {pet['raca']}, COR: {pet['cor']}, PORTE: {pet['porte']}")
            print("*" * 50)
            print("=" * 50)
    else:
        print("NENHUM PET CADASTRADO.")

def seus_pets(responsavel):
    pets = carregar_pets()
    pets_responsavel = [pet for pet in pets if pet.get('responsavel') == responsavel]
    return pets_responsavel