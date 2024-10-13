""" 
CONTADOR DE VOCALES
Crea un programa que cuente cuantas vocales tiene una cadena de texto
"""

import re

def contar_vocales(texto):
    # Definir el patrón de vocales incluyendo mayúsculas y vocales acentuadas
    patron_vocales = r'[aeiouáéíóúAEIOUÁÉÍÓÚ]'
    
    # Usar re.findall para encontrar todas las coincidencias de vocales
    vocales_encontradas = re.findall(patron_vocales, texto)
    
    # Retornar la cantidad de vocales encontradas
    return len(vocales_encontradas)

# Solicitar al usuario que introduzca una cadena de texto
texto = input("Introduce una cadena de texto: ").strip()

# Verificar si el usuario ingresó algo
if not texto:
    print("No has introducido ningún texto.")
else:
    total_vocales = contar_vocales(texto)
    print(f"Total de vocales: {total_vocales}")