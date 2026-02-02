from krypto_lib.asymmetric.elliptic_curve.ecc import EllipticCurve, Point

def ecdh(curve: EllipticCurve, private_a: int, private_b: int, base_point: Point) -> Point:
    if base_point.is_infinity:
        raise ValueError("Base point cannot be the point at infinity.")
    if base_point.curve != curve:
        raise ValueError("Base point must be on the given curve.")

    # Alice computes her public key
    public_a = base_point * private_a

    # Bob computes his public key
    public_b = base_point * private_b

    # Both compute the shared secret
    shared_secret_a = public_b * private_a
    shared_secret_b = public_a * private_b

    if shared_secret_a != shared_secret_b:
        raise ValueError("Shared secrets do not match.")

    return shared_secret_a

def ecdh_group(curve: EllipticCurve, secrets: list[int], base_point: Point) -> Point:
    """
    Computes the shared secret for a group of participants.
    The secret is calculated as (s1 * s2 * ... * sn) * G.
    """
    if base_point.is_infinity:
        raise ValueError("Base point cannot be the point at infinity.")
    if base_point.curve != curve:
        raise ValueError("Base point must be on the given curve.")
    if len(secrets) < 2:
        raise ValueError("At least 2 secrets are required.")

    shared_secret = base_point

    for s in secrets:
        shared_secret = shared_secret * s

    return shared_secret
