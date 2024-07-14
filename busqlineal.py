# busqueda.py

def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1  # Retorna -1 si el objetivo no se encuentra

# Ejemplo de uso
if __name__ == "__main__":
    arr = [10, 23, 4, 7, 35, 50]
    target = 35
    result = linear_search(arr, target)
    print(f"Índice del objetivo ({target}) en la lista: {result}")
