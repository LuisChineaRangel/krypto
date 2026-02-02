from krypto_lib.asymmetric.elliptic_curve.ecc import EllipticCurve, Point
from krypto_lib.asymmetric.elliptic_curve.ecdh import ecdh, ecdh_group

def test_ecdh_basic():
    # Curve: y^2 = x^3 + 2x + 2 (mod 17)
    curve = EllipticCurve(a=2, b=2, p=17)
    G = Point(curve, 5, 1) # Generator point

    private_a = 6
    private_b = 10

    shared_secret = ecdh(curve, private_a, private_b, G)

    # QA = 6 * (5,1) = (13, 10)
    # QB = 10 * (5,1) = (7, 11)
    # S = 10 * (13, 10) = 6 * (7, 11) = (10, 6)

    assert shared_secret.x == 10
    assert shared_secret.y == 6

def test_ecdh_group():
    # Curve: y^2 = x^3 + 2x + 2 (mod 17)
    curve = EllipticCurve(a=2, b=2, p=17)
    G = Point(curve, 5, 1)

    # 3 users with secrets 2, 3, 4
    # Result should be (2 * 3 * 4) * G = 24 * G
    # Since the order of G in this curve is 19 (let's verify or just trust the math)
    # y^2 = x^3 + 2x + 2 (mod 17)
    # Points: Inf, (5,1), (6,3), (10,6), (3,1), (9,16), (16,13), (0,6), (13,7), (7,6), (7,11), (13,10), (0,11), (16,4), (9,1), (3,16), (10,11), (6,14), (5,16) -> 19 points
    # 24 * G = (24 mod 19) * G = 5 * G

    secrets = [2, 3, 4]
    shared_secret = ecdh_group(curve, secrets, G)

    # 5 * G = 2 * G + 3 * G
    # 2*G = (6,3)
    # 3*G = (10,6)
    # (6,3) + (10,6) -> lambda = (6-3)/(10-6) = 3/4 mod 17. 4*13=52=1 mod 17. lambda = 3*13 = 39 = 5 mod 17.
    # x3 = 5^2 - 6 - 10 = 25 - 16 = 9.
    # y3 = 5*(6-9) - 3 = 5*(-3) - 3 = -15 - 3 = -18 = 16 mod 17.
    # 5 * G = (9, 16)

    assert shared_secret.x == 9
    assert shared_secret.y == 16
