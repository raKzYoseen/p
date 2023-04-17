import psycopg2

conn = psycopg2.connect(dbname = "17-04-2023" ,host = "localhost", port = "5432", user = "postgres", password = "postgres" )
cursor = conn.cursor()

cursor.execute('''
select * from "Alunos" 
''')

print(cursor.fetchall())


for aluno in cursor.fetchall():
    print (f"{aluno[0]} - {aluno[2]}")


cursor.execute('''


''')