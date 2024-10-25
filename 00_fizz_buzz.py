"""
EL FAMOSO "FIZZ BUZZ"
Escribe un programa que muestre por consola (con un print) los números de 1 al 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
Múltiplos de 3 por la palabra "fizz"
Múltiplos de 5 por la palabra "buzz"
Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz"
"""

def fizz_buzz():
    """
    Imprime los números del 1 al 100, sustituyendo:
    - Múltiplos de 3 por "fizz"
    - Múltiplos de 5 por "buzz"
    - Múltiplos de ambos 3 y 5 por "fizzbuzz"
    """
    for numero in range(1, 101):
        salida = ""
        if numero % 3 == 0:
            salida += "fizz"
        if numero % 5 == 0:
            salida += "buzz"
        print(salida or numero)

def main():
    """
    Función principal que ejecuta el programa Fizz Buzz.
    """
    print("Programa Fizz Buzz: Números del 1 al 100\n")
    fizz_buzz()

if __name__ == "__main__":
    main()