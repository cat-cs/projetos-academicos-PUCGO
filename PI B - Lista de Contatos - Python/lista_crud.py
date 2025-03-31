import mysql.connector
from tabulate import tabulate #Biblioteca para print em tabela

#-----Inicia conexao com servidor MySQL--------------------------------------------------------------------------------------------
conexaoMysql = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='listacontatos'
)

cursor = conexaoMysql.cursor()

#---------------CREATE-------------------------------------------------------------------------------------------------------------
def create ():
    print("___Adcione as informações de contato___")
    nome = input("Nome: ")
    while True:
        try: 
            ddd = input("DDD: ")
            telefone = input("Telefone: ")
            int(ddd)
            int(telefone)
            break
        except: 
            print("Entrada Inválida! Insira apenas números")

    email = input("Email: ")

    inserir_nome(nome)
    id_contatos = cursor.lastrowid

    inserir_telefone(ddd, telefone, id_contatos)
    inserir_email (email, id_contatos)

    print("___Contato adicionado a lista com sucesso!___");


#---------------READ---------------------------------------------------------------------------------------------------------------
def read ():
    lerBD = 'SELECT contatos.id, contatos.Nome, GROUP_CONCAT(DISTINCT emails.Email SEPARATOR "; ") AS Emails, GROUP_CONCAT(DISTINCT CONCAT("(", telefones.DDD,") " ,telefones.Telefone) SEPARATOR "; ") AS Telefones FROM contatos LEFT JOIN telefones ON contatos.id = telefones.id_contatos INNER JOIN emails ON contatos.id = emails.id_contatos GROUP BY contatos.id, contatos.Nome;'
    cursor.execute(lerBD)
    resultado = cursor.fetchall();
    late(resultado, headers=["ID", "Nome", "Emaprint(tabuils", "Telefones"], tablefmt="grid"))

#---------------UPDATE-------------------------------------------------------------------------------------------------------------
def update ():
    id_update = int (input("Digite ID para selecionar um contato -> "))
    nomeSelecionado = exibeNomeContato(id_update)
    print(f"Contato selecionado: {nomeSelecionado}")
    opcao_update = int(input("Qual operação deseja realizar? 1- Atualizar Contato   2-Adicionar ao Contato \n -> "))
    
    if opcao_update == 1:
        atualizaContato(id_update)
        print("___Contato atualizado com Sucesso!___ \n")
    elif opcao_update == 2:
        adicionaNovoItem(id_update)
        print("Retornando ao menu...")
    
#---------------DELETE-------------------------------------------------------------------------------------------------------------
def delete ():
    id_delete = int (input("Digite ID para selecionar um contato -> "))
    deletar = f'DELETE FROM contatos WHERE id = (%s)' 
    nomeExcluido = exibeNomeContato(id_delete)
    verifica = input (f"Deseja excluir o contato de {nomeExcluido}? Digite SIM/NAO\n -> ")
    if verifica.upper() == "SIM":
        cursor.execute(deletar, (id_delete))
        conexaoMysql.commit();
        print("___Contato excluído com sucesso!___ \n")
    elif verifica.upper() == "NAO":
        print("Retornando ao menu...");
    else:
        print("Opção Inválida. Digite SIM ou NAO");

#---------------FUNÇÕES AUXILIARES-------------------------------------------------------------------------------------------------
def inserir_nome (nome):
    insert_nome= f'INSERT INTO contatos (nome) VALUES (%s)'
    cursor.execute(insert_nome, (nome,))
    conexaoMysql.commit();
    
def inserir_telefone (ddd, telefone, id_contatos):     
    insert_telefone = f'INSERT INTO telefones (DDD, Telefone, id_contatos) VALUES (%s, %s, %s)'
    cursor.execute(insert_telefone, (ddd, telefone, id_contatos))
    conexaoMysql.commit();
        
def inserir_email (email, id_contatos):
    insert_email= f'INSERT INTO emails (email, id_contatos) VALUES (%s, %s)'
    cursor.execute(insert_email, (email, id_contatos)) 
    conexaoMysql.commit();


def exibeNomeContato(id):
    exibeNomeporID = f'SELECT Nome FROM contatos WHERE id = %s'
    cursor.execute(exibeNomeporID, (id,))
    nome_retornado = cursor.fetchone()
    return nome_retornado[0].upper();

def exibeEmailsContato(id):
        exibeEmailporID = f'SELECT id_email, Email FROM emails WHERE id_contatos = (%s)'
        cursor.execute(exibeEmailporID, (id,))
        email_retornado = cursor.fetchall()
        return email_retornado;

def exibeTelefonesContato(id):
        exibeTelefoneporID = f'SELECT id_telefone, ddd, Telefone FROM telefones WHERE id_contatos = (%s)'
        cursor.execute(exibeTelefoneporID, (id,))
        telefone_retornado = cursor.fetchall()
        return telefone_retornado;



def adicionaNovoItem(id):
    opcao_adiciona = int(input("1- Adicionar Email      2- Adicionar Telefone \n -> "))
    if opcao_adiciona == 1:
        email = input("Email: ")
        inserir_email(email, id)
        print("Email adicionado com sucesso!")
        
    elif opcao_adiciona == 2:
        while True:
            try: 
                ddd = input("DDD: ")
                telefone = input("Telefone: ")
                int(ddd)
                int(telefone)
                break
            except: 
                print("Entrada Inválida! Insira apenas números")
        inserir_telefone(ddd, telefone, id)
        print("Telefone adicionado com sucesso!")
    else: 
        print("Opção Inválida")

def atualizaContato(id):
    opcao_atualizaContato = int(input("Qual campo deseja alterar? 1- Nome   2-Email    3-Telefone \n -> "))
    if opcao_atualizaContato == 1: #ALTERAR NOME
        novo_nome = input("Novo nome: ")
        atualizaNome = f'UPDATE contatos SET nome=(%s) WHERE id = (%s)'
        cursor.execute(atualizaNome, (novo_nome, id))
        conexaoMysql.commit();
    
    elif opcao_atualizaContato == 2: #ALTERAR EMAIL
        lista_email = exibeEmailsContato(id)
        print(tabulate(lista_email, headers=["ID Email", "Emails do Contato"], tablefmt="grid"))
        id_email_alterado = int(input("Digite o ID do email a ser alterado -> "))        
        novo_email = input("Novo email: ")
        atualizaEmail = f'UPDATE emails SET email=(%s) WHERE id_email = (%s)'
        cursor.execute(atualizaEmail, (novo_email, id_email_alterado))
        conexaoMysql.commit();
    
    elif opcao_atualizaContato == 3: #ALTERAR TELEFONE
        lista_telefone = exibeTelefonesContato(id)
        print(tabulate(lista_telefone, headers=["ID Telefone", "DDD","Telefone do Contato"], tablefmt="grid"))
        id_telefone_alterado = int(input("Digite o ID do telefone a ser alterado -> "))        
        while True:
            try: 
                novo_ddd = input("Novo DDD: ")
                novo_telefone = input("Novo teleone: ")
                int(novo_ddd)
                int(novo_telefone)
                break
            except: 
                print("Entrada Inválida! Insira apenas números")

        atualizaTelefone = f'UPDATE telefones SET ddd=(%s), telefone=(%s) WHERE id_telefone = (%s)'
        cursor.execute(atualizaTelefone, (novo_ddd, novo_telefone, id_telefone_alterado))
        conexaoMysql.commit();  
    else:
        print("Opção Inválida");
        
    

#---------------APLICAÇÃO---------------------------------------------------------------------------------------------------------

while True: 
    print("_-_-_-_-_|Lista de Contatos|_-_-_-_-_")
    opcao = int (input("\n Escolha a opção desejada \n 1- Adicionar Contato \n 2- Vizualizar Lista \n 3- Sair \n -> "))

    if opcao == 1:
        create()

    elif opcao == 2:
        read()
    #-------------SUBMENU ALTERAÇÃO---------------------------------------------------------------------------------------------
        print("\n______________Opções da Lista_____________")
        opcao_contato = input("1- Alterar Dados    2- Apagar Contato da Lista     SAIR- Retornar ao início \n -> ")
        if opcao_contato == "1":
            update()
        elif opcao_contato == "2":
            delete()
        elif opcao_contato.upper() == "SAIR":
            print("Retornando...\n")
            continue
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
        
#-----Fecha conexao---------------------------------------------------------------------------------------------------------------
cursor.close()
conexaoMysql.close()
