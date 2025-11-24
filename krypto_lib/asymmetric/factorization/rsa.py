import math
import string
from krypto_lib.utils import fast_pow, euclid_extended, text_to_int_blocks
from krypto_lib.utils import lehman_peralta_primality_test as is_prime


def rsa(plaintext: str, e: int, p: int, q: int, alphabet: str = string.ascii_uppercase) -> list[int]:
    """Encrypts a message using RSA encryption.
    Args:
        plaintext (str): The plaintext message.
        e (int): The public exponent.
        p (int): The first prime number.
        q (int): The second prime number.
        alphabet (str, optional): The alphabet used for encoding the message. Defaults to ASCII uppercase letters.
    Returns:
        int: The encrypted ciphertext as an integer.
    """
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both p and q must be prime numbers.")

    n = p * q
    phi = (p - 1) * (q - 1)

    gcd, inversed_d, _ = euclid_extended(e, phi)
    if gcd != 1:
        raise ValueError("e and φ(n) are not coprime.")
    d = inversed_d % phi

    block_size = math.floor(math.log(n, len(alphabet)))
    plaintext_blocks = text_to_int_blocks(plaintext, block_size, alphabet)

    encrypted_blocks = [fast_pow(block, e, n) for block in plaintext_blocks]
    return encrypted_blocks
