"""
IMC
Crea una calculadora del
índice de masa corporal.
"""

def calcular_imc(peso: float, altura: float) -> float:
    """Calcula el índice de masa corporal (IMC)"""
    return peso / (altura ** 2)

def clasificar_imc(imc: float) -> str:
    """Clasifica el IMC en categorías"""
    if imc < 18.5:
        return "Peso bajo"
    elif 18.5 <= imc <= 24.9:
        return "Peso normal"
    elif 25 <= imc <= 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"

def obtener_datos_usuario() -> tuple:
    """Solicita y valida el peso y altura ingresados por el usuario"""
    while True:
        try:
            peso = float(input("Peso en Kg: "))
            altura = float(input("Altura en m: "))
            if peso <= 0 or altura <= 0:
                print("Por favor, ingresa valores mayores a 0.")
                continue
            return peso, altura
        except ValueError:
            print("Entrada no válida. Por favor ingresa números.")

def main():
    """Función principal para calcular y mostrar el IMC"""
    peso, altura = obtener_datos_usuario()
    imc = calcular_imc(peso, altura)
    clasificacion = clasificar_imc(imc)

    print(f"Tu IMC es: {imc:.2f}")
    print(f"Clasificación: {clasificacion}")

if __name__ == "__main__":
    main()