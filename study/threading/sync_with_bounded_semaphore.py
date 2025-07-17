from ncmv import default_logging
import threading
import time
import random

# Define a fixed-size buffer
BUFFER_SIZE = 5
buffer = []

# BoundedSemaphore to control access to the buffer slots (empty slots)
empty_slots = threading.BoundedSemaphore(BUFFER_SIZE)

# BoundedSemaphore to control access to the items in the buffer (filled slots)
filled_slots = threading.BoundedSemaphore(0) # Initially, no items are in the buffer

# Lock to protect shared buffer access
buffer_lock = threading.Lock()

class Producer(threading.Thread):
    def __init__(self):
        super().__init__()
        self.name = "Producer"
        self.daemon = True  # Set as a daemon thread to exit when the main program exits

    def run(self):
        item_id = 0
        while True:
            # Acquire an empty slot in the buffer
            empty_slots.acquire()
            with buffer_lock:
                item = f"item_{item_id}"
                buffer.append(item)
                print(f"Producer produced: {item}. Buffer: {buffer}")
                item_id += 1
            # Release a filled slot, indicating an item is available
            filled_slots.release()
            time.sleep(random.uniform(0.1, 0.5))

class Consumer(threading.Thread):
    def __init__(self):
        super().__init__()
        self.name = "Consumer"
        self.daemon = True  # Set as a daemon thread to exit when the main program exits

    def run(self):
        while True:
            # Acquire a filled slot, indicating an item is available
            filled_slots.acquire()
            with buffer_lock:
                item = buffer.pop(0)
                print(f"Consumer consumed: {item}. Buffer: {buffer}")
            # Release an empty slot, indicating a slot is now free
            empty_slots.release()
            time.sleep(random.uniform(0.1, 0.5))

if __name__ == "__main__":
    producer_thread = Producer()
    consumer_thread = Consumer()

    producer_thread.start()
    consumer_thread.start()

    # In a real application, you'd have a mechanism to stop these infinite loops.
    # For demonstration, we'll let them run for a short period.
    time.sleep(3)
    print("\nDemonstration finished.")
    # In a real scenario, you'd join threads here or signal their termination.