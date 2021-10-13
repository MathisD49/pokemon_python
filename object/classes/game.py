import random

from classes.pokemon import Pokemon
from classes.pokeball import Pokeball

class Game:
    def __init__(self, pokemon_list, player_inventory, my_shop, nb_spawn):
        self.pokemon_list = pokemon_list
        self.player_inventory = player_inventory
        self.nb_spawn = nb_spawn
        self.generation = []
        self.percent_data = []
        self.total_percent_pokemon = 0
        self.verif = 0
        self.my_shop = my_shop
        self.calculate_total_percent()
        self.main_menu()

    # calcul la somme des pourcentages des pokemons
    def calculate_total_percent(self):
        for i in self.pokemon_list:
            self.total_percent_pokemon += i.percent_spawn

    # fait spawn un certain nombre de pokemon au hasard
    def spawn(self):
        for _i in range(self.nb_spawn):
            rdm = random.randint(0, self.total_percent_pokemon)
            nb = 0
            for j in range(len(self.pokemon_list)):
                nb += self.pokemon_list[j].percent_spawn
                if j == 0:
                    if rdm > 0 and rdm <= nb:
                        self.generation.append(self.pokemon_list[j])
                else:
                    if rdm > (nb - self.pokemon_list[j].percent_spawn) and rdm <= nb:
                        self.generation.append(self.pokemon_list[j])

    # permet de savoir si une pokemon à spawn plus ou moins que le dit son pourcentage
    def calculate_percent(self):
        for i in self.pokemon_list:
            name_count = 0
            for j in self.generation:
                if j.name == i.name:
                    name_count += 1
            self.percent_data.append((name_count*100)/self.nb_spawn)

        for percent_pokemon in range(len(self.percent_data)):
            real_percent = (self.pokemon_list[percent_pokemon].percent_spawn*100)/self.total_percent_pokemon
            if real_percent > self.percent_data[percent_pokemon]:
                print(self.pokemon_list[percent_pokemon].name, "apparait moins de fois que prévu (", str(self.percent_data[percent_pokemon]), " au lieu de ", str(real_percent), ")")
            elif real_percent < self.percent_data[percent_pokemon]:
                print(self.pokemon_list[percent_pokemon].name, "apparait plus de fois que prévu (", str(self.percent_data[percent_pokemon]), " au lieu de ", str(real_percent), ")")
            else:
                print(self.pokemon_list[percent_pokemon].name, "apparait autant de fois que prévu (", str(self.percent_data[percent_pokemon]), " au lieu de ", str(real_percent), ")")

    # méthode pour selectionner quelque chose (pokeball / pokemon)
    def choice_object(self, list_object):
        print("\n")
        for i in list_object:
            print(str(list_object.index(i)+1), " - ", i.name)
        print("99 - quitter")
        choice = int(input("Que voulez-vous ? : "))

        if choice == 99:
            self.verif += 1
            return None
        elif choice > len(list_object)+1 or choice < 0:
            print("Cela n'existe pas")
        else:
            return list_object[choice-1]

    # méthode qui gère la partie combat
    def fight(self, pokemon_player, pokemon_wild):
        if pokemon_player != None:
            ratio1 = pokemon_player.attack / pokemon_player.defense
            ratio2 = pokemon_wild.attack / pokemon_wild.defense
            total = ratio1+ratio2

            rdm = random.randint(0, round(total))
            rdm_pokedollars = random.randint(0, 2000)

            if rdm >= 0 and rdm <= ratio1:
                self.player_inventory.add_pokedollars(rdm_pokedollars)
                print("Vous avez gagné")
            else:
                print("Vous avez perdu")

            self.generation.clear()

    # méthode qui gère la partie pour attraper un pokemon
    def catch(self):
        self.verif = 0
        self.spawn()
        while self.verif != 1:
            pokeball = self.choice_object(self.player_inventory.get_pokeball_list())
            if pokeball == None:
                break
            elif self.player_inventory.get_nb(pokeball) > 0:
                new_percent = self.player_inventory.get_percent(pokeball)
                if self.player_inventory.get_name(pokeball) != "masterball":
                    new_percent = (self.player_inventory.get_percent(pokeball) - (self.generation[0].percent_resistance*self.player_inventory.get_percent(pokeball))/100)
                rdm = random.randint(0, 100)
                if rdm >= 0 and rdm <= new_percent:
                    self.player_inventory.add_pokemon(self.generation[0])
                    self.generation.clear()
                    print("Vous avez attrapé le pokemon !")
                    self.verif = 1
                else:
                    print("Vous ne l'avez pas attrapé")

                self.player_inventory.remove_nb(pokeball, 1)

            else:
                print("Vous n'avez pas cette pokeball")

    # gère la partie shop
    def shop(self):
        while self.verif != 1:
            pokeball = self.choice_object(self.player_inventory.get_pokeball_list())
            if pokeball == None:
                break
            else:
                self.my_shop.buy(self.player_inventory.get_name(pokeball), self.player_inventory.get_pokedollars())

    def main_menu(self):
        while True:
            self.verif = 0
            print("\nBienvenue dans Pokemon")
            print("1 - Shop")
            print("2 - Spawn")
            print("3 - Inventaire objets")
            print("4 - Inventaire pokemon")
            choix_menu = int(input("Que voulez-vous faire ? : "))

            if choix_menu == 1:
                self.shop()
            elif choix_menu == 2:
                while self.verif != 1:
                    print("\n1 - Combat")
                    print("2 - Attraper")
                    print("99 - Quitter")
                    choix_spawn = int(input("Un pokemon a spawn que voulez vous faire ? : "))
                    if choix_spawn == 99:
                        self.verif += 1
                        break
                    elif choix_spawn == 1:
                        pass
                        self.spawn()
                        self.fight(self.choice_object(self.player_inventory.get_pokemon_list()), self.generation[0])
                    elif choix_spawn == 2:
                        self.catch()
                    else:
                        print("Mauvaise input")
            elif choix_menu == 3:
                print("Solde pokedollars : ", str(self.player_inventory.get_pokedollars()))
                print(self.player_inventory.format_text(self.player_inventory.get_pokeball_list()))
            elif choix_menu == 4:
                print(self.player_inventory.format_text(self.player_inventory.get_pokemon_list()))
            elif choix_menu == 99:
                break
            else:
                print("Mauvaise input")