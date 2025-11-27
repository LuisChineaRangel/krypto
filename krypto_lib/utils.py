import string
import random
from typing import Literal

system_randomizer = random.SystemRandom()


def pad_bytes(
    b: bytes, size: int, pad_byte: bytes = b"\x00", from_left: bool = False
) -> bytes:
    """Resizes a byte sequence to the specified size by padding.
    Args:
        b (bytes): The byte sequence to resize.
        size (int): The desired size of the byte sequence.
        pad_byte (bytes, optional): The byte to use for padding. Defaults to b'\x00'.
        from_left (bool, optional): If True, pad from the left. Otherwise, pad from the right. Defaults to False.
    Raises:
        ValueError: If the byte sequence is longer than the desired size.
    Returns:
        bytes: The resized byte sequence.
    """
    if len(b) > size:
        raise ValueError("Byte sequence is longer than the desired size")
    padding = pad_byte * (size - len(b))
    return (padding + b) if from_left else (b + padding)


def fast_pow(base: int, exponent: int, modulus: int) -> int:
    """Computes (base ** exponent) % modulus using the method of exponentiation by squaring.
    Args:
        base (int): The base integer.
        exponent (int): The exponent integer.
        modulus (int): The modulus integer.
    Returns:
        int: The result of (base ** exponent) % modulus.
    """
    result = 1
    base = base % modulus
    while exponent > 0:
        if (exponent % 2) == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result


def lehman_peralta_primality_test(n: int, k: int = 5) -> bool:
    """Perform the Lehman-Peralta primality test on a given integer n.
    Args:
        n (int): The integer to be tested for primality.
        k (int): The number of iterations for the test (default is 5).
    Returns:
        bool: True if n is probably prime, False if n is composite.
    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    for _ in range(k):
        a = system_randomizer.randint(2, n - 2)
        x = pow(a, (n - 1) // 2, n)
        if x != 1 and x != n - 1:
            return False
    return True


def euclid_extended(a: int, b: int) -> tuple[int, int, int]:
    """Computes the Extended Euclidean Algorithm.
    This function applies the extended version of Euclid's algorithm to compute:
        gcd(a, b)  — the greatest common divisor of a and b
        x, y       — integers satisfying Bézout's identity:
                        a*x + b*y = gcd(a, b)
    Args:
        a (int): First integer.
        b (int): Second integer.
    Returns:
        tuple[int, int, int]:
            - gcd (int): The greatest common divisor of a and b.
            - x (int): Coefficient such that a*x + b*y = gcd(a, b).
            - y (int): Coefficient such that a*x + b*y = gcd(a, b).
    """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = euclid_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def str_to_int_blocks(
    text: str, block_size: int, alphabet: str = string.ascii_uppercase
) -> tuple[list[int], list[int]]:
    """Encodes text into integer blocks based on the provided alphabet and block size.
    Args:
        text (str): The input text to convert.
        block_size (int): The size of each block.
        alphabet (str): The alphabet used for encoding the text.
    Returns:
        tuple[list[int], list[int]]: A tuple containing:
            - A list of integers representing the encoded blocks.
            - A list of integers representing the lengths of each block.
    """
    base = len(alphabet)
    blocks = []
    lengths = []
    for i in range(0, len(text), block_size):
        block = text[i : i + block_size]
        block_value = 0
        for j, char in enumerate(block):
            index = alphabet.index(char)
            block_value += index * (base ** (len(block) - j - 1))
        blocks.append(block_value)
        lengths.append(len(block))
    return blocks, lengths


def int_blocks_to_str(
    blocks: list[int], lengths: list[int], alphabet: str = string.ascii_uppercase
) -> str:
    """Decodes integer blocks back into text based on the provided alphabet and block size.
    Args:
        blocks (list[int]): The list of integer blocks to decode.
        lengths (list[int]): The lengths of each block.
        alphabet (str): The alphabet used for decoding the text.
    Returns:
        str: The decoded text.
    """
    base = len(alphabet)
    text = ""
    for block, length in zip(blocks, lengths):
        block_text = ""
        for _ in range(length):
            index = block % base
            block_text = alphabet[index] + block_text
            block //= base
        text += block_text
    return text
