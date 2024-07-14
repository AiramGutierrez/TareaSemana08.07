from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

def encrypt_aes(plain_text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv, ct

def decrypt_aes(iv, ct, key):
    iv = base64.b64decode(iv)
    ct = base64.b64decode(ct)
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode()

# Ejemplo de uso
if __name__ == "__main__":
    key = get_random_bytes(16)  # Clave de 16 bytes para AES-128
    plain_text = "Hola, mundo!"

    iv, cipher_text = encrypt_aes(plain_text, key)
    print(f"Cifrado: {cipher_text}")
    print(f"IV: {iv}")

    decrypted_text = decrypt_aes(iv, cipher_text, key)
    print(f"Descifrado: {decrypted_text}")
