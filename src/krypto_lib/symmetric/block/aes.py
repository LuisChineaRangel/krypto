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

# AES Inverse MixColumns transformation matrix
INV_MIX_COLUMNS_M = np.array(
    [
        [0x0E, 0x0B, 0x0D, 0x09],
        [0x09, 0x0E, 0x0B, 0x0D],
        [0x0D, 0x09, 0x0E, 0x0B],
        [0x0B, 0x0D, 0x09, 0x0E],
    ],
    dtype=np.uint8,
)

# AES Round Constants
RC = np.array(
    [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36], dtype=np.uint8
)
RC_vectors = np.array([[v, 0, 0, 0] for v in RC], dtype=np.uint8)


def generate_sbox() -> ArrayBytes:
    """Generates the AES S-box used for the SubBytes step.

    This box is created by finding the multiplicative inverse in GF(2^8) and then applying an affine transformation.

    Returns:
        ArrayBytes: The 16x16 AES S-box.
    """
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
INV_SBOX = np.zeros(256, dtype=np.uint8)
INV_SBOX[SBOX] = np.arange(256, dtype=np.uint8)


def precompute_mix_columns_tables():
    """Precomputes tables for MixColumns to speed up the process.

    Each table represents the multiplication of a byte by one of the constants
    in the MixColumns matrix (0x01, 0x02, 0x03, 0x09, 0x0B, 0x0D, 0x0E).

    Returns:
        dict: A dictionary mapping constants to their multiplication tables.
    """
    constants = [0x01, 0x02, 0x03, 0x09, 0x0B, 0x0D, 0x0E]
    tables = {}
    for c in constants:
        table = np.zeros(256, dtype=np.uint8)
        for b in range(256):
            table[b] = gf2_multiply(c, b)
        tables[c] = table
    return tables


MIX_TABLES = precompute_mix_columns_tables()


def _aes_transform(states: NDArray, key_schedule: NDArray, reverse: bool = False) -> NDArray:
    """Core AES transformation rounds for one or more blocks.

    Args:
        states (NDArray): NumPy array of shape (4, 4) or (N, 4, 4).
        key_schedule (NDArray): Key schedule from key_expansion.
        reverse (bool, optional): If True, performs decryption. Defaults to False.

    Returns:
        NDArray: Transformed states.
    """
    if not reverse:
        # Initial round
        states = add_round_key(states, key_schedule[0])

        # Main rounds
        for i in range(1, len(key_schedule) - 1):
            states = sub_bytes(states)
            states = shift_rows(states)
            states = mix_columns(states)
            states = add_round_key(states, key_schedule[i])

        # Final round
        states = sub_bytes(states)
        states = shift_rows(states)
        states = add_round_key(states, key_schedule[-1])
    else:
        # Initial round
        states = add_round_key(states, key_schedule[-1])

        # Main rounds
        for i in range(len(key_schedule) - 2, 0, -1):
            states = shift_rows(states, reverse=True)
            states = sub_bytes(states, reverse=True)
            states = add_round_key(states, key_schedule[i])
            states = mix_columns(states, reverse=True)

        # Final round
        states = shift_rows(states, reverse=True)
        states = sub_bytes(states, reverse=True)
        states = add_round_key(states, key_schedule[0])

    return states

def key_expansion(key: bytes) -> ArrayBytes:
    """Expands the input key into a key schedule for AES.

    Args:
        key (bytes): The original encryption key (16, 24, or 32 bytes).

    Returns:
        ArrayBytes: A 3D numpy array containing the round keys.
    """
    _check_key(key)
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


def sub_bytes(state: ArrayBytes, reverse: bool = False) -> ArrayBytes:
    """Applies the S-box substitution to each byte of the state.

    Args:
        state (ArrayBytes): The current state matrix (or array of matrices).
        reverse (bool, optional): If True, uses the inverse S-box. Defaults to False.

    Returns:
        ArrayBytes: The state matrix after substitution.
    """
    box = INV_SBOX if reverse else SBOX
    return box[state].astype(np.uint8)


def shift_rows(state: ArrayBytes, reverse: bool = False) -> ArrayBytes:
    """Cyclically shifts the rows of the state matrix.

    Args:
        state (ArrayBytes): The current state matrix (or array of matrices).
        reverse (bool, optional): If True, shifts in the opposite direction for decryption. Defaults to False.

    Returns:
        ArrayBytes: The state matrix after shifting.
    """
    res = state.copy()
    for r in range(1, 4):
        # Shift each row r by r positions
        res[..., r, :] = np.roll(res[..., r, :], r if reverse else -r, axis=-1)
    return res


def mix_columns(state: ArrayBytes, reverse: bool = False) -> ArrayBytes:
    """Mixes the columns of the state matrix using GF(2^8) arithmetic.

    Args:
        state (ArrayBytes): The current state matrix (or array of matrices).
        reverse (bool, optional): If True, uses the inverse mixing matrix. Defaults to False.

    Returns:
        ArrayBytes: The state matrix after mixing.
    """
    matrix = INV_MIX_COLUMNS_M if reverse else MIX_COLUMNS_M
    new_state = np.zeros_like(state, dtype=np.uint8)
    for r in range(4):
        # Each row of the result is a combination of the rows of the input
        new_state[..., r, :] = (
            MIX_TABLES[matrix[r, 0]][state[..., 0, :]]
            ^ MIX_TABLES[matrix[r, 1]][state[..., 1, :]]
            ^ MIX_TABLES[matrix[r, 2]][state[..., 2, :]]
            ^ MIX_TABLES[matrix[r, 3]][state[..., 3, :]]
        )
    return new_state


def add_round_key(state: ArrayBytes, round_key: ArrayBytes) -> ArrayBytes:
    """XORs the state matrix with a round key.

    Args:
        state (ArrayBytes): The current 4x4 state matrix.
        round_key (ArrayBytes): The 4x4 round key matrix.

    Returns:
        ArrayBytes: The state matrix after XORing with the round key.
    """
    return np.bitwise_xor(state, round_key)


def _check_key(key: bytes):
    """Validates that the key length is valid for AES (16, 24, or 32 bytes)."""
    if not isinstance(key, (bytes, bytearray)):
        raise TypeError("Key must be bytes or bytearray.")
    if len(key) not in (16, 24, 32):
        raise ValueError("Key length must be 16, 24, or 32 bytes (128, 192, or 256 bits).")


def _check_data(data: bytes, multiple_of: int = 16, exact: bool = False, name: str = "Data"):
    """Validates the data length and type."""
    if not isinstance(data, (bytes, bytearray)):
        raise TypeError(f"{name} must be bytes or bytearray.")
    if exact:
        if len(data) != multiple_of:
            raise ValueError(f"{name} must be exactly {multiple_of} bytes.")
    elif len(data) % multiple_of != 0:
        raise ValueError(f"{name} length must be a multiple of {multiple_of} bytes.")


def aes(plaintext: bytes, key: bytes, reverse: bool = False) -> bytes:
    """Performs AES encryption or decryption on a 16-byte block.

    Args:
        plaintext (bytes): The 16-byte block to encrypt or decrypt.
        key (bytes): The encryption key (16, 24, or 32 bytes).
        reverse (bool, optional): If True, performs decryption. Defaults to False.

    Raises:
        ValueError: If plaintext is not 16 bytes or key length is invalid.

    Returns:
        bytes: The resulting 16-byte encrypted or decrypted block.
    """
    _check_data(plaintext, exact=True, name="Plaintext")

    key_schedule = key_expansion(key)
    state = np.frombuffer(plaintext, dtype=np.uint8).reshape(4, 4).T

    state = _aes_transform(state, key_schedule, reverse=reverse)

    return state.T.tobytes()

def aes_ecb(data: bytes, key: bytes, reverse: bool = False) -> bytes:
    """Performs AES encryption or decryption in ECB (Electronic Codebook) mode.

    Args:
        data (bytes): The data to encrypt or decrypt. Must be a multiple of 16 bytes.
        key (bytes): The encryption key (16, 24, or 32 bytes).
        reverse (bool, optional): If True, performs decryption. Defaults to False.

    Raises:
        ValueError: If data length is not a multiple of 16 bytes.

    Returns:
        bytes: The resulting encrypted or decrypted data.
    """
    _check_data(data)

    key_schedule = key_expansion(key)
    num_blocks = len(data) // 16
    states = (
        np.frombuffer(data, dtype=np.uint8).reshape(num_blocks, 4, 4).transpose(0, 2, 1)
    )

    states = _aes_transform(states, key_schedule, reverse=reverse)

    return states.transpose(0, 2, 1).tobytes()


def aes_cbc(data: bytes, key: bytes, iv: bytes, reverse: bool = False) -> bytes:
    """Performs AES encryption or decryption in CBC (Cipher Block Chaining) mode.

    Args:
        data (bytes): The data to encrypt or decrypt. Must be a multiple of 16 bytes.
        key (bytes): The encryption key (16, 24, or 32 bytes).
        iv (bytes): The initialization vector (16 bytes).
        reverse (bool, optional): If True, performs decryption. Defaults to False.

    Raises:
        ValueError: If data length is not a multiple of 16 bytes or IV is not 16 bytes.

    Returns:
        bytes: The resulting encrypted or decrypted data.
    """
    _check_data(data)
    _check_data(iv, exact=True, name="IV")

    key_schedule = key_expansion(key)

    if not reverse:
        result = bytearray()
        prev_block = np.frombuffer(iv, dtype=np.uint8).reshape(4, 4).T
        for i in range(0, len(data), 16):
            block = np.frombuffer(data[i : i + 16], dtype=np.uint8).reshape(4, 4).T
            # XOR with previous ciphertext (or IV for the first block)
            xored = add_round_key(block, prev_block)
            encrypted_state = _aes_transform(xored, key_schedule, reverse=False)
            result.extend(encrypted_state.T.tobytes())
            prev_block = encrypted_state
        return bytes(result)
    else:
        num_blocks = len(data) // 16
        # Vectorize decryption part of CBC
        ciphertext_states = (
            np.frombuffer(data, dtype=np.uint8)
            .reshape(num_blocks, 4, 4)
            .transpose(0, 2, 1)
        )
        decrypted_states = _aes_transform(ciphertext_states, key_schedule, reverse=True)

        # Prepare blocks for XORing (previous ciphertext blocks + IV)
        iv_state = np.frombuffer(iv, dtype=np.uint8).reshape(4, 4).T
        prev_states = np.empty_like(ciphertext_states)
        prev_states[0] = iv_state
        if num_blocks > 1:
            prev_states[1:] = ciphertext_states[:-1]

        # Final XOR step (vectorized)
        plaintext_states = decrypted_states ^ prev_states
        return plaintext_states.transpose(0, 2, 1).tobytes()
