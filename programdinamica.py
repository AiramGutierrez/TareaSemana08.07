def knapsack(weights, values, W):
    """
    Resuelve el problema de la mochila 0/1 utilizando programación dinámica.

    :param weights: Lista de pesos de los elementos.
    :param values: Lista de valores de los elementos.
    :param W: Capacidad máxima de la mochila.
    :return: El valor máximo que se puede obtener sin exceder la capacidad de la mochila.
    """
    n = len(weights)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

# Ejemplo de uso
if __name__ == "__main__":
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    W = 5
    max_value = knapsack(weights, values, W)
    print(f"Valor máximo que se puede obtener: {max_value}")
