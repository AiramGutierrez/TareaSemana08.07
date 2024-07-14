import heapq
from collections import Counter, defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    """
    Construye el árbol de Huffman a partir del texto dado.
    
    :param text: Texto de entrada para construir el árbol.
    :return: La raíz del árbol de Huffman.
    """
    frequency = Counter(text)
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

def build_codes(node, prefix='', codebook=defaultdict()):
    """
    Construye el diccionario de códigos de Huffman a partir del árbol.
    
    :param node: Nodo del árbol de Huffman.
    :param prefix: Prefijo actual para el código.
    :param codebook: Diccionario para almacenar los códigos.
    :return: Diccionario de códigos de Huffman.
    """
    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        build_codes(node.left, prefix + '0', codebook)
        build_codes(node.right, prefix + '1', codebook)
    return codebook

def encode(text, codebook):
    """
    Codifica el texto usando el diccionario de códigos de Huffman.
    
    :param text: Texto de entrada.
    :param codebook: Diccionario de códigos de Huffman.
    :return: Texto codificado.
    """
    return ''.join(codebook[char] for char in text)

def decode(encoded_text, tree):
    """
    Decodifica el texto codificado usando el árbol de Huffman.
    
    :param encoded_text: Texto codificado.
    :param tree: Raíz del árbol de Huffman.
    :return: Texto decodificado.
    """
    decoded_text = []
    node = tree
    for bit in encoded_text:
        node = node.left if bit == '0' else node.right
        if node.char is not None:
            decoded_text.append(node.char)
            node = tree
    return ''.join(decoded_text)

# Ejemplo de uso
if __name__ == "__main__":
    text = "this is an example for huffman encoding"
    tree = build_huffman_tree(text)
    codebook = build_codes(tree)

    encoded_text = encode(text, codebook)
    print(f"Texto codificado: {encoded_text}")

    decoded_text = decode(encoded_text, tree)
    print(f"Texto decodificado: {decoded_text}")
