# Database Agence de location - Python + MySQL Connector

import mysql.connector
# Création de la database
#mydb = mysql.connector.connect(
#  host="localhost",
#  user="student",
#  password="mdpSQL2021",
#)
#mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE agence_python")

mydb = mysql.connector.connect(
  host="localhost",
  user="student",
  password="mdpSQL2021",
  database='agence_python'
)
mycursor = mydb.cursor()

# Création des tables

#mycursor.execute("CREATE TABLE Type (type VARCHAR(10) PRIMARY KEY, base_loyer SMALLINT)")

#mycursor.execute("CREATE TABLE City (city_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, city_name VARCHAR(40), nombre_habitants INT, distance_agence SMALLINT)")

#mycursor.execute("CREATE TABLE Logement (logement_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, adresse VARCHAR(40), size SMALLINT, quartier VARCHAR(30), loyer INT, type VARCHAR(10), FOREIGN KEY(type) REFERENCES Type(type))")
#mycursor.execute("ALTER TABLE Logement ADD COLUMN city_id INT ")
#mycursor.execute("ALTER TABLE Logement ADD FOREIGN KEY(city_id) REFERENCES City(city_id) ")

#mycursor.execute("CREATE TABLE civilite (civilite VARCHAR(15) PRIMARY KEY, sexe CHAR(1))")

#mycursor.execute("CREATE TABLE client (client_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(30), prenom VARCHAR(30), date_of_birth DATE, civilite VARCHAR(15), FOREIGN KEY(civilite) REFERENCES civilite(civilite) )")

#mycursor.execute("CREATE TABLE telephone (telephone VARCHAR(10) PRIMARY KEY, client_id INT, FOREIGN KEY (client_id) REFERENCES client(client_id))")

#mycursor.execute("CREATE TABLE contrat (contrat_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, debut_contrat DATE NOT NULL, fin_contrat DATE, logement_id INT, client_id INT, FOREIGN KEY(logement_id) REFERENCES Logement(logement_id), FOREIGN KEY(client_id) REFERENCES client(client_id))")

#Afficher toutes les tables de la database
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)

#Inserer des données dans la table Type
sql = "INSERT INTO Type (type, base_loyer) VALUES (%s, %s)"
val = [('T0', 10),('T1', 20),('T2', 30),('Maison', 50),('Peniche', 100)]

#mycursor.executemany(sql, val)

#mydb.commit()

#Print la table Type
mycursor.execute("SELECT * FROM Type")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#Inserer des données dans la table City
sql = "INSERT INTO City (city_name, nombre_habitants, distance_agence) VALUES(%s, %s, %s)"
val = [
  ('Lille', 232741, 0),
  ('Croix', 21239, 11),
  ('Wambrechies', 10162, 9),
  ('Lomme', 27483, 6),
  ('Englos', 602, 9)
]
#mycursor.executemany(sql, val)

#mydb.commit()

#Print la table City
mycursor.execute("SELECT * FROM City")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#Inserer des données dans la table Logement
sql = "INSERT INTO Logement (adresse, size, quartier, loyer, type, city_id) VALUES (%s, %s, %s, %s, %s, %s)"
val = [
  ('4 rue solferino', 42, 'solferino', 480, 'T1', 1),
  ('12 rue basse', 56, 'centre', 350, 'T0', 2),
  ('65 rue du moulin', 80, 'est', 450, 'T2', 5),
  ('78 avenue du general leclerc', 180, 'sud', 750, 'Maison', 4),
  ('8 quai nord', 150, 'quai', 780, 'Peniche', 3)
]
#mycursor.executemany(sql, val)

#mydb.commit()

#Print la table Logement
mycursor.execute("SELECT * FROM Logement")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#Inserer des données dans la table civilite
sql = "INSERT INTO civilite (civilite, sexe) VALUES (%s, %s)"
val = [
  ('Monsieur', 'H'),
  ('Madame', 'F')
]
#mycursor.executemany(sql, val)

#mydb.commit()

#Print la table civilite
mycursor.execute("SELECT * FROM civilite")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#Inserer des données dans la table client
sql = "INSERT INTO client (nom, prenom, date_of_birth, civilite) VALUES (%s, %s, %s, %s)"
val = [
  ('Doe', 'John', '2000-09-09', 'Monsieur'),
  ('Light', 'Gary', '2000-09-01', 'Monsieur'),
  ('Doe', 'Jane', '2000-10-09', 'Madame'),
  ('Starch', 'Floyd', '2000-05-09', 'Monsieur'),
  ('Dupont', 'Steve', '2000-09-05', 'Monsieur')
]
#mycursor.executemany(sql, val)

#mydb.commit()

#Print la table client
mycursor.execute("SELECT * FROM client")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#Inserer des données dans la table telephone
sql = "INSERT INTO telephone (telephone, client_id) VALUES (%s, %s)"
val = [(3321333333, 1),
       (3321333322, 2),
       (3321333312, 3),
       (3321333355, 4),
       (3321333368, 5)
       ]
#mycursor.executemany(sql, val)

#mydb.commit()

#Print la table telephone
mycursor.execute("SELECT * FROM telephone")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#Inserer des données dans la table contrat
sql = "INSERT INTO contrat (debut_contrat, fin_contrat, logement_id, client_id) VALUES (%s, %s, %s, %s)"
val = [('2021-01-01', '2021-12-31', 1, 1),
       ('2020-01-01', '2020-12-31', 2, 2),
       ('2021-01-12', '2021-12-31', 3, 4),
       ('2021-02-01', '2021-12-31', 4, 3),
       ('2021-01-01', '2021-12-31', 5, 5)
       ]
#mycursor.executemany(sql, val)

#mydb.commit()

#Print la table contrat
mycursor.execute("SELECT * FROM contrat")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

##Modifier les données
sql = "UPDATE Type SET base_loyer=0 WHERE type='T0' "
#mycursor.execute(sql)
#mydb.commit()

sql = "UPDATE City SET nombre_habitants = 612 WHERE city_name='Englos' "
#mycursor.execute(sql)
#mydb.commit()

sql = "UPDATE Logement SET adresse='4 rue du changement' WHERE logement_id=1 "
#mycursor.execute(sql)
#mydb.commit()

sql = "UPDATE contrat SET fin_contrat='2021-03-03' WHERE client_id=4 "
#mycursor.execute(sql)
#mydb.commit()

sql = "UPDATE client SET nom='Delelis' WHERE client_id=5 "
#mycursor.execute(sql)
#mydb.commit()

sql = "UPDATE civilite SET sexe='Y' WHERE civilite='Monsieur' "
#mycursor.execute(sql)
#mydb.commit()

sql = "UPDATE telephone SET telephone=3344444444 WHERE client_id = 3 "
#mycursor.execute(sql)
#mydb.commit()

#Print la table Type
mycursor.execute("SELECT * FROM Type")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#Print la table City
mycursor.execute("SELECT * FROM City")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#Print la table Logement
mycursor.execute("SELECT * FROM Logement")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
#Print la table civilite
mycursor.execute("SELECT * FROM civilite")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
#Print la table client
mycursor.execute("SELECT * FROM client")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
#Print la table telephone
mycursor.execute("SELECT * FROM telephone")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
#Print la table contrat
mycursor.execute("SELECT * FROM contrat")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#Supprimer des données
sql = "DELETE FROM telephone WHERE client_id=1;"
mycursor.execute(sql)
mydb.commit()
#Print la table telephone
mycursor.execute("SELECT * FROM telephone")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

