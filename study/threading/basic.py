from ncmv import default_logging
import logging
import threading
import time

def worker(name, delay=1):
    logging.info(f"Worker {name} starting")
    time.sleep(delay)
    logging.info(f"Worker {name} finished")

if __name__ == "__main__":
    t = threading.Thread(target=worker, args=("Thread-1", 2))
    t.start()
    try:
        t.join()
    except KeyboardInterrupt:
        logging.info("KeyboardInterrupt received, exiting")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
