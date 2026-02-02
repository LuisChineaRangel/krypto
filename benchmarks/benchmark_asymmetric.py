import time
from krypto_lib.asymmetric.factorization.rsa import rsa

def benchmark_asymmetric_ops():
    print("--- Asymmetric (RSA) Operations ---")
    p, q = 104729, 104723 # Primes around 10^5
    e = 65537
    message = "HELLORSABENCHMARK"

    iterations = 50
    start = time.perf_counter()
    for _ in range(iterations):
        ciphertext = rsa(message, e, p, q)
    end = time.perf_counter()
    print(f"RSA Encryption: {iterations / (end - start):.2f} ops/s")

    start = time.perf_counter()
    for _ in range(iterations):
        _ = rsa(ciphertext, e, p, q, decrypt=True)
    end = time.perf_counter()
    print(f"RSA Decryption: {iterations / (end - start):.2f} ops/s")
    print()

if __name__ == "__main__":
    benchmark_asymmetric_ops()
