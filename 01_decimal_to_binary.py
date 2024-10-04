"""
DECIMAL A BINARIO
Crea un programa se encargue de
transformar un número decimal a binario.
"""

def decimal_to_binary(decimal):

    # Verificamos que el número sea un entero no negativo
    if not isinstance(decimal, int) or decimal < 0:
        raise ValueError("El número debe ser un entero no negativo")
    
    # Usamos la función interna bin()
    return bin(decimal)[2:]

# Ejemplo de uso:
try:
    print(decimal_to_binary(387))
except ValueError as e:
    print(e)