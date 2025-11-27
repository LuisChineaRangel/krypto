G2_TAPS = {
    1: (2, 6),
    2: (3, 7),
    3: (4, 8),
    4: (5, 9),
    5: (1, 9),
    6: (2, 10),
    7: (1, 8),
    8: (2, 9),
    9: (3, 10),
    10: (2, 3),
    11: (3, 4),
    12: (5, 6),
    13: (6, 7),
    14: (7, 8),
    15: (8, 9),
    16: (9, 10),
    17: (1, 4),
    18: (2, 5),
    19: (3, 6),
    20: (4, 7),
    21: (5, 8),
    22: (6, 9),
    23: (1, 3),
    24: (4, 6),
    25: (5, 7),
    26: (6, 8),
    27: (7, 9),
    28: (8, 10),
    29: (1, 6),
    30: (2, 7),
    31: (3, 8),
    32: (4, 9),
}


def get_g2_taps(sv_id: int) -> tuple[int, int]:
    """Get the G2 tap positions for a given satellite vehicle ID.
    Args:
        sv_id (int): Satellite vehicle ID (1-32).
    Returns:
        tuple[int, int]: The tap positions for the G2 register.
    Raises:
        ValueError: If sv_id is not in the range 1-32.
    """
    if sv_id not in G2_TAPS:
        raise ValueError("sv_id must be in the range 1-32.")
    return G2_TAPS[sv_id][0], G2_TAPS[sv_id][1]


def generate_g1_sequence() -> list[int]:
    """Generate the G1 sequence for GPS L1 C/A code.
    Returns:
        list[int]: The G1 sequence as a list of bits (0s and 1s).
    """
    g1 = [1] * 10
    g1_sequence = []

    for _ in range(1023):
        g1_output = g1[-1]
        g1_sequence.append(g1_output)

        # Feedback calculation
        feedback = g1[2] ^ g1[9]
        g1 = [feedback] + g1[:-1]
    return g1_sequence


def generate_g2_sequence(sv_id: int) -> list[int]:
    """Generate the G2 sequence for a given satellite vehicle ID.
    Args:
        sv_id (int): Satellite vehicle ID (1-32).
    Returns:
        list[int]: The G2 sequence as a list of bits (0s and 1s).
    """
    g2 = [1] * 10
    g2_sequence = []
    taps = get_g2_taps(sv_id)

    for _ in range(1023):
        g2_output = g2[taps[0] - 1] ^ g2[taps[1] - 1]
        g2_sequence.append(g2_output)

        # Feedback calculation
        feedback = g2[1] ^ g2[2] ^ g2[5] ^ g2[7] ^ g2[8] ^ g2[9]
        g2 = [feedback] + g2[:-1]
    return g2_sequence


def generate_ca_code(sv_id: int) -> list[int]:
    """Generate the GPS L1 C/A code for a given satellite vehicle ID.
    Args:
        sv_id (int): Satellite vehicle ID (1-32).
    Returns:
        list[int]: The C/A code as a list of bits (0s and 1s).
    """
    g1_sequence = generate_g1_sequence()
    g2_sequence = generate_g2_sequence(sv_id)

    ca_code = [(g1 ^ g2) for g1, g2 in zip(g1_sequence, g2_sequence)]
    return ca_code
