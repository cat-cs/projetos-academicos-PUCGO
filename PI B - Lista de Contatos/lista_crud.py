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
def create ():
    print("***Adcione as informações de contato***")
    nome = input("Nome: ")
    ddd = int(input("DDD: "))
    telefone = int(input("Telefone: "))
    email = input("Email: ")

    inserir_nome = f'INSERT INTO contatos (nome) VALUES ("{nome}")'
    cursor.execute(inserir_nome)
    id_contatos = cursor.lastrowid

    inserir_telefone = f'INSERT INTO telefones (DDD, Telefone, id_contatos) VALUES ({ddd}, {telefone}, {id_contatos})'
    inserir_email = f'INSERT INTO emails (email, id_contatos) VALUES ("{email}", {id_contatos})'
    
    
    cursor.execute(inserir_telefone)
    cursor.execute(inserir_email)

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
def delete ():
    tabela = input("Escolha a tabela:")
    id_user = int (input("Escolha o id:"))
    deletar = f'DELETE FROM {tabela} WHERE id = {id_user}' 
    cursor.execute(deletar)   
    conexaoMysql.commit();

opcao = int (input("Escolha a opção desejada \n 1- Adicionar Contato \n 2- Vizualizar Lista \n ->"))

#\n 3- Atualizar \n 4- Deletar \n 
# elif opcao == 3:
    #update() #adciona mais um telefone ou email/ altera telefone, email, nome
#elif opcao == 4:
    #delete()

if opcao == 1:
    create()# adcionar telefone e email em tabelas fk
elif opcao == 2:
    read()# listar tabela contatos || Criar segundo read com join das duas tabelas para cada contato
else: 
    print("Opção Inválida")



#Fecha conexao
cursor.close()
conexaoMysql.close()