import pytest
from krypto_lib.prng.gps_l1_ca import generate_g1_sequence, generate_g2_sequence, generate_ca_code

def test_generate_g1_sequence_length():
    g1_sequence = generate_g1_sequence()
    assert len(g1_sequence) == 1023
    assert all(bit in (0, 1) for bit in g1_sequence)

def test_generate_g2_sequence_length():
    sv_id = 1
    g2_sequence = generate_g2_sequence(sv_id)
    assert len(g2_sequence) == 1023
    assert all(bit in (0, 1) for bit in g2_sequence)

def test_generate_g2_sequence_invalid_sv_id():
    with pytest.raises(ValueError):
        generate_g2_sequence(0)
    with pytest.raises(ValueError):
        generate_g2_sequence(33)

def test_generate_g2_sequence_different_sv_ids():
    sv_id1 = 1
    sv_id2 = 2
    g2_sequence1 = generate_g2_sequence(sv_id1)
    g2_sequence2 = generate_g2_sequence(sv_id2)
    assert g2_sequence1 != g2_sequence2

def test_generate_ca_code_known_output():
    sv_id = 1
    expected_first_10_bits = [1, 1, 0, 0, 1, 0, 0, 0, 0, 0]
    ca_code = generate_ca_code(sv_id)
    print(ca_code[:10], generate_g1_sequence()[:10], generate_g2_sequence(sv_id)[:10])
    assert ca_code[:10] == expected_first_10_bits
