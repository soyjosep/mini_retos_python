""" 
CONVERSOR DE TEMPERATURAS
Crea un conversor entre grados Celsius y Fahrenheit.
"""

def celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    """Convierte grados Fahrenheit a Celsius."""
    return (fahrenheit - 32) * 5/9

def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("Conversor de Temperaturas")
    print("Seleccione la conversión que desea realizar:")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Salir")

def obtener_opcion():
    """Obtiene y valida la opción seleccionada por el usuario."""
    while True:
        opcion = input("Ingrese el número de la opción (1-3): ")
        if opcion in ['1', '2', '3']:
            return opcion
        else:
            print("Opción no válida. Por favor, seleccione 1, 2 o 3.")

def main():
    while True:
        mostrar_menu()
        opcion = obtener_opcion()

        if opcion == '1':
            try:
                celsius = float(input("Ingrese la temperatura en grados Celsius: "))
                fahrenheit = celsius_a_fahrenheit(celsius)
                print(f"{celsius} °C equivalen a {fahrenheit:.2f} °F.\n")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.\n")
        elif opcion == '2':
            try:
                fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
                celsius = fahrenheit_a_celsius(fahrenheit)
                print(f"{fahrenheit} °F equivalen a {celsius:.2f} °C.\n")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.\n")
        else:
            print("Gracias por usar el conversor de temperaturas. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()