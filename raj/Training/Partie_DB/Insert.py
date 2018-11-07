import sqlite3

connection = sqlite3.connect("baseDoc.db")
cursor = connection.cursor()

lesvaleurs=("Requin","Poisson")
cursor.execute('insert into theme(mot, synonyme) values(?,?)', lesvaleurs)#insertion sécurisé
connection.commit()

connection.close()

