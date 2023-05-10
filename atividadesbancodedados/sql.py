import psycopg2

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


con = Conexao(dbname = "Escola" ,host = "localhost", port = "5432", user = "postgres", password = "postgres" )

def criartabelaAlunos():
    con.manipularBanco('''
    create table "Alunos"(
    "NroMatricula" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "cpf" char(11) not null,
    "nome" varchar(255) not null,
    "endereço" varchar(255) not null,
    "telefone" char(11) not null,
    "ano nascimento" int not null
    )''')

    print("Tabela Alunos criada com sucesso!")


def criartabelaDisciplina():
    con.manipularBanco('''
    create table "Disciplinas"(
    "CodDisciplina" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "nome" varchar(255) not null,
    "CodCurso" int not null
    )''')

    print("Tabela Disciplinas criada com sucesso!")


def criartabelaMatricula():
    con.manipularBanco('''
    create table "Matriculas"(
    "id_matricula" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "NroMatricula" int,
    "CodDisciplina" int,
    "semestre" int not null,
    "ano" int not null,
    "notas" float(2) not null,
    "NroFaltas" int not null,

    CONSTRAINT fk_NroMatricula
      FOREIGN KEY ("NroMatricula")
      REFERENCES "Alunos"("NroMatricula"),

    CONSTRAINT fk_CodDisciplina
      FOREIGN KEY ("CodDisciplina")
      REFERENCES "Disciplinas"("CodDisciplina")
    )''')

    print("Tabela Matriculas criada com sucesso!")

# criartabelaAlunos()
# criartabelaDisciplina()
# criartabelaMatricula()

# TESTES EXERCICIO ------------------------------------------------------------------------------------------------------------

