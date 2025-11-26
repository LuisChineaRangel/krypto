import math
import pytest
import string
from krypto_lib.utils import int_blocks_to_str
from krypto_lib.asymmetric.factorization.rsa import rsa

plaintext = "HELLO"
e = 65537
p = 61
q = 53
block_size = math.floor(math.log(p * q, len(string.ascii_uppercase)))
lengths = [len(plaintext[i:i + block_size]) for i in range(0, len(plaintext), block_size)]

def test_rsa_encryption():
    encrypted_text = rsa(plaintext, e, p, q, string.ascii_uppercase)
    encrypted_text_str = int_blocks_to_str(encrypted_text, lengths, string.ascii_uppercase)
    expected_encrypted_text = [601, 826, 2549]
    assert encrypted_text == expected_encrypted_text
    assert encrypted_text_str != plaintext  # Ensure encryption changes the text

def test_rsa_decryption():
    encrypted_text = [601, 826, 2549]
    decrypted_text = rsa(encrypted_text, e, p, q, string.ascii_uppercase, decrypt=True)
    decrypted_text_str = int_blocks_to_str(decrypted_text, lengths, string.ascii_uppercase)

    assert decrypted_text_str == plaintext
    assert decrypted_text != encrypted_text  # Ensure decryption changes the text

def test_rsa_invalid_primes():
    with pytest.raises(ValueError, match="Both p and q must be prime numbers."):
        rsa(plaintext, e, 60, 53, string.ascii_uppercase)
    with pytest.raises(ValueError, match="Both p and q must be prime numbers."):
        rsa(plaintext, e, 61, 54, string.ascii_uppercase)

def test_rsa_non_coprime_e_phi():
    with pytest.raises(ValueError, match="e and φ\\(n\\) are not coprime."):
        rsa(plaintext, 12, 61, 53, string.ascii_uppercase)  # 12 is not coprime with φ(61*53)=3120
