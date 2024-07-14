from collections import deque

def bfs(graph, start):
    """
    Implementación del algoritmo de Búsqueda en Anchura (BFS).
    
    :param graph: Un diccionario que representa el grafo donde las claves son los nodos y los valores son listas de nodos vecinos.
    :param start: El nodo de inicio.
    :return: Un diccionario con la distancia desde el nodo de inicio a cada nodo.
    """
    # Cola para explorar los nodos
    queue = deque([start])
    # Diccionario para almacenar las distancias
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    while queue:
        current = queue.popleft()
        
        for neighbor in graph[current]:
            if distances[neigh
