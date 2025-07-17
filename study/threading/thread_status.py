from ncmv import default_logging
import logging
import threading
import time

def worker():
    thread_name = threading.current_thread().name
    logging.info(f"Thread {thread_name} starting")
    time.sleep(2)
    logging.info(f"Thread {thread_name} finished")

if __name__ == "__main__":
    thread = threading.Thread(target=worker, name="WorkerThread")
    thread.start()
    
    while (thread.is_alive()):
        logging.info(f"Thread {thread.name} is still running")
        time.sleep(1)
    
    thread.join()
    logging.info(f"Thread {thread.name} has completed")
    logging.info("Thread status example finished")