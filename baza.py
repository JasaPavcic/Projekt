import sqlite3

connection = sqlite3.conect("BlackJack.db")

cursor = connection.cursor()


tabela = """ CREATE TABLE IF NOT EXISTS
uporabnik(uporabnikov_id INTEGER PRIMARY KEY, ime TEXT, priimek TEXT, denar FLOAT) """

cursor.execute(tabela)


cursor.execute("INSERT INTO uporabnik VALUES()")

cursor.execute("SELECT * FROM uporabnik")

podatki = cursor.fetchall()
print(podatki)

