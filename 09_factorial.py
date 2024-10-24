"""
FACTORIAL
Crea una función que calcule
el factorial de un número.
"""

def calcular_factorial(n):
    """
    Calcula el factorial de un número entero no negativo.

    Parámetros:
    n (int): El número del cual se desea calcular el factorial.

    Retorna:
    int: El factorial de n.

    Lanza:
    ValueError: Si n es un número negativo.
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def main():
    print("Cálculo del Factorial de un Número")
    while True:
        try:
            numero = int(input("Ingrese un número entero no negativo: "))
            resultado = calcular_factorial(numero)
            print(f"El factorial de {numero} es {resultado}.")
            break
        except ValueError as e:
            print(f"Entrada no válida: {e}")
        except Exception:
            print("Ocurrió un error inesperado. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()