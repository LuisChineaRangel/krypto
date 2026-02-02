from krypto_lib.asymmetric.elliptic_curve.ecc import Point

def eceg_encrypt(base_point: Point, public_key: Point, message_point: Point, k: int) -> tuple[Point, Point]:
    """
    Encrypts a message (represented as a Point) using Elliptic Curve ElGamal.
    C1 = k * G
    C2 = M + k * Q (where Q is the public key)
    """
    if base_point.curve != public_key.curve or base_point.curve != message_point.curve:
        raise ValueError("All points must be on the same curve")

    c1 = base_point * k
    c2 = message_point + (public_key * k)

    return c1, c2

def eceg_decrypt(private_key: int, ciphertext: tuple[Point, Point]) -> Point:
    """
    Decrypts a ciphertext (tuple of Points) using Elliptic Curve ElGamal.
    M = C2 - d * C1 (where d is the private key)
    """
    c1, c2 = ciphertext

    # M = C2 - d * C1
    shared_secret = c1 * private_key
    message_point = c2 - shared_secret

    return message_point


def eceg_encrypt_multi(base_point: Point, public_keys: list[Point], message_point: Point, k: int) -> tuple[Point, list[Point]]:
    """
    Encrypts a message (Point) for multiple recipients.
    C1 = k * G
    C2_i = M + k * Q_i
    """
    if base_point.is_infinity:
        raise ValueError("Base point cannot be infinity")

    c1 = base_point * k
    c2_list = []

    for q in public_keys:
        if q.curve != base_point.curve:
            raise ValueError("All points must be on the same curve")
        shared_secret = q * k
        c2 = message_point + shared_secret
        c2_list.append(c2)

    return c1, c2_list
