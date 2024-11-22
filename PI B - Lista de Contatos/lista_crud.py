import mysql.connector

#Inicia conexao com servidor MySQL
conexaoMysql = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='listacontatos'
)

cursor = conexaoMysql.cursor()


#CREATE(Inserir no Banco de Dados)
    #inserir = 'INSERT INTO contatos (nome) VALUE ("Joao Felipe da Silva")'
    #cursor.execute(inserir)
    #conexaoMysql.commit()

#READ
    #  lerBD = 'SELECT * FROM contatos'
    #  cursor.execute(lerBD)
    #  resultado = cursor.fetchall()
    #  print(resultado)

#UPDATE
    # atualizaDB = 'UPDATE contatos SET nome="João Carlos da Silva Moraes" WHERE id = 1'
    # cursor.execute(atualizaDB)
    # conexaoMysql.commit()

#DELETE
#   deletar = 'DELETE FROM contatos WHERE id = 1' 
#   cursor.execute(deletar)   
#   conexaoMysql.commit()

#comando = 'entre aspas simples' comando a ser executado, "asppas duplas para texto no sql"
#cursor.execute(comando)

# conexao.commit() para EDITAR banco de dados
#resultado = cursor.fetchall() para LER banco de dados

#Fecha conexao
cursor.close()
conexaoMysql.close()