import time

def worker(n):
    """A simple worker function that simulates some work."""
    sum([i * i for i in range(n)])

if __name__ == "__main__":
    start_time = time.perf_counter()
    result = worker(10000000)
    end_time = time.perf_counter()
    
    print(f"Worker finished with result: {result}")
    print(f"Time taken: {end_time - start_time:.9f} seconds")