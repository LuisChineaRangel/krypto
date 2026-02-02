# Kypto

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=LuisChineaRangel_krypto&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=LuisChineaRangel_krypto)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=LuisChineaRangel_krypto&metric=coverage)](https://sonarcloud.io/summary/new_code?id=LuisChineaRangel_krypto)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=LuisChineaRangel_krypto&metric=bugs)](https://sonarcloud.io/summary/new_code?id=LuisChineaRangel_krypto)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=LuisChineaRangel_krypto&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=LuisChineaRangel_krypto)

---

**Kypto** is a modular Python framework for modern cryptography.
It aims to provide tools for encryption, hashing, key management, and secure data handling in a structured and extensible way.

---

## Table of Contents

- [Current Status](#current-status)
- [Project Structure](#project-structure)
- [Symmetric Ciphers](#symmetric-ciphers)
    - [Vigenère Cipher](#vigenère-cipher)
    - [RC4 (ARC4)](#rc4-arc4)
    - [AES (Advanced Encryption Standard)](#aes-advanced-encryption-standard)
    - [ChaCha20](#chacha20)
- [Asymmetric Ciphers](#asymmetric-ciphers)
    - [RSA (Rivest–Shamir–Adleman)](#rsa-rivestshamiradleman)
    - [Diffie-Hellman (DH)](#diffie-hellman-dh)
    - [ElGamal](#elgamal)
    - [Elliptic Curve Cryptography (ECC)](#elliptic-curve-cryptography-ecc)
- [Issues](#issues)

---

## Current Status

- Initial project structure in place
- Core modules and basic setup planned
- RSA, Vigenère, ARC4, and ChaCha20 ciphers implemented
- GPS L1C/A signal simulator implemented
- Basic unit tests for implemented ciphers
- Symmetric Ciphers:
    - AES (ECB, CBC)
    - ChaCha20
    - RC4 (ARC4)
    - Vigenère Cipher
- Asymmetric Ciphers:
    - RSA
    - Diffie-Hellman (Discrete Logarithm & Elliptic Curve)
    - ElGamal (Discrete Logarithm & Elliptic Curve)
- Pseudorandom Number Generators:
    - PRGA of ARC4
    - GPS C/A PRN Code Generator

---

## Project Structure

The project is organized into the following main directories:

- `krypto_lib/`: Core library code for cryptographic operations.
- `krypto_lib/asymmetric/`: Asymmetric cryptography algorithms (e.g., RSA, ECC).
- `krypto_lib/symmetric/`: Symmetric cryptography algorithms (e.g., AES, ChaCha20).
- `krypto_lib/prng/`: Pseudorandom number generators (e.g., ARC4).
- `tests/`: Unit and integration tests for the library.
- `cli/`: Command-line interface tools for interacting with the library.
- `api/`: RESTful API endpoints for remote cryptographic services.
- `requirements.txt`: List of dependencies required for the project.
- `pyproject.toml`: Project metadata and configuration.

Each module is designed to be independent, allowing for easy maintenance and future expansion.

---

## Symmetric Ciphers

### Vigenère Cipher

The **Vigenère cipher** is a classic method of encrypting alphabetic text by using a series of interwoven Caesar ciphers, based on the letters of a keyword. It is a form of **polyalphabetic substitution**, meaning that a single letter in the plaintext can be represented by different letters in the ciphertext depending on its position.

---

Unlike the Caesar cipher, which shifts every letter by the same fixed number, the Vigenère cipher uses a **keyword** to determine the shift for each letter.

- **Key Mapping:** Each letter of the keyword corresponds to a shift value based on its position in the alphabet ($A=0, B=1, C=2, \dots, Z=25$).
- **Key Repetition:** The keyword is repeated cyclically until it matches the length of the plaintext.
- **Mathematical Formula:** The ciphertext is generated using the formula:
    $E_i = (P_i + K_i) \pmod{26}$
    *(Where $P$ is the plaintext letter and $K$ is the key letter)*.

---
To simplify manual encryption, users traditionally utilized a **Vigenère Square**. This is a $26 \times 26$ grid containing the alphabet shifted 26 times.

- **Encryption:** Find the row corresponding to the key letter and the column corresponding to the plaintext letter. The intersection is the ciphertext letter.
- **Decryption:** Find the row of the key letter, then look along that row to find the ciphertext letter. The column header above that letter is the original plaintext.

---

For centuries, the Vigenère cipher was known as **"le chiffre indéchiffrable"** (the indecipherable cipher). It successfully resisted frequency analysis—the primary method for breaking simple substitution ciphers—because the same plaintext letter (e.g., "E") is encrypted differently each time. It wasn't until the 19th century (by Friedrich Kasiski and Charles Babbage) that a systematic way to break it using the "Kasiski examination" was discovered.

---

### RC4 (ARC4)

**ARC4** is a software-based stream cipher that was famously used in protocols such as WEP, WPA, and SSL/TLS. It is a **Symmetric Key Stream Cipher**, meaning it encrypts plaintext by combining it with a pseudo-random stream of bits (a keystream) using the XOR operation.

---

ARC4 consists of two main components: the **Key Scheduling Algorithm (KSA)** and the **Pseudo-Random Generation Algorithm (PRGA)**.

- **KSA (Initialization):** It starts with an array of 256 bytes (the "S-box") initialized from 0 to 255. The secret key is used to permute (shuffle) this array.
- **PRGA (Generation):** Once initialized, the cipher generates a keystream one byte at a time by continuously swapping elements in the S-box based on internal counters.
- **Encryption Formula:** The ciphertext is generated by XORing the plaintext with the keystream:
    $$C_i = P_i \oplus K_i$$
    *(Where $P$ is the plaintext byte and $K$ is the keystream byte generated from the S-box).*

---

While historically popular, ARC4 is now considered **cryptographically broken** and insecure for modern use:

- **Keystream Biases:** The first few bytes of the keystream are not truly random and reveal information about the key (this led to the "RC4-drop" practice where the first 768 bytes were discarded).
- **Vulnerabilities:** Flaws in how it was implemented in WEP allowed attackers to crack Wi-Fi passwords in minutes.
- **Current Status:** It has been prohibited in TLS (RFC 7465) and replaced by more secure algorithms like **AES-GCM** or **ChaCha20**.

---

### AES (Advanced Encryption Standard)

**AES** is the most widely used symmetric block cipher in the world. Established by NIST in 2001 after a global competition, it replaced the aging DES algorithm. It is a **Block Cipher**, meaning it encrypts data in fixed-size chunks of 128 bits (16 bytes) using keys of 128, 192, or 256 bits.

---

AES operates on a $4 \times 4$ column-major matrix of bytes called the **State**. The encryption process consists of a specific number of rounds (10, 12, or 14) depending on the key length.

- **Key Expansion:** The original key is expanded into several "Round Keys" using a Rijndael key schedule, ensuring each round uses a unique sub-key.
- **The Four Stages:** Each round (except the last) performs four mathematical transformations:
    1. **SubBytes:** A non-linear substitution using a lookup table (S-Box).
    2. **ShiftRows:** A transposition step where rows are shifted cyclically.
    3. **MixColumns:** A mixing operation that operates on the columns of the state, providing diffusion.
    4. **AddRoundKey:** A simple XOR between the current state and the round key.
- **Encryption Formula:** Unlike stream ciphers, AES transforms the entire block through multiple layers of substitution and permutation:
    $$State_{new} = Round(State_{old}, RoundKey)$$

---

#### Modes of Operation

To encrypt data of arbitrary length, AES is used with different **modes of operation**:

- **ECB (Electronic Codebook):** The simplest mode where each block is encrypted independently. It is generally **insecure** for complex data because it reveals patterns in the plaintext (the famous "Tux" image).
- **CBC (Cipher Block Chaining):** Each block of plaintext is XORed with the previous ciphertext block before being encrypted. This provides better security and hides patterns, but requires an **Initialization Vector (IV)** and is non-parallelizable during encryption.

---

AES is considered the "gold standard" of modern cryptography due to its high security and efficiency:

- **Hardware Acceleration:** Most modern CPUs include **AES-NI** (New Instructions), which allow the processor to perform the encryption rounds directly in hardware, making it incredibly fast.
- **Unbroken Security:** Despite decades of intensive cryptanalysis, there are no known practical attacks against the full-round AES algorithm when implemented correctly.
- **Versatility:** It is used everywhere, from securing your Wi-Fi (WPA2/WPA3) and hard drive encryption (BitLocker/FileVault) to protecting government classified information and modern web traffic (HTTPS).

---

### ChaCha20

**ChaCha20** is a modern, high-speed stream cipher developed by Daniel J. Bernstein. It is designed to be a high-performance successor to the older Salsa20 cipher and a secure, software-friendly alternative to AES. It encrypts data by generating a keystream based on a 256-bit key, a 96-bit nonce, and a 32-bit counter.

---

ChaCha20 operates on an internal state of **64 bytes**, organized as a $4 \times 4$ matrix of 32-bit words. The core of the cipher is the **Quarter Round** operation, which is repeated across 20 rounds.

- **The State:** The matrix consists of constants (to prevent "all-zero" keys), the 256-bit key, a block counter (allowing seekable encryption), and a nonce (to ensure the same key never produces the same stream twice).
- **The Quarter Round (QR):** This is the fundamental building block. It uses only three simple operations: **Addition (A)**, **XOR (X)**, and **Rotation (R)**—often called the "ARX" design.
- **Encryption Formula:** Like other stream ciphers, the final state is XORed with the plaintext to produce the ciphertext:
    $$C_i = P_i \oplus K_i$$
    *(Where $P$ is the plaintext and $K$ is the keystream block generated after 20 rounds of permutations).*

---

ChaCha20 has become the industry standard for secure stream encryption due to several key advantages:

- **Speed on CPU:** Unlike AES, which often requires dedicated hardware (AES-NI) to be fast, ChaCha20 is extremely efficient in pure software, making it ideal for mobile devices and older processors.
- **Resistance to Timing Attacks:** Because it only uses ARX operations (which take a constant amount of time on most CPUs), it is naturally resistant to cache-timing side-channel attacks.
- **Current Status:** It is a mandatory component of **TLS 1.3** and is used by default in **OpenSSH**, **WireGuard**, and **Google’s** internet traffic (often paired with Poly1305 for authentication).

---

## Asymmetric Ciphers

### RSA (Rivest–Shamir–Adleman)

**RSA** is the first and most widely used **Asymmetric (Public-Key) Cipher** in the world. Unlike AES or ChaCha20, it uses a pair of mathematically linked keys: a **Public Key** for encryption and a **Private Key** for decryption. Its security is based on the extreme difficulty of factoring the product of two large prime numbers.

---

RSA operation is built upon modular exponentiation and number theory. The process involves key generation, encryption, and decryption stages.

- **Key Generation:** Two distinct large prime numbers, $p$ and $q$, are multiplied to create $n = p \times q$. This $n$ is part of both the public and private keys. The public exponent $e$ (usually 65537) and the private exponent $d$ are then calculated.
- **The Trapdoor Function:** The security relies on the fact that while it is easy to multiply $p \times q$, it is computationally "impossible" to find $p$ and $q$ starting from $n$ if the numbers are sufficiently large (e.g., 2048 or 4096 bits).
- **Encryption and Decryption Formula:** A message $M$ is transformed into ciphertext $C$ using the public key $(n, e)$, and reversed using the private key $d$:
    $$C = M^e \pmod{n}$$
    $$M = C^d \pmod{n}$$

---

RSA remains a foundational pillar of internet security, though it is increasingly being supplemented by Elliptic Curve Cryptography (ECC):

- **Digital Signatures:** Beyond encryption, RSA is used to "sign" documents. By encrypting a hash with a private key, anyone with the public key can verify the sender's identity and the document's integrity.
- **Key Exchange:** Because RSA is slow for large data, it is rarely used to encrypt files directly. Instead, it is used to securely exchange a "session key" (like an AES key) which is then used for the actual data transfer.
- **Current Status:** While 1024-bit RSA is considered insecure, **2048-bit** and **4096-bit** keys are still standard for SSL/TLS certificates and PGP email encryption.

---

### Diffie-Hellman (DH)

**Diffie-Hellman** is a fundamental protocol for secure **Key Exchange**. It allows two or more parties to establish a shared secret over an insecure channel, which can then be used for symmetric encryption. Its security is based on the **Discrete Logarithm Problem (DLP)**.

- **The Process:** Parties agree on a large prime $p$ and a generator $g$. Each chooses a private secret $a$ and $b$, and they exchange $g^a \pmod p$ and $g^b \pmod p$.
- **Shared Secret:** Both compute the same value $K = g^{ab} \pmod p$, but an eavesdropper cannot find $a$ or $b$ from the exchanged values.
- **DLP:** The difficulty lies in finding $x$ when given $y = g^x \pmod p$.
- **Group Support:** Implementation includes support for $N$ participants (Group Key Exchange).
- **Elliptic Curve:** Also implemented as **ECDH**, providing equivalent security with much smaller keys.

---

### ElGamal

**ElGamal** is an asymmetric encryption system based on the Diffie-Hellman key exchange. It is **probabilistic**, meaning that encrypting the same plaintext twice with the same key will yield different ciphertexts.

- **Security:** Like Diffie-Hellman, it relies on the difficulty of solving the **Discrete Logarithm Problem**.
- **Efficiency:** The ciphertext is twice the size of the plaintext, as it consists of two parts $(a, b)$ representing the ephemeral public key and the masked message.
- **Multi-recipient:** Implementation includes efficient broadcast encryption (`encrypt_multi`).
- **Elliptic Curve:** Implementation as **ECEG** (Elliptic Curve ElGamal) included.

---

### Elliptic Curve Cryptography (ECC)

**ECC** is a modern approach to public-key cryptography based on the algebraic structure of elliptic curves over finite fields. It provides the same level of security as RSA but with significantly smaller key sizes (e.g., a 256-bit ECC key is equivalent to a 3072-bit RSA key).

- **Primitives:** Implementation of point addition, point doubling, and scalar multiplication on Weierstrass curves ($y^2 = x^3 + ax + b$).
- **ECDH:** Elliptic Curve Diffie-Hellman for key exchange.
- **ECEG:** Elliptic Curve ElGamal for asymmetric encryption.

---

## Issues

If you encounter any bugs, have questions, or would like to suggest new features, please open an issue on the [GitHub Issues](https://github.com/LuisChineaRangel/krypto/issues) page.

When reporting an issue, please include:

- A clear and descriptive title.
- Steps to reproduce the problem.
- Expected vs. actual behavior.
- Any relevant logs or screenshots.
