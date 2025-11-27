import pytest
from krypto_lib.symmetric.stream.chacha20 import chacha20, keystream_block

# Test data for ChaCha20
key = bytes.fromhex(
    "f95fd5b41783595e41f4cbcd8dc26a782599184e97ccd768ac531aae729781d3"
)
nonce = bytes.fromhex("84133f2261ef44796e3669dc")
plaintext = b"Python & ChaCha20 encryption example."
initial_counter = 1

def test_error_on_invalid_types():
    with pytest.raises(TypeError):
        chacha20(plaintext, key, nonce, initial_counter, hex_input=True)

    invalid_key = bytes.fromhex("1234")
    invalid_nonce = bytes.fromhex("5678")
    invalid_counter = 99999999999999999999999999999999999  # Too large

    with pytest.raises(ValueError):
        chacha20(plaintext, invalid_key, nonce, initial_counter)
    with pytest.raises(ValueError):
        chacha20(plaintext, key, invalid_nonce, initial_counter)
    with pytest.raises(ValueError):
        chacha20(plaintext, key, nonce, invalid_counter)
def test_encrypt_returns_bytes():
    ciphertext = chacha20(plaintext, key, nonce, initial_counter)
    assert isinstance(ciphertext, bytes)
    assert len(ciphertext) == len(plaintext)

def test_encrypt_with_string_input():
    text_plaintext = plaintext.decode("utf-8")
    ciphertext = chacha20(text_plaintext, key, nonce, initial_counter)
    assert isinstance(ciphertext, bytes)
    assert len(ciphertext) == len(plaintext)

def test_encrypt_with_hex_input():
    hex_plaintext = plaintext.hex()
    ciphertext = chacha20(
        hex_plaintext, key, nonce, initial_counter, hex_input=True
    )
    assert isinstance(ciphertext, bytes)
    assert len(ciphertext) == len(plaintext)

def test_keystream_block_length():
    ks = keystream_block(key, initial_counter, nonce)
    assert isinstance(ks, bytes)
    assert len(ks) == 64  # ChaCha20 block size is 64 bytes

def test_encrypt_deterministic():
    ct1 = chacha20(plaintext, key, nonce, initial_counter)
    ct2 = chacha20(plaintext, key, nonce, initial_counter)
    assert ct1 == ct2  # Same input and key produce the same ciphertext

def test_encrypt_xor_property():
    ciphertext = chacha20(plaintext, key, nonce, initial_counter)
    # XOR plaintext ^ keystream = ciphertext
    ks = keystream_block(key, initial_counter, nonce)
    # Only the first bytes, because the block is 64 bytes
    ct_manual = bytes([p ^ k for p, k in zip(plaintext, ks)])
    assert ct_manual == ciphertext
