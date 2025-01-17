# Modern Encryption Schemes

## About
This project aims to provide an in-depth exploration of modern encryption schemes used in securing data and communications today. It covers a variety of encryption methods, from widely adopted algorithms to those still under research or rarely used. Topics include:

- Public Key Infrastructure (PKI)
- Symmetric Key Encryption
- Lattice-Based Encryption
- Digital Signatures
- Hashing Algorithms
- Homomorphic Encryption
- And more

## Encryption Algorithms

### 1. Symmetric Key Encryption
Symmetric key encryption uses the same key for both encryption and decryption. Common algorithms include:

- **AES** (Advanced Encryption Standard)
- **3DES** (Triple DES)
- **ChaCha20** (a stream cipher)

### 2. Asymmetric Encryption / PKI
Asymmetric encryption relies on key pairs, one for encryption and one for decryption. This section covers widely used public key infrastructure (PKI) algorithms:

- **ECC** (Elliptic Curve Cryptography)
- **RSA** (Rivest–Shamir–Adleman)
- **Diffie-Hellman** (Key exchange protocol)

### 3. Lattice-Based Encryption
Lattice-based cryptography is a promising area in post-quantum cryptography. One example is:

- **NTRUEncrypt** (A secure lattice-based encryption algorithm)

### 4. Homomorphic Encryption
Homomorphic encryption enables computation on encrypted data without decrypting it. Different levels of homomorphic encryption are explored:

- **Partial** (Supports only some operations)
- **Somewhat** (Supports more operations but not fully)
- **Fully** (Supports all operations on encrypted data)

### 5. Hashing Algorithms
Hash functions are used for generating fixed-size output from variable-size input, crucial in digital signatures and data integrity checks. Common algorithms include:

- **SHA-1** (Secure Hash Algorithm 1)
- **SHA-256** (Secure Hash Algorithm 256-bit)
- **MD4** (Message Digest 4)
- **MD5** (Message Digest 5)

### 6. Digital Signatures
Digital signatures are used to authenticate and verify the integrity of data. Common algorithms include:

- **DSA** (Digital Signature Algorithm)

## Getting Started
To get started with the encryption algorithms in this project, you can clone the repository and follow the instructions in the individual algorithm directories. Each directory contains an implementation of the encryption scheme along with example usage and explanations.

### Installation
```bash
git clone https://github.com/yourusername/modern-encryption-schemes.git
cd modern-encryption-schemes
