import pytest
from krypto_lib.utils import str_to_bytes, bytes_to_str, int_to_bytes, bytes_to_int, hex_to_bytes, bytes_to_hex, pad_bytes

def test_str_to_bytes_and_back():
    original_str = "Hello, Krypto!"
    b = str_to_bytes(original_str)
    converted_str = bytes_to_str(b)
    assert original_str == converted_str

def test_int_to_bytes_and_back():
    original_int = 123456789
    length = 4
    b = int_to_bytes(original_int, length, 'big')
    converted_int = bytes_to_int(b, 'big')
    assert original_int == converted_int

def test_hex_to_bytes_and_back():
    original_hex = "deadbeef"
    b = hex_to_bytes(original_hex)
    converted_hex = bytes_to_hex(b)
    assert original_hex == converted_hex

def test_pad_bytes():
    original_bytes = b'\x01\x02\x03'
    resized_left = pad_bytes(original_bytes, 5, pad_byte=b'\x00', from_left=True)
    resized_right = pad_bytes(original_bytes, 5, pad_byte=b'\x00', from_left=False)

    assert resized_left == b'\x00\x00\x01\x02\x03'
    assert resized_right == b'\x01\x02\x03\x00\x00'

    # Test error on smaller size
    with pytest.raises(ValueError):
        pad_bytes(original_bytes, 2)
