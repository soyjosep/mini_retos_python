"""
INVERSIÓN DE CADENAS
Crea una función que invierta
una cadena de texto.
"""

def invertir_cadena(cadena):
    """
    Invierte una cadena de texto.

    Parámetros:
    cadena (str): La cadena de texto a invertir.

    Retorna:
    str: La cadena invertida.
    """
    return cadena[::-1]

def main():
    print("Inversión de Cadenas de Texto")
    cadena = input("Ingrese una cadena de texto: ")
    cadena_invertida = invertir_cadena(cadena)
    print(f"La cadena invertida es: {cadena_invertida}")

if __name__ == "__main__":
    main()