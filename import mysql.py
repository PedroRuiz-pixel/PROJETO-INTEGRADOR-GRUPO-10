import mysql.connector 

conexao = mysql.connector.connect(
    host="127.0.0.1",   
    user="root",
    password="Dudu4189*",
    database="projeto_integrador",
    port=3306
)

cursor = conexao.cursor()
cursor.execute("SELECT DATABASE();")
print(cursor.fetchone())

cursor.close()
conexao.close()
