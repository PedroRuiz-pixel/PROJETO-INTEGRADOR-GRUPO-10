import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Dudu4189*",
        database="projeto_integrador",
        port=3306
    )
    return conexao
