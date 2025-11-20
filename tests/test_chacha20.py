import pytest
from krypto_lib.symmetric.chacha20 import encrypt, keystream_block
from krypto_lib.utils import bytes_to_hex

# Test data for ChaCha20
key = bytes.fromhex(
    "f95fd5b41783595e41f4cbcd8dc26a782599184e97ccd768ac531aae729781d3"
)
nonce = bytes.fromhex("84133f2261ef44796e3669dc")
plaintext = b"Python & ChaCha20 encryption example."
initial_counter = 1

def test_encrypt_returns_bytes():
    ciphertext = encrypt(plaintext, key, nonce, initial_counter)
    assert isinstance(ciphertext, bytes)
    assert len(ciphertext) == len(plaintext)

def test_keystream_block_length():
    ks = keystream_block(key, initial_counter, nonce)
    assert isinstance(ks, bytes)
    assert len(ks) == 64  # ChaCha20 block size is 64 bytes

def test_encrypt_deterministic():
    ct1 = encrypt(plaintext, key, nonce, initial_counter)
    ct2 = encrypt(plaintext, key, nonce, initial_counter)
    assert ct1 == ct2  # Same input and key produce the same ciphertext

def test_encrypt_xor_property():
    ciphertext = encrypt(plaintext, key, nonce, initial_counter)
    # XOR plaintext ^ keystream = ciphertext
    from krypto_lib.symmetric.chacha20 import keystream_block
    ks = keystream_block(key, initial_counter, nonce)
    # Only the first bytes, because the block is 64 bytes
    ct_manual = bytes([p ^ k for p, k in zip(plaintext, ks)])
    assert ct_manual == ciphertext
