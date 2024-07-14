class CODICompressor:
    def __init__(self):
        self.dictionary = {}
        self.next_code = 256  # Comenzamos a partir del código ASCII extendido

    def compress(self, data):
        """
        Comprime datos usando un enfoque basado en diccionario.

        :param data: Datos a comprimir.
        :return: Datos comprimidos como una lista de códigos.
        """
        compressed = []
        current = ""
        
        for char in data:
            current += char
            if current not in self.dictionary:
                if len(current) > 1:
                    compressed.append(self.dictionary[current[:-1]])
                compressed.append(ord(current[-1]))  # Enviar el código ASCII del último carácter
                self.dictionary[current] = self.next_code
                self.next_code += 1
                current = ""

        if current:
            if current in self.dictionary:
                compressed.append(self.dictionary[current])
            else:
                compressed.append(ord(current))

        return compressed

    def decompress(self, compressed):
        """
        Descomprime datos usando el diccionario construido durante la compresión.

        :param compressed: Datos comprimidos.
        :r
