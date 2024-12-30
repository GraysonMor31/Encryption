from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

# Define 64-bit key and 64-bit IV
key = os.urandom(8)
iv = os.urandom(8)

# Ask for plaintext and encode it into bytes
plaintext = input("Enter plaintext: ")
plaintext = plaintext.encode()

try:
    # Pad the plaintext
    padder = padding.PKCS7(64).padder()
    padded_data = padder.update(plaintext) + padder.finalize()

    # Encrypt the plaintext
    cipher = Cipher(algorithms.DES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Print the ciphertext
    print("Ciphertext: ", ciphertext)
except ValueError:
    print("Invalid key length. DES requires a 64-bit key.")

try:
    # Decrypt the ciphertext
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

    # Unpad the decrypted data
    unpadder = padding.PKCS7(64).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    # Print the decrypted plaintext
    print("Decrypted plaintext: ", unpadded_data.decode())
except ValueError:
    print("Invalid key length. DES requires a 64-bit key.")