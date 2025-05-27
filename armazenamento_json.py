import json
import time
from pathlib import Path
from typing import Union, List, Dict, Optional


BASE_DIR = Path(__file__).parent
ARMAZENAMENTO_DIR = BASE_DIR / 'armazenamentoJSON'


ARMAZENAMENTO_DIR.mkdir(exist_ok=True, parents=True)

def get_caminho_arquivo(nome_arquivo: str) -> Path:
    return ARMAZENAMENTO_DIR / nome_arquivo

def carregar_arquivo(nome_json: str) -> Optional[Union[List, Dict]]:
    """
    Carrega o conteúdo de um arquivo JSON.
    Se o arquivo não existir, cria um novo com uma lista vazia.
    
    Args:
        nome_json (str): Nome do arquivo JSON (incluindo extensão)
        
    Returns:
        Union[List, Dict]: Conteúdo do arquivo JSON
        None: Em caso de erro crítico
    """
    caminho_arquivo = get_caminho_arquivo(nome_json)
    
    for tentativa in range(3):
        try:
            
            if not caminho_arquivo.exists():
                with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                    json.dump([], f, indent=4)
                return []
                  
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                conteudo = json.load(f)
                return conteudo
                
        except json.JSONDecodeError:
            print(f"AVISO: Arquivo {nome_json} corrompido. Tentando recuperar...")
           
            try:
                backup_path = caminho_arquivo.with_suffix('.bak')
                if caminho_arquivo.exists():
                    caminho_arquivo.rename(backup_path)
                continue
            except Exception as e:
                print(f"ERRO ao tentar fazer backup: {e}")
                return None
                
        except PermissionError:
            print(f"ERRO: Sem permissão para acessar {caminho_arquivo}")
            return None
            
        except Exception as e:
            print(f"ERRO inesperado ao ler {nome_json}: {e}")
            time.sleep(1)  
            continue
    
    print(f"FALHA: Não foi possível carregar {nome_json} após 3 tentativas")
    return None

def criar_entrada(dados: Dict, nome_json: str) -> bool:
    
    conteudo = carregar_arquivo(nome_json)
    if conteudo is None:
        return False

    if not isinstance(conteudo, list):
        print(f"ERRO: O arquivo {nome_json} não contém uma lista válida")
        return False

    conteudo.append(dados)
    caminho_arquivo = get_caminho_arquivo(nome_json)

    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            json.dump(conteudo, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"ERRO ao salvar {nome_json}: {e}")
        return False

def ler_entrada(id: int, chave_id: str, nome_json: str) -> Optional[Dict]:
    
    conteudo = carregar_arquivo(nome_json)
    if conteudo is None:
        return None

    if not isinstance(conteudo, list):
        print(f"ERRO: O arquivo {nome_json} não contém uma lista válida")
        return None

    for entrada in conteudo:
        if isinstance(entrada, dict) and entrada.get(chave_id) == id:
            return entrada

    print(f"AVISO: Entrada com {chave_id}={id} não encontrada em {nome_json}")
    return None

def editar_entrada(id: int, chave_id: str, dados_atualizados: Dict, nome_json: str) -> bool:
    
    conteudo = carregar_arquivo(nome_json)
    if conteudo is None:
        return False

    if not isinstance(conteudo, list):
        print(f"ERRO: O arquivo {nome_json} não contém uma lista válida")
        return False

    entrada_encontrada = False
    for entrada in conteudo:
        if isinstance(entrada, dict) and entrada.get(chave_id) == id:
            entrada.update(dados_atualizados)
            entrada_encontrada = True
            break

    if not entrada_encontrada:
        print(f"AVISO: Entrada com {chave_id}={id} não encontrada")
        return False

    caminho_arquivo = get_caminho_arquivo(nome_json)
    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            json.dump(conteudo, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"ERRO ao salvar {nome_json}: {e}")
        return False

def deletar_entrada(id: int, chave_id: str, nome_json: str) -> bool:
    """
    Remove uma entrada do arquivo JSON.
    
    Args:
        id (int): ID da entrada a ser removida
        chave_id (str): Nome da chave que contém o ID
        nome_json (str): Nome do arquivo JSON
        
    Returns:
        bool: True se bem sucedido, False caso contrário
    """
    conteudo = carregar_arquivo(nome_json)
    if conteudo is None:
        return False

    if not isinstance(conteudo, list):
        print(f"ERRO: O arquivo {nome_json} não contém uma lista válida")
        return False

    nova_lista = [entrada for entrada in conteudo 
                 if isinstance(entrada, dict) and entrada.get(chave_id) != id]
    
    if len(nova_lista) == len(conteudo):
        print(f"AVISO: Entrada com {chave_id}={id} não encontrada")
        return False

    caminho_arquivo = get_caminho_arquivo(nome_json)
    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            json.dump(nova_lista, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"ERRO ao salvar {nome_json}: {e}")
        return False

def verificar_configuracao():
    """Verifica as configurações de armazenamento"""
    print("\n=== VERIFICAÇÃO DE CONFIGURAÇÃO ===")
    print(f"Diretório base: {BASE_DIR}")
    print(f"Diretório de armazenamento: {ARMAZENAMENTO_DIR}")
    
    
    try:
        ARMAZENAMENTO_DIR.mkdir(exist_ok=True)
        print("✓ Diretório de armazenamento acessível")
    except Exception as e:
        print(f"✗ ERRO: Não foi possível acessar o diretório: {e}")
        return False
    
    
    test_file = ARMAZENAMENTO_DIR / 'teste_config.json'
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

if __name__ == "__main__":
    
    verificar_configuracao()
    print("Teste do módulo armazenamento_json:")
    
    TEST_JSON = "teste_crud.json"
    
    print("\n1. Criando entrada...")
    dados = {"id": 1, "nome": "Teste"}
    if criar_entrada(dados, TEST_JSON):
        print("✓ Criado com sucesso")
    else:
        print("✗ Falha ao criar")
    
    print("\n2. Lendo entrada...")
    entrada = ler_entrada(1, "id", TEST_JSON)
    if entrada:
        print(f"✓ Lido com sucesso: {entrada}")
    else:
        print("✗ Falha ao ler")
    
    print("\n3. Editando entrada...")
    if editar_entrada(1, "id", {"nome": "Teste Modificado"}, TEST_JSON):
        print("✓ Editado com sucesso")
        print(f"Novos dados: {ler_entrada(1, 'id', TEST_JSON)}")
    else:
        print("✗ Falha ao editar")
    
    print("\n4. Deletando entrada...")
    if deletar_entrada(1, "id", TEST_JSON):
        print("✓ Deletado com sucesso")
    else:
        print("✗ Falha ao deletar")
    
    
    try:
        (ARMAZENAMENTO_DIR / TEST_JSON).unlink()
    except:
        pass