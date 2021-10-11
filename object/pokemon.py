from pokemon.procedural.pokemon_proc import spawn


class Pokemon:
    def __init__(self, name, percent_spawn, percent_resistance, attaque, defense):
        self.name = name
        self.percent_spawn = percent_spawn
        self.percent_resistance = percent_resistance
        self.attaque = attaque
        self.defense = defense



