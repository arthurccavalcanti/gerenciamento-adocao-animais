import re
import armazenamento_json as armazenamento

def crud_adotantes(tipo_operacao: str):
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
    elif tipo_operacao == "editar":
        return atualizar_adotante()
    elif tipo_operacao == "deletar":
        return excluir_adotante()
    elif tipo_operacao == "ler":
        return ler_adotante()
    else:
        return "Operação inválida. Tente novamente."


# -----------------------------------------------------------

def validar_contato(contato):
    return str(contato).isdigit() and len(str(contato)) >= 8

def validar_cpf(cpf):
    return re.match(r"^\d{11}$", cpf) is not None

def validar_idade(idade):
    return idade.isdigit() and int(idade) > 0

def validar_cep(cep):
    return re.match(r"^\d{8}$", cep) is not None

def listar_todos_adotantes():
    adotantes = armazenamento.carregar_arquivo("adotantes.json")
    if adotantes == 1:
        print("Erro ao criar arquivo adotantes.json")
    elif adotantes == 2:
        print("Erro ao abrir arquivo adotantes.json")
    else:
        print("="*50)
        print("LISTA DE ADOTANTES:")
        for adotante in adotantes:
            print("-"*50)
            print(f"ID: {adotante['CPF']}")
            print(f"Nome completo: {adotante['nome']}")
            print(f"Idade: {adotante['idade']}")
            print(f"Profissão: {adotante['profissao']}")
            print(f"Endereço: {adotante['endereco']}")
            print(f"Contato: {adotante['contato']}")
            for preferencia in adotante['preferencias']:
                print(f"Preferência: {preferencia}")
        print("="*50)


# ------------------------------------------------------------

def ler_adotante():
    cpf = input("Digite o CPF do adotante: ")
    while not validar_cpf(cpf):
        cpf = input("CPF inválido. Digite o CPF do adotante: ")
    adotante = armazenamento.ler_entrada(cpf, 'CPF', "adotantes.json")
    if adotante == 2:
        return f"Erro ao ler adotante: adotante com id {cpf} não encontrado."
    elif adotante == 1:
        return f"Erro ao ler adotante: o arquivo adotantes.json não existe."
    return ('ler', adotante)

# --------------------------------

def cadastrar_adotante():
    while True:
        cpf = input("Digite o CPF do adotante: ")
        while not validar_cpf(cpf):
            cpf = input("CPF inválido. Digite o CPF do adotante: ")

        nome = input("Digite o nome completo: \n")

        idade = input("Digite a idade: \n")
        while not validar_idade(idade):
            print("Idade inválida!\n")
            continue
        idade = int(idade)

        profissao = input("Digite a profissão: \n")
        
        endereco = input("Digite o CEP (somente números): \n")
        while not validar_cep(endereco):
            print("CEP inválido! Deve conter 8 dígitos.\n")
            endereco = input("Digite o CEP (somente números): \n")
            continue

        contato = input("Digite o contato (somente números): ")
        while not validar_contato(contato):
            print("Contato inválido! Deve conter ao menos 8 dígitos.\n")
            contato = input("Digite o contato (somente números): ")
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
            "CPF": cpf,
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
            return ("criar", adotante)
        else:
            return "Cadastro cancelado."
        
# --------------------------------

def atualizar_adotante():
    cpf = input("Digite o CPF do adotante: ")
    while not validar_cpf(cpf):
        cpf = input("CPF inválido. Digite o CPF do adotante: ")

    dados_atuais = armazenamento.ler_entrada(cpf, "CPF", "adotantes.json")
    if dados_atuais == 1 or dados_atuais == 2:
        return f"Erro ao atualizar: problema ao ler adotante com id {cpf}."
    
    dados_antigos = dados_atuais

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
    
    confirm = input("Deseja prosseguir com a atualização? (s/n): ").lower()
    if confirm == "s":
        armazenamento.editar_entrada(cpf, novos_dados, "adotantes.json")
        return ("atualizar", (dados_antigos, dados_atuais))
    else:
        return f"Atualização do adotante com id {cpf} cancelada."

# --------------------------------

def excluir_adotante():
    cpf = input("Digite o CPF do adotante: ")
    while not validar_cpf(cpf):
        cpf = input("CPF inválido. Digite o CPF do adotante: ")

    adotante = armazenamento.ler_entrada(cpf, "CPF", "adotantes.json")
    if adotante == 1 or adotante == 2:
        return f"Erro ao excluir: problema ao ler adotante com id {cpf}."

    print("Adotante encontrado:")
    for k, v in adotante.items():
        print(f"{k}: {v}")
    confirm = input("Deseja realmente excluir esse adotante? (s/n): ").lower()
    if confirm == "s":
        armazenamento.deletar_entrada(cpf, "adotantes.json")
        return ("deletar", adotante)
    else:
        return f"Exclusão do adotante com id {cpf} cancelada."
