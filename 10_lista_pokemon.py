"""
LISTA POKÉMON
Lista los 151 primeros Pokémon
utilizando la PokéAPI.
"""

import requests

def obtener_pokemon(limit=151):
    """ 
    Obtiene una lista de nombres de los primeros Pokémon utilizando la PokeAPI.

    Parámetros:
    limit (int): El número de Pokémon a obtener.

    Retorna:
    list: Una lista con los nombres de los Pokémon.
    """
    url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        nombres_pokemon = [pokemon['name'] for pokemon in data['results']]
        return nombres_pokemon
    else:
        print("Error al conectar con la PokéAPI.")
        return[]
    
def main():
        print("Lista de los primeros 151 Pokémon:\n")
        nombres_pokemon = obtener_pokemon()
        for idx, nombre in enumerate(nombres_pokemon, start=1):
             print(f"{idx}. {nombre.capitalize()}")

if __name__ == "__main__":
    main()