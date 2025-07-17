from ncmv import default_logging
import threading
import time
import random

# Define the available tools and their quantities
TOOLS = {
    "hammer": 2,
    "screwdriver": 3,
    "wrench": 1
}

# Create a semaphore for each tool type
tool_semaphores = {tool: threading.Semaphore(count) for tool, count in TOOLS.items()}

def worker_task(worker_id, required_tools):
    print(f"Worker {worker_id}: Attempting to acquire tools: {required_tools}")
    acquired_successful = True
    acquired_tools_list = []

    # Attempt to acquire all required tools
    for tool_name in required_tools:
        if tool_name in tool_semaphores:
            if tool_semaphores[tool_name].acquire(blocking=False): # Non-blocking acquisition
                acquired_tools_list.append(tool_name)
                print(f"Worker {worker_id}: Acquired {tool_name}")
            else:
                print(f"Worker {worker_id}: Failed to acquire {tool_name}. Releasing previously acquired tools.")
                acquired_successful = False
                break
        else:
            print(f"Worker {worker_id}: Error: Tool '{tool_name}' not recognized.")
            acquired_successful = False
            break

    if acquired_successful:
        print(f"Worker {worker_id}: All tools acquired. Performing work...")
        time.sleep(random.uniform(0.5, 2.0)) # Simulate work
        print(f"Worker {worker_id}: Work complete. Releasing tools.")
    else:
        print(f"Worker {worker_id}: Could not acquire all tools. Retrying later.")

    # Release all acquired tools
    for tool_name in acquired_tools_list:
        if tool_name in tool_semaphores:
            tool_semaphores[tool_name].release()
            print(f"Worker {worker_id}: Released {tool_name}")

# Create and start worker threads
threads = []
tasks = [
    {"worker_id": 1, "required_tools": ["hammer", "screwdriver"]},
    {"worker_id": 2, "required_tools": ["screwdriver", "wrench"]},
    {"worker_id": 3, "required_tools": ["hammer"]},
    {"worker_id": 4, "required_tools": ["screwdriver", "hammer"]},
    {"worker_id": 5, "required_tools": ["wrench", "hammer"]},
]

for task in tasks:
    t = threading.Thread(target=worker_task, args=(task["worker_id"], task["required_tools"]))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All workers have completed their tasks or attempted to.")