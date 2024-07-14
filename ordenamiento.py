def bubble_sort(arr):
    n = len(arr)
    # Recorrer todos los elementos del array
    for i in range(n):
        # Los últimos i elementos ya están en su lugar
        for j in range(0, n - i - 1):
            # Recorrer el array desde 0 hasta n-i-1
            # Intercambiar si el elemento encontrado es mayor que el siguiente elemento
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
print("Array original:", arr)
sorted_arr = bubble_sort(arr)
print("Array ordenado:", sorted_arr)
