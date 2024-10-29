"""
LISTA POKÉMON
Lista los 151 primeros Pokémon
utilizando la PokéAPI.
"""

import requests
def listar_pokemons(limite=151):
    url = f"https://pokeapi.co/api/v2/pokemon?limit={limite}"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        for index, pokemon in enumerate(datos["results"], start=1):
            print(f"{index}. {pokemon['name'].capitalize()}")
    else:
        print("No se pudo obtener la lista de pokémon.")

# Ejemplo de uso
listar_pokemons()