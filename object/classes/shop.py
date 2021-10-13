class Shop:
    def __init__(self, content, inventaire):
        self.content = content
        self.inventaire = inventaire
    
    def get_content(self):
        return self.content

    def get_price(self, name):
        for i in self.content:
            if i.name == name:
                return i.price

    def buy(self, pokeball_name, nb_pokedollars):
        for i in self.inventaire:
            if self.inventaire.get_name(i) == pokeball_name:
                for j in self.content:
                    if pokeball_name == j['name']:
                        if nb_pokedollars < j['price']:
                            print("vous n'avez pas assez de pokedollars")
                    else:
                        self.inventaire.add_nb(i, 1)
                        self.inventaire.withdraw_pokedollars(j['price'])
                        print("Pokeball acheté !")