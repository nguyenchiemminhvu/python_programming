from ncmv import default_logging
import logging
import threading
import time

def worker(name, delay=1):
    logging.info(f"Worker {name} starting")
    time.sleep(delay)
    logging.info(f"Worker {name} finished")

if __name__ == "__main__":
    t = threading.Thread(target=worker, args=("Thread-1", 2), daemon=True)
    t.start()
    
    time.sleep(1)
    logging.info("Main thread finished")