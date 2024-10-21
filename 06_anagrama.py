"""
ANAGRAMAS
Comprueba si dos cadenas
de texto son anagramas.
"""

import string

def es_anagrama(cadena1, cadena2):
    """ 
    Comprueba si dos cadenas de texto son anagramas.

    Parámetros:
    cadena1 (str): Primera cadena de texto.
    cadena2 (str): Segunda cadena de texto.
    
    Retorna:
    bool: true si las cadenas son anagramas, False en caso contrario.
    """
    # Convertir a minúsculas, y eliminar espacios y puntuación
    traductor = str.maketrans('', '', string.punctuation + string.whitespace)
    cadena1_limpia = cadena1.lower().translate(traductor)
    cadena2_limpia = cadena2.lower().translate(traductor)

    # Contar la frecuencia de cada letra
    return sorted(cadena1_limpia) == sorted(cadena2_limpia)

def main():
    print("Comprobador de Anagramas")
    cadena1 = input("Ingrese la primera cadena de texto: ")
    cadena2 = input("Ingrese la segunda cadena de texto: ")

    if es_anagrama(cadena1, cadena2):
        print("Las cadenas son anagramas.")
    else:
        print("Las cadenas no son anagramas.")

if __name__ == "__main__":
    main()