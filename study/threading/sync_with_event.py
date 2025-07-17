from ncmv import default_logging
import logging
import threading
import time

def worker(events):
    logging.info("Worker thread is waiting for the event to be set.")
    for event in events:
        event.wait()
        logging.info(f"Event {event} has been set, continuing work.")
    logging.info("Worker thread has been notified and is now running.")

def main():
    logging.info("Main thread is starting.")
    
    event_database = threading.Event()  # Create an Event object
    event_network = threading.Event()  # Create another Event object
    events = [event_database, event_network]  # List of events
    
    # Start the worker thread
    thread = threading.Thread(target=worker, args=(events,))
    thread.start()
    
    # Simulate some work in the main thread
    time.sleep(2)
    event_database.set()
    time.sleep(1)
    event_network.set() 

    # Wait for the worker thread to finish
    thread.join()
    logging.info("Main thread has finished.")

if __name__ == "__main__":
    main()