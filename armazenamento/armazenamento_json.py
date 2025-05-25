import json
import os


caminho_diretorio = os.path.dirname(os.path.abspath(__name__))


def carregar_arquivo(nome_json: str):

    caminho_arquivo = os.path.join(caminho_diretorio, 'armazenamento', nome_json)

    if not os.path.exists(caminho_arquivo):
        print("Arquivo não existe. Criando arquivo...")
        try:
            with open(caminho_arquivo, 'w') as f:
                json.dump([], f, indent=4)
        except:
            print(f"Erro criando arquivo: {caminho_arquivo}.")
            return 1

    with open(caminho_arquivo, 'r') as f:
        try:
            return json.loads(f)
        except:
            print(f"Erro ao abrir arquivo: {caminho_arquivo}")
            return 2


# O parâmetro 'nome_json' é o nome do json, incluindo a extensão '.json' (ex. 'animais.json')
def criar_entrada(dados: dict, nome_json: str):

    caminho_arquivo = os.path.join(caminho_diretorio, 'armazenamento', nome_json)

    if not os.path.exists(caminho_arquivo):
        print("Arquivo não existe. Criando arquivo...")
        try:
            with open(caminho_arquivo, 'w') as f:
                json.dump([], f, indent=4)
        except:
            print(f"Erro criando arquivo {caminho_arquivo}.")
            return 1

    try:
        with open(caminho_arquivo, 'r') as f:
            arquivo_json = json.load(f)
    
        arquivo_json.append(dados)

        with open(caminho_arquivo, 'w') as f:
            json.dump(arquivo_json, f, indent=4)
    except:
        print("Erro ao adicionar entrada.")
        return 2

    print(f"Os dados {dados} foram adicionados ao arquivo {nome_json}.")

    return True


# ---------------------------------------------

def ler_entrada(id: int, chave_id: str, nome_json: str):

    caminho_arquivo = os.path.join(caminho_diretorio, 'armazenamento', nome_json)

    if not os.path.exists(caminho_arquivo):
        print(f"O arquivo não existe: {caminho_arquivo}")
        return 1
    
    with open(caminho_arquivo, 'r') as f:
        arquivo_json = json.load(f)

    for entrada in arquivo_json:
        if entrada[chave_id] == id:
            return entrada
        
    print(f"O ID {id} não existe.")
    return 2

# --------------------------------------------------

def editar_entrada(id: int, chave_id: str, dados_atualizados: dict, nome_json: str):

    caminho_arquivo = os.path.join(caminho_diretorio, 'armazenamento', nome_json)

    if not os.path.exists(caminho_arquivo):
        print(f"O arquivo não existe: {caminho_arquivo}")
        return 1
    
    with open(caminho_arquivo, 'r') as f:
        arquivo_json = json.load(f)

    for entrada in arquivo_json:
        if entrada[chave_id] == id:
            for chave, valor in dados_atualizados.items():
                entrada[chave] = valor

            with open(caminho_arquivo, 'w') as f:
                json.dump(arquivo_json, f, indent=4)

            print(f"O arquivo {nome_json} foi atualizado com {dados_atualizados}.")
            return True
        
    print(f"Não há entrada com o id {id}.")
    return 2
        
# -------------------------------------------------------

def deletar_entrada(id: int, chave_id: str, nome_json: str):

    caminho_arquivo = os.path.join(caminho_diretorio, 'armazenamento', nome_json)

    if not os.path.exists(caminho_arquivo):
        print(f"O arquivo não existe: {caminho_arquivo}.")
        return 1
    
    with open(caminho_arquivo, 'r') as f:
        arquivo_json = json.load(f)

    for entrada in arquivo_json:
        if entrada[chave_id] == id:
            arquivo_json.remove(entrada)
            with open(caminho_arquivo, 'w') as f:
                json.dump(arquivo_json, f, indent=4)
            print(f"A entrada com id {id} foi deletada.")
            return True
    
    print(f"Não há entrada com o id {id}.")
    return 2

