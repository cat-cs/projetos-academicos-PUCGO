import mysql.connector

#Inicia conexao com servidor MySQL
conexaoMysql = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='listacontatos'
)

cursor = conexaoMysql.cursor()

#comando = 'entre aspas simples' comando a ser executado, "aspas duplas para texto no sql"
#cursor.execute(comando)
# conexao.commit() para EDITAR banco de dados
#resultado = cursor.fetchall() para LER banco de dados

#CREATE(Inserir no Banco de Dados)
def create (tabela, nome):
    inserir = f'INSERT INTO contatos {tabela} VALUE ("{nome}")'
    cursor.execute(inserir)
    conexaoMysql.commit();

#READ
def read (tabela):
    lerBD = f'SELECT * FROM {tabela}'
    cursor.execute(lerBD)
    resultado = cursor.fetchall();
    print(resultado)

#UPDATE
def update (tabela, nome):
    atualizaDB = f'UPDATE {tabela} SET nome="{nome}" WHERE id = 1'
    cursor.execute(atualizaDB)
    conexaoMysql.commit();

#DELETE
def delete (tabela, nome):
    deletar = f'DELETE FROM {tabela} WHERE id = 1' 
    cursor.execute(deletar)   
    conexaoMysql.commit();

opcao = input("Escolha a opção desejada \n 1- Adicionar \n 2- Ler \n 3- Atualizar \n 4- Deletar \n")

if opcao == 1:
    create()
elif opcao == 2:
    read()
elif opcao == 3:
    update()
elif opcao == 4:
    delete()
else: 
    print("Opção Inválida")



#Fecha conexao
cursor.close()
conexaoMysql.close()