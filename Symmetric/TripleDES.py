from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

"""3DES (Triple Data Encryption Standard) is a symmetric encryption algorithm that uses a block cipher with a block size of 64 bits.
It uses key sizes of 112, 168, or 192 bits. 3DES differs from DES in that it performs the encryption 3 times on each block of data. 3DES is used in symmetric encryption, which means that the same key is used for both encryption and decryption.
3DES is considered insecure for modern applications due to its small block size and vulnerability to attacks."""

# Define 192-bit key and 64-bit IV
key = os.urandom(24)
iv = os.urandom(8)

# Ask for plaintext and encode it into bytes
plaintext = input("Enter plaintext: ")
plaintext = plaintext.encode()

try:
    padder = padding.PKCS7(64).padder()
    padded_data = padder.update(plaintext) + padder.finalize()
    
    # Encrypt the plaintext
    cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    
    # Print the ciphertext
    print("Ciphertext: ", ciphertext)
except ValueError:
    print("Invalid key length. 3DES requires a 192-bit key.")

try:
    # Decrypt the ciphertext
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    
    # Unpad the decrypted data
    unpadder = padding.PKCS7(64).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    print("Decrypted plaintext: ", unpadded_data.decode())
except ValueError:
    print("Invalid key length. 3DES requires a 192-bit key.")
