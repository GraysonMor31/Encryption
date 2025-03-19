from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

"""DES (Data Encryption Standard) is a symmetric encryption algorithm that uses a block cipher with a block size of 64 bits.
DES supports key sizes of 56 bits. DES is used in symmetric encryption, which means that the same key is used for both encryption and decryption.
The security of DES is based on the complexity of its key schedule and the non-linear transformations that are applied to the data in multiple rounds.
DES is considered insecure for modern applications due to its small key size and vulnerability to brute-force attacks."""

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
    # file deepcode ignore InsecureCipher: <please specify a reason of ignoring this>
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