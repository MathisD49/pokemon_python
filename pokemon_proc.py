# 1 - créer une liste des pokémons, incluant une chance de spawn (0% - 100%) 
# 2 - créer une méthode spwan, qui, en fonction de la chance de spawn, fait spawn un pokémon (affiche son nom)
# 3 - faire spawn 10000 pokémons, calculer le % de chaque pokémon spawn
# 4 - comparer le % de spawn avec la chance de spawn du pokémon. Afficher pour chaque pokémon spawn,
# s'il y en a eu + ou - que la proba de spawn initiale

# 5 - Créer les pokeball (30%), superball (50%), hyperball (70%), masterball (100%). Mettre un % de chance d'attraper le pokemon pour chacune.

# 6 - Ajouter une "résistance" à chaque pokemon, entre 0 et 50%. La résistance est la diminution de la proba d'attraper les pokémons.
# Attention, la masterball de ne prend pas en compte la resistance.

# 7 - Mettre en place un inventaire des objets obtenus :
#       -> 1 inventaire pokemon
#       -> 1 inventaire pokeballs

# 8 - Ajouter des stats par pokémon (attaque / défense)
# 9 - Mettre en place les combats (pokemon_1 vs pokemon_2) :
#       - ratio1 = attaque_pokemon_1 / defense_pokemon_1
#       - ratio2 = attaque_pokemon_2 / defense_pokemon_2
#       - gagnant = random de 0 à somme(ratio1, ratio2). (meme principe que % spawn)

# 10 - Mettre en place les pokedollars ($). Chaque combat gagné rapporte entre 1 et 2000 pokedollars

# 11 - Ajouter un shop, avec les prix suivants : 
#       -> pokeball : 200$
#       -> superball : 600$
#       -> hyperball : 1 200$
#       -> masterball : 50 000$

# 12 - Mettre en place le tout dans un programme en CLI, avec un menu : 
#       -> shop
#       -> spawn (entraine capture OU combat (combat entraine le choix d'un de vos pokémon qui va combattre) )
#       -> inventaire objets
#       -> inventaire pokemon

# TODO:
# - ne pas mettre de pokemon 2 dans combat, juste demander pokemon utilisateur et faire appel à "génération"

import random

# --------------- CONSTANT -----------------
NB_SPAWN = 1
RDM_MIN = 0

# --------------- VARIABLE -----------------
total_percent_pokemon = 0
generation = []
nb_pokedollars = 600


pokemon_list = [
    {
        'name': 'a',
        'percent_spawn': 50,
        'percent_resistance': 5,
        'attaque': 10,
        'defense': 10
    },
    {
        'name': 'b',
        'percent_spawn': 30,
        'percent_resistance': 15,
        'attaque': 30,
        'defense': 10
    },
    {
        'name': 'c',
        'percent_spawn': 10,
        'percent_resistance': 50,
        'attaque': 50,
        'defense': 30
    },
    {
        'name': 'd',
        'percent_spawn': 80,
        'percent_resistance': 15,
        'attaque': 60,
        'defense': 60
    },
    {
        'name': 'e',
        'percent_spawn': 60,
        'percent_resistance': 20,
        'attaque': 30,
        'defense': 50
    },
]

pokeball_list = [
    {
        'name': 'pokeball',
        'percent': 30,

    },
        {
        'name': 'superball',
        'percent': 50,

    },
        {
        'name': 'hyperball',
        'percent': 70

    },
        {
        'name': 'masterball',
        'percent': 100

    },
]

inventaire_objets = [
        {
        'name': 'pokeball',
        'percent': 30,
        'nb': 3

    },
        {
        'name': 'superball',
        'percent': 50,
        'nb': 0

    },
        {
        'name': 'hyperball',
        'percent': 70,
        'nb': 0

    },
        {
        'name': 'masterball',
        'percent': 100,
        'nb': 0

    },
]

inventaire_pokemon = [
    {
        'name': 'a',
        'percent_spawn': 50,
        'percent_resistance': 5,
        'attaque': 10,
        'defense': 10
    },
]

for i in pokemon_list:
    total_percent_pokemon += i['percent_spawn']

def spawn():
    for _i in range(NB_SPAWN):
        rdm = random.randint(RDM_MIN, total_percent_pokemon)
        nb = 0
        for j in range(len(pokemon_list)):
            if j == 0:
                nb += pokemon_list[j]['percent_spawn']
                if rdm > RDM_MIN and rdm <= nb:
                    generation.append(pokemon_list[j])
            else:
                nb += pokemon_list[j]['percent_spawn']
                if rdm > (nb - pokemon_list[j]['percent_spawn']) and rdm <= nb:
                    generation.append(pokemon_list[j])

def get_percent():
    percent_data = []
    for i in pokemon_list:
        name_count = generation.count(i['name'])
        percent_data.append((name_count*100)/NB_SPAWN)

    return percent_data

def verify_percent():
    result = get_percent()
    for i in range(len(pokemon_list)):
        real_percent = (pokemon_list[i]['percent_spawn']*100)/total_percent_pokemon
        if real_percent > result[i]:
            print(pokemon_list[i]['name'], "apparait moins de fois que prévu (", str(result[i]), " au lieu de ", str(real_percent), ")")
        elif real_percent < result[i]:
            print(pokemon_list[i]['name'], "apparait plus de fois que prévu (", str(result[i]), " au lieu de ", str(real_percent), ")")
        else:
            print(pokemon_list[i]['name'], "apparait autant de fois que prévu (", str(result[i]), ")")

def combat(pokemon_joueur, pokemon_sauvage):
    ratio1 = pokemon_joueur['attaque'] / pokemon_joueur['defense']
    ratio2 = pokemon_sauvage['attaque'] / pokemon_sauvage['defense']
    total = ratio1+ratio2
    rdm = random.randint(0, total)

    if rdm >= 0 and rdm <= ratio1:
        return True
    else:
        return False

def resultat_combat(result, pokedollars_joueur):
    rdm = random.randint(0, 2000)
    if result:
        print("Vous avez gagné le combat")
        pokedollars_joueur += rdm
    else:
        print("Vous avez perdu")

def attraper():
    spawn()
    print("un ", generation[0]['name'], " apparait !")
    verif = 0
    while verif != 1:
        pokeball = input("Quelle pokeball voulez-vous utiliser ? : ")
        if pokeball == "quitter":
            verif = 1
        else:
            for i in inventaire_objets:
                if i['name'] == pokeball and i['nb'] > 0:
                    nouveau_percent = (generation[0]['percent_resistance']*i['percent'])/100
                    rdm = random.randint(0, 100)
                    if rdm >= 0 and rdm <= nouveau_percent:
                        pokemon_list.append(generation[0])
                        i['nb'] -= 1
                        generation[0] = []
                        print("Vous avez attrapé le pokemon !")
                        verif = 1
                    else:
                        i['nb'] -= 1
                        print("vous ne l'avez pas attrapé")
                else:
                    print("vous ne disposez pas de cette pokeball")

def shop(pokedollars_joueur):
    content = [ 
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

    verif = 0

    # PROBLEME BOUCLE SUR TOUS LES OBJETS ET NE S'ARRETE PAS SUR LA BALL QU'ON VEUT
    # mais pokeball voulu bien dans l'inventaire
    while verif != 1:
        achat = input("Que voulez-vous acheter ? : ")
        for item in content:
            if achat == item['name']:
                pokedollars_joueur -= item['price']
                for i in pokeball_list:
                    if i['name'] == item['name']:
                        inventaire_objets.append(i)
                        print("Vous avez acheté une ", achat, " pour ", item['price'])
                verif += 1
            elif achat == "quitter":
                verif += 1
            else:
                print("Nous n'avons pas ça dans notre shop")

    # while verif != 1:
    #     for item in content:
    #         print(item)
    #     verif += 1

def menu():
    while True:
        print("1 - shop")
        print("2 - spawn")
        print("3 - inventaire objet")
        print("4 - inventaire pokemon")

        choix = input("Que choisissez-vous ? : ")

        if choix == "1":
            shop(nb_pokedollars)
        elif choix == "2":
            while True:
                print("1 - combattre")
                print("2 - attraper")
                choix_spawn = input("Que voulez vous : ")
                if choix_spawn == "1":
                    resultat_combat(combat(inventaire_pokemon[0], generation[0]), nb_pokedollars)
                elif choix_spawn == "2":
                    attraper()
                elif choix_spawn == "quitter":
                    break
                else:
                    print("mauvaise input")
        elif choix == "3":
            print(inventaire_objets)
            # faire une fonction avec un formatage du texte
        elif choix == "4":
            print(inventaire_pokemon)
            # faire une fonction avec un formatage du texte
        elif choix == "quitter":
            print("Quitter !")
            break
        else:
            print("mauvaise input !")

menu()

# spawn()
# print(generation)
# verify_percent()