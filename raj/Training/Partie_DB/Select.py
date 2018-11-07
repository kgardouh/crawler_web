#import os #Pour Windows
import sqlite3

connection = sqlite3.connect("baseDoc.db")
cursor = connection.cursor()

cursor.execute('select * from Theme')
#print(cursor.fetchone()[1])
print(cursor.fetchall())

connection.close()
#os.system("pause")#Pour Windows
