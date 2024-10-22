"""
TABLAS DE MULTIPLICAR
Imprime todas las tablas de
multiplicar de 1 al 10.
"""

def imprimir_tabla(numero):
    """
    Imprime la tabla de multiplicar de un número dado del 1 al 10.

    Parámetros:
    numero (int): El número del cual se va a imprimir la tabla de multiplicar.
    """
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
    print()  # Línea en blanco para separar las tablas

def main():
    """
    Función principal que permite al usuario elegir qué tabla de multiplicar visualizar.
    """
    while True:
        try:
            numero = int(input("Ingrese el número de la tabla de multiplicar que desea ver (1-10): "))
            if 1 <= numero <= 10:
                imprimir_tabla(numero)
                break
            else:
                print("Por favor, ingrese un número entre 1 y 10.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

if __name__ == "__main__":
        main()
