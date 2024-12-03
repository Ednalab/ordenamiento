import math
import random

def shor_classic(n):
    if n % 2 == 0:
        return [2, n // 2]  # Caso trivial: si es par
    
    # Paso 1: Escoge un número aleatorio 'a'
    a = random.randint(2, n - 1)
    print(f"Número aleatorio seleccionado: {a}")
    
    # Paso 2: Comprueba si 'a' comparte un divisor común con 'n'
    gcd = math.gcd(a, n)
    if gcd > 1:
        return [gcd, n // gcd]  # Ya encontramos factores

    # Paso 3: (Simulando encontrar el período 'r')
    # En computación cuántica, aquí encontraríamos 'r'. Aquí lo hacemos manualmente:
    r = None
    for i in range(1, n):
        if pow(a, i, n) == 1:
            r = i
            break
    
    print(f"Período encontrado: {r}")

    if r is None or r % 2 != 0:
        print("No se pudo encontrar un período adecuado.")
        return None

    # Paso 4: Calcula los factores
    x = pow(a, r // 2, n)
    factor1 = math.gcd(x - 1, n)
    factor2 = math.gcd(x + 1, n)

    if factor1 * factor2 == n:
        return [factor1, factor2]
    else:
        print("No se encontraron factores válidos.")
        return None

# Ejemplo de uso:
n = 15
factores = shor_classic(n)
print(f"Factores de {n}: {factores}")
