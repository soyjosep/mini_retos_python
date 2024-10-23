"""
INVERSIÓN DE CADENAS
Crea una función que invierta
una cadena de texto.
"""

def invertir_cadena(cadena):
    return cadena[::-1]

# Ejemplo de uso
texto = input("Ingresa una cadena de texto: ")
texto_invertido = invertir_cadena(texto)
print(f"Texto invertido: {texto_invertido}")