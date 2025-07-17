from ncmv import default_logging
import logging
import threading
import time
import queue
import random

task_queue = queue.Queue(maxsize=10)

def producer(event):
    while (True):
        try:
            item = random.randint(1, 100)
            task_queue.put(item)
            time.sleep(random.uniform(0.1, 0.5))  # Simulate variable production time
        except queue.Full:
            logging.warning("Queue is full, waiting to produce more items...")
        finally:
            if (event.is_set()):
                logging.info("Producer stopping...")
                break

def consumer(event):
    while (True):
        try:
            item = task_queue.get(timeout=1)
            logging.info(f"Consumed item: {item}, remaining in queue: {task_queue.qsize()}")
            task_queue.task_done()
            time.sleep(random.uniform(0.1, 0.5))  # Simulate
        except queue.Empty:
            logging.info("No items to consume, waiting...")
        except Exception as e:
            logging.error(f"Error consuming item: {e}")
        finally:
            if (event.is_set() and task_queue.empty()):
                logging.info("Consumer stopping...")
                break

def main():
    event = threading.Event()
    producer_thread = threading.Thread(target=producer, args=(event,))
    consumer_thread = threading.Thread(target=consumer, args=(event,), daemon=True)
    
    producer_thread.start()
    consumer_thread.start()
    
    while (True):
        s = input("Press Enter to stop the threads...")
        if s == "":
            event.set()
            break
    
    producer_thread.join()
    task_queue.join()  # Wait for all tasks to be processed

if __name__ == "__main__":
    main()