from armazenamento import armazenamento_json

def test_armazenamento():

    armazenamento_json.verificar_configuracao()
    print("Teste do módulo armazenamento_json:")

    TEST_JSON = "teste_crud.json"
    dados = {"id": 1, "nome": "Teste"}

    def test_criar_entrada():
        print("\n1. Criando entrada...")
        if not isinstance(armazenamento_json.criar_entrada(dados, TEST_JSON), int):
            print("✓ Criado com sucesso")
        else:
            print("✗ Falha ao criar")
    
    def test_ler_entrada():
        print("\n2. Lendo entrada...")
        entrada = armazenamento_json.ler_entrada(1, "id", TEST_JSON)
        if not isinstance(entrada, int):
            print(f"✓ Lido com sucesso: {entrada}")
        else:
            print("✗ Falha ao ler")

    def test_editar_entrada():
        print("\n3. Editando entrada...")
        res = armazenamento_json.editar_entrada(1, "id", {"nome": "Teste Modificado"}, TEST_JSON)
        if not isinstance(res, int):
            print("✓ Editado com sucesso")
            print(f"Novos dados: {armazenamento_json.ler_entrada(1, 'id', TEST_JSON)}")
        else:
            print("✗ Falha ao editar")

    def test_deletar_entrada():
        print("\n4. Deletando entrada...")
        res = armazenamento_json.deletar_entrada(1, "id", TEST_JSON)
        if not isinstance(res, int):
            print("✓ Deletado com sucesso")
        else:
            print("✗ Falha ao deletar")