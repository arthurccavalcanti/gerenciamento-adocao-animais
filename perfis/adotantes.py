import re
import sys
import os
from datetime import datetime
from perfis.voluntarios import validar_cpf, validar_email, tem_algarismos, validar_data_nascimento

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import armazenamento_json


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



def validar_telefone(telefone):
    return str(telefone).isdigit() and len(str(telefone)) >= 8

def validar_cep(cep):
    return re.match(r"^\d{8}$", cep) is not None

def listar_todos_adotantes():
    adotantes = armazenamento_json.carregar_arquivo("adotantes.json")
    if adotantes is None:
        print("Erro ao carregar arquivo adotantes.json")
    elif not adotantes:
        print("Não há adotantes registrados.")
    else:
        print("=" * 50)
        print("LISTA DE ADOTANTES:")
        for adotante in adotantes:
            print("-" * 50)
            for k, v in adotante.items():
                print(f"{k}: {v}")
        print("=" * 50)

def entrada_usuario(msg):
    entrada = input(msg).strip()
    if entrada.lower() == 'cancelar':
        raise KeyboardInterrupt
    return entrada

def escolher_opcao(opcoes, mensagem):
    print(mensagem)
    for i, opcao in enumerate(opcoes, 1):
        print(f"{i} - {opcao}")
    while True:
        escolha = entrada_usuario("Escolha uma opção: ")
        if escolha.isdigit() and 1 <= int(escolha) <= len(opcoes):
            return opcoes[int(escolha) - 1]
        else:
            print("Opção inválida, tente novamente.")

def escolher_temperamentos():
    print("Escolha as personalidades preferidas (separe por vírgula):")
    for i, temp in enumerate(PREFERENCIAS_TEMPERAMENTO, 1):
        print(f"{i} - {temp}")
    while True:
        escolhas = entrada_usuario("Digite os números correspondentes: ")
        if all(e.strip().isdigit() and 1 <= int(e.strip()) <= len(PREFERENCIAS_TEMPERAMENTO) for e in escolhas.split(",")):
            return [PREFERENCIAS_TEMPERAMENTO[int(e.strip()) - 1] for e in escolhas.split(",")]
        else:
            print("Entrada inválida! Tente novamente.")


PREFERENCIAS_TEMPERAMENTO = ['Brincalhão', 'Calmo', 'Protetor', 'Sociável', 'Independente']
def coletar_preferencias():
    tipo = escolher_opcao(['Canino', 'Felino'], "Prefere qual tipo de animal?")
    porte = escolher_opcao(['Pequeno', 'Médio', 'Grande'], "Porte preferido?")
    temperamento = escolher_temperamentos()
    sexo = escolher_opcao(['Macho', 'Fêmea'], "Sexo preferido?")
    faixa_etaria = escolher_opcao(['Filhote', 'Adulto', 'Idoso'], "Faixa etária preferida?")
    experiencia = escolher_opcao(['Sim', 'Não'], "Tem experiência com animais?")
    return {
        "Tipo": tipo.lower(),
        "Porte": porte.lower(),
        "Temperamento": temperamento,
        "Sexo": sexo.lower(),
        "Faixa etária": faixa_etaria.lower(),
        "Experiência": experiencia
    }

def cadastrar_adotante():
    try:
        while True:
            cpf = entrada_usuario("Digite o CPF do adotante (apenas números,(ou digite 'cancelar' para voltar)): ")
            if not cpf.isdigit() or len(cpf) < 11 or not validar_cpf(cpf):
                print("CPF inválido! Deve conter pelo menos 11 dígitos e ser válido.")
                continue
            cpf = int(cpf)
            break

        nome = entrada_usuario("Digite o nome completo (ou digite 'cancelar' para voltar): ")
        while tem_algarismos(nome):
            nome = entrada_usuario("Nome inválido! Não deve conter algarismos. Digite novamente: ")

        profissao = entrada_usuario("Digite a profissão (ou digite 'cancelar' para voltar): ")
        while tem_algarismos(profissao):
            profissao = entrada_usuario("Profissão inválida! Não deve conter algarismos. Digite novamente: ")

        nascimento = entrada_usuario("Digite a data de nascimento (DD/MM/AAAA) (ou digite 'cancelar' para voltar): ")
        while not validar_data_nascimento(nascimento):
            nascimento = entrada_usuario("Data inválida. Tente novamente (ou digite 'cancelar' para voltar): ")

        data_nascimento = datetime.strptime(nascimento, "%d/%m/%Y")
        hoje = datetime.today()
        idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

        endereco = entrada_usuario("Digite o CEP (somente números, 8 dígitos) (ou digite 'cancelar' para voltar): ")
        while not validar_cep(endereco):
            endereco = entrada_usuario("CEP inválido! Digite novamente: ")

        telefone = entrada_usuario("Digite o telefone (somente números, mínimo 8 dígitos) (ou digite 'cancelar' para voltar): ")
        while not validar_telefone(telefone):
            telefone = entrada_usuario("Telefone inválido! Digite novamente: ")

        email = entrada_usuario("Digite o e-mail: ")
        while not validar_email(email):
            email = entrada_usuario("E-mail inválido. Digite novamente: ")

        data_cadastro = datetime.today().strftime("%d/%m/%Y")

        preferencias = coletar_preferencias()

        adotante = {
            "CPF": cpf,
            "Nome": nome,
            "Idade": idade,
            "Profissão": profissao,
            "Endereço": endereco,
            "Telefone": int(telefone),
            "Email": email,
            "Data de cadastro": data_cadastro,
            "Data de nascimento": data_nascimento.strftime("%d/%m/%Y"),
            "Preferências": preferencias
        }

        print("\nConfira os dados inseridos:")
        for k, v in adotante.items():
            print(f"{k}: {v}")

        confirm = entrada_usuario("Deseja salvar esse adotante? (s/n): ").lower()
        if confirm == "s":
            if armazenamento_json.criar_entrada(adotante, "adotantes.json"):
                return ("criar", adotante)
            else:
                return "Erro ao criar entrada em adotantes.json."
        else:
            return "Cadastro cancelado pelo usuário."
    except KeyboardInterrupt:
        return "Operação cancelada pelo usuário."

def atualizar_adotante():
    try:
        cpf = entrada_usuario("Digite o CPF do adotante a ser atualizado (ou digite 'cancelar' para voltar): ")
        if not cpf.isdigit() or len(cpf) < 11 or not validar_cpf(cpf):
            return "CPF inválido ou não encontrado."

        cpf = int(cpf)
        dados_atuais = armazenamento_json.ler_entrada(cpf, "CPF", "adotantes.json")
        if dados_atuais is None:
            return f"Adotante com CPF {cpf} não encontrado."

        print("Dados atuais:")
        for k, v in dados_atuais.items():
            print(f"{k}: {v}")

        nome = entrada_usuario("Novo nome (ou digite 'cancelar' para voltar): ")
        while tem_algarismos(nome):
            nome = entrada_usuario("Nome inválido! Não deve conter algarismos. Digite novamente: ")

        nascimento = entrada_usuario("Nova data de nascimento (DD/MM/AAAA) (ou digite 'cancelar' para voltar): ")
        while not validar_data_nascimento(nascimento):
            nascimento = entrada_usuario("Data inválida. Tente novamente: ")

        data_nascimento = datetime.strptime(nascimento, "%d/%m/%Y")
        hoje = datetime.today()
        idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

        profissao = entrada_usuario("Nova profissão (ou digite 'cancelar' para voltar): ")
        while tem_algarismos(profissao):
            profissao = entrada_usuario("Profissão inválida! Digite novamente: ")

        endereco = entrada_usuario("Novo CEP (somente números) (ou digite 'cancelar' para voltar): ")
        while not validar_cep(endereco):
            endereco = entrada_usuario("CEP inválido! Digite novamente: ")

        telefone = entrada_usuario("Novo telefone (somente números) (ou digite 'cancelar' para voltar): ")
        while not validar_telefone(telefone):
            telefone = entrada_usuario("Telefone inválido! Digite novamente: ")

        email = entrada_usuario("Novo email (ou digite 'cancelar' para voltar): ")
        while not validar_email(email):
            email = entrada_usuario("Email inválido! Digite novamente: ")

        novos_dados = {
            "Nome": nome,
            "Idade": idade,
            "Profissão": profissao,
            "Endereço": endereco,
            "Telefone": int(telefone),
            "Email": email,
            "Data de nascimento": data_nascimento.strftime("%d/%m/%Y")
        }

        alterar_pref = entrada_usuario("Deseja atualizar as preferências? (s/n): ").lower()
        if alterar_pref == "s":
            preferencias = coletar_preferencias()
            novos_dados["Preferências"] = preferencias

        confirm = entrada_usuario("Deseja atualizar os dados? (s/n): ").lower()
        if confirm == "s":
            if armazenamento_json.editar_entrada(cpf, "CPF", novos_dados, "adotantes.json"):
                return ("editar", (dados_atuais, novos_dados))
            else:
                return "Erro ao atualizar adotante."
        else:
            return "Atualização cancelada."
    except KeyboardInterrupt:
        return "Operação cancelada pelo usuário."

def excluir_adotante():
    try:
        cpf = entrada_usuario("Digite o CPF do adotante a ser excluído (ou digite 'cancelar' para voltar): ")
        if not cpf.isdigit() or len(cpf) < 11 or not validar_cpf(cpf):
            return "CPF inválido."

        cpf = int(cpf)
        adotante = armazenamento_json.ler_entrada(cpf, "CPF", "adotantes.json")
        if adotante is None:
            return f"Adotante com CPF {cpf} não encontrado."

        confirm = entrada_usuario("Deseja realmente excluir esse adotante? (s/n): ").lower()
        if confirm == "s":
            if armazenamento_json.deletar_entrada(cpf, "CPF", "adotantes.json"):
                return ("deletar", adotante)
            else:
                return "Erro ao excluir adotante."
        else:
            return "Exclusão cancelada."
    except KeyboardInterrupt:
        return "Operação cancelada pelo usuário."

def ler_adotante():
    try:
        cpf = entrada_usuario("Digite o CPF do adotante (ou digite 'cancelar' para voltar): ")
        if not cpf.isdigit() or len(cpf) < 11 or not validar_cpf(cpf):
            return "CPF inválido."

        cpf = int(cpf)
        adotante = armazenamento_json.ler_entrada(cpf, "CPF", "adotantes.json")
        if adotante is not None:
            return ("ler", adotante)
        else:
            return f"Adotante com CPF {cpf} não encontrado."
    except KeyboardInterrupt:
        return "Operação cancelada pelo usuário."
