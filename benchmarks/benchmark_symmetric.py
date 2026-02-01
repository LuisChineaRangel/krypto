import time
import numpy as np
import string
from krypto_lib.symmetric.block.aes import aes_ecb, aes_cbc
from krypto_lib.symmetric.stream.arc4 import arc4
from krypto_lib.symmetric.stream.chacha20 import chacha20
from krypto_lib.symmetric.classical.vigenere import vigenere

def benchmark_symmetric_throughput():
    print("--- Symmetric Ciphers Throughput ---")
    data_size = 1024 * 1024  # 1 MB
    data = np.random.bytes(data_size)
    key_32 = np.random.bytes(32)
    key_16 = np.random.bytes(16)
    iv = np.random.bytes(16)
    nonce = np.random.bytes(12)
    
    # AES ECB
    start = time.perf_counter()
    _ = aes_ecb(data, key_32)
    end = time.perf_counter()
    print(f"AES-256 ECB: {data_size / (end - start) / 1024:.2f} KB/s")

    # AES CBC
    start = time.perf_counter()
    encrypted = aes_cbc(data, key_32, iv)
    end = time.perf_counter()
    print(f"AES-256 CBC Encrypt (Sequential): {data_size / (end - start) / 1024:.2f} KB/s")

    start = time.perf_counter()
    _ = aes_cbc(encrypted, key_32, iv, reverse=True)
    end = time.perf_counter()
    print(f"AES-256 CBC Decrypt (Vectorized): {data_size / (end - start) / 1024:.2f} KB/s")

    # ChaCha20
    start = time.perf_counter()
    _ = chacha20(data, key_32, nonce)
    end = time.perf_counter()
    print(f"ChaCha20: {data_size / (end - start) / 1024:.2f} KB/s")

    # ARC4
    start = time.perf_counter()
    _ = arc4(data, key_16)
    end = time.perf_counter()
    print(f"ARC4: {data_size / (end - start) / 1024:.2f} KB/s")

    # Vigenere (Classical)
    classical_size = 100_000
    v_data = "".join(np.random.choice(list(string.ascii_uppercase), classical_size))
    v_key = "KRYPTOBENCHMARK"
    start = time.perf_counter()
    _ = vigenere(v_data, v_key)
    end = time.perf_counter()
    print(f"Vigenere: {classical_size / (end - start) / 1024:.2f} KB/s")
    print()

if __name__ == "__main__":
    benchmark_symmetric_throughput()
