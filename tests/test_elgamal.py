from krypto_lib.asymmetric.discrete_logarithm.elgamal import generate_keys, encrypt, decrypt, encrypt_multi

def test_elgamal():
    p = 2357
    g = 2
    message = 1234

    # Key Generation
    private_key, public_key = generate_keys(p, g, x=175)
    print(f"Private Key: {private_key}")
    print(f"Public Key: {public_key}")

    # Encryption
    a, b = encrypt(p, g, public_key, message, k=112)
    print(f"Encrypted Message: (a={a}, b={b})")

    # Decryption
    decrypted_message = decrypt(p, private_key, a, b)
    print(f"Decrypted Message: {decrypted_message}")

    assert decrypted_message == message

def test_elgamal_multi():
    p = 2357
    g = 2
    message = 555

    # Recipient 1
    x1, y1 = generate_keys(p, g, x=100)
    # Recipient 2
    x2, y2 = generate_keys(p, g, x=200)

    # Broadcast encryption
    a, bs = encrypt_multi(p, g, [y1, y2], message, k=50)

    m1 = decrypt(p, x1, a, bs[0])
    m2 = decrypt(p, x2, a, bs[1])

    assert m1 == message
    assert m2 == message
