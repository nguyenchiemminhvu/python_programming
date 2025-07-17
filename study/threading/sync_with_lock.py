from ncmv import default_logging
from threading import Thread, Lock
from concurrent.futures import ThreadPoolExecutor
import time
import logging

shared_resource = 0

def worker(name, lock):
    global shared_resource
    logging.info(f"Worker {name} starting")
    with lock:
        logging.info(f"Worker {name} acquired lock")
        # Simulate some work with the shared resource
        local_value = shared_resource
        local_value += 1
        time.sleep(0.1)
        shared_resource = local_value

if __name__ == "__main__":
    lock = Lock()
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(lambda x: worker(x, lock), range(10))
    logging.info(f"Final value of shared resource: {shared_resource}")