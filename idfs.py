def iddfs(graph, start, goal):
    """
    Implementación de la búsqueda en profundidad iterativa (IDDFS).
    
    :param graph: Un diccionario que representa el grafo donde las claves son los nodos y los valores son listas de nodos vecinos.
    :param start: El nodo de inicio.
    :param goal: El nodo objetivo.
    :return: Una lista que representa el camino más corto desde el nodo de inicio hasta el nodo objetivo.
    """
    def dfs(node, depth, path):
        if depth == 0:
            return path if node == goal else None
        if depth > 0:
            for neighbor in graph.get(node, []):
                if neighbor not in path:
                    new_path = path + [neighbor]
                    result = dfs(neighbor, depth - 1, new_path)
                    if result:
                        return result
        return None

    depth = 0
    while True:
        path = dfs(start, depth, [start])
        if path:
            return path
        depth += 1

# Ejemplo de uso
if __name__ == "__main__":
    # Grafo representado como un diccionario de listas
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    start_node = 'A'
    goal_node = 'F'
    path = iddfs(graph, start_node, goal_node)
    print(f"Camino desde '{start_node}' hasta '{goal_node}': {path}")
