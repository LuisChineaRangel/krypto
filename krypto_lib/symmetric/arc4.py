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

def prga(s: list, data_length: int):
    """Pseudo-Random Generation Algorithm (PRGA) for RC4 cipher.
    Args:
        s (list): The state array s from KSA.
        data_length (int): The length of the data to encrypt/decrypt.
    Yields:
        int: The next byte of the keystream.
    """
    i = 0
    j = 0
    for _ in range(data_length):
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        K = s[(s[i] + s[j]) % 256]
        yield K

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
