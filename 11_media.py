"""
MEDIA
Calcula la media de un
listado de números.
"""

def calcular_media(numeros):
    if not numeros:
        return "La lista esta vacia, no se puede calcular la media"
    return sum(numeros) / len(numeros)

#Ejemplo de uso
numeros = [10, 20, 30, 40, 50]
media = calcular_media(numeros)
print(f"La media de los numeros es: {media}")
    