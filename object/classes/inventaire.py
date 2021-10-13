class Inventaire:
    def __init__(self, pokemon, pokeball, pokedollars):
        self.pokemon = pokemon
        self.pokeball = pokeball
        self.pokedollars = pokedollars

    def get_pokemon_list(self):
        return self.pokemon

    def get_pokeball_list(self):
        return self.pokeball

    def add_pokedollars(self, nb):
        self.pokedollars += nb

    def withdraw_pokedollars(self, nb):
        self.pokedollars -= nb
    
