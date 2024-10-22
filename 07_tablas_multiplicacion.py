"""
TABLAS DE MULTIPLICAR
Imprime todas las tablas de
multiplicar de 1 al 10.
"""

for i in range(1, 11):
    print(f"Table del {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()