from krypto_lib.asymmetric.elliptic_curve.ecc import EllipticCurve, Point

def test_point_arithmetic():
    # Curve: y^2 = x^3 + 2x + 2 (mod 17)
    curve = EllipticCurve(a=2, b=2, p=17)

    # Point P = (5, 1)
    P = Point(curve, 5, 1)

    # Verify P + Infinity = P
    Inf = Point(curve)
    assert P + Inf == P
    assert Inf + P == P

    P_neg = Point(curve, 5, 16)
    assert P + P_neg == Inf

    P2 = P + P
    assert P2.x == 6 and P2.y == 3

    # Scalar multiplication
    P3 = P * 3
    assert P3.x == 10 and P3.y == 6

    curve = EllipticCurve(a=-2, b=0, p=89)
    P = Point(curve, 29, 37)
    P3 = P * 3
    P5 = P * 5
    assert P3.x == 70 and P3.y ==78
    assert P5.x == 27 and P5.y ==82

if __name__ == "__main__":
    test_point_arithmetic()
