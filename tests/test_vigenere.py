import pytest
import string
from krypto_lib.symmetric.vigenere import encrypt

# Test data for Vigenère cipher
plaintext = "ATTACK AT DAWN!"
key = "LEMON"


def test_encrypt_basic():
    ciphertext = encrypt(plaintext.replace(" ", ""), key, string.ascii_uppercase)
    assert isinstance(ciphertext, str)
    assert len(ciphertext) == len(plaintext.replace(" ", ""))
    assert ciphertext == "LXFOPVEFRNHR!"
    assert encrypt(ciphertext, key, string.ascii_uppercase, reverse=True) == plaintext.replace(" ", "")

def test_encrypt_with_non_alphabet_chars():
    ciphertext = encrypt(plaintext, key, string.ascii_uppercase)
    assert isinstance(ciphertext, str)
    assert len(ciphertext) == len(plaintext)
    assert ciphertext == "LXFOPV EF RNHR!"
    assert encrypt("LXFOPV EF RNHR!", key, string.ascii_uppercase, reverse=True) == plaintext
