def compress(input_string):
    """
    Comprime una cadena de texto usando el algoritmo LZW.
    
    :param input_string: Cadena de texto a comprimir.
    :return: Una lista de códigos LZW.
    """
    dictionary = {chr(i): i for i in range(256)}  # Diccionario inicial con caracteres ASCII
    dict_size = 256
    w = ""
    result = []

    for c in input_string:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    if w:
        result.append(dictionary[w])

    return result

def decompress(compressed):
    """
    Descomprime una lista de códigos LZW usando el diccionario de compresión.
    
    :param compressed: Lista de códigos LZW.
    :return: Cadena de texto descomprimida.
    """
    dictionary = {i: chr(i) for i in range(256)}
    dict_size = 256
    w = chr(compressed.pop(0))
    result = w

    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Código inválido de diccionario')

        result += entry

        dictionary[dict_size] = w + entry[0]
        dict_size += 1
        w = entry

    return result

# Ejemplo de uso
if __name__ == "__main__":
    text = "ABABABAABABABA"

    # Compresión
    compressed = compress(text)
    print(f"Datos comprimidos: {compressed}")

    # Descompresión
    decompressed = decompress(compressed)
    print(f"Datos descomprimidos: {decompressed}")
