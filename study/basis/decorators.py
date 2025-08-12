import logging

def decor_logs(func):
    def wrapper(*args, **kwargs):
        logging.info(f"calling function {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"function {func.__name__} returned: {result}")
        return result
    return wrapper

def decor_record_log(func):
    import datetime
    def wrapper(*args, **kwargs):
        cur_time = datetime.datetime.now()
        logging.info(f"Function {func.__name__} called at {cur_time}")
        result = func(*args, **kwargs)
        return result
    return wrapper

def decor_perf_counter(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        logging.info(f"function {func.__name__} executed in {end_time - start_time:.6f} seconds")
        return result
    return wrapper

def decor_playback(count=3):
    def inner_decor(func):
        def wrapper(*args, **kwargs):
            for i in range(count):
                logging.info(f"Playback {i + 1} for function {func.__name__}")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return inner_decor

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    @decor_logs
    def add(a, b):
        return a + b

    @decor_logs
    def multiply(a, b):
        return a * b
    
    @decor_record_log
    def subtract(a, b):
        return a - b
    
    @decor_record_log
    def divide(a, b):
        return a / b if b != 0 else "Cannot divide by zero"

    add(2, 3)
    multiply(4, 5)
    subtract(10, 4)
    divide(20, 4)

    @decor_perf_counter
    def slow_function(seconds):
        import time
        time.sleep(seconds)
        return "Finished"

    slow_function(2)
    slow_function(3)

    @decor_playback(count=2)
    def greet(name):
        return f"Hello, {name}!"

    greet("Alice")
    greet("Bob")