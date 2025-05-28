import re
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import cli_interface
import armazenamento_json

def crud_adotantes(tipo_operacao: str):
    while True:
        print("Deseja visualizar os dados antes da operação?")
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

    if tipo_operacao == "criar adotante":
        return cadastrar_adotante()
    elif tipo_operacao == "editar adotante":
        return atualizar_adotante()
    elif tipo_operacao == "deletar adotante":
        return excluir_adotante()
    elif tipo_operacao == "ler adotantes":

        return ler_adotante()
    else:
        return ("erro", "Operação inválida. Tente novamente.")

# -----------------------------------------------------------

def validar_contato(contato):
    return str(contato).isdigit() and len(str(contato)) >= 8

def validar_cpf(cpf):
    return re.match(r"^\d{11}$", cpf) is not None

def validar_idade(idade):
    return idade.isdigit() and int(idade) > 0

def validar_cep(cep):
    return re.match(r"^\d{8}$", cep) is not None

# ------------------------------------------------------------

def listar_todos_adotantes():
    adotantes = armazenamento_json.carregar_arquivo("adotantes.json")
    if adotantes is None:
        print("Erro ao carregar arquivo adotantes.json.")
        return
    if not adotantes:
        print("Não há adotantes cadastrados no momento.")
        return

    print("\n===== LISTA DE ADOTANTES CADASTRADOS =====\n")
    for adotante in adotantes:
        print("-" * 50)
        print(f"CPF: {adotante['CPF']}")
        print(f"Nome completo: {adotante['nome']}")
        print(f"Idade: {adotante['idade']}")
        print(f"Profissão: {adotante['profissao']}")
        print(f"Endereço (CEP): {adotante['endereco']}")
        print(f"Contato: {adotante['contato']}")
        print("Preferências:")
        pref = adotante['preferencias']
        temperamentos = ', '.join(pref['temperamento']) if pref.get('temperamento') else 'Nenhuma'
        print(f" - Tipo: {pref.get('tipo', 'N/A').capitalize()}")
        print(f" - Porte: {pref.get('porte', 'N/A').capitalize()}")
        print(f" - Temperamento: {temperamentos}")
        print(f" - Sexo: {pref.get('sexo', 'N/A').capitalize()}")
        print(f" - Faixa Etária: {pref.get('faixa_etaria', 'N/A').capitalize()}")
        print(f" - Experiência: {pref.get('experiencia', 'N/A')}")
    print("-" * 50)


def ler_adotante():
    while True:
        cpf = input("\nDigite o CPF do adotante (11 números) ou '0' para cancelar: ").strip()
        if cpf == '0':
            print("Operação cancelada. Voltando ao menu principal.")
            return None
        if validar_cpf(cpf):
            break
        print("CPF inválido! Deve conter exatamente 11 números.")

    cpf_int = int(cpf)
    adotante = armazenamento_json.ler_entrada(cpf_int, 'CPF', 'adotantes.json')
    if adotante is None:
        print(f"Adotante com CPF {cpf} não encontrado.")
        return None

    print("\n--- DADOS DO ADOTANTE ---")
    print(f"CPF: {adotante['CPF']}")
    print(f"Nome: {adotante['nome']}")
    print(f"Idade: {adotante['idade']}")
    print(f"Profissão: {adotante['profissao']}")
    print(f"Endereço (CEP): {adotante['endereco']}")
    print(f"Contato: {adotante['contato']}")
    print("Preferências:")
    pref = adotante['preferencias']
    temperamentos = ', '.join(pref['temperamento']) if pref.get('temperamento') else 'Nenhuma'
    print(f" - Tipo: {pref.get('tipo', 'N/A').capitalize()}")
    print(f" - Porte: {pref.get('porte', 'N/A').capitalize()}")
    print(f" - Temperamento: {temperamentos}")
    print(f" - Sexo: {pref.get('sexo', 'N/A').capitalize()}")
    print(f" - Faixa Etária: {pref.get('faixa_etaria', 'N/A').capitalize()}")
    print(f" - Experiência: {pref.get('experiencia', 'N/A')}")

    print("\nAdotante carregado com sucesso!")
    return ('ler', adotante)


# --------------------------------

def cadastrar_adotante():
    print("\n--- CADASTRO DE ADOTANTE ---")
    while True:
        cpf = input("Digite o CPF do adotante (ou '0' para cancelar): ").strip()
        if cpf == '0':
            return ("erro", "Cadastro cancelado.")
        if not cpf.isdigit() or len(cpf) != 11:
            print("CPF inválido! Deve conter exatamente 11 números.")
            continue
        cpf = int(cpf)
        break

    nome = input("Digite o nome completo: ").strip()
    if nome == '':
        return ("erro", "Cadastro cancelado: nome não pode ser vazio.")

    while True:
        idade = input("Digite a idade: ").strip()
        if idade == '0':
            return ("erro", "Cadastro cancelado.")
        if idade.isdigit() and int(idade) > 0:
            idade = int(idade)
            break
        print("Idade inválida! Deve ser um número inteiro positivo.")

    profissao = input("Digite a profissão: ").strip()
    if profissao == '':
        return ("erro", "Cadastro cancelado: profissão não pode ser vazia.")

    while True:
        endereco = input("Digite o CEP (8 números): ").strip()
        if endereco == '0':
            return ("erro", "Cadastro cancelado.")
        if endereco.isdigit() and len(endereco) == 8:
            break
        print("CEP inválido! Deve conter exatamente 8 números.")

    while True:
        contato = input("Digite o contato (mínimo 8 números): ").strip()
        if contato == '0':
            return ("erro", "Cadastro cancelado.")
        if contato.isdigit() and len(contato) >= 8:
            contato = int(contato)
            break
        print("Contato inválido! Deve conter pelo menos 8 números.")

    print("\n--- Preferências do adotante ---")

    while True:
        tipo = input("Prefere qual tipo de animal? (canino/felino): ").strip().lower()
        if tipo == '0':
            return ("erro", "Cadastro cancelado.")
        if tipo in ["canino", "felino"]:
            break
        print("Entrada inválida. Digite 'canino' ou 'felino'.")

    while True:
        porte = input("Porte preferido? (pequeno/medio/grande): ").strip().lower()
        if porte == '0':
            return ("erro", "Cadastro cancelado.")
        if porte in ["pequeno", "medio", "grande"]:
            break
        print("Entrada inválida. Digite 'pequeno', 'médio' ou 'grande'.")

    temp = input("Personalidades preferidas (separe por vírgula): ").lower()
    temperamento = [t.strip() for t in temp.split(",") if t.strip()]

    while True:
        sexo = input("Sexo preferido? (macho/femea): ").strip().lower()
        if sexo == '0':
            return ("erro", "Cadastro cancelado.")
        if sexo in ["macho", "femea","m","f"]:
            break
        print("Entrada inválida. Digite 'macho' ou 'fêmea'.")

    while True:
        faixa_etaria = input("Faixa etária preferida? (filhote/adulto/idoso): ").strip().lower()
        if faixa_etaria == '0':
            return ("erro", "Cadastro cancelado.")
        if faixa_etaria in ["filhote", "adulto", "idoso"]:
            break
        print("Entrada inválida. Digite 'filhote', 'adulto' ou 'idoso'.")

    while True:
        experiencia = input("Tem experiência com animais? (s/n): ").strip().lower()
        if experiencia == '0':
            return ("erro", "Cadastro cancelado.")
        if experiencia in ['s', 'n']:
            experiencia = 'Sim' if experiencia == 's' else 'Não'
            break
        print("Opção inválida. Digite 's' ou 'n'.")

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

    while True:
        confirm = input("Deseja salvar esse adotante? (s/n): ").strip().lower()
        if confirm == "s":
            if armazenamento_json.criar_entrada(adotante, "adotantes.json"):
                return ("criar", adotante)
            else:
                return ("erro", "Erro ao criar entrada.")
        elif confirm == "n":
            return ("erro", "Cadastro cancelado.")
        else:
            print("Opção inválida. Digite 's' ou 'n'.")

# --------------------------------

def atualizar_adotante():
    print("\n--- ATUALIZAÇÃO DE ADOTANTE ---")
    while True:
        cpf = input("Digite o CPF do adotante a ser atualizado (ou '0' para cancelar): ").strip()
        if cpf == '0':
            return ("erro", "Atualização cancelada.")
        if cpf.isdigit() and len(cpf) == 11:
            cpf_int = int(cpf)
            break
        print("CPF inválido! Deve conter exatamente 11 números.")

    dados_atuais = armazenamento_json.ler_entrada(cpf_int, "CPF", "adotantes.json")
    if dados_atuais is None:
        return ("erro", f"Erro: adotante com CPF {cpf} não encontrado.")

    print("\nDados atuais:")
    for k, v in dados_atuais.items():
        print(f"{k}: {v}")

    nome = input("Novo nome (pressione Enter para manter o atual): ").strip()
    if nome == '':
        nome = dados_atuais['nome']

    while True:
        idade = input("Nova idade (pressione Enter para manter a atual): ").strip()
        if idade == '':
            idade = dados_atuais['idade']
            break
        elif idade.isdigit() and int(idade) > 0:
            idade = int(idade)
            break
        else:
            print("Idade inválida! Deve ser um número inteiro positivo ou vazio para manter o atual.")

    profissao = input("Nova profissão (pressione Enter para manter a atual): ").strip()
    if profissao == '':
        profissao = dados_atuais['profissao']

    while True:
        endereco = input("Novo CEP (8 números) (pressione Enter para manter o atual): ").strip()
        if endereco == '':
            endereco = dados_atuais['endereco']
            break
        elif endereco.isdigit() and len(endereco) == 8:
            break
        else:
            print("CEP inválido! Deve conter exatamente 8 números ou vazio para manter o atual.")

    while True:
        contato = input("Novo contato (mínimo 8 números) (pressione Enter para manter o atual): ").strip()
        if contato == '':
            contato = dados_atuais['contato']
            break
        elif contato.isdigit() and len(contato) >= 8:
            contato = int(contato)
            break
        else:
            print("Contato inválido! Deve conter pelo menos 8 números ou vazio para manter o atual.")

    print("\n--- Atualização das preferências ---")
    prefs = dados_atuais['preferencias']

    tipo = input(f"Tipo (canino/felino) [{prefs['tipo']}]: ").strip().lower()
    if tipo == '':
        tipo = prefs['tipo']
    elif tipo not in ["canino", "felino"]:
        print("Tipo inválido, mantendo o valor anterior.")
        tipo = prefs['tipo']

    porte = input(f"Porte (pequeno/medio/grande) [{prefs['porte']}]: ").strip().lower()
    if porte == '':
        porte = prefs['porte']
    elif porte not in ["pequeno", "medio", "grande"]:
        print("Porte inválido, mantendo o valor anterior.")
        porte = prefs['porte']

    temp = input(f"Temperamento(s) (separe por vírgula) [{', '.join(prefs['temperamento'])}]: ").strip().lower()
    if temp == '':
        temperamento = prefs['temperamento']
    else:
        temperamento = [t.strip() for t in temp.split(",") if t.strip()]

    sexo = input(f"Sexo (macho/femea) [{prefs['sexo']}]: ").strip().lower()
    if sexo == '':
        sexo = prefs['sexo']
    elif sexo not in ["macho", "femea"]:
        print("Sexo inválido, mantendo o valor anterior.")
        sexo = prefs['sexo']

    faixa_etaria = input(f"Faixa etária (filhote/adulto/idoso) [{prefs['faixa_etaria']}]: ").strip().lower()
    if faixa_etaria == '':
        faixa_etaria = prefs['faixa_etaria']
    elif faixa_etaria not in ["filhote", "adulto", "idoso"]:
        print("Faixa etária inválida, mantendo o valor anterior.")
        faixa_etaria = prefs['faixa_etaria']

    experiencia = input(f"Experiência com animais (Sim/Não) [{prefs['experiencia']}]: ").strip().lower()
    if experiencia == '':
        experiencia = prefs['experiencia']
    elif experiencia not in ['sim', 'não', 'nao']:
        print("Experiência inválida, mantendo o valor anterior.")
        experiencia = prefs['experiencia']
    else:
        if experiencia == 'sim':
            experiencia = 'Sim','s'
        else:
            experiencia = 'Não','n'

    novas_preferencias = {
        "tipo": tipo,
        "porte": porte,
        "temperamento": temperamento,
        "sexo": sexo,
        "faixa_etaria": faixa_etaria,
        "experiencia": experiencia
    }

    novos_dados = {
        "CPF": cpf_int,
        "nome": nome,
        "idade": idade,
        "profissao": profissao,
        "endereco": endereco,
        "contato": contato,
        "preferencias": novas_preferencias
    }

    print("\nNovos dados:")
    for k, v in novos_dados.items():
        print(f"{k}: {v}")

    while True:
        confirm = input("Deseja prosseguir com a atualização? (s/n): ").strip().lower()
        if confirm == "s":
            if armazenamento_json.editar_entrada(cpf_int, 'CPF', novos_dados, "adotantes.json"):
                return ("atualizar", (dados_atuais, novos_dados))
            else:
                return ("erro", "Erro ao atualizar adotante.")
        elif confirm == "n":
            return ("erro", "Atualização cancelada.")
        else:
            print("Opção inválida. Digite 's' ou 'n'.")

# -----------------------------------

def excluir_adotante():
    print("\n--- EXCLUSÃO DE ADOTANTE ---")
    while True:
        cpf = input("Digite o CPF do adotante a ser excluído (ou '0' para cancelar): ").strip()
        if cpf == '0':
            return ("erro", "Exclusão cancelada.")
        if cpf.isdigit() and len(cpf) == 11:
            cpf_int = int(cpf)
            break
        print("CPF inválido! Deve conter exatamente 11 números.")

    adotante = armazenamento_json.ler_entrada(cpf_int, 'CPF', "adotantes.json")
    if adotante is None:
        return ("erro", f"Erro ao excluir: adotante com CPF {cpf} não encontrado.")

    print("\nDados do adotante a ser excluído:")
    for k, v in adotante.items():
        print(f"{k}: {v}")

    confirm = input("Deseja realmente excluir esse adotante? (s/n): ").strip().lower()
    while True:
        if confirm == "s":
            sucesso = armazenamento_json.deletar_entrada(cpf_int, 'CPF', "adotantes.json")
            if sucesso:
                return ("deletar", adotante)
            else:
                return ("erro", "Erro ao excluir adotante.")
        elif confirm == "n":
            return ("erro", f"Exclusão do adotante com CPF {cpf} cancelada.")
        else:
            confirm = input("Opção inválida. Digite 's' ou 'n': ").strip().lower()
