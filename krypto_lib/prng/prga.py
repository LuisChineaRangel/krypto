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
