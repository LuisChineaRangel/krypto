import secrets
from typing import Optional
from krypto_lib.utils import lehman_peralta_primality_test, fast_pow, mod_inverse


def generate_keys(p: int, g: int, x: Optional[int] = None) -> tuple[int, int]:
    """Generates ElGamal keys.

    Args:
        p (int): A large prime number.
        g (int): A generator for the group.
        x (int, optional): The private key. If None, it's generated randomly.

    Returns:
        tuple[int, int]: (private_key x, public_key y)
    """
    if not lehman_peralta_primality_test(p):
        raise ValueError("p must be a prime number.")

    if x is None:
        x = secrets.randbelow(p - 3) + 2

    y = fast_pow(g, x, p)
    return x, y


def encrypt(p: int, g: int, y: int, message: int, k: Optional[int] = None) -> tuple[int, int]:
    """Encrypts a message using ElGamal.

    Args:
        p (int): The prime number.
        g (int): The generator.
        y (int): The public key.
        message (int): The message to encrypt (must be 0 <= message < p).
        k (int, optional): The ephemeral secret key. If None, it's generated randomly.

    Returns:
        tuple[int, int]: The ciphertext pair (a, b).
    """
    if message >= p:
        raise ValueError("Message must be smaller than p.")

    if k is None:
        k = secrets.randbelow(p - 3) + 2

    a = fast_pow(g, k, p)
    s = fast_pow(y, k, p)  # Shared secret y^k mod p
    b = (message * s) % p

    return a, b


def decrypt(p: int, x: int, a: int, b: int) -> int:
    """Decrypts a ciphertext using ElGamal.

    Args:
        p (int): The prime number.
        x (int): The private key.
        a (int): First part of ciphertext (g^k mod p).
        b (int): Second part of ciphertext (m * y^k mod p).

    Returns:
        int: The decrypted message.
    """
    s = fast_pow(a, x, p)  # Shared secret s = a^x = g^(kx) mod p
    s_inv = mod_inverse(s, p)
    message = (b * s_inv) % p

    return message


def encrypt_multi(p: int, g: int, public_keys: list[int], message: int, k: Optional[int] = None) -> tuple[int, list[int]]:
    """Encrypts a message for multiple recipients using ElGamal.
    This is efficient as it reuses the same ephemeral k.

    Returns:
        tuple[int, list[int]]: (a, [b1, b2, ..., bn])
    """
    if message >= p:
        raise ValueError("Message must be smaller than p.")

    if k is None:
        k = secrets.randbelow(p - 3) + 2

    a = fast_pow(g, k, p)
    ciphertexts_b = []

    for y in public_keys:
        s = fast_pow(y, k, p)
        b = (message * s) % p
        ciphertexts_b.append(b)

    return a, ciphertexts_b
