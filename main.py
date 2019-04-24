#!/usr/local/bin/python3.7
#import
import sqlite3

# Connexion DB SQLite et curseur
db_connect = sqlite3.connect('pharmacy.db')
db_cursor = db_connect.cursor()

# Creation de table huiles-essentielles
# db_cursor.execute('''CREATE TABLE medicaments (nom, type, pourquoi , comment, duree)''')

# Insert a row of data
db_cursor.execute("INSERT INTO medicaments VALUES ('doliprane','anti douleurs','douleurs','none','maximum 4jours')")

# Save (commit) the changes
db_connect.commit()
db_cursor.close()

# Fonction d'accueil
def hi_there():
      usr_name = input('Comment vous appelez vous ? ')
      usr_ans = input('Bonjour à vous, je suis le chatbot Healpy, enchanté de vous connaître, que puis-je faire pour vous servir ?')
      print ('Je vais vous aider', usr_name)

hi_there()
