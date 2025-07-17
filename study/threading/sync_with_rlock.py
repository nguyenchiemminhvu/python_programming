from ncmv import default_logging
from threading import RLock, Thread
import time

def worker(name, lock):
    def inner_function():
        with lock:
            print(f"{name} has acquired the lock.")
            time.sleep(1)
    
    with lock:
        print(f"{name} is about to call inner_function.")
        inner_function()
        print(f"{name} has released the lock.")

if __name__ == "__main__":
    lock = RLock()

    threads = []
    for i in range(5):
        t = Thread(target=worker, args=(f"Thread-{i+1}", lock))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    
    print("All threads have finished execution.")