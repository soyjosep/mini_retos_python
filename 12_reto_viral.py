"""
RETO VIRAL 12345678
Simula el reto viral 12345678.
Crea una función que cuente de
1 a 8, eliminando cada vez un
dígito y mostrando un espacio en
blanco en su lugar, de manera
ascendente y descendente.
"""

def reto_viral():
    numero = "12345678"
    
    # Ascendente
    for i in range(len(numero)):
        print(" " * i + numero[i:])
    
    # Punto de unión entre ascendente y descendente
    print(" " * len(numero[:-1]) + numero[-1])  # Último número de la parte ascendente sin salto de línea extra

    # Descendente
    for i in range(len(numero) - 2, -1, -1):
        print(" " * i + numero[i:])

# Ejecutar la función
reto_viral()