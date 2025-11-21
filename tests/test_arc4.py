import pytest
from krypto_lib.symmetric.stream.arc4 import ksa, prga, arc4

def test_ksa_length():
    key = b"testkey"
    S = ksa(key)
    assert len(S) == 256
    assert all(0 <= x <= 255 for x in S)

def test_prga_length():
    key = b"testkey"
    S = ksa(key)
    keystream = list(prga(S, 10))
    assert len(keystream) == 10
    assert all(0 <= x <= 255 for x in keystream)

def test_arc4_encrypt_decrypt():
    key = b"secret"
    plaintext = b"Hello, ARC4!"
    ciphertext = arc4(plaintext, key)
    assert ciphertext != plaintext
    decrypted = arc4(ciphertext, key)
    assert decrypted == plaintext

def test_empty_data():
    key = b"secret"
    assert arc4(b"", key) == b""

def test_different_keys():
    data = b"Sample data for ARC4."
    key1 = b"evasive"
    key2 = b"secret"
    out1 = arc4(data, key1)
    out2 = arc4(data, key2)
    assert out1 != out2
