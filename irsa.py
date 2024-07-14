from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def generate_keys():
    """
    Genera un par de claves RSA (pública y privada).
    
    :return: Tupla que contiene la clave pública y la clave privada.
    """
    key = RSA.generate(2048)
    public_key = key.publickey()
    private_key = key
    return public_key, private_key

def encrypt_rsa(plain_text, public_key):
    """
    Cifra un texto usando la clave pública RSA.

    :param plain_text: Texto a cifrar.
    :param public_key: Clave pública RSA.
    :return: Texto cifrado en base64.
    """
    cipher = PKCS1_OAEP.new(public_key)
    cipher_text = cipher.encrypt(plain_text.encode())
    return base64.b64encode(cipher_text).decode('utf-8')

def decrypt_rsa(cipher_text, private_key):
    """
    Descifra un texto usando la clave privada RSA.

    :param cipher_text: Texto cifrado en base64.
    :param private_key: Clave privada RSA.
    :return: Texto descifrado.
    """
    cipher = PKCS1_OAEP.new(private_key)
    cipher_text = base64.b64decode(cipher_text)
    plain_text = cipher.decrypt(cipher_text)
    return plain_text.decode()

# Ejemplo de uso
if __name__ == "__main__":
    public_key, private_key = generate_keys()
    plain_text = "Hola, mundo!"
    
    cipher_text = encrypt_rsa(plain_text, public_key)
    print(f"Cifrado: {cipher_text}")
    
    decrypted_text = decrypt_rsa(cipher_text, private_key)
    print(f"Descifrado: {decrypted_text}")
