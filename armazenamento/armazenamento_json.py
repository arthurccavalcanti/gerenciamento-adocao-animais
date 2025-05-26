import json
import os
from typing import List, Dict


caminho_diretorio_projeto = os.path.dirname(os.path.abspath(__name__))
caminho_diretorio_armazenamento = caminho_diretorio_projeto + '\\armazenamentoJSON'
caminho_diretorio_armazenamento.mkdir(exist_ok=True, parents=True)

def get_caminho_arquivo(nome_arquivo: str):
    return caminho_diretorio_armazenamento + f'\\{nome_arquivo}'


def carregar_arquivo(nome_json: str) -> List:

    caminho_arquivo = get_caminho_arquivo(nome_json)
    if not os.path.exists(caminho_arquivo):
        print("Arquivo não existe. Criando arquivo...")
        try:
            with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                json.dump([], f, indent=4)
            with open(caminho_arquivo, 'r') as f:
                return json.loads(f)
        except:
            print(f"Erro ao criar arquivo: {caminho_arquivo}")
            return 1
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            return json.loads(f)
    except json.JSONDecodeError:
        print(f"Arquivo {nome_json} corrompido.")
        return 2
    except PermissionError:
        print(f"ERRO: Sem permissão para acessar {caminho_arquivo}")
        return 3        
    except Exception as e:
        print(f"ERRO inesperado ao ler {nome_json}: {e}")
        return 4


def criar_entrada(dados: Dict, nome_json: str) -> bool:
    
    conteudo = carregar_arquivo(nome_json)
    if isinstance(conteudo, int):
        return conteudo 

    conteudo.append(dados)
    caminho_arquivo = get_caminho_arquivo(nome_json)

    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            json.dump(conteudo, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"ERRO ao salvar {nome_json}: {e}")
        return 6


def ler_entrada(id: int, chave_id: str, nome_json: str) -> Dict:
    
    conteudo = carregar_arquivo(nome_json)
    if isinstance(conteudo, int):
        return conteudo 

    for entrada in conteudo:
        if isinstance(entrada, dict) and entrada.get(chave_id) == id:
            return entrada

    print(f"AVISO: Entrada com {chave_id}={id} não encontrada em {nome_json}")
    return 7


def editar_entrada(id: int, chave_id: str, dados_atualizados: Dict, nome_json: str) -> bool:
    
    conteudo = carregar_arquivo(nome_json)
    if isinstance(conteudo, int):
        return conteudo
    
    for entrada in conteudo:
        if entrada[chave_id] == id:
            for chave, valor in dados_atualizados.items():
                entrada[chave] = valor

            try:
                with open(get_caminho_arquivo(nome_json), 'w') as f:
                    json.dump(conteudo, f, indent=4)

                print(f"O arquivo {nome_json} foi atualizado com {dados_atualizados}.")
                return True
            except Exception as e:
                print(f"ERRO inesperado ao editar {nome_json}: {e}")
                return 8
       
    print(f"ERRO: Não há entrada com o id {id}.")
    return 9


def deletar_entrada(id: int, chave_id: str, nome_json: str) -> bool:

    conteudo = carregar_arquivo(nome_json)
    if isinstance(conteudo, int):
        return conteudo

    for entrada in conteudo:
        if entrada[chave_id] == id:
            conteudo.remove(entrada)
            try:
                with open(get_caminho_arquivo(nome_json), 'w') as f:
                    json.dump(conteudo, f, indent=4)
                print(f"A entrada com id {id} foi deletada.")
                return True
            except Exception as e:
                print(f"ERRO inesperado ao deletar entrada em {nome_json}: {e}")
                return 10
            
    print(f"Não há entrada com o id {id} em {nome_json}.")
    return 11


def verificar_configuracao():
    """Verifica as configurações de armazenamento"""
    print("\n=== VERIFICAÇÃO DE CONFIGURAÇÃO ===")
    print(f"Diretório base: {caminho_diretorio_projeto}")
    print(f"Diretório de armazenamento: {caminho_diretorio_armazenamento}")
    
    try:
        caminho_diretorio_armazenamento.mkdir(exist_ok=True)
        print("✓ Diretório de armazenamento acessível")
    except Exception as e:
        print(f"✗ ERRO: Não foi possível acessar o diretório: {e}")
        return False
    
    test_file = get_caminho_arquivo('teste_config.json')
    try:
        with open(test_file, 'w', encoding='utf-8') as f:
            json.dump({"teste": "ok"}, f)
        
        with open(test_file, 'r', encoding='utf-8') as f:
            conteudo = json.load(f)
        
        test_file.unlink()
        print("✓ Leitura/gravação funcionando corretamente")
        return True
    except Exception as e:
        print(f"✗ ERRO: Problema ao ler/escrever arquivo: {e}")
        return False
    finally:
        print("="*50 + "\n")
