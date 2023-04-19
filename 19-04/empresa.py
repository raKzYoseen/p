import psycopg2
import os

def criartabelafuncionario():
    sql= ('''
    create table "Funcionario"(
    "ID_Func" int GENERATED ALWAYS AS IDENTITY,
    "Nome_Func" varchar(255) Not null,
    "Salario_Func" float(2) Not null default 0.00,
    "Cargo_Func" varchar(255) NOT NULL default 'Autônomo',
    "ID_Departamento" integer default 1,
    Primary Key ("ID_Func")
    )
    ''')
    return sql

def criartabeladepartamento():
    sql= ('''
    create table "Departamento"(
    "ID_Departamento" int GENERATED ALWAYS AS IDENTITY,
    "Nome_Depart" varchar(255) Not null,
    Primary Key ("ID_Departamento")
    )
    ''')
    return sql


def verFuncionarios():
    cursor.execute('''
    select * from "Funcionario"
    order by "ID_Func" ASC
''')
    a = cursor.fetchall()
    for nome in a:
        print(f'{nome[0]} - {nome[1]}')

def verDepartamento():
    os.system('cls')
    cursor.execute('''
    select * from "Departamento"
    order by "ID_Departamento" ASC
''')
    b = cursor.fetchall()
    for nome in b:
        print(f'{nome[0]} - {nome[1]}')
      
        

def inserirFuncionario():
    novoFuncionarioNome = input("Digite o Nome do novo Funcionario: ")
    novoFuncionarioSalario = input("Digite o Salario do novo Funcionario: ")
    novoFuncionarioCargo = input("Digite o Cargo do novo Funcionario: ")
    novoFuncionarioDepartamento = input("Digite o Departamento do novo Funcionario: ")

    cursor.execute(f'''
    insert into "Funcionario" 
    values (default,'{novoFuncionarioNome}', '{novoFuncionarioSalario}', '{novoFuncionarioCargo}', '{novoFuncionarioDepartamento}')''')
    conn.commit()


def inserirDepartamento():
    os.system('cls')
    novoDepartamentoNome = input("Digite o Nome do novo Departamento: ")

    cursor.execute(f'''
    insert into "Departamento"
    values (default,'{novoDepartamentoNome}')
    
    ''')

    print(f'Departamento {nome[1]} cadastrado com sucesso!')

    conn.commit()

try:
    conn = psycopg2.connect(dbname = "Empresa" ,host = "localhost", port = "5432", user = "postgres", password = "postgres" )
    cursor = conn.cursor()


   # Código para verificar tabelas que existem no seu DB
    cursor.execute('''
    SELECT table_name
  FROM information_schema.tables
 WHERE table_schema='public'
   AND table_type='BASE TABLE';
    ''') 

    resultado = cursor.fetchall()
    controle = False

    for nome in resultado:
        if nome[0] == 'Funcionario':
            controle = True
        # else:
        #     controle = False

    if controle == False:
        cursor.execute(criartabelafuncionario())
        conn.commit()
        print("Tabela Funcionario foi criada com sucesso.")


    for nome in resultado:
        if nome[0] == 'Departamento':
            controle = True
        # else:
        #     controle = False   

    if controle == False:
        cursor.execute(criartabeladepartamento())
        conn.commit()
        print("Tabela Departamento foi criada com sucesso.")

except(Exception,psycopg2.Error) as error:
    print("Ocorreu um erro!", error)

while True:
    try:
        print('''
                Menu
        1 - Ver Funcionarios
        2 - Ver Departamento
        3 - Inserir Funcionario
        4 - Inserir Departamento

        0 - SAIR!
        
        
        ''')

        a = input('> ')

        match a:
            case '1':
                verFuncionarios()
                input()
            case '2':
                verDepartamento()
            case '3':
                inserirFuncionario()
            case '4':
                inserirDepartamento()
            case '0':
                cursor.close()
                conn.close()
                break


    except(Exception,psycopg2.Error)as error:
        print('Ocorreu um erro!', error)
        