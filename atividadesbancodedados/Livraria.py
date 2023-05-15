#Cenário: Biblioteca

# Construir um sistema de cadastro de aluguéis de livros.

# - Deve conter um banco com as seguintes tabelas: Clientes, Aluguéis e Livros
# - Deve conter as seguintes funcionalidades: Cadastro de Clientes, Cadastro de Aluguéis, Cadastro de Livros e Visualização dos dados das 3 tabelas.

#Requisitos:
#   - Deve utilizar chave estrangeira

import psycopg2
import sys
import os
import time

class Conexao:

    def __init__(self, dbname, host, port, user, password) -> None:
        self._dbname = dbname
        self._host = host
        self._port = port
        self._user = user
        self._password = password
    
    def consultarBanco(self, sql):
        conn = psycopg2.connect(dbname = self._dbname, host = self._host, port = self._port, user = self._user, password = self._password)

        cursor = conn.cursor()

        cursor.execute(sql)

        resultado = cursor.fetchall()

        cursor.close()
        conn.close()

        return resultado
    
    def manipularBanco(self,sql):
        conn = psycopg2.connect(dbname = self._dbname, host = self._host, port = self._port, user = self._user, password = self._password)
        cursor = conn.cursor()

        cursor.execute(sql)

        conn.commit()

        cursor.close()

        conn.close()


con = Conexao(dbname = "Livraria" ,host = "localhost", port = "5432", user = "postgres", password = "postgres" )

#Funções para criação de tabelas -----------------------------------------------------------------------------------

def criartabelaClientes():
    con.manipularBanco('''
    create table "Clientes"(
    "id_cliente" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "nome" varchar(255) not null
    )
    ''')

    print("Tabela Clientes criada com sucesso!")

def criartabelaLivros():
    con.manipularBanco('''
    create table "Livros"(
    "id_livro" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "preço" float(2) not null,
    "nome" varchar(255) not null
    )
    ''')

    print("Tabela Livros criada com sucesso!")

def criartabelaAlugueis():
    con.manipularBanco('''
    create table "Alugueis"(
    "id_aluguel" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "id_cliente" int,
    "id_livro" int,
    "quantidade" int not null default 1,
    "Horário" timestamp default CURRENT_TIMESTAMP(0),
    "valortotal" float(2) not null,

        CONSTRAINT fk_cliente
            FOREIGN KEY("id_cliente")
            REFERENCES "Clientes"("id_cliente"),
    
        CONSTRAINT fk_livro
            FOREIGN KEY("id_livro")
            REFERENCES "Livros"("id_livro")
    )
    ''')

    print("Tabela Alugueis criada com sucesso!")

# Slow print -----------------------------------------------------------------------------------------------------------

def slowprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1./10)

# Função para cadastrar Clientes ----------------------------------------------------------------------------------

def cadastrarCliente():
    nome = input("Insira o nome do cliente: ")
    con.manipularBanco(f'''
    insert into "Clientes"
    values (default, '{nome}')
    ''')

    print("Cliente cadastrado com sucesso!")

# Função para cadastrar livros -------------------------------------------------------------------------------------

def cadastrarLivro():
    nome = input("Insira o nome do Livro: ")
    preço = input("Insira o valor do livro:")
    preço2 = preço.replace(',','.')

    con.manipularBanco(f'''
    insert into "Livros"(
    values (default, '{preço2}','{nome}')
    )
    ''')
    
    print("Livros cadastrado com sucesso!")

# Função para cadastrar alugueis ------------------------------------------------------------------------------------------

def cadastrarAluguel():
    cliente = input("Insira o nome do cliente: ")
    livro = input("Insira o nome do livro: ")
    quantidade = int(input("Digite a quantidade alugada do livro em questão: "))   



# Função que vai ser usada para ver o ID do cliente sem que o usuario da aplicação tenha que digitar o ID 
# e sim somente o nome do cliente em questão --------------------------------------------------------------------------------------------

    def verCliente():
        while True:
            verCliente = con.consultarBanco('''
            select * from "Clientes"
            order by "id_cliente"
            ''')
            for x in verCliente:
                if x[1] == cliente:
                    return x[0]
                
    # Parte do codigo para cadastrar um cliente 
    # sem que o usuario da aplicação tenha que retornar para a parte do menu que cadastra um cliente.
    # Caso o usuario queira cadastrar um aluguel de um cliente que não tenha cadastro ainda, o sistema cadastra automaticamente
    # para o usuario. --------------------------------------------------------------------------------------------------------------------------------

                else:
                    con.manipularBanco(f'''
                    insert into "Clientes"
                    values (default, '{cliente}')
                    ''')
                    if x[1] == cliente:
                        print(f'{x[0]}')
                        break
                
            print("Cliente não cadastrado no sistema!")
            slowprint("Castrando cliente . . .")
            print("Cliente cadastrado com sucesso!")

# Função que vai ser usada para ver o ID do Livro sem que o usuario da aplicação tenha que digitar o ID 
# e sim somente o nome do livro em questão. --------------------------------------------------------------------------------------------------------------

    def verLivro():
        verLivro = con.consultarBanco('''
        select * from "Livros"
        order by "id_livro"
        ''')
        for x in verLivro:
            if x[2] == livro:
                return x[0]

# Função para ver o preço do livro na tabela Livros para multiplicar pela quantidade na tabela Alugueis e calcular o valor total -----------------------------

    def verValor():
        verValor = con.consultarBanco('''
        select * from "Livros"
        order by "id_livro"
        ''')

        for x in verValor:
            if x[2] == livro:
                return x[1]   
            
# Variavel com o calculo do valor total ----------------------------------------------------------------------------------------

    valorTotal = verValor()*quantidade
    
# Continuação da função de cadastro de algueis ------------------------------------------------------------------------------

    con.manipularBanco(f'''
    insert into "Alugueis"(
    values (default, '{verCliente()}', '{verLivro()}', '{quantidade}', default, '{valorTotal}')
    )
    ''')

    print("Aluguel cadastrado com sucesso!")


# Função para visualizar os clientes no sistema ---------------------------------------------------------------------------------

def visualizarClientes():
    print('Lista de clientes!')
    verClientes = con.consultarBanco('''
    select * from "Clientes"
    order by "id_cliente" ASC
    ''')
    for cliente in verClientes:
        print(f'''
ID - {cliente[0]}
Nome - {cliente[1]}
''')

# Função para visualizar os livros no sistema --------------------------------------------------------------------------------------

def visualizarLivros():
    print('Lista de livros!')
    verLivros = con.consultarBanco('''
    select * from "Livros"
    order by "id_livro" ASC
    ''')
    for livro in verLivros:
        print(f'''
ID - {livro[0]}
Nome - {livro[1]}
Valor - R${livro[2]}
''')

# Função para visualizar os alugueis no sistema ---------------------------------------------------------------------------------------

def visualizarAlugueis():
    print('Lista de Alugueis!')
    alugueis = con.consultarBanco('''
    select * from "Alugueis"
    order by "id_aluguel" ASC
    ''')
    for x in alugueis:

        nome_cliente = con.consultarBanco(f'''
        select "nome" from "Clientes"
        where "id_cliente" = {x[1]}
        ''')[0][0]

        nome_livro = con.consultarBanco(f'''
        select "nome" from "Livros"
        where "id_livro" = {x[2]}
        ''')[0][0]

        print (f'''
ID - {x[0]}
Cliente - {nome_cliente} 
Livro - {nome_livro} 
Quantidade - {x[3]}
Horário - {x[4]}
Valor Total - R${x[5]}
''')



while True:
    try:
        print('''

        Menu

        1 - Cadastrar novo cliente!
        2 - Cadastrar novo livro!
        3 - Cadastrar novo Aluguel!

        4 - Visualizar cadastros no sistema!


        0 - SAIR!
        ''')
        a = int(input('> '))
        match a:
            case 1:
                os.system('cls')
                cadastrarCliente()
                input('Enter para continuar . . .')
            case 2:
                os.system('cls')
                cadastrarLivro()
                input('Enter para continuar . . .')
            case 3:
                os.system('cls')
                cadastrarAluguel()
                input('Enter para continuar . . .')
            case 4:
                while True:
                    os.system('cls')
                    print('''
        Menu de cadastros do sistema!
        
        1 - Visualizar clientes!
        2 - Visualizar Livros!
        3 - Visualizar Alugueis!
        

        0 - Voltar ao menu anterior!
        ''')
                    b = int(input('> '))
                    match b:
                        case 1:
                            os.system('cls')
                            visualizarClientes()
                            input('Enter para continuar . . .')
                        case 2:
                            os.system('cls')
                            visualizarLivros()
                            input('Enter para continuar . . .')
                        case 3:
                            os.system('cls')
                            visualizarAlugueis()
                            input('Enter para continuar . . .')
                        case 0:
                            os.system('cls')
                            break
                    
            case 0:
                os.system('cls')
                sys.exit()
    except(ValueError):
        os.system('cls')
        print('Algo deu errado!')

