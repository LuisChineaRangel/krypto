from typing import Literal

def str_to_bytes(s:str, encoding:str='utf-8') -> bytes:
    """Converts a string to bytes using the specified encoding.
    Args:
        s (str): The input string to convert.
        encoding (str, optional): The encoding to use. Defaults to 'utf-8'.
    Returns:
        bytes: The encoded byte representation of the string.
    """
    return s.encode(encoding)

def bytes_to_str(b:bytes, encoding:str='utf-8') -> str:
    """Converts bytes to a string using the specified encoding.
    Args:
        b (bytes): The input bytes to convert.
        encoding (str, optional): The encoding to use. Defaults to 'utf-8'.
    Returns:
        str: The decoded string representation of the bytes.
    """
    return b.decode(encoding)

def int_to_bytes(n:int, length:int, endian:Literal['big', 'little']='big') -> bytes:
    """ Converts an integer to bytes of specified length and endianness.
    Args:
        n (int): The integer to convert.
        length (int): The length of the resulting byte sequence.
        endian (Literal['big', 'little'], optional): Byte order, either "big" or "little". Defaults to "big".
    Returns:
        bytes: The byte representation of the integer.
    """
    return n.to_bytes(length, endian)

def bytes_to_int(b:bytes, endian:Literal['big', 'little']='big') -> int:
    """Converts bytes to an integer with specified endianness.
    Args:
        b (bytes): The byte sequence to convert.
        endian (Literal['big', 'little'], optional): Byte order, either "big" or "little". Defaults to "big".
    Returns:
        int: The integer representation of the byte sequence.
    """
    return int.from_bytes(b, endian)

def hex_to_bytes(hex_str:str) -> bytes:
    """Converts a hexadecimal string to bytes.
    Args:
        hex_str (str): The hexadecimal string to convert.
    Returns:
        bytes: The byte representation of the hexadecimal string.
    """
    return bytes.fromhex(hex_str)

def bytes_to_hex(b:bytes) -> str:
    """Converts bytes to a hexadecimal string.
    Args:
        b (bytes): The byte sequence to convert.
    Returns:
        str: The hexadecimal string representation of the bytes.
    """
    return b.hex()

def resize_bytes(b:bytes, size:int, pad_byte:bytes=b'\x00', from_left:bool=False) -> bytes:
    """Resizes a byte sequence to the specified size by padding.
    Args:
        b (bytes): The byte sequence to resize.
        size (int): The desired size of the byte sequence.
        pad_byte (bytes, optional): The byte to use for padding. Defaults to b'\x00'.
        from_left (bool, optional): If True, pad from the left. Otherwise, pad from the right. Defaults to False.
    Raises:
        ValueError: If the byte sequence is longer than the desired size.
    Returns:
        bytes: The resized byte sequence.
    """
    if len(b) > size:
        raise ValueError("Byte sequence is longer than the desired size")
    padding = pad_byte * (size - len(b))
    return (padding + b) if from_left else (b + padding)
