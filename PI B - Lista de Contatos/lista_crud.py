import mysql.connector

#Inicia conexao com servidor MySQL
conexaoMysql = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='listacontatos'
)

cursor = conexaoMysql.cursor()

inserir = 'insert into contatos values (Lucas)'
cursor.execute(inserir)
conexaoMysql.commit()
#comando = 'entre aspas simples' comando a ser executado
#cursor.execute(comando)

# conexao.commit() para EDITAR banco de dados
#resultado = cursor.fetchall() para LER banco de dados

#Fecha conexao
cursor.close()
conexaoMysql.close()