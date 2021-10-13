import random

from pokemon import Pokemon
from pokeball import Pokeball

class Game:
    def __init__(self, pokemon_liste, inventaire_objets, content_shop, nb_spawn):
        self.pokemon_liste = pokemon_liste
        self.inventaire_objets = inventaire_objets
        self.content_shop = content_shop
        self.nb_spawn = nb_spawn
        self.generation = []
        self.percent_data = []
        self.inventaire_pokemon = []
        self.total_percent_pokemon = 0
        self.solde_pokedollars = 600
        self.verif = 0
        self.calcul_total_percent()
        self.main_menu()

    def calcul_total_percent(self):
        for i in self.pokemon_liste:
            self.total_percent_pokemon += i.percent_spawn

    def spawn(self):
        for _i in range(self.nb_spawn):
            rdm = random.randint(0, self.total_percent_pokemon)
            nb = 0
            for j in range(len(self.pokemon_liste)):
                if j == 0:
                    nb += self.pokemon_liste[j].percent_spawn
                    if rdm > 0 and rdm <= nb:
                        self.generation.append(self.pokemon_liste[j])
                else:
                    nb += self.pokemon_liste[j].percent_spawn
                    if rdm > (nb - self.pokemon_liste[j].percent_spawn) and rdm <= nb:
                        self.generation.append(self.pokemon_liste[j])

    def calcul_percent(self):
        for i in self.pokemon_liste:
            name_count = 0
            for j in self.generation:
                if j.name == i.name:
                    name_count += 1
            self.percent_data.append((name_count*100)/self.nb_spawn)

        for percent_pokemon in range(len(self.percent_data)):
            real_percent = (self.pokemon_liste[percent_pokemon].percent_spawn*100)/self.total_percent_pokemon
            if real_percent > self.percent_data[percent_pokemon]:
                print(self.pokemon_liste[percent_pokemon].name, "apparait moins de fois que prévu (", str(self.percent_data[percent_pokemon]), " au lieu de ", str(real_percent), ")")
            elif real_percent < self.percent_data[percent_pokemon]:
                print(self.pokemon_liste[percent_pokemon].name, "apparait plus de fois que prévu (", str(self.percent_data[percent_pokemon]), " au lieu de ", str(real_percent), ")")
            else:
                print(self.pokemon_liste[percent_pokemon].name, "apparait autant de fois que prévu (", str(self.percent_data[percent_pokemon]), " au lieu de ", str(real_percent), ")")

    def pokeball_choice(self):
        for i in self.inventaire_objets:
            print(str(self.inventaire_objets.index(i)+1), " - ", i.name)
        print("99 - quitter")
        choix = int(input("Quel pokeball voulez-vous ? : "))

        if choix == 99:
            self.verif += 1
        elif choix > len(self.inventaire_objets)+1 or choix < 0:
            print("cette pokeball n'existe pas")
        else:
            return self.inventaire_objets[choix-1]

    def pokemon_choice(self):
        for i in self.inventaire_pokemon:
            print(str(self.inventaire_pokemon.index(i)+1), " - ", i.name)
            print("99 - quitter")
            choix = int(input("Quel pokeball voulez-vous ? : "))

            if choix == 99:
                self.verif += 1
            elif choix > len(self.inventaire_pokemon)+1 or choix < 0:
                print("cette pokeball n'existe pas")
            else:
                return self.inventaire_pokemon[choix-1]

    def combat(self, pokemon_joueur, pokemon_sauvage):
        ratio1 = pokemon_joueur.attaque / pokemon_joueur.defense
        ratio2 = pokemon_sauvage.attaque / pokemon_sauvage.defense
        total = ratio1+ratio2

        rdm = random.randint(0, round(total))
        rdm_pokedollars = random.randint(0, 2000)

        if rdm >= 0 and rdm <= ratio1:
            self.solde_pokedollars += rdm_pokedollars
            self.generation.clear()
            print("Vous avez gagné")
        else:
            print("Vous avez perdu")
            self.generation.clear()

    def attraper(self):
        self.verif = 0
        self.spawn()
        print(self.generation[0])
        while self.verif != 1:
            pokeball = self.pokeball_choice()

            if pokeball == None:
                break
            elif pokeball.nb > 0:
                nouveau_percent = (self.generation[0].percent_resistance*pokeball.percent)/100
                rdm = random.randint(0, 100)
                if rdm >= 0 and rdm <= nouveau_percent:
                    self.inventaire_pokemon.append(self.generation[0])
                    pokeball.nb -= 1
                    self.generation.clear()
                    print("Vous avez attrapé le pokemon !")
                    self.verif = 1
                else:
                    pokeball.nb -= 1
                    print("Vous ne l'avez pas attrapé")
            else:
                print("Vous n'avez pas cette pokeball")

    def shop(self):
        while self.verif != 1:
            pokeball = self.pokeball_choice()
            if pokeball == None:
                break
            else:
                for i in self.inventaire_objets:
                    if i.name == pokeball.name:
                        for j in self.content_shop:
                            if pokeball.name == j['name']:
                                if self.solde_pokedollars < j['price']:
                                    print("vous n'avez pas assez de pokedollars")
                                else:
                                    i.nb += 1
                                    self.solde_pokedollars -= j['price']
                                    print("Pokeball acheté !")

    def format_texte(self, liste):
        texte_format = ""

        for i in liste:
            texte_format += "\n-----------------------------\n"
            liste_dict = i.__dict__
            for key, value in liste_dict.items():
                texte_format += "" + str(key) +  " : " + str(value) + "\n"
            texte_format += "-----------------------------"

        return texte_format

        # return liste[0].__dict__

    def main_menu(self):
        while True:
            self.verif = 0
            print("Bienvenue dans Pokemon")
            print("1 - Shop")
            print("2 - Spawn")
            print("3 - Inventaire objets")
            print("4 - Inventaire pokemon")
            choix_menu = int(input("Que voulez-vous faire ? : "))

            if choix_menu == 1:
                self.shop()
            elif choix_menu == 2:
                while True:
                    print("1 - Combat")
                    print("2 - Attraper")
                    print("99 - Quitter")
                    choix_spawn = int(input("Un pokemon a spawn que voulez vous faire ? : "))
                    if choix_spawn == 1:
                        pass
                        self.spawn()
                        self.combat(self.pokemon_choice(), self.generation[0])
                    elif choix_spawn == 2:
                        self.attraper()
                    elif choix_spawn == 99:
                        break
                    else:
                        print("Mauvaise input")
            elif choix_menu == 3:
                print("Solde pokedollars : ", str(self.solde_pokedollars))
                print(self.format_texte(self.inventaire_objets))
            elif choix_menu == 4:
                print(self.format_texte(self.inventaire_pokemon))
            elif choix_menu == 99:
                break
            else:
                print("Mauvaise input")

my_pokemon_list = [
    Pokemon('a', 50, 5, 10, 10),
    Pokemon('b', 30, 15, 30, 10),
    Pokemon('c', 10, 50, 50, 30),
    Pokemon('d', 80, 15, 60, 60),
    Pokemon('e', 60, 20, 30, 50),
]

my_pokeball_list = [
    Pokeball('pokeball', 30),
    Pokeball('superball', 50),
    Pokeball('hyperball', 70),
    Pokeball('masterball', 100),
]

shop_content = [ 
    {
        'name': 'pokeball',
        'price': 200
    },
    {
        'name': 'superball',
        'price': 600
    },
    {
        'name': 'hyperball',
        'price': 1200
    },
    {
        'name': 'masterball',
        'price': 50000
    }
]

a = Game(my_pokemon_list, my_pokeball_list, shop_content, 1)
# a.spawn()
# for i in a.generation:
#     print(i.name)
# a.calcul_percent()
# a.combat(my_pokemon_list[1], my_pokemon_list[0])
# my_pokeball_list[2].nb = 500
# a.attraper()
# print(a.inventaire_pokemon[0].name)
# print(a.inventaire_objets[2].nb)

# a.solde_pokedollars = 600

# print(a.solde_pokedollars)
# print(a.inventaire_objets[0].nb)
# a.shop()
# print(a.solde_pokedollars)
# print(a.inventaire_objets[0].nb)