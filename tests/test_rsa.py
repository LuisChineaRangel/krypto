import pytest
import string
from krypto_lib.asymmetric.factorization.rsa import rsa

def test_rsa_encryption():
    plaintext = "HELLO"
    e = 65537
    p = 61
    q = 53

    ciphertext = rsa(plaintext, e, p, q, string.ascii_uppercase)

    # Expected ciphertext calculated manually or from a trusted source
    expected_ciphertext = [2790, 576, 1283]

    assert ciphertext == expected_ciphertext
