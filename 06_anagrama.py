"""
ANAGRAMAS
Comprueba si dos cadenas
de texto son anagramas.
"""

def son_anagramas(cadena1, cadena2):
    # Eliminar espacios y convertir a minúsculas
    cadena1 = cadena1.replace(" ", "").lower()
    cadena2 = cadena2.replace(" ", "").lower()
    # Comparar las letras ordenadas
    return sorted(cadena1) == sorted(cadena2)

# Ejemplo de uso
cadena1 = input("Ingresa la primera palabra: ")
cadena2 = input("Ingresa la segunda palabra: ")

if son_anagramas(cadena1, cadena2):
    print("Las palabras son anagramas.")
else:
    print("Las palabras no son anagramas.")