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
            print(f"Erro criando arquivo {caminho_arquivo}.")
            return 1

    with open(caminho_arquivo, 'r') as f:
        try:
            conteudo = f.read().strip()
            if not conteudo:
                return []
            return json.loads(conteudo)
        except:
            print("Erro ao abrir arquivo.")
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

    return 0


# ---------------------------------------------

def ler_entrada(id: int, chave_id: str, nome_json: str):

    caminho_arquivo = os.path.join(caminho_diretorio, 'armazenamento', nome_json)

    if not os.path.exists(caminho_arquivo):
        print("O arquivo não existe.")
        return 1
    
    with open(caminho_arquivo, 'r') as f:
        arquivo_json = json.load(f)

    for entrada in arquivo_json:
        if entrada[chave_id] == id:
            return entrada
        
    print("O ID fornecido não existe.")
    return 2

# --------------------------------------------------

def editar_entrada(id: int, chave_id: str, dados_atualizados: dict, nome_json: str):

    caminho_arquivo = os.path.join(caminho_diretorio, 'armazenamento', nome_json)

    if not os.path.exists(caminho_arquivo):
        print("O arquivo não existe.")
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
            return 0
        
    print(f"Não há entrada com o id {id}.")
    return 1
        
# -------------------------------------------------------

def deletar_entrada(id: int, chave_id: str, nome_json: str):

    caminho_arquivo = os.path.join(caminho_diretorio, 'armazenamento', nome_json)

    if not os.path.exists(caminho_arquivo):
        print("O arquivo não existe.")
        return 1
    
    with open(caminho_arquivo, 'r') as f:
        arquivo_json = json.load(f)

    for entrada in arquivo_json:
        if entrada[chave_id] == id:
            arquivo_json.remove(entrada)
            with open(caminho_arquivo, 'w') as f:
                json.dump(arquivo_json, f, indent=4)
            print(f"A entrada com id {id} foi deletada.")
            return 0
    
    print(f"Não há entrada com o id {id}.")
    return 1

# ---------------------------------------------------------

if __name__ == "__main__":

    dados1 = {'id':1, 'idade':23}
    dados2 = {'id':2, 'idade':3}

    criar_entrada(dados1, 'teste.json')
    criar_entrada(dados2, 'teste.json')

    deletar_entrada(2, 'id', 'teste.json')

    entrada2 = ler_entrada(1, 'id', 'teste.json')
    print(entrada2)

    editar_entrada(1, 'id', {'id':3, 'idade':4}, 'teste.json')

    entrada5 = ler_entrada(3, 'id', 'teste.json')
    print(entrada5)