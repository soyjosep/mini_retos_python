"""
MEDIA
Calcula la media de un
listado de números.
"""

def calcular_media(numeros):
    """ 
    Calcoula la media de una lista de números.
    
    Parámetros:
    numeros (list): Lista de números (float o int) para calcular la media.

    Retorna:
    float: La media de los números en la lista.
    """

    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

def main():
    print("Cálculo de la Media de un Listado de Números")
    numeros = []
    while True:
        entrada = input("Ingrese un número (o 'fin' para calcular la media): ")
        if entrada.lower() == 'fin':
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
    if numeros:
        media = calcular_media(numeros)
        print(f"La media de los números ingresados es: {media: .2f}")
    else:
        print("No se ingresaro números para calcular la media.")

if __name__ == "__main__":
    main()
    