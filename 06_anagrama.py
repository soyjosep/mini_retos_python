"""
ANAGRAMAS
Comprueba si dos cadenas
de texto son anagramas.
"""

def are_anagramas(string1, string2):
    return sorted(string1.lower()) == sorted(string2.lower())

print(are_anagramas("Roma", "Amor"))
print(are_anagramas("Amiga", "Magia"))
print(are_anagramas("Hola", "Mundo"))