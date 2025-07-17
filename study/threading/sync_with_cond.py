from ncmv import default_logging
import logging
import threading
import time
import random

# Shared resource (a list acting as a buffer)
buffer = []
# Maximum size of the buffer
BUFFER_SIZE = 5

# Create a Condition object
# It implicitly creates a Lock if one is not provided.
condition = threading.Condition()

def producer():
    """Simulates a producer adding items to the buffer."""
    for i in range(10):
        time.sleep(random.uniform(0.1, 0.5)) # Simulate work
        with condition:
            # Wait if the buffer is full
            while len(buffer) >= BUFFER_SIZE:
                logging.info("Producer: Buffer is full, waiting...")
                condition.wait() # Releases the lock and waits

            item = f"item_{i}"
            buffer.append(item)
            logging.info(f"Producer: Produced {item}. Buffer: {buffer}")
            condition.notify_all() # Notify all waiting consumers

def consumer(consumer_id):
    """Simulates a consumer removing items from the buffer."""
    for _ in range(5): # Each consumer tries to consume 5 items
        time.sleep(random.uniform(0.1, 0.5)) # Simulate work
        with condition:
            # Wait if the buffer is empty
            while not buffer:
                logging.info(f"Consumer {consumer_id}: Buffer is empty, waiting...")
                condition.wait() # Releases the lock and waits

            item = buffer.pop(0)
            logging.info(f"Consumer {consumer_id}: Consumed {item}. Buffer: {buffer}")
            condition.notify_all() # Notify all waiting producers (if any)

if __name__ == "__main__":
    # Create producer and consumer threads
    producer_thread = threading.Thread(target=producer, name="ProducerThread")
    consumer_thread_1 = threading.Thread(target=consumer, args=(1,), name="ConsumerThread-1")
    consumer_thread_2 = threading.Thread(target=consumer, args=(2,), name="ConsumerThread-2")

    # Start the threads
    producer_thread.start()
    consumer_thread_1.start()
    consumer_thread_2.start()

    # Wait for all threads to complete
    producer_thread.join()
    consumer_thread_1.join()
    consumer_thread_2.join()

    logging.info("All threads finished.")