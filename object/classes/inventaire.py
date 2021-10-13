class Inventaire:
    def __init__(self, pokemon, pokeball, pokedollars):
        self.pokemon = pokemon
        self.pokeball = pokeball
        self.pokedollars = pokedollars

    # ---------- POKEMON ----------
    def get_pokemon_list(self):
        return self.pokemon

    def add_pokemon(self, pokemon):
        self.pokemon.append(pokemon)

    # ---------- POKEBALL ----------
    def get_pokeball_list(self):
        return self.pokeball

    def get_name(self, objet):
        return objet.name

    def get_nb(self, objet):
        return objet.nb

    def add_nb(self, objet, nb):
        objet.nb += nb

    def remove_nb(self, objet, nb):
        objet.nb -= nb

    # ---------- POKEDOLLARS ----------
    def get_pokedollars(self):
        return self.pokedollars

    def add_pokedollars(self, nb):
        self.pokedollars += nb

    def withdraw_pokedollars(self, nb):
        self.pokedollars -= nb
    
