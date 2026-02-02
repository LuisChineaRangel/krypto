import time
from krypto_lib.prng.gps_l1_ca import generate_ca_code

def benchmark_prng():
    print("--- PRNG (GPS L1 C/A) ---")
    iterations = 1000
    start = time.perf_counter()
    for i in range(iterations):
        _ = generate_ca_code((i % 32) + 1)
    end = time.perf_counter()
    print(f"GPS L1 C/A (1023 bits): {iterations / (end - start):.2f} codes/s")
    print()

if __name__ == "__main__":
    benchmark_prng()
