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
    if len(plaintext) != 16:
        raise ValueError("Plaintext must be exactly 16 bytes (128 bits).")
    if len(key) not in (16, 24, 32):
        raise ValueError("Key length must follow AES standards (16, 24, or 32 bytes).")

    key_schedule = key_expansion(key)

    # Initial round
    state = np.frombuffer(plaintext, dtype=np.uint8).reshape(4, 4).T
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

    return state.T.tobytes()


def key_expansion(key: bytes) -> ArrayBytes:
    nk = len(key) // 4
    nr = nk + 6
    nb = 4

    # Define kex schedule initialization
    total_words = nb * (nr + 1)
    key_schedule = np.zeros((total_words, 4), dtype=np.uint8)

    for i in range(nk):
        key_schedule[i] = np.array([key[4 * i + r] for r in range(4)], dtype=np.uint8)

    for i in range(nk, total_words):
        temp = key_schedule[i - 1].copy()

        if i % nk == 0:
            # RotWord + SubWord + Rcon
            temp = sub_bytes(np.roll(temp, -1))
            temp[0] ^= RC[i // nk - 1]
        elif nk > 6 and i % nk == 4:
            temp = sub_bytes(temp)
        # XOR con la palabra nk posiciones antes
        key_schedule[i] = key_schedule[i - nk] ^ temp
    return np.array(key_schedule, dtype=np.uint8).reshape(-1, 4, 4).transpose(0, 2, 1)


def sub_bytes(state: ArrayBytes) -> ArrayBytes:
    return SBOX[state].astype(np.uint8)


def shift_rows(state: ArrayBytes) -> ArrayBytes:
    res = state.copy()
    for r in range(1, 4):
        res[r] = np.roll(res[r], -r)
    return res


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
