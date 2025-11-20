from krypto_lib.utils import bytes_to_int, int_to_bytes

CHACHA20_CONSTANT = b"expand 32-byte k"


def init_state(key, counter, nonce, endian="little"):
    if len(key) != 32:
        raise ValueError("Key must be 32 bytes (256 bits)")
    if len(nonce) != 12:
        raise ValueError("Nonce must be 12 bytes (96 bits)")
    if not (0 <= counter <= 0xFFFFFFFF):
        raise ValueError("Counter must be a 32-bit unsigned integer")

    constants = [
        bytes_to_int(CHACHA20_CONSTANT[i : i + 4], endian) for i in range(0, 16, 4)
    ]
    key_words = [bytes_to_int(key[i : i + 4], endian) for i in range(0, 32, 4)]
    counter_word = bytes_to_int(int_to_bytes(counter, 4, endian), endian)
    nonce_words = [bytes_to_int(nonce[i : i + 4], endian) for i in range(0, 12, 4)]

    state = constants + key_words + [counter_word] + nonce_words
    return state


def quarter_round(a, b, c, d):
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


def chacha20_block(state):
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


def keystream_block(key, counter, nonce, endian="little"):
    state = init_state(key, counter, nonce, endian)
    block = chacha20_block(state)
    keystream = b"".join(int_to_bytes(word, 4, endian) for word in block)
    return keystream


def encrypt(
    plaintext, key, nonce, initial_counter=1, hex_input=False, little_endian=True
):
    if not isinstance(plaintext, str) and hex_input:
        raise ValueError("Hex input flag is set but plaintext is not a string")
    if hex_input:
        plaintext = bytes.fromhex(plaintext)
    elif isinstance(plaintext, str):
        plaintext = plaintext.encode("utf-8")
    endian = "little" if little_endian else "big"

    ciphertext = bytearray()
    block_count = (len(plaintext) + 63) // 64
    print("Block count:", block_count)
    for block_index in range(block_count):
        counter = initial_counter + block_index
        keystream = keystream_block(key, counter, nonce, endian)
        print(f"Keystream for block {block_index} (hex):", keystream.hex())
        start = block_index * 64
        end = min(start + 64, len(plaintext))
        block = plaintext[start:end]
        for i in range(len(block)):
            ciphertext.append(block[i] ^ keystream[i])

    return bytes(ciphertext)
