from typing import Literal

CHACHA20_CONSTANT = b"expand 32-byte k"


def chacha20(
    plaintext: str | bytes,
    key: bytes,
    nonce: bytes,
    initial_counter: int = 1,
    hex_input: bool = False,
    little_endian: bool = True,
) -> bytes:
    """Encrypts the given plaintext using the ChaCha20 stream cipher.
    Args:
        plaintext (str | bytes): The input plaintext to encrypt. Can be a string or bytes.
        key (bytes): A 32-byte (256-bit) key for ChaCha20.
        nonce (bytes): A 12-byte (96-bit) nonce for ChaCha20.
        initial_counter (int, optional): The initial block counter. Defaults to 1.
        hex_input (bool, optional): If True, treats the plaintext as a hex string. Defaults to False.
        little_endian (bool, optional): If True, uses little-endian byte order. Defaults to True.
    Returns:
        bytes: The resulting ciphertext as bytes.
    """
    if hex_input:
        if not isinstance(plaintext, str):
            raise TypeError("Hex input flag is set, so plaintext must be a string")
        plaintext = bytes.fromhex(plaintext)
    elif isinstance(plaintext, str):
        plaintext = plaintext.encode("utf-8")
    endian = "little" if little_endian else "big"

    ciphertext = bytearray()
    block_count = (len(plaintext) + 63) // 64
    for block_index in range(block_count):
        counter = initial_counter + block_index
        keystream = keystream_block(key, counter, nonce, endian)
        start = block_index * 64
        end = min(start + 64, len(plaintext))
        block = bytes(plaintext[start:end])
        for i in range(len(block)):
            ciphertext.append(block[i] ^ keystream[i])

    return bytes(ciphertext)


def keystream_block(
    key: bytes, counter: int, nonce: bytes, endian: Literal["big", "little"] = "little"
) -> bytes:
    """Generates a keystream block for the given key, counter, and nonce.
    Args:
        key (bytes): A 32-byte (256-bit) key for ChaCha20.
        counter (int): The block counter.
        nonce (bytes): A 12-byte (96-bit) nonce for ChaCha20.
        endian (Literal['big', 'little'], optional): Byte order, either "little" or "big". Defaults to "little".
    Returns:
        bytes: A 64-byte keystream block.
    """
    state = init_state(key, counter, nonce, endian)
    block = chacha20_block(state)
    keystream = b"".join(word.to_bytes(4, endian) for word in block)
    return keystream


def init_state(
    key: bytes, counter: int, nonce: bytes, endian: Literal["big", "little"] = "little"
) -> list[int]:
    """Initializes the ChaCha20 state matrix.
    Args:
        key (bytes): A 32-byte (256-bit) key for ChaCha20.
        counter (int): The block counter.
        nonce (bytes): A 12-byte (96-bit) nonce for ChaCha20.
        endian (Literal['big', 'little']): Byte order, either "little" or "big". Defaults to "little".
    Returns:
        list[int]: The initialized state matrix.
    """
    if len(key) != 32:
        raise ValueError("Key must be 32 bytes (256 bits)")
    if len(nonce) != 12:
        raise ValueError("Nonce must be 12 bytes (96 bits)")
    if not (0 <= counter <= 0xFFFFFFFF):
        raise ValueError("Counter must be a 32-bit unsigned integer")

    constants = [
        int.from_bytes(CHACHA20_CONSTANT[i : i + 4], endian) for i in range(0, 16, 4)
    ]
    key_words = [int.from_bytes(key[i : i + 4], endian) for i in range(0, 32, 4)]
    counter_word = int.from_bytes(counter.to_bytes(4, endian), endian)
    nonce_words = [int.from_bytes(nonce[i : i + 4], endian) for i in range(0, 12, 4)]

    state = constants + key_words + [counter_word] + nonce_words
    return state


def chacha20_block(state: list[int]) -> list[int]:
    """Generates a ChaCha20 block from the given state.
    Args:
        state (list[int]): The initial state matrix.
    Returns:
        list[int]: The transformed state after 20 rounds.
    """
    # Working state
    ws = state[:]
    for _ in range(10):
        # Column rounds
        ws[0], ws[4], ws[8], ws[12] = quarter_round(ws[0], ws[4], ws[8], ws[12])
        ws[1], ws[5], ws[9], ws[13] = quarter_round(ws[1], ws[5], ws[9], ws[13])
        ws[2], ws[6], ws[10], ws[14] = quarter_round(ws[2], ws[6], ws[10], ws[14])
        ws[3], ws[7], ws[11], ws[15] = quarter_round(ws[3], ws[7], ws[11], ws[15])

        # Diagonal rounds
        ws[0], ws[5], ws[10], ws[15] = quarter_round(ws[0], ws[5], ws[10], ws[15])
        ws[1], ws[6], ws[11], ws[12] = quarter_round(ws[1], ws[6], ws[11], ws[12])
        ws[2], ws[7], ws[8], ws[13] = quarter_round(ws[2], ws[7], ws[8], ws[13])
        ws[3], ws[4], ws[9], ws[14] = quarter_round(ws[3], ws[4], ws[9], ws[14])

    output = [(ws[i] + state[i]) & 0xFFFFFFFF for i in range(16)]
    return output


def quarter_round(a: int, b: int, c: int, d: int) -> tuple[int, int, int, int]:
    """Performs the ChaCha20 quarter round operation.
    Args:
        a (int): First 32-bit word.
        b (int): Second 32-bit word.
        c (int): Third 32-bit word.
        d (int): Fourth 32-bit word.
    Returns:
        tuple[int, int, int, int]: The transformed 32-bit words after the quarter round.
    """
    a = (a + b) & 0xFFFFFFFF
    d ^= a
    d = ((d << 16) | (d >> 16)) & 0xFFFFFFFF

    c = (c + d) & 0xFFFFFFFF
    b ^= c
    b = ((b << 12) | (b >> 20)) & 0xFFFFFFFF

    a = (a + b) & 0xFFFFFFFF
    d ^= a
    d = ((d << 8) | (d >> 24)) & 0xFFFFFFFF

    c = (c + d) & 0xFFFFFFFF
    b ^= c
    b = ((b << 7) | (b >> 25)) & 0xFFFFFFFF

    return a, b, c, d
