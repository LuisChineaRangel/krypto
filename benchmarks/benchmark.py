import time
from benchmarks.benchmark_symmetric import benchmark_symmetric_throughput
from benchmarks.benchmark_asymmetric import benchmark_asymmetric_ops
from benchmarks.benchmark_prng import benchmark_prng

if __name__ == "__main__":
    print("="*40)
    print("      KRYPTO LIBRARY BENCHMARK (ALL)")
    print("="*40)
    total_start = time.perf_counter()

    benchmark_symmetric_throughput()
    benchmark_asymmetric_ops()
    benchmark_prng()

    total_end = time.perf_counter()
    print("="*40)
    print(f"Total benchmark time: {total_end - total_start:.2f}s")
    print("="*40)
