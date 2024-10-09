import sqlite3

banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()

cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email)")
cursor.execute("INSERT INTO pessoas VALUES('maria',40,'maria_123@gmail.com')")

banco.commit()
