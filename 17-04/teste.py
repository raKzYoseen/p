import psycopg2

try:
    conn = psycopg2.connect(dbname = "ESCOLA" ,host = "localhost", port = "5432", user = "postgres", password = "postgres" )
    cursor = conn.cursor()

    print("Conectado com sucesso!")

    cursor.execute('''
    create table "Alunos"(
    "ID_Matricula" serial,
    "Nome" varchar(255) Not null,
    "CPF" char(11) Not null,
    "Endereço" varchar(255) default 'Não informado!',
    "Telefone" char(11) default '(xx) x xxxx-xxxx',
    "Ano Nascimento" int,
    Primary Key ("ID_Matricula")
    )
    ''')

    conn.commit()

    conn.close()

except(Exception, psycopg2.Error) as error:
    print ("Ocorreu um erro!", error)
