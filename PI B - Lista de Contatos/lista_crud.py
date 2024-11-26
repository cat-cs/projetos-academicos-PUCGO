import mysql.connector
from tabulate import tabulate #Biblioteca para print em tabela

#Inicia conexao com servidor MySQL
conexaoMysql = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='listacontatos'
)

cursor = conexaoMysql.cursor()

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
def read ():
    lerBD = 'SELECT contatos.id, contatos.Nome, GROUP_CONCAT(DISTINCT emails.Email SEPARATOR "; ") AS Emails, GROUP_CONCAT(DISTINCT CONCAT("(", telefones.DDD,") " ,telefones.Telefone) SEPARATOR "; ") AS Telefones FROM contatos LEFT JOIN telefones ON contatos.id = telefones.id_contatos INNER JOIN emails ON contatos.id = emails.id_contatos GROUP BY contatos.id, contatos.Nome;'
    cursor.execute(lerBD)
    resultado = cursor.fetchall();
    print(tabulate(resultado, headers=["ID", "Nome", "Emails", "Telefones"], tablefmt="grid"))

#UPDATE
def update ():
    id_update = int (input("Digite id para selecionar um contato -> "))
    nomeSelecionado = exibeNomeContato(id_update)
    print(f"Contato selecionado: {nomeSelecionado}")
    
    
    atualizaDB = f'UPDATE {tabela} SET nome="{nome}" WHERE id = 1'
    cursor.execute(atualizaDB)
    conexaoMysql.commit();

#DELETE
def delete ():
    #Digite id para selecionar um contato
    id_delete = int (input("Digite id para selecionar um contato -> "))
    deletar = f'DELETE FROM contatos WHERE id = {id_delete}' 
    nomeExcluido = exibeNomeContato(id_delete)
    verifica = input (f"Deseja excluir o contato de {nomeExcluido} ? Digite SIM/NAO\n -> ")
    if verifica.upper() == "SIM":
        cursor.execute(deletar)
        conexaoMysql.commit();
        print("___Contato excluído com sucesso!___")
    elif verifica.upper() == "NAO":
        print("Retornando ao menu...");
    else:
        print("Opção Inválida. Digite SIM/NAO");

def exibeNomeContato(id):
    exibeNomeporID = f'SELECT Nome FROM contatos WHERE id = {id}'
    cursor.execute(exibeNomeporID)
    nome_retornado = cursor.fetchone()
    return nome_retornado[0].upper();

def adicionaNovoItem(id):
    opcao_adiciona = int(input("1- Adicionar Email      2- Adicionar Telefone"))
    if opcao_adiciona == 1:
        email = input("Email: ")
        inserir_email = f'INSERT INTO emails (email, id_contatos) VALUES ("{email}", {id})'
        cursor.execute(inserir_email)
        conexaoMysql.commit();
        print("Email adicionado com sucesso!")
    elif opcao_adiciona == 2:
        ddd = int(input("DDD: "))
        telefone = int(input("Telefone: "))
        inserir_telefone = f'INSERT INTO telefones (DDD, Telefone, id_contatos) VALUES ({ddd}, {telefone}, {id})'
        cursor.execute(inserir_telefone)
        conexaoMysql.commit();
        print("Telefone adicionado com sucesso!")
    else: 
        print("Opção Inválida")

        
    

#---------------APLICAÇÃO---------------------------------------------------------------------------------------------------------

print("_____|Lista de Contatos|_____")
while True: 
    opcao = int (input("\n Escolha a opção desejada \n 1- Adicionar Contato \n 2- Vizualizar Lista \n 3- Sair \n -> "))

    if opcao == 1:
        create()
        print("___Contato adicionado a lista com sucesso!___")
        
    elif opcao == 2:
        read()
    #-------------SUBMENU ALTERAÇÃO---------------------------------------------------------------------------------------------
        opcao_contato = input("1- Alterar Dados    2- Apagar Contato da Lista     SAIR- Retornar ao início \n -> ")
        if opcao_contato == "1":
            update() #adciona mais um telefone ou email/ altera telefone, email, nome
        elif opcao_contato == "2":
            delete()
        elif opcao_contato.upper() == "SAIR":
            print("\n Encerrando...")
            cursor.close()
            conexaoMysql.close()
            break
        else: 
            print("Opção Inválida")
    #----------------------------------------------------------------------------------------------------------------------------
    
    elif opcao == 3:
        print("\n Encerrando...")
        cursor.close()
        conexaoMysql.close()
        break
    else: 
        print("Opção Inválida")
        
#Fecha conexao
cursor.close()
conexaoMysql.close()