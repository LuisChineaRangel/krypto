import numpy as np
from numpy.typing import NDArray

from krypto_lib.utils import gf2_multiply, gf2_inverse

ArrayBytes = NDArray[np.uint8]

# AES MixColumns transformation matrix
MIX_COLUMNS_M = np.array(
    [
        [0x02, 0x03, 0x01, 0x01],
        [0x01, 0x02, 0x03, 0x01],
        [0x01, 0x01, 0x02, 0x03],
        [0x03, 0x01, 0x01, 0x02],
    ],
    dtype=np.uint8,
)

# AES Round Constants
RC = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]


def generate_sbox() -> ArrayBytes:
    sbox = np.zeros((16, 16), dtype=int)
    for i in range(16):
        for j in range(16):
            byte = (i << 4) | j
            if byte == 0:
                inv = 0
            else:
                inv = gf2_inverse(byte)

            s = inv
            for _ in range(4):
                s = ((s << 1) | (s >> 7)) & 0xFF
                inv ^= s
            sbox[i][j] = inv ^ 0x63
    return sbox


# Precompute SBOX
SBOX = generate_sbox()


def encrypt(plaintext: bytes, key: bytes):
    text_words = np.array(
        [list(plaintext[i : i + 4]) for i in range(0, 16, 4)], dtype=np.uint8
    )
    key_schedule = key_expansion(key)
    state = add_round_key(text_words, key_schedule[0:4])
    # for i in range(1, len(key_schedule) // 4 - 1):
    #     state = sub_bytes([byte for row in state for byte in row], SBOX)
    #     state = [state[i : i + 4] for i in range(0, 16, 4)]
    #     state = shift_rows(state)
    #     state = mix_columns(state)
    #     state = add_round_key(state, key_schedule[4 * i : 4 * (i + 1)])
    # state = sub_bytes([byte for row in state for byte in row], SBOX)
    # state = [state[i : i + 4] for i in range(0, 16, 4)]
    # state = shift_rows(state)
    # state = add_round_key(state, key_schedule[4 * (len(key_schedule) // 4 - 1) :])

    # return bytes([byte for row in state for byte in row])


def key_expansion(key: bytes) -> ArrayBytes:
    Nk = len(key) // 4
    Nr = Nk + 6
    # Define kex schedule initialization
    key_schedule = np.array(
        [list(key[i : i + 4]) for i in range(0, len(key), 4)], dtype=np.uint8
    )

    # Is conformed by Nr + 1 round keys (if we include the initial key) of 16 bytes each
    key_schedule = key_schedule.reshape((Nr + 1), 16)

    print(key_schedule)

    # for i in range(Nk, 4 * (Nr + 1)):
    #     temp = key_schedule[i - 1][:]
    #     if i % Nk == 0:
    #         # Rotate
    #         temp = temp[1:] + temp[:1]
    #         # SubBytes
    #         temp = sub_bytes(temp, SBOX)
    #         # XOR with round constant
    #         temp[0] ^= RC[(i // Nk) - 1]
    #     elif Nk > 6 and i % Nk == 4:
    #         temp = sub_bytes(temp, SBOX)
    #     # XOR with the word Nk positions earlier
    #     word = [key_schedule[i - Nk][j] ^ temp[j] for j in range(4)]
    #     key_schedule.append(word)
    return key_schedule


def sub_bytes(state: ArrayBytes, sbox: ArrayBytes) -> ArrayBytes:
    return np.array([sbox[byte] for byte in state], dtype=np.uint8)


def shift_rows(state: ArrayBytes) -> ArrayBytes:
    new_state = state.copy()
    for r in range(1, 4):
        new_state[r] = np.roll(state[r], -r)
    return new_state


def mix_columns(state: ArrayBytes) -> ArrayBytes:
    state = state.copy()
    new_state = np.zeros_like(state, dtype=np.uint8)
    for c in range(4):
        col = state[:, c]
        for r in range(4):
            print(hex(MIX_COLUMNS_M[r, 0]), MIX_COLUMNS_M[r, 1], MIX_COLUMNS_M[r, 2], MIX_COLUMNS_M[r, 3])
            new_state[r, c] = (
                gf2_multiply(MIX_COLUMNS_M[r, 0], col[0])
                ^ gf2_multiply(MIX_COLUMNS_M[r, 1], col[1])
                ^ gf2_multiply(MIX_COLUMNS_M[r, 2], col[2])
                ^ gf2_multiply(MIX_COLUMNS_M[r, 3], col[3])
            )
    return new_state


def add_round_key(state: ArrayBytes, round_key: ArrayBytes) -> ArrayBytes:
    return np.bitwise_xor(state, round_key)
