from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

"""
AES (Advanced Encryption Standard) is a symmetric encryption algorithm that uses a block cipher with a block size of 128 bits.
AES supports key sizes of 128, 192, and 256 bits. In this example, we use a 256-bit key, as this is the current standard for AES encryption.
AES is used in symmetric encryption, which means that the same key is used for both encryption and decryption. The security of AES
is built on the complexity of its key schedule and the non-linear transformations that are applied to the data in multiple rounds.
AES does not rely on prime factorization; instead, it uses substitution-permutation networks to achieve security.
"""

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