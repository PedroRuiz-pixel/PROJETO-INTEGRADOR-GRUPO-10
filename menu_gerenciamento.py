from mysql.connector import Error
from conexao import conectar
import random


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


def cadastrar_eleitor():
    nome = input("Nome: ")
    titulo = input("Título de Eleitor: ")
    cpf = input("CPF: ")
    mesario = input("Mesário(S/N): ")

    if nome == "" or titulo == "" or cpf == "":
        print("Todos os campos são obrigatórios.")
    else:
        if mesario == "S":
            mesario = True
        else:
            if mesario == "N":
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

def menu_gerenciamento():
    continuar = 1

    while continuar == 1:
        print("\n----- MENU DE GERENCIAMENTO -----")
        print("1 - Cadastrar Eleitor")
        print("2 - Listar Eleitores")
        print("3 - Buscar Eleitor por CPF")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_eleitor()

        elif opcao == "0":
            print("Saindo do menu de gerenciamento...")
            continuar = 0

        elif opcao == "2":
            listar_eleitores()

        elif opcao == "3":
            buscar_eleitor()

        else:
            print("Opção inválida. Tente novamente.")

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

                if eleitor[4] == 1:
                    print("Mesário: Sim")
                else:
                    print("Mesário: Não")

                print("Chave de Acesso:", eleitor[5])

                if eleitor[6] == 1:
                    print("Já votou: Sim")
                else:
                    print("Já votou: Não")

                print("----------------------")

                i = i + 1

    except Error as erro:
        print("Erro ao listar eleitores:", erro)

    cursor.close()
    conexao.close()

def buscar_eleitor():
    cpf = input("Digite o CPF do eleitor: ")

    conexao = conectar()
    cursor = conexao.cursor()

    try:
        sql = "SELECT * FROM eleitores WHERE CPF = %s"
        cursor.execute(sql, (cpf,))
        dados = cursor.fetchall()

        if len(dados) == 0:
            print("Eleitor não encontrado.")
        else:
            i = 0
            while i < len(dados):
                eleitor = dados[i]

                print("\nID:", eleitor[0])
                print("Nome:", eleitor[1])
                print("Título:", eleitor[2])
                print("CPF:", eleitor[3])

                if eleitor[4] == 1:
                    print("Mesário: Sim")
                else:
                    print("Mesário: Não")

                print("Chave de Acesso:", eleitor[5])

                if eleitor[6] == 1:
                    print("Já votou: Sim")
                else:
                    print("Já votou: Não")

                print("----------------------")

                i = i + 1

    except Error as erro:
        print("Erro ao buscar eleitor:", erro)

    cursor.close()
    conexao.close()