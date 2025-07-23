def singleton(cls):
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Logger:
    def __init__(self):
        print("Initializing Logger")

    def log(self, message):
        print(f"Log: {message}")

if __name__ == "__main__":
    # Testing the Logger singleton
    logger1 = Logger()
    logger2 = Logger()

    print(logger1 is logger2)  # Should print True, indicating both are the same instance
    logger1.log("This is a log message.")
    logger2.log("This is another log message.")
    
    print(id(logger1), id(logger2))  # Should print the same ID for both instances