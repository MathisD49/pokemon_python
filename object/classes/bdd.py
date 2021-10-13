import sqlite3

# création d'une base de donnée pour une nouvelle sauvegarde
# suppression de la base de donnée des sauvegardes
# insertion des nouvelles données dans la base lors des sauvegardes en fin de jeu
# transfert des données de la base dans le jeu si le joueur prend une sauegarde

class BDD:
    def __init__(self, path_bdd):
        self.path_bdd = path_bdd
        self.db_conn

    def create_database(self):
        try:
            self.db_conn = sqlite3.connect(self.path_bdd)
            self.create_pokemon_table()
            self.create_pokeball_table()
            self.create_money_table()
        except sqlite3.Error as Error:
            print("Error : ", Error)

    def create_pokemon_table(self):
        cursor = self.db_conn.cursor()
        query = """CREATE TABLE pokemon(
                    id INT PRIMARY KEY,
                    name VARCHAR(50) NOT NULL,
                    percent_spawn INT NOT NULL,
                    percent_resistance INT NOT NULL,
                    attaque INT NOT NULL,
                    defense INT NOT NULL);"""

        cursor.execute(query)
        self.db_conn.commit()
        cursor.close()

    def create_pokeball_table(self):
        cursor = self.db_conn.cursor()
        query = """CREATE TABLE pokeball(
                    id INT PRIMARY KEY,
                    name VARCHAR(50) NOT NULL,
                    percent INT NOT NULL,
                    nb INT NOT NULL);"""

        cursor.execute(query)
        self.db_conn.commit()
        cursor.close() 

    def create_money_table(self):
        cursor = self.db_conn.cursor()
        query = """CREATE TABLE pokeball(
                    id INT PRIMARY KEY,
                    pokedollars INT NOT NULL);"""

        cursor.execute(query)
        self.db_conn.commit()
        cursor.close()


    
    