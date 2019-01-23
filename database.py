import sqlite3

class Base_donnee:
    def __init__(self):
       self.connection = 0
       self.cursor = 0
       self.connection = sqlite3.connect("baseDoc.db")
       self.cursor = self.connection.cursor()
       self.lesvaleurs = []
       self.urlRecu = ""
       self.idTheme = ""
       self.NumDoc = ""
       self.idTheme2 = ""
       self.NumDoc2 = ""
       self.lesvaleurs2 = ""

    def insertion(self, mot1, mot2, url):
       self.lesvaleurs = [mot1, mot2]
       self.urlRecu = url
       self.cursor.execute('''insert into theme(mot, synonyme) values(?,?)''', self.lesvaleurs)
       self.cursor.execute('''insert into documentation(url) values(?)''', (self.urlRecu,))
       
       #remplir la table Appartient
       self.cursor.execute('''select id_Theme from theme where mot =? and synonyme = ?''', self.lesvaleurs)
       self.idTheme = self.cursor.fetchone()
       self.idTheme2 = self.idTheme[0]
      # print(self.idTheme2)

       self.cursor.execute('''select num_Doc from Documentation where url= ?''', (self.urlRecu,))
       self.NumDoc = self.cursor.fetchone()
       self.NumDoc2 = self.NumDoc[0]
      # print(self.NumDoc2)

       self.lesvaleurs2 = [self.idTheme[0], self.NumDoc[0]]
       self.cursor.execute('''insert into Appartient(num_Doc, id_Theme, date) values(?,?,"10/02/2018")''', self.lesvaleurs2)       

       self.connection.commit()
             

       
    def selection(self, mot):
       self.cursor.execute('''select url from Documentation, Appartient, Theme where theme.id_Theme = Appartient.id_Theme and Appartient.num_Doc = Documentation.num_Doc  and Theme.mot = ?''', (mot,))
       return self.cursor.fetchall()
