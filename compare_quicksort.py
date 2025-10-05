import random
import time
from randomized_quicksort import randomized_quicksort
from deterministic_quicksort import deterministic_quicksort

def generate_arrays(n):
    return {
        "random": [random.randint(0, 10000) for _ in range(n)],
        "sorted": list(range(n)),
        "reversed": list(range(n, 0, -1)),
        "duplicates": [5] * n
    }

def benchmark():
    sizes = [1000, 5000, 10000]
    for n in sizes:
        print(f"\nArray size: {n}")
        arrays = generate_arrays(n)

        for name, arr in arrays.items():
            arr1 = arr.copy()
            arr2 = arr.copy()

            start = time.time()
            randomized_quicksort(arr1, 0, len(arr1) - 1)
            rand_time = time.time() - start

            start = time.time()
            deterministic_quicksort(arr2, 0, len(arr2) - 1)
            det_time = time.time() - start

            print(f"{name.capitalize()} array: Randomized QS = {rand_time:.6f}s, Deterministic QS = {det_time:.6f}s")

if __name__ == "__main__":
    benchmark()
