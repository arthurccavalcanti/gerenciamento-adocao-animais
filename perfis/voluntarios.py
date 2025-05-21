from armazenamento import armazenamento_json as armazenamento
import os
from datetime import datetime
import re
import requests

arquivo_voluntario = os.path.join(os.path.dirname(__file__), '..', 'armazenamento', 'voluntarios.json')

def solicitar_cpf():
    while True:
        cpf = input("Digite seu CPF: ").strip()
        if validar_cpf(cpf):
            print("CPF cadastrado!")
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

def criar_voluntario(cpf, nome, nascimento, endereco, disponibilidade, data_cadastro, email, telefone, nome_arquivo_json):
    data_nascimento = datetime.strptime(nascimento, "%d/%m/%Y")
    hoje = datetime.today()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

    novo_voluntario = {
        "CPF": cpf,
        "Nome Completo": nome,
        "Data Nascimento": nascimento,
        "Idade": idade,
        "Endereço": endereco,
        "Disponibilidade": disponibilidade,
        "Data Cadastro": data_cadastro,
        "e-Mail": email,
        "Telefone": telefone
    }

    return armazenamento.criar_entrada(novo_voluntario, nome_arquivo_json)

def buscar_voluntario(cpf, nome_arquivo_json):
    dados = armazenamento.ler_entradas(nome_arquivo_json)
    return next((v for v in dados if v.get("CPF") == cpf), None)

def editar_voluntario(cpf, novos_dados, nome_arquivo_json):
    dados = armazenamento.ler_entradas(nome_arquivo_json)
    for i, voluntario in enumerate(dados):
        if voluntario.get("CPF") == cpf:
            dados[i].update(novos_dados)
            return armazenamento.editar_entrada(dados, nome_arquivo_json)
    return False

def excluir_voluntario(cpf, nome_arquivo_json):
    dados = armazenamento.ler_entradas(nome_arquivo_json)
    novos_dados = [v for v in dados if v.get("CPF") != cpf]
    if len(novos_dados) == len(dados):
        return False
    return armazenamento.salvar_entradas(novos_dados, nome_arquivo_json)

def main():
    nome_arquivo_json = "voluntarios.json"

    while True:
        print("\n--- MENU CRUD VOLUNTÁRIOS ---")
        print("1. Cadastrar voluntário")
        print("2. Buscar voluntário por CPF")
        print("3. Editar voluntário")
        print("4. Excluir voluntário")
        print("5. Listar voluntários")
        print("6. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cpf = solicitar_cpf()
            nome = input("Nome completo: ").strip()
            nascimento = input("Data de nascimento (DD/MM/AAAA): ").strip()
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

            criar_voluntario(cpf, nome, nascimento, endereco, disponibilidade, data_cadastro, email, telefone_formatado, nome_arquivo_json)

        elif opcao == "2":
            cpf = solicitar_cpf()
            voluntario = buscar_voluntario(cpf, nome_arquivo_json)
            if voluntario:
                print("\n--- DADOS DO VOLUNTÁRIO ---")
                for chave, valor in voluntario.items():
                    print(f"{chave}: {valor}")
            else:
                print("Voluntário não encontrado.")

        elif opcao == "3":
            cpf = input("Digite o CPF do voluntário que deseja editar: ").strip()
            voluntario = buscar_voluntario(cpf, nome_arquivo_json)
            if voluntario:
                print(f"\nVoluntário encontrado: {voluntario['Nome Completo']}")
                print("Deixe em branco os campos que você **não** deseja alterar.")

                novo_nome = input("Novo nome completo: ").strip()
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

                if novos_dados:
                    if editar_voluntario(cpf, novos_dados, nome_arquivo_json):
                        print("Voluntário atualizado com sucesso.")
                    else:
                        print("Erro ao atualizar voluntário.")
                else:
                    print("Nenhum dado válido para atualizar.")
            else:
                print("Voluntário não encontrado.")

        elif opcao == "4":
            cpf = solicitar_cpf()
            if excluir_voluntario(cpf, nome_arquivo_json):
                print("Voluntário excluído com sucesso.")
            else:
                print("Voluntário não encontrado.")

        elif opcao == "5":
            voluntarios = armazenamento.ler_entradas(nome_arquivo_json)
            if voluntarios:
                print("\n--- LISTA DE VOLUNTÁRIOS ---")
                for v in voluntarios:
                    print(f"CPF: {v['CPF']}")
                    print(f"Nome: {v['Nome Completo']}")
                    print(f"E-mail: {v['E-mail']}")
                    print(f"Telefone: {v['Telefone']}")
                    print(f"Idade: {v['Idade']}")
                    print(f"Endereço: {v['Endereço']}")
                    print("Disponibilidade:")
                    for d in v['Disponibilidade']:
                        print(f"  - {d['Dia']}: {', '.join(d['Períodos'])}")
                    print("-" * 30)
            else:
                print("Nenhum voluntário cadastrado.")

        elif opcao == "6":
            print("Encerrando programa.")
            break
        else:
            print("Opção inválida.")

'''
A função principal recebe a operação a ser feita (criar, deletar, atualizar, ler) como parâmetro, realiza a operação e retorna o resultado.
A função também deve dar ao usuário a opção de visualizar todas as entradas.
'''
def main(tipo_operacao=None):
    return