import time
import timeit

def worker(n):
    """A simple worker function that simulates some work."""
    sum([i * i for i in range(n)])

if __name__ == "__main__":
    start_time = time.perf_counter()
    result = worker(10000000)
    end_time = time.perf_counter()
    print(f"Time taken: {end_time - start_time:.9f} seconds")

    # Using timeit to measure the execution time of the worker function
    code_to_measure = "sum([i * i for i in range(10000000)])"
    execution_time = timeit.timeit(code_to_measure, number=1)
    print(f"Execution time using timeit: {execution_time:.9f} seconds")