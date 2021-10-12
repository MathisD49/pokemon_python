import random

from pokemon import Pokemon
from pokeball import Pokeball

class Game:
    def __init__(self, pokemon_liste, inventaire_objets, nb_spawn):
        self.pokemon_liste = pokemon_liste
        self.total_percent_pokemon = 0
        self.calcul_total_percent()
        self.generation = []
        self.percent_data = []
        self.nb_spawn = nb_spawn
        self.inventaire_pokemon = []
        self.inventaire_objets = inventaire_objets
        self.solde_pokedollars = 0
        self.verif = 0

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


    def combat(self, pokemon_joueur, pokemon_sauvage):
        ratio1 = pokemon_joueur.attaque / pokemon_joueur.defense
        ratio2 = pokemon_sauvage.attaque / pokemon_sauvage.defense
        total = ratio1+ratio2

        rdm = random.randint(0, round(total))
        rdm_pokedollars = random.randint(0, 2000)

        if rdm >= 0 and rdm <= ratio1:
            self.solde_pokedollars += rdm_pokedollars
            print("Vous avez gagné")
        else:
            print("Vous avez perdu")

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

a = Game(my_pokemon_list, my_pokeball_list, 1)
a.spawn()
for i in a.generation:
    print(i.name)
a.calcul_percent()
# a.combat(my_pokemon_list[1], my_pokemon_list[0])
my_pokeball_list[2].nb = 500
a.attraper()
print(a.inventaire_pokemon[0].name)