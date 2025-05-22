import re
from armazenamento import armazenamento_json as armazenamento


# A FAZER:
'''
A função do perfil recebe a operação a ser feita (criar, deletar, atualizar, ler) como parâmetro, realiza a operação e retorna o resultado.
A função do perfil também deve dar ao usuário a opção de visualizar todas as entradas.
'''







            
def validar_contato(contato):
    return str(contato).isdigit() and len(str(contato)) >= 8

def validar_cpf(cpf):
    return re.match(r"^\d{11}$", cpf) is not None

def validar_idade(idade):
    return idade.isdigit() and int(idade) > 0

def validar_cep(cep):
    return re.match(r"^\d{8}$", cep) is not None

def listar_adotantes_por_cpf():
    cpf = input("Digite o CPF do adotante: \n")
    adotante = armazenamento.ler_entrada(cpf, 'CPF', "adotantes.json")
    if isinstance(adotante, dict):
        print(adotante)
    else:
        print("Adotante não encontrado.")

def confirmar_acao(msg="Deseja confirmar? (s/n): "):
    while True:
        resp = input(msg).strip().lower()
        if resp in ['s', 'n']:
            return resp == 's'
        print("Responda apenas com 's' ou 'n'")

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

        if confirmar_acao("Deseja salvar esse adotante? (s/n): "):
            armazenamento.criar_entrada(adotante, "adotantes.json")
            print("Adotante cadastrado com sucesso!")
        else:
            print("Cadastro cancelado.")
        break
            armazenamento.criar_entrada(adotante, "adotantes.json")
            print("Adotante cadastrado com sucesso!")
        else:
            print("Cadastro cancelado.")
        break

def atualizar_adotante():
    cpf = input("Digite o CPF do adotante: ")
    dados_atuais = armazenamento.ler_entrada(cpf, "CPF", "adotantes.json")
    if not dados_atuais:
        print("Adotante não encontrado.")
        return

    print("Dados atuais:")
    for k, v in dados_atuais.items():
        print(f"{k}: {v}")

    novos_dados = {
        "nome": input("Novo nome: "),
        "idade": input("Nova idade: "),
        "profissao": input("Nova profissão: "),
        "endereco": input("Novo CEP: "),
        "contato": input("Novo contato: ")
    }

    print("\nConfira as alterações:")
    for chave in novos_dados:
        print(f"{chave}: {dados_atuais[chave]} → {novos_dados[chave]}")

    if confirmar_acao("Deseja prosseguir com a atualização? (s/n): "):
        armazenamento.editar_entrada(cpf, novos_dados, "adotantes.json")
        print("Adotante atualizado com sucesso!")
    else:
        print("Atualização cancelada.")


def excluir_adotante():
    cpf = input("Digite o CPF do adotante a excluir: ")
    adotante = armazenamento.ler_entrada(cpf, "CPF", "adotantes.json")
    if not adotante:
        print("Adotante não encontrado.")
        return

    print("Adotante encontrado:")
    for k, v in adotante.items():
        print(f"{k}: {v}")

    if confirmar_acao("Deseja salvar esse adotante? (s/n): "):
            armazenamento.criar_entrada(cpf, "adotantes.json")
            print("Adotante cadastrado com sucesso!")
    else:
            print("Cadastro cancelado.")
  



