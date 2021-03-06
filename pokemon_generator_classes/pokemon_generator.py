import random
from pokemon_classes.pokemon import Pokemon
from api_class.API import get_pokemon_data


class PokemonGenerator:
    def __init__(self, pokemon_pool, spawnPoint={"x": 0, "y": 0}):
        self.pokemon_pool = pokemon_pool
        self.defaultSpawn = spawnPoint

    def get_random_pokemon_from_pool(self):
        pokemon_identifier_index = random.randint(
            0, len(self.pokemon_pool) - 1)
        pokemon_identifier = self.pokemon_pool[pokemon_identifier_index]

        return get_pokemon_data(pokemon_identifier)

    def generate_pokemon(self, number_of_pokemon):
        pokemon_data = [self.get_random_pokemon_from_pool()
                        for x in range(number_of_pokemon)]

        return list(map(lambda x, y: Pokemon(x, {"x": y, "y": y}), pokemon_data, range(number_of_pokemon)))
