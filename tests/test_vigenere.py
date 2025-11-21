import pytest
import string
from krypto_lib.symmetric.vigenere import encrypt

# Test data for Vigenère cipher
plaintext = "ATTACK AT DAWN!"
key = "LEMON"


def test_encrypt_basic():
    ciphertext = encrypt(plaintext.replace(" ", ""), key)
    ciphertext_lower = encrypt(
        plaintext.replace(" ", "").lower(), key.lower(), alphabet=string.ascii_lowercase
    )
    assert isinstance(ciphertext, str)
    assert len(ciphertext) == len(plaintext.replace(" ", ""))
    assert ciphertext == "LXFOPVEFRNHR!"
    assert encrypt(ciphertext, key, reverse=True) == plaintext.replace(" ", "")
    assert ciphertext_lower == "lxfopvefrnhr!"
    assert (
        encrypt(
            ciphertext_lower, key.lower(), alphabet=string.ascii_lowercase, reverse=True
        )
        == plaintext.replace(" ", "").lower()
    )


def test_encrypt_with_non_alphabet_chars():
    ciphertext = encrypt(plaintext, key)
    assert isinstance(ciphertext, str)
    assert len(ciphertext) == len(plaintext)
    assert ciphertext == "LXFOPV EF RNHR!"
    assert encrypt("LXFOPV EF RNHR!", key, reverse=True) == plaintext
