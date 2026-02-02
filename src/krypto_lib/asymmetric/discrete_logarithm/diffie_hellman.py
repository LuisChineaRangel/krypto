from krypto_lib.utils import lehman_peralta_primality_test, fast_pow

def diffie_hellman_group(p: int, g: int, secrets: list[int]) -> int:
    if not lehman_peralta_primality_test(p):
        raise ValueError("P number must be prime.")
    if g <= 1 or g >= p:
        raise ValueError("Base g must be in the range 1 < g < p.")
    if len(secrets) < 2:
        raise ValueError("At least 2 secrets are required.")

    shared_key = g

    for s in secrets:
        shared_key = fast_pow(shared_key, s, p)

    return shared_key

def diffie_hellman(p: int, g: int, private_a: int, private_b: int) -> int:
    shared_key = diffie_hellman_group(p, g, [private_a, private_b])
    return shared_key
