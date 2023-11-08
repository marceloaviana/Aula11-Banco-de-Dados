import sqlite3

# Conectar ou criar o banco de dados
conn = sqlite3.connect('alunos_python.db')

# Criar uma tabela
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS alunos (id INTEGER PRIMARY KEY, nome TEXT, nota REAL)')

# Inserir dados
cursor.execute('INSERT INTO alunos (id, nome, nota) VALUES (1, "João", 8.5)')
cursor.execute('INSERT INTO alunos (id, nome, nota) VALUES (2, "Maria", 6.5)')
cursor.execute('INSERT INTO alunos (id, nome, nota) VALUES (3, "Joaquim", 5.5)')

# Consultar dados
cursor.execute('SELECT * FROM alunos WHERE id = 1')
#cursor.execute('SELECT * FROM alunos')
aluno = cursor.fetchall()
for linha in aluno:
    print(linha)

# Atualizar dados
cursor.execute("UPDATE alunos SET nota = 7.5 WHERE id = 1")
cursor.execute("UPDATE alunos SET nome = 'Luca - alterado' WHERE id = 1")

cursor.execute('SELECT * FROM alunos WHERE id = 1')
aluno = cursor.fetchall()
for linha in aluno:
    print(linha)

# Apagar dados
cursor.execute('DELETE from alunos WHERE id = 2')
cursor.execute('SELECT * FROM alunos')
aluno = cursor.fetchall()
for linha in aluno:
    print(linha)

# Confirmar e fechar a conexão
conn.commit()
conn.close()

# fim