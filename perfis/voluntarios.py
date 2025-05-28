import armazenamento_json as armazenamento
from datetime import datetime
import re
import requests


def crud_voluntarios(tipo_operacao: str):

    nome_arquivo_json = "voluntarios.json"

    while True:
        print("Deseja visualizar os dados de voluntário antes da operação?")
        print("1 - Sim")
        print("2 - Não")
        deseja_listar = input(">>> ")
        if deseja_listar == '1':
            listar_voluntarios(nome_arquivo_json)
            break
        elif deseja_listar == '2':
            break
        else:
            print("Opção inválida.")    

    if tipo_operacao == "criar":
        print("--- CRIAÇÃO DE VOLUNTÁRIO ---")
        cpf = solicitar_cpf()
        cpf = int(cpf)

        nome = input("Nome completo: ").strip()
        while tem_algarismos(nome):
            nome = input("Nome inválido! Não deve conter algarismos.\n Digite o nome completo: \n")

        nascimento = input("Data de nascimento (DD/MM/AAAA): ").strip()
        while not validar_data_nascimento(nascimento):
            nascimento = input("Data inválida. Tente novamente.\n Data de nascimento (DD/MM/AAAA): ")

        endereco = solicitar_endereco()
        disponibilidade = verificar_disponibilidade()
        data_cadastro = datetime.today().strftime("%d/%m/%Y")

        email = input("Digite o e-mail: ").strip()
        while not validar_email(email):
            print("E-mail inválido.")
            email = input("Digite o e-mail: ").strip()

        telefone = input("Digite o número de celular (com DDD): ").strip()
        valido, telefone_formatado = validar_e_formatar_telefone(telefone)
        while not valido:
            print("Telefone inválido.")
            telefone = input("Digite o número de celular (com DDD): ").strip()
            valido, telefone_formatado = validar_e_formatar_telefone(telefone)

        return criar_voluntario(cpf, nome, nascimento, endereco, disponibilidade, data_cadastro, email, telefone_formatado, nome_arquivo_json)


    elif tipo_operacao == "editar":
        print("--- EDIÇÃO DE VOLUNTÁRIO ---")

        cpf = input("Digite o CPF do voluntário que deseja editar: ").strip()
        voluntario = armazenamento.ler_entrada(int(cpf), 'CPF', nome_arquivo_json)
        if voluntario is None:
            return f"Erro ao ler voluntário com id {cpf}."
        
        print("Deixe em branco os campos que você **não** deseja alterar.")
        novo_nome = input("Novo nome completo: ").strip()
        novo_nascimento = input("Nova data de nascimento: ").strip() # não está validado
        # novo_endereco = input("Novo endereço: ").strip()
        novo_email = input("Novo e-mail: ").strip()
        novo_telefone = input("Novo telefone: ").strip()
        alterar_disponibilidade = input("Deseja alterar a disponibilidade? (s/n): ").strip().lower()

        novos_dados = {}
        if novo_nome:
            novos_dados["Nome Completo"] = novo_nome
        if novo_email and validar_email(novo_email):
            novos_dados["E-mail"] = novo_email
        if novo_telefone:
            valido, telefone_formatado = validar_e_formatar_telefone(novo_telefone)
            if valido:
                novos_dados["Telefone"] = telefone_formatado
        if alterar_disponibilidade == 's':
            novos_dados["Disponibilidade"] = verificar_disponibilidade()
        if novo_nascimento and validar_data_nascimento(novo_nascimento):
            novos_dados['Data de Nascimento'] = novo_nascimento

        if novos_dados:
            if not armazenamento.editar_entrada(int(cpf), 'CPF', novos_dados, nome_arquivo_json):
                return f"Erro ao editar voluntário com CPF {cpf} no arquivo {nome_arquivo_json}."
            return ('editar', (voluntario, novos_dados))
        return "Usuário não editou nenhum dado"


    elif tipo_operacao == "deletar":
        print("--- DELEÇÃO DE VOLUNTÁRIO ---")
        cpf = solicitar_cpf()
        voluntario = armazenamento.ler_entrada(int(cpf), 'CPF', nome_arquivo_json)
        if voluntario is None:
            return f"Erro ao ler voluntário com CPF {cpf} para deleção."
        if armazenamento.deletar_entrada(int(cpf), 'CPF', nome_arquivo_json):
            return ('deletar', voluntario)
        
        return f"Erro ao deletar voluntário com CPF {cpf} no arquivo {nome_arquivo_json}."


    elif tipo_operacao == "ler":
        print("--- LEITURA DE VOLUNTÁRIO ---")
        cpf = solicitar_cpf()
        voluntario = armazenamento.ler_entrada(int(cpf), 'CPF', nome_arquivo_json)
        if voluntario is None:
            return f"Erro ao ler voluntário com CPF {cpf} no arquivo {nome_arquivo_json}."
        return ('ler', voluntario)


# -----------------------------------------------------


def solicitar_cpf():
    while True:
        cpf = input("Digite o CPF: ").strip()
        if validar_cpf(cpf):
            return re.sub(r'[^0-9]', '', cpf)
        else:
            print("CPF inválido, tente novamente.")

def validar_cpf(cpf: str) -> bool:
    cpf = re.sub(r'[^0-9]', '', cpf)

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma1 * 10 % 11) % 10

    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma2 * 10 % 11) % 10

    return cpf[-2:] == f"{digito1}{digito2}"


def verificar_disponibilidade():
    dias_semana = {
        "1": "Domingo",
        "2": "Segunda",
        "3": "Terça",
        "4": "Quarta",
        "5": "Quinta",
        "6": "Sexta",
        "7": "Sábado"
    }
    periodos_validos = ["Manhã", "Tarde", "Noite"]
    disponibilidade = []

    while True:
        print("Escolha um dia da semana:")
        for numero, nome_dia in dias_semana.items():
            print(f"{numero}. {nome_dia}")

        dia_escolhido = input("Digite o número correspondente ao dia (1 a 7): ").strip()
        if dia_escolhido not in dias_semana:
            print("Opção inválida, digite um número de 1 a 7")
            continue

        dia_nome = dias_semana[dia_escolhido]
        periodos_escolhidos = []

        while True:
            print("Escolha o período para esse dia:")
            for i, periodo in enumerate(periodos_validos, 1):
                print(f"{i}. {periodo}")

            try:
                escolha_periodo = int(input("Digite o número do período (1 a 3): ").strip())
                if escolha_periodo not in [1, 2, 3]:
                    print("Período inválido.")
                    continue
            except ValueError:
                print("Entrada inválida.")
                continue

            periodo = periodos_validos[escolha_periodo - 1]
            if periodo not in periodos_escolhidos:
                periodos_escolhidos.append(periodo)
                print(f"Período {periodo} adicionado!")
            else:
                print("Esse período já foi selecionado.")

            if input("Deseja adicionar outro período para esse dia? (s/n) ").strip().lower() != 's':
                break

        disponibilidade.append({"Dia": dia_nome, "Períodos": periodos_escolhidos})

        if input("Deseja adicionar disponibilidade para outro dia? (s/n) ").strip().lower() != 's':
            break

    return disponibilidade


def solicitar_endereco():
    while True:
        cep = input("Digite seu CEP (somente números): ").strip()
        endereco = buscar_endereco_por_cep(cep)
        if endereco:
            print("Endereço encontrado:")
            for chave, valor in endereco.items():
                print(f"{chave}: {valor}")
            if input("Essas informações estão corretas? (s/n): ").strip().lower() == 's':
                return endereco
        else:
            print("Tente novamente com um CEP válido.")


def buscar_endereco_por_cep(cep):
    cep = re.sub(r'[^0-9]', '', cep)
    if len(cep) != 8:
        print("CEP inválido.")
        return None

    try:
        resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        dados = resposta.json()
        if 'erro' in dados:
            print("CEP não encontrado.")
            return None

        return {
            "logradouro": dados.get("logradouro", ""),
            "bairro": dados.get("bairro", ""),
            "cidade": dados.get("localidade", ""),
            "uf": dados.get("uf", "")
        }
    except requests.RequestException:
        print("Erro de conexão.")
        return None


def validar_email(email):
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$', email))


def validar_e_formatar_telefone(telefone):
    numeros = re.sub(r'\D', '', telefone)
    if re.fullmatch(r'\d{11}', numeros) and numeros[2] == '9':
        return True, f"({numeros[:2]}) {numeros[2:7]}-{numeros[7:]}"    
    elif re.fullmatch(r'\d{10}', numeros) and numeros[2] != '9':
        return True, f"({numeros[:2]}) {numeros[2:6]}-{numeros[6:]}"    
    return False, None

def tem_algarismos(string_usuario):
    return any(char.isdigit() for char in string_usuario)

def validar_data_nascimento(nascimento):
    try:
        data_nascimento = datetime.strptime(nascimento, "%d/%m/%Y")
        hoje = datetime.today()
        if data_nascimento > hoje:
            print("A data de nascimento não pode estar no futuro.")
            return False
        if data_nascimento.year < 1900:
            print("Ano de nascimento muito antigo.")
            return False
        return True
    except ValueError:
        print("Formato inválido. Use DD/MM/AAAA.")
        return False
    
# ------------------------------------------------------------------------------


def criar_voluntario(cpf, nome, nascimento, endereco, disponibilidade, data_cadastro, email, telefone, nome_arquivo_json):
    data_nascimento = datetime.strptime(nascimento, "%d/%m/%Y")
    hoje = datetime.today()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))  

    novo_voluntario = {
        "CPF": cpf,
        "Nome Completo": nome,
        "Data de Nascimento": nascimento,
        "Idade": idade,
        "Endereço": endereco,
        "Disponibilidade": disponibilidade,
        "Data Cadastro": data_cadastro,
        "E-mail": email,
        "Telefone": telefone
    }
    if armazenamento.criar_entrada(novo_voluntario, nome_arquivo_json):
        return ('criar', novo_voluntario)
    return f"Erro ao criar voluntário: não foi possível criar o arquivo {nome_arquivo_json}."


def listar_voluntarios(nome_arquivo):

    voluntarios = armazenamento.carregar_arquivo(nome_arquivo)

    if voluntarios is None:
        print(f"Erro ao listar voluntários: não foi possível criar o arquivo {nome_arquivo}")
        return
    elif not voluntarios:
        print("Oops. Parece que não há voluntários registrados.")
    
    print("\n--- LISTA DE VOLUNTÁRIOS ---")
    for v in voluntarios:
        print(f"CPF: {v['CPF']}")
        print(f"Nome: {v['Nome Completo']}")
        print(f"E-mail: {v['E-mail']}")
        print(f"Telefone: {v['Telefone']}")
        print(f"Idade: {v['Idade']}")
        print(f"Endereço: {v['Endereço']}")
        print(f"Data de nascimento: {v['Data de Nascimento']}")
        print(f"Data de cadastro: {v['Data Cadastro']}")
        print("Disponibilidade:")
        for d in v['Disponibilidade']:
            print(f"  - {d['Dia']}: {', '.join(d['Períodos'])}")
        print('\n')
        print("-" * 30)