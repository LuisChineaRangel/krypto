from krypto_lib.asymmetric.discrete_logarithm.diffie_hellman import diffie_hellman, diffie_hellman_group
import pytest

def test_diffie_hellman_basic():
    p = 23
    g = 5
    private_a = 6
    private_b = 15

    # The shared secret should be g^(a*b) mod p
    # 5^(6*15) mod 23 = 5^90 mod 23
    # 5^2 = 25 = 2 mod 23
    # 5^90 = (5^2)^45 = 2^45 mod 23
    # 2^11 = 2048 = 2048 / 23 = 89.04 -> 89 * 23 = 2047 -> 2048 mod 23 = 1
    # 2^45 = (2^11)^4 * 2 = 1^4 * 2 = 2 mod 23

    shared_key = diffie_hellman(p, g, private_a, private_b)
    assert shared_key == 2

def test_diffie_hellman_group():
    # Test with 3 users
    p = 23
    g = 5
    secrets = [6, 15, 11]

    # Key: ((g^a)^b)^c mod p
    # We already know that g^(a*b) mod 23 = 2
    # 2^11 mod 23 = 1

    shared_key = diffie_hellman_group(p, g, secrets)
    assert shared_key == 1
def test_diffie_hellman_invalid_prime():
    with pytest.raises(ValueError, match="P number must be prime."):
        diffie_hellman(10, 2, 3, 4)

def test_diffie_hellman_invalid_g():
    with pytest.raises(ValueError, match="Base g must be in the range 1 < g < p."):
        diffie_hellman(23, 1, 3, 4)
    with pytest.raises(ValueError, match="Base g must be in the range 1 < g < p."):
        diffie_hellman(23, 23, 3, 4)

def test_diffie_hellman_group_insufficient_secrets():
    with pytest.raises(ValueError, match="At least 2 secrets are required."):
        diffie_hellman_group(23, 5, [6])
