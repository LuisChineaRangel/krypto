import string

def encrypt(plaintext: str, key: str, alphabet: str = string.ascii_letters, reverse: bool = False) -> str:
    """Encrypts the given plaintext using the Vigenère cipher with the provided key and alphabet.
    Args:
        plaintext (str): The input plaintext to encrypt.
        key (str): The encryption key.
        alphabet (str, optional): The alphabet to use for encryption. Defaults to ASCII letters.
        reverse (bool, optional): If True, performs decryption instead of encryption. Defaults to False.
    Returns:
        str: The encrypted ciphertext.
    """
    alphabet_len = len(alphabet)
    alphabet_index = {char: idx for idx, char in enumerate(alphabet)}
    ciphertext = []
    key_len = len(key)
    key_index = 0
    for i, char in enumerate(plaintext):
        if char in alphabet_index:
            text_idx = alphabet_index[char]
            key_idx = alphabet_index[key[key_index % key_len]]
            if not reverse:
                cipher_idx = (text_idx + key_idx) % alphabet_len
            else:
                cipher_idx = (text_idx - key_idx + alphabet_len) % alphabet_len
            ciphertext.append(alphabet[cipher_idx])
            key_index += 1
        else:
            ciphertext.append(char)
    return ''.join(ciphertext)
