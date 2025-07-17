from ncmv import default_logging
import logging
import threading
import time

def worker(barrier, worker_id):
    logging.info(f"Worker {worker_id} is starting.")
    time.sleep(2)  # Simulate work
    logging.info(f"Worker {worker_id} is waiting at the barrier.")
    barrier.wait()
    logging.info(f"Worker {worker_id} has crossed the barrier.")

def main():
    barrier = threading.Barrier(3)  # 3 threads must wait at the barrier
    threads = []
    for i in range(3):
        thread = threading.Thread(target=worker, args=(barrier, i))
        threads.append(thread)
        thread.start()
        time.sleep(1)  # Stagger the start of threads
    
    for thread in threads:
        thread.join()
    logging.info("All workers have crossed the barrier.")

if __name__ == "__main__":
    main()
    logging.info("Main thread is exiting.")