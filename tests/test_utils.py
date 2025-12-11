import pytest
import krypto_lib.utils as utils


def test_pad_bytes():
    original_bytes = b"\x01\x02\x03"
    resized_left = utils.pad_bytes(original_bytes, 5, pad_byte=b"\x00", from_left=True)
    resized_right = utils.pad_bytes(
        original_bytes, 5, pad_byte=b"\x00", from_left=False
    )

    assert resized_left == b"\x00\x00\x01\x02\x03"
    assert resized_right == b"\x01\x02\x03\x00\x00"

    # Test error on smaller size
    with pytest.raises(ValueError):
        utils.pad_bytes(original_bytes, 2)


def test_fast_pow():
    assert utils.fast_pow(2, 3, 5) == 3  # 2^3 % 5 = 8 % 5 = 3
    assert utils.fast_pow(3, 4, 7) == 4  # 3^4 % 7 = 81 % 7 = 4
    assert utils.fast_pow(10, 0, 6) == 1  # Any number to the power of 0 is 1
    assert utils.fast_pow(5, 3, 13) == 8  # 5^3 % 13 = 125 % 13 = 8


def test_lehman_peralta_primality_test():
    # Test cases for number 1
    assert utils.lehman_peralta_primality_test(1) == False

    # Test known primes
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    for prime in primes:
        assert utils.lehman_peralta_primality_test(prime) == True

    # Test known composites
    composites = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
    for composite in composites:
        assert utils.lehman_peralta_primality_test(composite) == False


def test_euclid_extended():
    a, b = 30, 12
    gcd, x, y = utils.euclid_extended(a, b)
    assert gcd == 6
    assert a * x + b * y == gcd

    a, b = 101, 23
    gcd, x, y = utils.euclid_extended(a, b)
    assert gcd == 1
    assert a * x + b * y == gcd

def test_gf2_multiply():
    multiply_cases = [
        (0x57, 0x83, 0xc1),
        (0x07, 0x0B, 0x31),
        (0x13, 0x11, 0x38),
        (0xFF, 0xFF, 0x13),
        (0x01, 0x01, 0x01),
        (0x00, 0xAB, 0x00),
        (0xAB, 0x00, 0x00),
    ]
    for a, b, expected in multiply_cases:
        assert utils.gf2_multiply(a, b) == expected

def test_gf2_pow():
    pow_cases = [
        (0x02, 0x03 , 0x08),
        (0x02, 0x04 , 0x10),
        (0x02, 0x14 , 0x97),
        (0x03, 0x0A , 0x72),
        (0x03, 0x05 , 0x33),
    ]
    for base, exponent, expected in pow_cases:
        assert utils.gf2_pow(base, exponent) == expected

def test_gf2_inverse():
    inverse_cases = [
        (0x01, 0x01),
        (0x02, 0x8D),
        (0x03, 0xF6),
        (0x0B, 0xC0),
        (0x13, 0x4B),
        (0x57, 0xBF),
        (0x83, 0x80),
    ]
    for a, expected in inverse_cases:
        assert utils.gf2_inverse(a) == expected
    with pytest.raises(ValueError):
        utils.gf2_inverse(0x00)  # Inverse of 0 does not exist
