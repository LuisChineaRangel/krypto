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
RC = np.array(
    [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36], dtype=np.uint8
)
RC_vectors = np.array([[v, 0, 0, 0] for v in RC], dtype=np.uint8)


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
SBOX = generate_sbox().flatten()


def aes(plaintext: bytes, key: bytes) -> bytes:
    key_schedule = key_expansion(key)

    # Initial round
    state = np.array([[plaintext[4*c + r] for c in range(4)] for r in range(4)], dtype=np.uint8)
    state = add_round_key(state, key_schedule[0])

    # Main rounds
    for i in range(1, len(key_schedule) - 1):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, key_schedule[i])

    # Final round
    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, key_schedule[-1])

    return bytes([state[r, c] for c in range(4) for r in range(4)])


def key_expansion(key: bytes) -> ArrayBytes:
    Nk = len(key) // 4
    Nr = Nk + 6
    Nb = 4
    # Define kex schedule initialization
    key_schedule = [
        np.array([key[4 * c + r] for r in range(4)], dtype=np.uint8) for c in range(Nk)
    ]

    for i in range(Nk, Nb * (Nr + 1)):
        temp = key_schedule[i - 1].copy()

        if i % Nk == 0:
            # RotWord
            temp = np.roll(temp, -1)
            # SubWord usando SBOX
            temp = sub_bytes(temp)
            # XOR con Rcon
            temp[0] ^= RC[i // Nk - 1]

        elif Nk > 6 and i % Nk == 4:
            temp = sub_bytes(temp)

        # XOR con la palabra Nk posiciones antes
        word = key_schedule[i - Nk] ^ temp
        key_schedule.append(word)
    return np.array(key_schedule, dtype=np.uint8).reshape(-1, 4, 4).transpose(0, 2, 1)


def sub_bytes(state: ArrayBytes) -> ArrayBytes:
    return np.array([SBOX[byte] for byte in state], dtype=np.uint8)


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
            new_state[r, c] = (
                gf2_multiply(MIX_COLUMNS_M[r, 0], col[0])
                ^ gf2_multiply(MIX_COLUMNS_M[r, 1], col[1])
                ^ gf2_multiply(MIX_COLUMNS_M[r, 2], col[2])
                ^ gf2_multiply(MIX_COLUMNS_M[r, 3], col[3])
            )
    return new_state


def add_round_key(state: ArrayBytes, round_key: ArrayBytes) -> ArrayBytes:
    return np.bitwise_xor(state, round_key)
