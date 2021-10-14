import sqlite3

# création d'une base de donnée pour une nouvelle sauvegarde
# suppression de la base de donnée des sauvegardes
# insertion des nouvelles données dans la base lors des sauvegardes en fin de jeu
# transfert des données de la base dans le jeu si le joueur prend une sauegarde

class BDD:
    def __init__(self, path_bdd):
        self.path_bdd = path_bdd
        self.db_conn
        self.cursor = self.db_conn.cursor()

    # ---------- CREATION ----------
    def create_database(self):
        try:
            self.db_conn = sqlite3.connect(self.path_bdd)
            self.create_pokemon_table()
            self.create_pokeball_table()
            self.create_money_table()
        except sqlite3.Error as Error:
            print("Error : ", Error)

    def create_pokemon_table(self):
        query = """CREATE TABLE IF NOT EXIST pokemon(
                    id INT PRIMARY KEY,
                    name VARCHAR(50) NOT NULL,
                    percent_spawn INT NOT NULL,
                    percent_resistance INT NOT NULL,
                    attack INT NOT NULL,
                    defense INT NOT NULL);"""

        self.cursor.execute(query)
        self.db_conn.commit()
        self.cursor.close()

    def create_pokeball_table(self):
        query = """CREATE TABLE pokeball(
                    id INT PRIMARY KEY,
                    name VARCHAR(50) NOT NULL,
                    percent INT NOT NULL,
                    nb INT NOT NULL);"""

        self.cursor.execute(query)
        self.db_conn.commit()
        self.cursor.close() 

    def create_pokedollars_table(self):
        # cursor = self.db_conn.cursor()
        query = """CREATE TABLE pokedollars(
                    id INT PRIMARY KEY,
                    nb INT NOT NULL);"""

        self.cursor.execute(query)
        self.db_conn.commit()
        self.cursor.close()

    # ---------- SUPPRESSION ----------
    def delete_database(self):
        try:
            self.db_conn = sqlite3.connect(self.path_bdd)
            self.delete_pokemon_table()
            self.delete_pokeball_table()
            self.delete_money_table()
        except sqlite3.Error as Error:
            print("Error : ", Error)

    def delete_pokemon_table(self):
        # cursor = self.db_conn.cursor()
        query = """DROP TABLE IF EXISTS pokemon;"""
        self.cursor.execute(query)
        self.db_conn.commit()
        self.cursor.close()

    def delete_pokeball_table(self):
        # cursor = self.db_conn.cursor()
        query = """DROP TABLE IF EXISTS pokeball;"""
        self.cursor.execute(query)
        self.db_conn.commit()
        self.cursor.close()

    def delete_pokedollars_table(self):
        # cursor = self.db_conn.cursor()
        query = """DROP TABLE IF EXISTS pokedollars;"""
        self.cursor.execute(query)
        self.db_conn.commit()
        self.cursor.close()
    
    # ---------- INSERTION ----------
    def insert_pokemon(self, pokemon):
        query = "INSERT INTO pokemon (name, percent_spawn, percent_resistance, attack, defense) VALUES (?, ?, ?, ?, ?);"
        self.cursor.execute(query, (pokemon.name, pokemon.percent_spawn, pokemon.percent_resistance, pokemon.attack, pokemon.defense))
        self.db_conn.commit()
        self.cursor.close()

    def insert_pokeball(self, pokeball):
        query = "INSERT INTO pokeball (name, percent, nb) VALUES (?, ?, ?);"
        self.cursor.execute(query, (pokeball.name, pokeball.percent, pokeball.nb))
        self.db_conn.commit()
        self.cursor.close()

    def insert_pokedollars(self, pokedollars):
        query = "INSERT INTO pokeball (nb) VALUES (?);"
        self.cursor.execute(query, (pokedollars.nb))
        self.db_conn.commit()
        self.cursor.close()

    # ---------- RECUPERATION ----------
    def recovery_pokemon(self):
        list_pokemon = []

        query = "SELECT name, percent_spawn, percent_resistance, attack, defense FROM pokemon;"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        for row in rows:
            list_pokemon.append(row)

        self.cursor.close()

        return list_pokemon

    def recovery_pokeball(self):
        list_pokeball = []

        query = "SELECT name, percent, nb FROM pokeball;"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        for row in rows:
            list_pokeball.append(row)

        self.cursor.close()

        return list_pokeball

    def recovery_pokedollars(self):
        query = "SELECT nb FROM pokedollars;"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        self.cursor.close()

        return rows
