import math
import string
import hashlib
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
    check_primality(p, q)
    n, phi = calculate_phi(p, q)

    block_size = math.floor(math.log(n, len(alphabet)))
    if isinstance(message, str):
        plaintext_blocks, _ = str_to_int_blocks(message, block_size, alphabet)
    else:
        plaintext_blocks = message

    d = calculate_private_exponent(e, phi)
    match decrypt:
        case True:
            result = [fast_pow(block, d, n) for block in plaintext_blocks]
        case _:
            result = [fast_pow(block, e, n) for block in plaintext_blocks]
    return result


def sign(message: str, e: int, p: int, q: int) -> int:
    """Generates a digital signature for a message using RSA signing.

    Args:
        message (str): The message to sign.
        e (int): The public exponent (used to derive the private exponent).
        p (int): The first prime number.
        q (int): The second prime number.

    Returns:
        int: The digital signature as an integer.
    """
    check_primality(p, q)
    n, phi = calculate_phi(p, q)

    d = calculate_private_exponent(e, phi)

    digest = hashlib.sha256(message.encode()).digest()
    h = int.from_bytes(digest, byteorder="big") % n

    return fast_pow(h, d, n)


def verify_signature(message: str, signature: int, e: int, p: int, q: int) -> bool:
    """Verifies a digital signature for a message using RSA verification.
    Args:
        message (str): The original message.
        signature (int): The digital signature to verify.
        e (int): The public exponent.
        p (int): The first prime number.
        q (int): The second prime number.
    Returns:
        bool: True if the signature is valid, False otherwise.
    """
    check_primality(p, q)
    n, _ = calculate_phi(p, q)

    digest = hashlib.sha256(message.encode()).digest()
    h = int.from_bytes(digest, byteorder="big") % n
    recovered_hash = fast_pow(signature, e, n)

    # Compare the recovered hash with the original hash
    return h == recovered_hash


def check_primality(p: int, q: int) -> bool:
    """Checks if both p and q are prime numbers.
    Args:
        p (int): The first number to check.
        q (int): The second number to check.
    Returns:
        bool: True if both numbers are prime
    Raises:
        ValueError: If either p or q is not prime.
    """
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both p and q must be prime numbers.")
    return True


def calculate_phi(p: int, q: int) -> tuple[int, int]:
    """Calculates Euler's totient function φ(n) for n = p * q.
    Args:
        p (int): The first prime number.
        q (int): The second prime number.
    Returns:
        tuple[int, int]: A tuple containing n and φ(n).
    """
    return (p * q, (p - 1) * (q - 1))


def calculate_private_exponent(e: int, phi: int) -> int:
    """Calculates the private exponent d given e and φ(n).
    Args:
        e (int): The public exponent.
        phi (int): The value of φ(n).
    Returns:
        int: The private exponent d.
    """
    gcd, inversed_d, _ = euclid_extended(e, phi)
    if gcd != 1:
        raise ValueError("e and φ(n) are not coprime.")
    return inversed_d % phi
