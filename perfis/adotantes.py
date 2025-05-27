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
        print("CRIAÇÃO DE ADOTANTE")
        return cadastrar_adotante()
    elif tipo_operacao == "editar":
        print("EDIÇÃO DE ADOTANTE")
        return atualizar_adotante()
    elif tipo_operacao == "deletar":
        print("DELETAÇÃO DE ADOTANTE")
        return excluir_adotante()
    elif tipo_operacao == "ler":
        print("LEITURA DE ADOTANTE")
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

# ------------------------------------------------------------

def listar_todos_adotantes():
    adotantes = armazenamento.carregar_arquivo("adotantes.json")
    
    if adotantes is None:
        print("Erro ao carregar arquivo de adotantes.")
    elif not adotantes:
        print("O arquivo de adotantes está vazio. Criando arquivo...")
    else:
        print("=" * 50)
        print("LISTA DE ADOTANTES:")
        
        for adotante in adotantes:
            print("-" * 50)
            print(f"CPF: {adotante['CPF']}")
            print(f"Nome completo: {adotante['nome']}")
            print(f"Idade: {adotante['idade']}")
            print(f"Profissão: {adotante['profissao']}")
            print(f"Endereço: {adotante['endereco']}")
            print(f"Contato: {adotante['contato']}")
            
            print("Preferências:")
            for chave, valor in adotante['preferencias'].items():
                print(f"  {chave}: {valor}")
        
        print("=" * 50)


# ------------------------------------------------------------

def ler_adotante():
    cpf = input("Digite o CPF do adotante: ").strip()
    while not validar_cpf(cpf):
        cpf = input("CPF inválido. Digite o CPF do adotante: ").strip()
    adotante = armazenamento.ler_entrada(cpf, 'CPF', "adotantes.json")
    if adotante is not None:
        return ('ler', adotante)
    return f"Erro ao ler adotante com CPF {cpf}"

# --------------------------------

def cadastrar_adotante():
    while True:
        cpf = input("Digite o CPF do adotante: ").strip()
        while not validar_cpf(cpf):
            cpf = input("CPF inválido. Digite o CPF do adotante: ").strip()

        nome = input("Digite o nome completo: \n")

        idade = input("Digite a idade: \n").strip()
        while not validar_idade(idade):
            idade = input("Idade inválida!\nDigite a idade: \n").strip()
        idade = int(idade)

        profissao = input("Digite a profissão: \n")

        endereco = input("Digite o CEP (somente números): \n").strip()
        while not validar_cep(endereco):
            print("CEP inválido! Deve conter 8 dígitos.\n")
            endereco = input("Digite o CEP (somente números): \n").strip()

        contato = input("Digite o contato (somente números): ").strip()
        while not validar_contato(contato):
            print("Contato inválido! Deve conter ao menos 8 dígitos.\n")
            contato = input("Digite o contato (somente números): ").strip()

        print("\n--- Preferências do adotante ---")

        tipo = input("Prefere qual tipo de animal? (canino/felino): ").strip().lower()
        while tipo not in ["canino", "felino"]:
            tipo = input("Entrada inválida. Digite canino ou felino: ").strip().lower()

        porte = input("Porte preferido? (pequeno/médio/grande): ").strip().lower()
        while porte not in ["pequeno", "médio", "grande"]:
            porte = input("Entrada inválida. Digite pequeno, médio ou grande: ").strip().lower()

        temp = input("Personalidades preferidas (separe por vírgula, ex: brincalhão, calmo, protetor): ").lower()
        temperamento = [t.strip() for t in temp.split(",") if t.strip()]

        sexo = input("Sexo preferido? (macho/fêmea): ").strip().lower()
        while sexo not in ["macho", "fêmea"]:
            sexo = input("Entrada inválida. Digite macho ou fêmea: ").strip().lower()

        faixa_etaria = input("Faixa etária preferida? (filhote/adulto/idoso): ").strip().lower()
        while faixa_etaria not in ["filhote", "adulto", "idoso"]:
            faixa_etaria = input("Entrada inválida. Digite filhote, adulto ou idoso: ").strip().lower()

        experiencia = input("Tem experiência com animais? (s/n): ").strip().lower()
        while experiencia not in ['s', 'n']:
            experiencia = input("Opção inválida. Digite 's' ou 'n': ").strip().lower()
        experiencia = 'Sim' if experiencia == 's' else 'Não'

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

        confirm = input("Deseja salvar esse adotante? (s/n): ").strip().lower()
        while True:
            if confirm == "s":
                if armazenamento.criar_entrada(adotante, "adotantes.json"):
                    return ("criar", adotante)
                return "Erro ao criar entrada."
            elif confirm == "n":
                return "Cadastro cancelado."
            else:
                print("Opção inválida.")
                confirm = input("Deseja salvar esse adotante? (s/n): ").strip().lower()

# --------------------------------

def atualizar_adotante():
    cpf = input("Digite o CPF do adotante a ser atualizado: ").strip()
    while not validar_cpf(cpf):
        cpf = input("CPF inválido. Digite o CPF do adotante: ").strip()

    dados_atuais = armazenamento.ler_entrada(cpf, "CPF", "adotantes.json")
    if dados_atuais is None:
        return f"Erro ao atualizar: problema ao ler adotante com id {cpf}."

    dados_antigos = dados_atuais

    print("Dados atuais:")
    for k, v in dados_atuais.items():
        print(f"{k}: {v}")

    nome = input("Novo nome: ")

    while True:
        idade = input("Nova idade: ").strip()
        if validar_idade(idade):
            idade = int(idade)
            break
        print("Idade inválida!")

    profissao = input("Nova profissão: ")

    while True:
        endereco = input("Novo CEP (somente números): ").strip()
        if validar_cep(endereco):
            break
        print("CEP inválido! Deve conter 8 dígitos.")

    while True:
        contato = input("Novo contato (somente números): ").strip()
        if validar_contato(contato):
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

    confirm = input("Deseja prosseguir com a atualização? (s/n): ").strip().lower()
    while True:
        if confirm == "s":
            if armazenamento.editar_entrada(cpf, 'CPF', novos_dados, "adotantes.json"):
                return ("atualizar", (dados_antigos, dados_atuais))
            return "Erro ao atualizar adotante."
        elif confirm == "n":
            return f"Atualização do adotante com id {cpf} cancelada."
        else:
            print('Opção inválida. Digite \'s\' ou \'n\'')
            confirm = input("Deseja prosseguir com a atualização? (s/n): ").strip().lower()

# --------------------------------

def excluir_adotante():
    cpf = input("Digite o CPF do adotante: ").strip()
    while not validar_cpf(cpf):
        cpf = input("CPF inválido. Digite o CPF do adotante: ").strip()

    adotante = armazenamento.ler_entrada(cpf, "CPF", "adotantes.json")
    if adotante is None:
        return f"Erro ao excluir: problema ao ler adotante com id {cpf}."

    print("Adotante encontrado:")
    for k, v in adotante.items():
        print(f"{k}: {v}")

    confirm = input("Deseja realmente excluir esse adotante? (s/n): ").strip().lower()
    while True:
        if confirm == "s":
            armazenamento.deletar_entrada(cpf, "CPF", "adotantes.json")
            return ("deletar", adotante)
        elif confirm == "n":
            return f"Exclusão do adotante com id {cpf} cancelada."
        else:
            print("Opção inválida.")
            confirm = input("Deseja realmente excluir esse adotante? (s/n): ").strip().lower()


# --------------------------------

if __name__ == "__main__":
    tipo = input("Qual operação deseja realizar? (criar/editar/deletar/ler): ").strip().lower()
    resultado = crud_adotantes(tipo)
    print(f"Resultado: {resultado}")
