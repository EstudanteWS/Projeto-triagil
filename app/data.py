class Squad:
    def __init__(self, owner, pokemons):
        self.owner = owner
        self.pokemons = pokemons

    def to_dict(self):
        return {
            "owner": self.owner,
            "pokemons": [
                {
                    "id": pokemon["id"],
                    "name": pokemon["name"],
                    "weight": pokemon["weight"],
                    "height": pokemon["height"]
                }
                for pokemon in self.pokemons
            ]
        }
