from krypto_lib.prng.prga import prga


def arc4(data: bytes, key: bytes) -> bytes:
    """Encrypts or decrypts data using the RC4 (ARC4) cipher.
    Args:
        data (bytes): The input data to encrypt or decrypt.
        key (bytes): The encryption key as bytes.
    Returns:
        bytes: The encrypted or decrypted output data.
    """
    s = ksa(key)
    keystream = prga(s, len(data))
    return bytes([data_byte ^ next(keystream) for data_byte in data])


def ksa(key: bytes) -> list:
    """Key Scheduling Algorithm (KSA) for RC4 cipher.
    Args:
        key (bytes): The encryption key as bytes.
    Returns:
        list: The initialized state array s.
    """
    key_length = len(key)
    s = list(range(256))
    j = 0
    for i in range(256):
        j = (j + s[i] + key[i % key_length]) % 256
        s[i], s[j] = s[j], s[i]
    return s
