def gerar_chave_acesso(nome):
    partes = nome.strip().upper().split()

    if len(partes[0]) < 2:
        print("Nome precisa ter pelo menos 2 letras.")
        return ""

    if len(partes) >= 2:
        inicio = partes[0][0] + partes[0][1] + partes[1][0]
    else:
        inicio = partes[0][0] + partes[0][1] + "X"

    numero = str(random.randint(1000, 9999))
    chave = inicio + numero
    return chave


def validar_cpf(cpf):
    if cpf == cpf[0] * 11:
        print("CPF inválido.")
        return False

    # 1º
    soma = 0
    i = 0
    while i < 9:
        soma += int(cpf[i]) * (10 - i)
        i += 1

    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0

    if resto != int(cpf[9]):
        print("CPF inválido.")
        return False

    # 2º
    soma = 0
    i = 0
    while i < 10:
        soma += int(cpf[i]) * (11 - i)
        i += 1

    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0

    if resto != int(cpf[10]):
        print("CPF inválido.")
        return False

    return True


def validar_titulo(titulo):
    titulo_limpo = ""

    for c in titulo:
        if c >= '0' and c <= '9':
            titulo_limpo = titulo_limpo + c

    titulo = titulo_limpo

    if len(titulo) != 12:
        print("Título de eleitor deve ter 12 números.")
        return False

    return True


def cadastrar_eleitor():
    nome = input("Nome: ")
    titulo = input("Título de Eleitor: ")

    
    if not validar_titulo(titulo):
        return

    titulo_limpo = ""
    for c in titulo:
        if c >= '0' and c <= '9':
            titulo_limpo = titulo_limpo + c

    titulo = titulo_limpo

    cpf = input("CPF: ")

    if nome == "" or titulo == "" or cpf == "":
        print("Todos os campos são obrigatórios.")
        return

    cpf_limpo = ""
    for c in cpf:
        if c >= '0' and c <= '9':
            cpf_limpo = cpf_limpo + c

    cpf = cpf_limpo

    if len(cpf) != 11:
        print("CPF deve ter 11 números.")
        return

    if not validar_cpf(cpf):
        return

    mesario = input("Mesário(S/N): ").upper()

    if mesario == "S":
        mesario = True
    elif mesario == "N":
        mesario = False
    else:
        print("Digite apenas S ou N para mesário.")
        return

    chave_acesso = gerar_chave_acesso(nome)

    if chave_acesso == "":
        return

    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("SELECT * FROM eleitores WHERE cpf = %s", (cpf,))
        if len(cursor.fetchall()) > 0:
            print("Erro: CPF já cadastrado.")
            return

        sql = "INSERT INTO eleitores VALUES (NULL, %s, %s, %s, %s, %s, %s)"
        valores = (nome, titulo, cpf, mesario, chave_acesso, False)

        cursor.execute(sql, valores)
        conexao.commit()

        print("Eleitor cadastrado com sucesso!")
        print("Chave de Acesso:", chave_acesso)

    except Error as erro:
        print("Erro ao cadastrar eleitor:", erro)

    cursor.close()
    conexao.close()


def listar_eleitores():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("SELECT * FROM eleitores")
        dados = cursor.fetchall()

        if len(dados) == 0:
            print("Nenhum eleitor cadastrado.")
        else:
            i = 0
            while i < len(dados):
                eleitor = dados[i]

                print("\nID:", eleitor[0])
                print("Nome:", eleitor[1])
                print("Título:", eleitor[2])
                print("CPF:", eleitor[3])
                print("Mesário:", "Sim" if eleitor[4] == 1 else "Não")
                print("Chave de Acesso:", eleitor[5])
                print("Já votou:", "Sim" if eleitor[6] == 1 else "Não")
                print("----------------------")

                i += 1

    except Error as erro:
        print("Erro ao listar eleitores:", erro)

    cursor.close()
    conexao.close()


def buscar_eleitor():
    cpf = input("Digite o CPF do eleitor: ")

    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("SELECT * FROM eleitores WHERE cpf = %s", (cpf,))
        dados = cursor.fetchall()

        if len(dados) == 0:
            print("Eleitor não encontrado.")
        else:
            eleitor = dados[0]

            print("\nID:", eleitor[0])
            print("Nome:", eleitor[1])
            print("Título:", eleitor[2])
            print("CPF:", eleitor[3])
            print("Mesário:", "Sim" if eleitor[4] == 1 else "Não")
            print("Chave de Acesso:", eleitor[5])
            print("Já votou:", "Sim" if eleitor[6] == 1 else "Não")

    except Error as erro:
        print("Erro ao buscar eleitor:", erro)

    cursor.close()
    conexao.close()


def editar_eleitor():
    cpf = input("Digite o CPF do eleitor que deseja editar: ")

    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("SELECT * FROM eleitores WHERE cpf = %s", (cpf,))
        dados = cursor.fetchall()

        if len(dados) == 0:
            print("Eleitor não encontrado.")
            return

        novo_nome = input("Novo nome: ")
        novo_titulo = input("Novo título: ")

        cursor.execute(
            "UPDATE eleitores SET nome=%s, titulo=%s WHERE cpf=%s",
            (novo_nome, novo_titulo, cpf)
        )
        conexao.commit()

        print("Eleitor atualizado com sucesso!")

    except Error as erro:
        print("Erro ao editar eleitor:", erro)

    cursor.close()
    conexao.close()


def remover_eleitor():
    cpf = input("Digite o CPF do eleitor que deseja remover: ")

    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("SELECT * FROM eleitores WHERE cpf = %s", (cpf,))
        if len(cursor.fetchall()) == 0:
            print("Eleitor não encontrado.")
            return

        cursor.execute("DELETE FROM eleitores WHERE cpf = %s", (cpf,))
        conexao.commit()

        print("Eleitor removido com sucesso!")

    except Error as erro:
        print("Erro ao remover eleitor:", erro)

    cursor.close()
    conexao.close()


def menu_eleitor():
    opcao = ""

    while opcao != "0":
        print("\nVocê entrou no modulo de Eleitor!")
        print("1- Cadastrar eleitor")
        print("2- Editar eleitor")
        print("3- Remover eleitor")
        print("4- Buscar eleitor")
        print("5- Listar eleitores")
        print("0- Voltar")

        opcao = input("Digite uma opção: ").strip()

        if opcao == "1":
            cadastrar_eleitor()
        elif opcao == "2":
            editar_eleitor()
        elif opcao == "3":
            remover_eleitor()
        elif opcao == "4":
            buscar_eleitor()
        elif opcao == "5":
            listar_eleitores()
        elif opcao == "0":
            print("Voltando...")
        else:
            print("Opção inválida!")
