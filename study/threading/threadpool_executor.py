from ncmv import default_logging
import logging
import threading
import time

from concurrent.futures import ThreadPoolExecutor

def work_function(name, duration):
    logging.info(f"Thread {name} starting")
    time.sleep(duration)
    logging.info(f"Thread {name} finished after {duration} seconds")
    return f"Result from {name}"

if __name__ == "__main__":
    logging.info("Starting ThreadPoolExecutor example")
    
    pool = ThreadPoolExecutor(max_workers=3)
    pool.submit(work_function, "A", 2)
    pool.submit(work_function, "B", 3)
    pool.submit(work_function, "C", 1)
    pool.shutdown(wait=True)
    
    with ThreadPoolExecutor(max_workers=2) as pool:
        tasks = [
            pool.submit(work_function, "D", 1),
            pool.submit(work_function, "E", 2),
            pool.submit(work_function, "F", 3)
        ]
        pool.map(lambda f: print(f.result()), tasks)

    logging.info("All threads have completed")
    logging.info("ThreadPoolExecutor example finished")