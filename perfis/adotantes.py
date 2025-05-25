import re
from armazenamento import armazenamento_json as armazenamento

def main(tipo_operacao: str):
    while True:
        print("DESEJA VISUALIZAR OS DADOS ANTES DA OPERAÇÃO?")
        print("1 - SIM")
        print("2 - NÃO")
        deseja_listar = input(">>> ")
        if deseja_listar == "1":
            listar_todos_adotantes()  
            break
        elif deseja_listar == "2":
            break
        else:
            print("Opção inválida.")    
    
    if tipo_operacao == "criar":
        return cadastrar_adotante()
    elif tipo_operacao == "atualizar":
        return atualizar_adotante()
    elif tipo_operacao == "deletar":
        return excluir_adotante()
    elif tipo_operacao == "ler":
        return ler_adotante()
    else:
        return "Operação inválida. Tente novamente."

def validar_contato(contato):
    return str(contato).isdigit() and len(str(contato)) >= 8

def validar_cpf(cpf):
    return re.match(r"^\d{11}$", cpf) is not None

def validar_idade(idade):
    return idade.isdigit() and int(idade) > 0

def validar_cep(cep):
    return re.match(r"^\d{8}$", cep) is not None

def listar_todos_adotantes():
    adotantes = armazenamento.listar_todos("adotantes.json")
    if isinstance(adotantes, list) and adotantes:
        print("\n--- Lista de Adotantes ---")
        for adotante in adotantes:
            print("-" * 30)
            for chave, valor in adotante.items():
                print(f"{chave}: {valor}")
    else:
        print("Nenhum adotante encontrado.")

def ler_adotante():
    cpf = input("Digite o CPF do adotante: \n")
    adotante = armazenamento.ler_entrada(cpf, 'CPF', "adotantes.json")
    if isinstance(adotante, dict):
        print("\n--- Dados do Adotante ---")
        for chave, valor in adotante.items():
            print(f"{chave}: {valor}")
        return ("ler", adotante)
    else:
        print("Adotante não encontrado.")
        return ("ler", None)

def cadastrar_adotante():
    while True:
        cpf = input("Digite o CPF (somente números, 11 dígitos): \n")
        if not validar_cpf(cpf):
            print("CPF inválido!\n")
            continue

        nome = input("Digite o nome completo: \n")

        idade = input("Digite a idade: \n")
        if not validar_idade(idade):
            print("Idade inválida!\n")
            continue
        idade = int(idade)

        profissao = input("Digite a profissão: \n")
        
        endereco = input("Digite o CEP (somente números): \n")
        if not validar_cep(endereco):
            print("CEP inválido! Deve conter 8 dígitos.\n")
            continue

        contato = input("Contato (somente números): ")
        if not validar_contato(contato):
            print("Contato inválido! Deve conter ao menos 8 dígitos.\n")
            continue
        contato = int(contato)

        print("\n--- Preferências do adotante ---")

        tipo = input("Prefere qual tipo de animal? (canino/felino): ").lower()
        while tipo not in ["canino", "felino"]:
            tipo = input("Entrada inválida. Digite canino ou felino: ").lower()

        porte = input("Porte preferido? (pequeno/médio/grande): ").lower()
        while porte not in ["pequeno", "médio", "grande"]:
            porte = input("Entrada inválida. Digite pequeno, médio ou grande: ").lower()

        temp = input("Personalidades preferidas (separe por vírgula, ex: brincalhão,calmo): ").lower()
        temperamento = [t.strip() for t in temp.split(",") if t.strip()]

        sexo = input("Sexo preferido? (macho/fêmea): ").lower()
        while sexo not in ["macho", "fêmea"]:
            sexo = input("Entrada inválida. Digite macho ou fêmea: ").lower()

        faixa_etaria = input("Faixa etária preferida? (filhote/adulto/idoso): ").lower()
        while faixa_etaria not in ["filhote", "adulto", "idoso"]:
            faixa_etaria = input("Entrada inválida. Digite filhote, adulto ou idoso: ").lower()

        experiencia = input("Tem experiência com animais? (s/n): ").lower()
        experiencia = True if experiencia == "s" else False

        preferencias = {
            "tipo": tipo,
            "porte": porte,
            "temperamento": temperamento,
            "sexo": sexo,
            "faixa_etaria": faixa_etaria,
            "experiencia": experiencia
        }

        adotante = {
            "id": cpf,
            "nome": nome,
            "idade": idade,
            "profissao": profissao,
            "endereco": endereco,
            "contato": contato,
            "preferencias": preferencias
        }

        print("\nConfira os dados inseridos:")
        for k, v in adotante.items():
            print(f"{k}: {v}")

        confirm = input("Deseja salvar esse adotante? (s/n): ").lower()
        if confirm == "s":
            armazenamento.criar_entrada(adotante, "adotantes.json")
            print("Adotante cadastrado com sucesso!")
            return ("criar", adotante)
        else:
            print("Cadastro cancelado.")
            return ("criar", None)

def atualizar_adotante():
    cpf = input("Digite o CPF do adotante: ")
    dados_atuais = armazenamento.ler_entrada(cpf, "CPF", "adotantes.json")
    if not dados_atuais:
        print("Adotante não encontrado.")
        return ("atualizar", None)

    print("Dados atuais:")
    for k, v in dados_atuais.items():
        print(f"{k}: {v}")

    nome = input("Novo nome: ")

    while True:
        idade = input("Nova idade: ")
        if validar_idade(idade):
            idade = int(idade)
            break
        print("Idade inválida!")

    profissao = input("Nova profissão: ")

    while True:
        endereco = input("Novo CEP (somente números): ")
        if validar_cep(endereco):
            break
        print("CEP inválido! Deve conter 8 dígitos.")

    while True:
        contato = input("Novo contato (somente números): ")
        if validar_contato(contato):
            contato = int(contato)
            break
        print("Contato inválido! Deve conter ao menos 8 dígitos.")

    novos_dados = {
        "nome": nome,
        "idade": idade,
        "profissao": profissao,
        "endereco": endereco,
        "contato": contato
    }

    print("\nConfira as alterações:")
    for chave in novos_dados:
        print(f"{chave}: {dados_atuais[chave]} → {novos_dados[chave]}")

    if confirmar_acao("Deseja prosseguir com a atualização? (s/n): "):
        armazenamento.editar_entrada(cpf, novos_dados, "adotantes.json")
        dados_atuais.update(novos_dados)
        print("Adotante atualizado com sucesso!")
        return ("atualizar", dados_atuais)
    else:
        print("Atualização cancelada.")
        return ("atualizar", None)

def excluir_adotante():
    cpf = input("Digite o CPF do adotante a excluir: ")
    adotante = armazenamento.ler_entrada(cpf, "CPF", "adotantes.json")
    if not adotante:
        print("Adotante não encontrado.")
        return ("deletar", None)

    print("Adotante encontrado:")
    for k, v in adotante.items():
        print(f"{k}: {v}")
    confirm = input("Deseja realmente excluir esse adotante? (s/n): ").lower()
    if confirm == "s":
        armazenamento.deletar_entrada(cpf, "adotantes.json")
        print("Adotante excluído.")
        return ("deletar", adotante)
    else:
        print("Exclusão cancelada.")
        return ("deletar", None)

if __name__ == "__main__":
    main()