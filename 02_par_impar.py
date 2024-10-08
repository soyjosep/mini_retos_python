def es_par_o_impar(numero: int) -> str:
    """Función que determina si un número es par o impar."""
    return "par" if numero % 2 == 0 else "impar"

def obtener_numero() -> int:
    """Función que solicita al usuario un número entero."""
    while True:
        entrada = input("Introduce un número entero (o escribe 'salir' para terminar): ").strip()
        if entrada.lower() == 'salir':
            return None  # Salimos cuando el usuario lo indica.
        try:
            return int(entrada)  # Intentamos convertir la entrada en entero.
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")

def main():
    """Función principal que ejecuta el programa."""
    while True:
        numero = obtener_numero()
        if numero is None:
            print("Programa finalizado. ¡Hasta luego!")
            break
        resultado = es_par_o_impar(numero)
        print(f"El número {numero} es {resultado}.")

if __name__ == "__main__":
    main()