import heapq

def a_star(graph, start, goal, heuristic):
    """
    Implementación del algoritmo A* para encontrar el camino más corto entre el nodo de inicio y el nodo objetivo.
    
    :param graph: Un diccionario que representa el grafo donde las claves son los nodos y los valores son diccionarios con los nodos vecinos y los pesos de las aristas.
    :param start: El nodo de inicio.
    :param goal: El nodo objetivo.
    :param heuristic: Una función heurística que estima el costo desde un nodo hasta el objetivo.
    :return: Una lista que representa el camino más corto desde el nodo de inicio hasta el nodo objetivo.
    """
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start), start))
    
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    f_score = {node: float('inf') f
