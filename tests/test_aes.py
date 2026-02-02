import numpy as np
from krypto_lib.symmetric.block.aes import (
    generate_sbox,
    sub_bytes,
    shift_rows,
    mix_columns,
    add_round_key,
    key_expansion,
    aes,
    aes_ecb,
    aes_cbc,
)


def test_generate_sbox():
    expected_sbox_strings = np.array(
        [
            "63 7C 77 7B F2 6B 6F C5 30 01 67 2B FE D7 AB 76",
            "CA 82 C9 7D FA 59 47 F0 AD D4 A2 AF 9C A4 72 C0",
            "B7 FD 93 26 36 3F F7 CC 34 A5 E5 F1 71 D8 31 15",
            "04 C7 23 C3 18 96 05 9A 07 12 80 E2 EB 27 B2 75",
            "09 83 2C 1A 1B 6E 5A A0 52 3B D6 B3 29 E3 2F 84",
            "53 D1 00 ED 20 FC B1 5B 6A CB BE 39 4A 4C 58 CF",
            "D0 EF AA FB 43 4D 33 85 45 F9 02 7F 50 3C 9F A8",
            "51 A3 40 8F 92 9D 38 F5 BC B6 DA 21 10 FF F3 D2",
            "CD 0C 13 EC 5F 97 44 17 C4 A7 7E 3D 64 5D 19 73",
            "60 81 4F DC 22 2A 90 88 46 EE B8 14 DE 5E 0B DB",
            "E0 32 3A 0A 49 06 24 5C C2 D3 AC 62 91 95 E4 79",
            "E7 C8 37 6D 8D D5 4E A9 6C 56 F4 EA 65 7A AE 08",
            "BA 78 25 2E 1C A6 B4 C6 E8 DD 74 1F 4B BD 8B 8A",
            "70 3E B5 66 48 03 F6 0E 61 35 57 B9 86 C1 1D 9E",
            "E1 F8 98 11 69 D9 8E 94 9B 1E 87 E9 CE 55 28 DF",
            "8C A1 89 0D BF E6 42 68 41 99 2D 0F B0 54 BB 16",
        ],
        dtype=str,
    )
    expected_sbox = np.array(
        [[int(byte, 16) for byte in row.split()] for row in expected_sbox_strings],
        dtype=int,
    )
    sbox = generate_sbox()
    assert len(sbox) == 16
    assert len(sbox) == len(expected_sbox)
    assert all(np.array_equal(sbox[i], expected_sbox[i]) for i in range(16))


def test_sub_bytes():
    sbox = generate_sbox().flatten()
    input = np.array(
        [
            [0x32, 0x88, 0x31, 0xE0],
            [0x43, 0x5A, 0x31, 0x37],
            [0xF6, 0x30, 0x98, 0x07],
            [0xA8, 0x8D, 0xA3, 0x2B],
        ],
        dtype=np.uint8,
    )
    expected = sbox[input]
    output = sub_bytes(input)
    assert len(output) == 4
    assert len(output) == len(expected)
    assert np.array_equal(output, expected)


def test_shift_rows():
    input = np.array(
        [
            [0x00, 0x01, 0x02, 0x03],
            [0x10, 0x11, 0x12, 0x13],
            [0x20, 0x21, 0x22, 0x23],
            [0x30, 0x31, 0x32, 0x33],
        ],
        dtype=np.uint8,
    )
    expected = np.array(
        [
            [0x00, 0x01, 0x02, 0x03],
            [0x11, 0x12, 0x13, 0x10],
            [0x22, 0x23, 0x20, 0x21],
            [0x33, 0x30, 0x31, 0x32],
        ],
        dtype=np.uint8,
    )
    output = shift_rows(input)
    assert len(output) == 4
    assert len(output) == len(expected)
    assert np.array_equal(output, expected)


def test_mix_columns():
    input = np.array(
        [
            [0xDB, 0xF2, 0x01, 0xC6],
            [0x13, 0x0A, 0x01, 0xC6],
            [0x53, 0x22, 0x01, 0xC6],
            [0x45, 0x5C, 0x01, 0xC6],
        ],
        dtype=np.uint8,
    )
    expected = np.array(
        [
            [0x8E, 0x9F, 0x01, 0xC6],
            [0x4D, 0xDC, 0x01, 0xC6],
            [0xA1, 0x58, 0x01, 0xC6],
            [0xBC, 0x9D, 0x01, 0xC6],
        ],
        dtype=np.uint8,
    )
    output = mix_columns(input)
    assert len(output) == 4
    assert len(output) == len(expected)
    assert np.array_equal(output, expected)


def test_add_round_key():
    input = np.array(
        [
            [0x32, 0x88, 0x31, 0xE0],
            [0x43, 0x5A, 0x31, 0x37],
            [0xF6, 0x30, 0x98, 0x07],
            [0xA8, 0x8D, 0xA2, 0x34],
        ],
        dtype=np.uint8,
    )
    round_key = np.array(
        [
            [0xA0, 0xFA, 0xFE, 0x17],
            [0x88, 0x54, 0x2C, 0xB1],
            [0x23, 0xA3, 0x39, 0x39],
            [0x2A, 0x6C, 0x76, 0x05],
        ],
        dtype=np.uint8,
    )
    expected = np.array(
        [
            [0x92, 0x72, 0xCF, 0xF7],
            [0xCB, 0x0E, 0x1D, 0x86],
            [0xD5, 0x93, 0xA1, 0x3E],
            [0x82, 0xE1, 0xD4, 0x31],
        ],
        dtype=np.uint8,
    )
    output = add_round_key(input, round_key)
    assert np.array_equal(output, expected)


def test_key_expansion():
    key = bytes.fromhex("2b7e151628aed2a6abf7158809cf4f3c")
    # Only test the first, second, and last round keys
    expected = np.array(
        [
            [
                [0x2B, 0x28, 0xAB, 0x09],
                [0x7E, 0xAE, 0xF7, 0xCF],
                [0x15, 0xD2, 0x15, 0x4F],
                [0x16, 0xA6, 0x88, 0x3C],
            ],
            [
                [0xA0, 0x88, 0x23, 0x2A],
                [0xFA, 0x54, 0xA3, 0x6C],
                [0xFE, 0x2C, 0x39, 0x76],
                [0x17, 0xB1, 0x39, 0x05],
            ],
            [
                [0xD0, 0xC9, 0xE1, 0xB6],
                [0x14, 0xEE, 0x3F, 0x63],
                [0xF9, 0x25, 0x0C, 0x0C],
                [0xA8, 0x89, 0xC8, 0xA6],
            ],
        ],
        dtype=np.uint8,
    )
    key_schedule = key_expansion(key)
    assert np.array_equal(key_schedule[0], expected[0])
    assert np.array_equal(key_schedule[1], expected[1])
    assert np.array_equal(key_schedule[-1], expected[-1])
    assert len(key_schedule) == 11  # AES-128 has 11 round keys


def test_aes_encryption():
    key = bytes.fromhex("2b7e151628aed2a6abf7158809cf4f3c")
    plaintext = bytes.fromhex("3243f6a8885a308d313198a2e0370734")
    expected_ciphertext = bytes.fromhex("3925841d02dc09fbdc118597196a0b32")

    ciphertext = aes(plaintext, key)
    assert ciphertext == expected_ciphertext

    key = bytes.fromhex("5468617473206D79204B756E67204675")
    plaintext = bytes.fromhex("54776F204F6E65204E696E652054776F")
    expected_ciphertext = bytes.fromhex("29C3505F571420F6402299B31A02D73A")

    ciphertext = aes(plaintext, key)
    assert ciphertext == expected_ciphertext

    # 32 bytes key (AES-256)
    key = bytes.fromhex("000102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F")
    plaintext = bytes.fromhex("00112233445566778899AABBCCDDEEFF")
    expected_ciphertext = bytes.fromhex("8EA2B7CA516745BFEAFC49904B496089")

    ciphertext = aes(plaintext, key)
    assert ciphertext == expected_ciphertext


def test_aes_decryption():
    key = bytes.fromhex("2b7e151628aed2a6abf7158809cf4f3c")
    ciphertext = bytes.fromhex("3925841d02dc09fbdc118597196a0b32")
    expected_plaintext = bytes.fromhex("3243f6a8885a308d313198a2e0370734")

    plaintext = aes(ciphertext, key, reverse=True)
    assert plaintext == expected_plaintext

    # Check consistency
    p = bytes.fromhex("00112233445566778899AABBCCDDEEFF")
    k = bytes.fromhex("000102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F")
    c = aes(p, k)
    assert aes(c, k, reverse=True) == p


def test_inverse_functions():
    state = np.random.randint(0, 256, (4, 4), dtype=np.uint8)

    # SubBytes
    assert np.array_equal(sub_bytes(sub_bytes(state), reverse=True), state)

    # ShiftRows
    assert np.array_equal(shift_rows(shift_rows(state), reverse=True), state)

    # MixColumns
    # Note: MixColumns inverse only works if state is valid
    assert np.array_equal(mix_columns(mix_columns(state), reverse=True), state)


def test_aes_ecb():
    key = bytes.fromhex("2b7e151628aed2a6abf7158809cf4f3c")
    # 32 bytes (2 blocks)
    plaintext = bytes.fromhex(
        "3243f6a8885a308d313198a2e0370734" "00112233445566778899aabbccddeeff"
    )

    ciphertext = aes_ecb(plaintext, key)
    assert len(ciphertext) == 32

    decrypted = aes_ecb(ciphertext, key, reverse=True)
    assert decrypted == plaintext

    # Verify blocks are independent (characteristic of ECB)
    block1 = plaintext[:16]
    block2 = plaintext[16:]
    assert ciphertext[:16] == aes(block1, key)
    assert ciphertext[16:] == aes(block2, key)


def test_aes_cbc():
    key = bytes.fromhex("2b7e151628aed2a6abf7158809cf4f3c")
    iv = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
    plaintext = bytes.fromhex(
        "3243f6a8885a308d313198a2e0370734" "00112233445566778899aabbccddeeff"
    )

    ciphertext = aes_cbc(plaintext, key, iv)
    assert len(ciphertext) == 32
    assert ciphertext != aes_ecb(plaintext, key)  # CBC should be different from ECB

    decrypted = aes_cbc(ciphertext, key, iv, reverse=True)
    assert decrypted == plaintext

    # Verify chain property
    block1 = plaintext[:16]
    xored1 = bytes([b ^ i for b, i in zip(block1, iv)])
    expected_c1 = aes(xored1, key)
    assert ciphertext[:16] == expected_c1

    block2 = plaintext[16:]
    xored2 = bytes([b ^ c for b, c in zip(block2, expected_c1)])
    expected_c2 = aes(xored2, key)
    assert ciphertext[16:] == expected_c2
