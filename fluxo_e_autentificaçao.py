from datetime import datetime
import random


def votar(conexao):

    cursor = conexao.cursor()

    print("\n=== IDENTIFICAÇÃO DO ELEITOR ===")

    titulo = input("Digite o título de eleitor: ")
    cpf4 = input("Digite os 4 primeiros dígitos do CPF: ")
    chave = input("Digite a chave de acesso: ")

    sql = """
    SELECT id, cpf_criptografado, chave_criptografada, ja_votou
    FROM eleitores
    WHERE titulo = %s
    """

    cursor.execute(sql, (titulo,))
    eleitor = cursor.fetchone()

    if eleitor is None:
        print("Eleitor não encontrado.")
        registrar_log("ALERTA: Tentativa de acesso negado")
        return

    id_eleitor = eleitor[0]
    cpf_banco = decifrar_hill(eleitor[1])
    chave_banco = decifrar_hill(eleitor[2])
    ja_votou = eleitor[3]

    cpf_banco = cpf_banco.rstrip("X")
    chave_banco = chave_banco.rstrip("X")

    if cpf_banco[:4] != cpf4 or chave_banco != chave:
        print("Dados inválidos.")
        registrar_log("ALERTA: Tentativa de acesso negado")
        return

    if ja_votou:
        print("Este eleitor já votou.")
        registrar_log("ALERTA: Tentativa de voto duplo")
        return

    print("\nEleitor autenticado com sucesso!")  
#------------------------------------------------------

    while True:
        numero = input("\nDigite o número do candidato: ")

        sql = """
        SELECT id, nome, numero, partido
        FROM candidatos
        WHERE numero = %s
        """

        cursor.execute(sql, (numero,))
        candidato = cursor.fetchone()

        if candidato is None:
        print("\nCandidato não encontrado.")
        print("Se confirmar, o voto será NULO.")
        else:
            print("\nCandidato encontrado:")
            print("Nome:", candidato[1])
            print("Número:", candidato[2])
            print("Partido:", candidato[3])

        confirmar = input("Confirmar voto? (sim/nao): ")

        if confirmar.lower() == "sim":
            break

        print("Voto cancelado. Digite novamente.")

        protocolo = "V" + str(random.randint(100000, 999999))
        protocolo_criptografado = cifrar_hill(protocolo)
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if candidato is None:
            sql = """
            INSERT INTO votos
            (candidato_id, voto_nulo, data_hora, protocolo_criptografado)
            VALUES (%s, %s, %s, %s)
            """

        cursor.execute(sql, (None, True, data_hora, protocolo_criptografado))

        else:
        id_candidato = candidato[0]

        sql = """
        INSERT INTO votos
        (candidato_id, voto_nulo, data_hora, protocolo_criptografado)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(sql, (id_candidato, False, data_hora, protocolo_criptografado))

        sql = """
        UPDATE eleitores
        SET ja_votou = 1
        WHERE id = %s
        """

        cursor.execute(sql, (id_eleitor,))
        conexao.commit()

        print("\nVoto registrado com sucesso!")
        print("Seu protocolo é:", protocolo)

        registrar_log("SUCESSO: Voto realizado com sucesso")