from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

# Define 256-bit key and 128-bit IV
key = os.urandom(32)
iv = os.urandom(16)

# Ask for plaintext and encode it into bytes
plaintext = input("Enter plaintext: ")
plaintext = plaintext.encode()

# Pad the plaintext
padder = padding.PKCS7(128).padder()
padded_data = padder.update(plaintext) + padder.finalize()

# Encrypt the plaintext
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_data) + encryptor.finalize()

# Print the ciphertext
print("Ciphertext: ", ciphertext)

# Decrypt the ciphertext
decryptor = cipher.decryptor()
decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

# Unpad the decrypted data
unpadder = padding.PKCS7(128).unpadder()
unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

# Print the decrypted plaintext
print("Decrypted plaintext: ", unpadded_data.decode())