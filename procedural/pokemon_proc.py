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


import random

# --------------- CONSTANT -----------------
NB_SPAWN = 1
RDM_MIN = 0

# --------------- VARIABLE -----------------
total_percent_pokemon = 0
generation = []
nb_pokedollars = 60000


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
        'nb': 500

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

def pokemon_choice():
    for i in inventaire_pokemon:
        print(str(inventaire_pokemon.index(i)+1), " - ", i['name'])
    
    choix = int(input("Quel pokemon voulez-vous ? : "))

    if choix > len(inventaire_pokemon)+1 or choix < 0:
        print("ce pokemon n'existe pas")
    else:
        return inventaire_pokemon[choix-1]

def pokeball_choice(verif):
        for i in inventaire_objets:
            print(str(inventaire_objets.index(i)+1), " - ", i['name'])
        print("99 - quitter")
        
        choix = int(input("Quel pokeball voulez-vous ? : "))

        if choix > len(inventaire_objets)+1 or choix < 0:
            print("cette pokeball n'existe pas")
        elif choix == 99:
            return 1
        else:
            return inventaire_objets[choix-1]

def combat(pokemon_joueur, pokemon_sauvage):

    ratio1 = pokemon_joueur['attaque'] / pokemon_joueur['defense']
    print(type(ratio1))
    ratio2 = pokemon_sauvage['attaque'] / pokemon_sauvage['defense']
    print(type(ratio2))
    total = ratio1+ratio2
    rdm = random.randint(0, round(total))

    if rdm >= 0 and rdm <= ratio1:
        return True
    else:
        return False

def resultat_combat(result, pokedollars_joueur, pokemon_sauvage):
    rdm = random.randint(0, 2000)
    if result:
        print("Vous avez gagné le combat")
        inventaire_pokemon.append(pokemon_sauvage)
        pokedollars_joueur += rdm
        generation.clear()
    else:
        print("Vous avez perdu")
        generation.clear()

def attraper():
    spawn()
    print("un ", generation[0]['name'], " apparait !")
    verif = 0
    while verif != 1:
        pokeball = pokeball_choice(verif)
        if pokeball['nb'] > 0:
            nouveau_percent = (generation[0]['percent_resistance']*pokeball['percent'])/100
            rdm = random.randint(0, 100)
            if rdm >= 0 and rdm <= nouveau_percent:
                inventaire_pokemon.append(generation[0])
                pokeball['nb'] -= 1
                generation.clear()
                print("Vous avez attrapé le pokemon !")
                verif = 1
            else:
                pokeball['nb'] -= 1
                print("vous ne l'avez pas attrapé")
        else:
            print("Vous n'avez pas cette pokeball")
            
def shop(pokedollars_joueur):
    global nb_pokedollars

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
    while verif != 1:
        pokeball = pokeball_choice(verif)
        if pokeball == None:
            verif += 1
        else:
            for i in inventaire_objets:
                if i['name'] == pokeball['name']:
                    for j in content:
                        if pokeball['name'] == j['name']:
                            if pokedollars_joueur < j['price']:
                                print("pas assez de pokedollars pour l'achat")
                                verif += 1
                            else:
                                i['nb'] += 1
                                nb_pokedollars -= j['price']
                                print("Pokeball acheté !")
                                verif += 1
        

def format_list(liste):
    texte_format = ""

    for i in liste:
        texte_format += "\n-----------------------------\n"
        for key, value in i.items():
            texte_format += "" + str(key) +  " : " + str(value) + "\n"

        texte_format += "-----------------------------"

    return texte_format

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
                    spawn()
                    print(generation)
                    resultat_combat(combat(pokemon_choice(), generation[0]), nb_pokedollars, generation[0])
                elif choix_spawn == "2":
                    attraper()
                elif choix_spawn == "quitter":
                    break
                else:
                    print("mauvaise input")
        elif choix == "3":
            print("\nSolde Pokedollars : ", str(nb_pokedollars))
            print(format_list(inventaire_objets))
            # faire une fonction avec un formatage du texte
        elif choix == "4":
            print(format_list(inventaire_pokemon))
            # faire une fonction avec un formatage du texte
        elif choix == "quitter":
            print("Quitter !")
            break
        else:
            print("mauvaise input !")

menu()