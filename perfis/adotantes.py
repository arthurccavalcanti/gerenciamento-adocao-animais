import re
import armazenamento_json as armazenamento
from perfis.voluntarios import validar_cpf, validar_email, tem_algarismos, validar_data_nascimento
from datetime import datetime

def crud_adotantes(tipo_operacao: str):
    while True:
        print("Deseja visualizar os dados de adotantes antes da operação?")
        print("1 - Sim")
        print("2 - Não")
        deseja_listar = input(">>> ")
        if deseja_listar == "1":
            listar_todos_adotantes()  
            break
        elif deseja_listar == "2":
            break
        else:
            print("Opção inválida.")    
    
    if tipo_operacao == "criar":
        print("--- CRIAÇÃO DE ADOTANTE ---")
        return cadastrar_adotante()
    elif tipo_operacao == "editar":
        print("--- EDIÇÃO DE ADOTANTE ---")
        return atualizar_adotante()
    elif tipo_operacao == "deletar":
        print("--- DELEÇÃO DE ADOTANTE ---")
        return excluir_adotante()
    elif tipo_operacao == "ler":
        print("--- LEITURA DE ADOTANTE ---")
        return ler_adotante()
    else:
        return "Operação inválida. Tente novamente."

# -----------------------------------------------------------

def validar_telefone(telefone):
    return str(telefone).isdigit() and len(str(telefone)) >= 8

def validar_cep(cep):
    return re.match(r"^\d{8}$", cep) is not None

def listar_todos_adotantes():
    adotantes = armazenamento.carregar_arquivo("adotantes.json")
    if adotantes is None:
        print("Erro ao carregar arquivo adotantes.json")
    if not adotantes:
        print("Oops. Parece que não há pets registrados.")
    else:
        print("="*50)
        print("LISTA DE ADOTANTES:")
        for adotante in adotantes:
            print("-"*50)
            print(f"CPF: {adotante['CPF']}")
            print(f"Nome completo: {adotante['nome']}")
            print(f"Idade: {adotante['idade']}")
            print(f"Profissão: {adotante['profissao']}")
            print(f"Endereço: {adotante['endereco']}")
            print(f"Telefone: {adotante['telefone']}")
            print(f"Data de cadastro: {adotante['data_cadastro']}")
            print(f"Data de nascimento: {adotante['nascimento']}")
            print(f"E-mail: {adotante['email']}")
            for preferencia in adotante['preferencias']:
                print(f"Preferência: {preferencia}\n")
        print('=' * 50)


# ------------------------------------------------------------

def cadastrar_adotante():
    while True:
        cpf = input("Digite o CPF do adotante: ")
        while not validar_cpf(cpf):
            cpf = input("CPF inválido. Digite o CPF do adotante: ")
        cpf = int(cpf)

        nome = input("Digite o nome completo: \n")
        while tem_algarismos(nome):
            nome = input("Nome inválido! Não deve conter algarismos.\n Digite o nome completo: \n")

        profissao = input("Digite a profissão: \n")
        while tem_algarismos(profissao):
            profissao = input("Profissão inválida! Não deve conter algarismos.\n Digite a profissão: \n")
        
        nascimento = input("Data de nascimento (DD/MM/AAAA): ").strip()
        while not validar_data_nascimento(nascimento):
            nascimento = input("Data inválida. Tente novamente.\n Data de nascimento (DD/MM/AAAA): ")
        hoje = datetime.today()
        idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))  
        
        endereco = input("Digite o CEP (somente números): \n")
        while not validar_cep(endereco):
            print("CEP inválido! Deve conter 8 dígitos.\n")
            endereco = input("Digite o CEP (somente números): \n")

        telefone = input("Digite o telefone (somente números): ")
        while not telefone(telefone):
            print("Telefone inválido! Deve conter ao menos 8 dígitos.\n")
            telefone = input("Digite o telefone (somente números): ")
        telefone = int(telefone)

        email = input("Digite o e-mail: ").strip()
        while not validar_email(email):
            print("E-mail inválido.")
            email = input("Digite o e-mail: ").strip()

        data_cadastro = datetime.today().strftime("%d/%m/%Y")

        print("\n--- Preferências do adotante ---")

        tipo = input("Prefere qual tipo de animal? (canino/felino): ").lower()
        while tipo not in ["canino", "felino"]:
            tipo = input("Entrada inválida. Digite canino ou felino: ").lower()

        porte = input("Porte preferido? (pequeno/médio/grande): ").lower()
        while porte not in ["pequeno", "médio", "grande"]:
            porte = input("Entrada inválida. Digite pequeno, médio ou grande: ").lower()

        temp = input("Personalidades preferidas (separe por vírgula, ex: brincalhão, calmo, protetor): ").lower()
        temperamento = [t.strip() for t in temp.split(",") if t.strip()]

        sexo = input("Sexo preferido? (macho/fêmea): ").lower()
        while sexo not in ["macho", "fêmea"]:
            sexo = input("Entrada inválida. Digite macho ou fêmea: ").lower()

        faixa_etaria = input("Faixa etária preferida? (filhote/adulto/idoso): ").lower()
        while faixa_etaria not in ["filhote", "adulto", "idoso"]:
            faixa_etaria = input("Entrada inválida. Digite filhote, adulto ou idoso: ").lower()

        experiencia = input("Tem experiência com animais? (s/n): ").lower()
        while True:
            if experiencia == 's':
                experiencia = 'Sim'
                break
            elif experiencia == 'n':
                experiencia = 'Não'
                break
            else:
                print("Opção inválida.")

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
            "Nome": nome,
            "Idade": idade,
            "Profissão": profissao,
            "Endereço": endereco,
            "Telefone": telefone,
            "Email": email,
            "Data de cadastro": data_cadastro,
            "Data de nascimento":nascimento,
            "Preferências": preferencias
        }

        print("\nConfira os dados inseridos:")
        for k, v in adotante.items():
            print(f"{k}: {v}")

        confirm = input("Deseja salvar esse adotante? (s/n): ").lower()
        while True:
            if confirm == "s":
                if armazenamento.criar_entrada(adotante, "adotantes.json"):
                    return ("criar", adotante)
                return "Erro ao criar entrada em adotantes.json."
            elif confirm == "n":
                return "Cadastro cancelado pelo usuário."
            else:
                print("Opção inválida.")
        
# ------------------------------------------------------------

def atualizar_adotante():

    cpf = input("Digite o CPF do adotante a ser atualizado: ")
    while not validar_cpf(cpf):
        cpf = input("CPF inválido. Digite o CPF do adotante: ")
    cpf = int(cpf)

    dados_atuais = armazenamento.ler_entrada(cpf, "CPF", "adotantes.json")
    if dados_atuais is None:
        return f"Erro ao atualizar: problema ao ler adotante com id {cpf}."
    
    dados_antigos = dados_atuais

    print("Dados atuais:")
    for k, v in dados_atuais.items():
        print(f"{k}: {v}")

    nome = input("Novo nome: ")
    while tem_algarismos(nome):
        nome = input("Novo nome inválido! Não deve conter algarismos.\n Novo nome: \n")

    nascimento = input("Nova data de nascimento (DD/MM/AAAA): ").strip()
    while not validar_data_nascimento(nascimento):
        nascimento = input("Data inválida. Tente novamente.\n Data de nascimento (DD/MM/AAAA): ")
    hoje = datetime.today()
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))  

    profissao = input("Digite a nova profissão: \n")
    while tem_algarismos(profissao):
        profissao = input("Nova profissão inválida! Não deve conter algarismos.\n Digite a nova profissão: \n")

    while True:
        endereco = input("Novo CEP (somente números): ")
        if validar_cep(endereco):
            break
        print("CEP inválido! Deve conter 8 dígitos.")

    while True:
        telefone = input("Novo telefone (somente números): ")
        if validar_telefone(telefone):
            telefone = int(telefone)
            break
        print("Telefone inválido! Deve conter ao menos 8 dígitos.")

    while True:
        email = input("Novo email: ")
        if validar_email(email):
            break
        print("Email inválido! Tente novamente.")

    novos_dados = {
        "Nome": nome,
        "Idade": idade,
        "Profissão": profissao,
        "Endereço": endereco,
        "Telefone": telefone,
        "Email": email,
        "Data de nascimento": nascimento
    }

    print("\nConfira as alterações:")
    for chave in novos_dados:
        print(f"{chave}: {dados_atuais[chave]} → {novos_dados[chave]}")
    
    confirm = input("Deseja prosseguir com a atualização? (s/n): ").lower()
    while True:
        if confirm == "s":
            if armazenamento.editar_entrada(int(cpf), 'CPF', novos_dados, "adotantes.json"):
                return ("atualizar", (dados_antigos, dados_atuais))
            return "Erro ao atualizar adotante."
        elif confirm == "n":
            return f"Atualização do adotante com id {cpf} cancelada."
        else:
            print('Opção inválida. Digite \'s\' ou \'n\'')

# ------------------------------------------------------------

def excluir_adotante():
    cpf = input("Digite o CPF do adotante: ")
    while not validar_cpf(cpf):
        cpf = input("CPF inválido. Digite o CPF do adotante: ")

    cpf = int(cpf)
    adotante = armazenamento.ler_entrada(cpf, "CPF", "adotantes.json")
    if adotante is None:
        return f"Erro ao excluir: problema ao ler adotante com id {cpf}."

    print("Adotante encontrado:")
    for k, v in adotante.items():
        print(f"{k}: {v}")
    confirm = input("Deseja realmente excluir esse adotante? (s/n): ").lower()
    while True:
        if confirm == "s":
            armazenamento.deletar_entrada(cpf, 'CPF', "adotantes.json")
            return ("deletar", adotante)
        elif confirm == "n":
            return f"Exclusão do adotante com id {cpf} cancelada."
        else:
            print("Opção inválida.")

# ------------------------------------------------------------

def ler_adotante():
    cpf = input("Digite o CPF do adotante: ")
    while not validar_cpf(cpf):
        cpf = input("CPF inválido. Digite o CPF do adotante: ")
    adotante = armazenamento.ler_entrada(cpf, 'CPF', "adotantes.json")
    if adotante is not None:
        return ('ler', adotante)
    return f"Erro ao ler adotante com CPF {cpf}"