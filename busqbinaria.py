# busqueda.py

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Retorna -1 si el objetivo no se encuentra

# Ejemplo de uso
if __name__ == "__main__":
    arr = [10, 23, 35, 50, 7]
    target = 35
    arr.sort()  # La búsqueda binaria requiere una lista ordenada
    result = binary_search(arr, target)
    print(f"Índice del objetivo ({target}) en la lista ordenada: {result}")
