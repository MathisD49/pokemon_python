import random

from pokemon import Pokemon
from pokeball import Pokeball

class Game:
    def __init__(self, pokemon_liste):
        self.pokemon_liste = pokemon_liste
        self.total_percent_pokemon = 0
        self.calcul_total_percent()
        self.generation = []

    def calcul_total_percent(self):
        for i in self.pokemon_liste:
            self.total_percent_pokemon += i.percent_spawn

    def spawn(self, nb_spawn):
        for _i in range(nb_spawn):
            rdm = random.randint(0, self.total_percent_pokemon)
            nb = 0
            for j in range(len(self.pokemon_liste)):
                if j == 0:
                    if rdm > 0 and rdm <= nb:
                        self.generation.append(self.pokemon_liste[j])
                else:
                    nb += self.pokemon_liste[j].percent_spawn
                    if rdm > (nb - self.pokemon_liste[j].percent_spawn) and rdm <= nb:
                        self.generation.append(self.pokemon_liste[j])

my_pokemon_list = [
    Pokemon('a', 50, 5, 10, 10),
    Pokemon('b', 30, 15, 30, 10),
    Pokemon('c', 10, 50, 50, 30),
    Pokemon('d', 80, 15, 60, 60),
    Pokemon('e', 60, 20, 30, 50),
]


a = Game(my_pokemon_list)
a.spawn(100)
for i in a.generation:
    print(i.name)
