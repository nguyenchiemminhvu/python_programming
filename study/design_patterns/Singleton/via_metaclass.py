class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def __new__(cls, name, bases, attrs):
        return super(SingletonMeta, cls).__new__(cls, name, bases, attrs)

class Logger(metaclass=SingletonMeta):
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