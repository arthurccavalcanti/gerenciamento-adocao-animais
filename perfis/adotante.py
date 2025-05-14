import json
import re
import sys
sys.path.append(r"C:\Users\Casa\gerenciamento-adocao-animais")
from armazenamento.armazenamento_json import criar_entrada, ler_entrada, editar_entrada, deletar_entrada

CAMINHO_ARQUIVO = "json-test.json"



def validar_cpf(cpf):
    if re.match(r"^\d{11}$", cpf):  
        return True
    return False


def validar_idade(idade):
    return idade.isdigit() and int(idade) > 0


def validar_contato(contato):
    return contato.isdigit()


def carregar_dados():
     try:
         with open(CAMINHO_ARQUIVO, "r") as f:
             return json.load(f)
     except FileNotFoundError:
         return [] 
     


def salvar_dados(adotantes):
    with open(CAMINHO_ARQUIVO, "w") as f:
        json.dump(adotantes, f, indent=4)



def cadastrar_adotante(adotantes):
    while True:
        cpf = input("CPF (somente números, 11 dígitos): ")
        if not validar_cpf(cpf):
            print("CPF inválido! Certifique-se de que está no formato correto (11 dígitos).")
            continue

        nome = input("Nome completo: ")
        idade = input("Idade: ")
        if not validar_idade(idade):
            print("Idade inválida! Deve ser um número.")
            continue

        profissao = input("Profissão: ")
        endereco = input("Endereço: ")

        contato = input("Contato (somente números): ")
        if not validar_contato(contato):
            print("Contato inválido! Deve conter apenas números.")
            continue

        adotante = {
            "id": cpf,
            "nome": nome,
            "idade": int(idade),
            "profissao": profissao,
            "endereco": endereco,
            "contato": contato
        }

        criar_entrada(adotante, "json-test.json")
        break
        


def listar_adotantes_por_cpf():
    cpf = input("Digite o cpf do adotante")
    adotante = ler_entrada(cpf,"json-test.json")
    if isinstance(adotante,dict):
        print(adotante)


