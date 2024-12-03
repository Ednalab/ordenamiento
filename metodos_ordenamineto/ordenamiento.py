def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):  # Número de pasadas
        for j in range(n - i - 1):  # Comparaciones en cada pasada
            if arr[j] > arr[j + 1]:
                # Intercambia si el elemento actual es mayor al siguiente
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Ejemplo de uso
mi_lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", mi_lista)
print("Lista ordenada:", bubble_sort(mi_lista))
