'''
Funções CREATE, READ, UPDATE, UPLOAD, DELETE 
'''
import json
import os


# Define o caminho do diretório.
caminho_diretorio = os.path.dirname(os.path.abspath(__name__))


# FUNÇÃO CRIAR
'''
O parâmetro 'dados' é um dicionário com os dados a serem acrescentados.
O parâmetro 'nome_json' é uma string com o nome do json, incluindo a extensão '.json' (ex. 'animais.json')
A função adiciona o dicionário dado ao arquivo json.
'''
def criar_entrada(dados, nome_json):

    caminho_arquivo = os.path.join(caminho_diretorio, 'armazenamento', nome_json)

    # Cria arquivo json caso ele não exista.
    if not os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, 'w') as f:
            json.dump([], f, indent=4)

    with open(caminho_arquivo, 'r') as f:
        arquivo_json = json.load(f)
    
    arquivo_json.append(dados)

    with open(caminho_arquivo, 'w') as f:
        json.dump(arquivo_json, f, indent=4)

    print(f"Os dados {dados} foram adicionados ao arquivo {nome_json}.")

    return 0


# ---------------------------------------------

# FUNÇÃO LEITURA
'''
A função deve ser atualizada se a ID fornecida não tiver como chave uma string 'id'.
Neste caso, o programa que chamar a função pode enviar a string da chave como um parâmetro extra.
'''

def ler_entrada(id, nome_json):

    caminho_arquivo = os.path.join(caminho_diretorio, 'armazenamento', nome_json)

    if not os.path.exists(caminho_arquivo):
        print("O arquivo não existe.")
        return 1
    
    with open(caminho_arquivo, 'r') as f:
        arquivo_json = json.load(f)

    for entrada in arquivo_json:
        if entrada['id'] == id:
            return entrada
        
    print("O ID fornecido não existe.")
    return 2

# --------------------------------------------------

# FUNÇÃO ATUALIZAR

def editar_entrada(id, dados_atualizados, nome_json):

    caminho_arquivo = os.path.join(caminho_diretorio, 'armazenamento', nome_json)

    if not os.path.exists(caminho_arquivo):
        print("O arquivo não existe.")
        return 1
    
    with open(caminho_arquivo, 'r') as f:
        arquivo_json = json.load(f)

    for entrada in arquivo_json:
        if entrada['id'] == id:
            for chave, valor in dados_atualizados.items():
                entrada[chave] = valor
            with open(caminho_arquivo, 'w') as f:
                json.dump(arquivo_json, f, indent=4)
            print(f"O arquivo {nome_json} foi atualizado com {dados_atualizados}")
            return 0
    
    print(f"Não há entradas com o id {id}.")
    return 1
        
# -------------------------------------------------------

# FUNÇÃO UPLOAD
'''
Carrega dados de um arquivo JSON externo e adiciona ao arquivo principal de armazenamento.

Parâmetros:
- caminho_upload: caminho para o JSON de onde os dados serão lidos.
- nome_json: nome do arquivo JSON de destino (armazenamento) onde os dados serão adicionados.
'''

def upload_entradas(caminho_upload, nome_json):
    caminho_destino = os.path.join(caminho_diretorio, 'armazenamento', nome_json)

    if not os.path.exists(caminho_upload):
        print(f"O arquivo de upload {caminho_upload} não foi encontrado.")
        return 1

    # Garante que o destino existe
    if not os.path.exists(caminho_destino):
        with open(caminho_destino, 'w') as f:
            json.dump([], f, indent=4)

    # Lê os dados do arquivo externo
    with open(caminho_upload, 'r') as f:
        dados_upload = json.load(f)

    # Lê os dados existentes no destino
    with open(caminho_destino, 'r') as f:
        dados_destino = json.load(f)

    # Adiciona os novos dados
    dados_destino.extend(dados_upload)

    # Salva de volta
    with open(caminho_destino, 'w') as f:
        json.dump(dados_destino, f, indent=4)

    print(f"{len(dados_upload)} entradas foram carregadas de {caminho_upload} para {nome_json}.")
    return 0

# -------------------------------------------------------

# FUNÇÃO DELETAR

def deletar_entrada(id, nome_json):

    caminho_arquivo = os.path.join(caminho_diretorio, 'armazenamento', nome_json)

    if not os.path.exists(caminho_arquivo):
        print("O arquivo não existe.")
        return 1
    
    with open(caminho_arquivo, 'r') as f:
        arquivo_json = json.load(f)

    for entrada in arquivo_json:
        if entrada['id'] == id:
            arquivo_json.remove(entrada)
            with open(caminho_arquivo, 'w') as f:
                json.dump(arquivo_json, f, indent=4)
            print(f"A entrada com id {id} foi deletada")
            return 0
    
    print(f"Não há entradas com o id {id}.")
    return 1

# ---------------------------------------------------------

if __name__ == "__main__":

    dados1 = {'id':1, 'idade':23}
    dados2 = {'id':2, 'idade':3}

    criar_entrada(dados1, 'teste.json')
    criar_entrada(dados2, 'teste.json')

    deletar_entrada(2, 'teste.json')

    entrada2 = ler_entrada(1, 'teste.json')
    print(entrada2)

    editar_entrada(1, {'id':3, 'idade':4}, 'teste.json')

    entrada5 = ler_entrada(3, 'teste.json')
    print(entrada5)

# ---------------------------------------------------------
