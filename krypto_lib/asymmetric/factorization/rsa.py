import math
import string
from krypto_lib.utils import fast_pow, euclid_extended, str_to_int_blocks
from krypto_lib.utils import lehman_peralta_primality_test as is_prime


def rsa(
    message: str | list[int],
    e: int,
    p: int,
    q: int,
    alphabet: str = string.ascii_uppercase,
    decrypt: bool = False,
) -> list[int]:
    """Encrypts a message using RSA encryption.
    Args:
        message (str | list[int]): The message to encrypt or decrypt. If decrypt is True, this should be a list of integers representing the ciphertext.
        e (int): The public exponent.
        p (int): The first prime number.
        q (int): The second prime number.
        alphabet (str, optional): The alphabet used for encoding the message. Defaults to ASCII uppercase letters.
        decrypt (bool, optional): Whether to decrypt the message. Defaults to False.
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

    block_size = math.floor(math.log(n, len(alphabet)))

    if isinstance(message, str):
        plaintext_blocks, _ = str_to_int_blocks(message, block_size, alphabet)
    else:
        plaintext_blocks = message

    match decrypt:
        case True:
            d = inversed_d % phi
            result = [fast_pow(block, d, n) for block in plaintext_blocks]
        case _:
            result = [fast_pow(block, e, n) for block in plaintext_blocks]
    return result
