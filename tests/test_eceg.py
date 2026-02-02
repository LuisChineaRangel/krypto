from krypto_lib.asymmetric.elliptic_curve.ecc import EllipticCurve, Point
from krypto_lib.asymmetric.elliptic_curve.eceg import eceg_encrypt, eceg_decrypt, eceg_encrypt_multi

def test_eceg_basic():
    # Curve: y^2 = x^3 + 2x + 2 (mod 17)
    curve = EllipticCurve(a=2, b=2, p=17)
    G = Point(curve, 5, 1) # Generator point

    # Private Key d = 7
    d = 7
    # Public Key Q = d * G
    Q = G * d

    # Message M = (10, 6)
    M = Point(curve, 10, 6)

    # Random k = 3
    k = 3

    # Encryption
    C1, C2 = eceg_encrypt(G, Q, M, k)

    # Decryption
    M_decrypted = eceg_decrypt(d, (C1, C2))

    assert M_decrypted == M

def test_eceg_infinity():
    curve = EllipticCurve(a=2, b=2, p=17)
    G = Point(curve, 5, 1)
    d = 4
    Q = G * d

    # Message is Point at Infinity
    M = Point(curve)
    k = 5

    C1, C2 = eceg_encrypt(G, Q, M, k)
    M_decrypted = eceg_decrypt(d, (C1, C2))

    assert M_decrypted == M

def test_eceg_multi():
    curve = EllipticCurve(a=2, b=2, p=17)
    G = Point(curve, 5, 1)

    # Message
    M = Point(curve, 10, 6)

    # Recipients
    d1 = 3
    Q1 = G * d1
    d2 = 5
    Q2 = G * d2

    # Encryption
    C1, C2s = eceg_encrypt_multi(G, [Q1, Q2], M, k=7)

    M1 = eceg_decrypt(d1, (C1, C2s[0]))
    M2 = eceg_decrypt(d2, (C1, C2s[1]))

    assert M1 == M
    assert M2 == M
