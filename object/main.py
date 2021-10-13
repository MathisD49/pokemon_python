from classes.game import Game
from classes.pokemon import Pokemon
from classes.pokeball import Pokeball

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