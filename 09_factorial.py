"""
FACTORIAL
Crea una función que calcule
el factorial de un número.
"""

def factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

# Ejemplo de uso
numero = int(input("Ingresa un número entero: "))
print(f"El factorial de {numero} es {factorial(numero)}")