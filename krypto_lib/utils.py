def str_to_bytes(s, encoding='utf-8'):
    return s.encode(encoding)

def bytes_to_str(b, encoding='utf-8'):
    return b.decode(encoding)

def int_to_bytes(n, length, endian='big'):
    return n.to_bytes(length, endian)

def bytes_to_int(b, endian='big'):
    return int.from_bytes(b, endian)

def hex_to_bytes(hex_str):
    return bytes.fromhex(hex_str)

def bytes_to_hex(b):
    return b.hex()
