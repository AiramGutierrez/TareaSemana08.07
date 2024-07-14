import heapq

def dijkstra(graph, start):
    """
    Implementación del algoritmo de Dijkstra para encontrar el camino más corto desde el nodo de inicio a todos los demás nodos.
    
    :param graph: Un diccionario que representa el grafo donde las claves son los nodos y los valores son diccionarios con los nodos vecinos y los pesos de las aristas.
    :param start: El nodo de inicio.
    :return: Un diccionario con la distancia más corta desde el nodo de inicio a cada nodo.
    """
    # Priority queue para explorar los nodos con la menor distancia conocida primero
    queue = [(0, start)]
    # Diccionario para almacenar las distancias más cortas a cada nodo
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while queue:
        # Extraer el nodo con la distancia mínima
        current_distance, current_node = heapq.heappop(queue)
        
        # Si la distancia extraída es mayor que la distancia conocida, ignorar
        if current_distance > distances[current_node]:
            continue
        
        # Explorar los vecinos del nodo actual
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Solo considerar el nuevo camino si es más corto
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return distances

# Ejemplo de uso
if __name__ == "__main__":
    # Grafo representado como un diccionario de diccionarios
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    
    start_node = 'A'
    distances = dijkstra(graph, start_node)
    print(f"Distancias desde el nodo '{start_node}':")
    for node, distance in distances.items():
        print(f"Distancia a '{node}': {distance}")
