from abc import ABC, abstractmethod

class i_logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass

class base_logger(i_logger):
    def log(self, message: str):
        print(f"Log: {message}")

class file_logger(i_logger):
    def __init__(self, logger: base_logger):
        self._logger = logger
    
    def log(self, message: str):
        self._logger.log(message)
        with open("log.txt", "a") as file:
            file.write(f"File Log: {message}\n")

class database_logger(i_logger):
    def __init__(self, logger: base_logger):
        self._logger = logger
    
    def log(self, message: str):
        self._logger.log(message)
        print(f"Database Log: {message}")

if __name__ == "__main__":
    base = base_logger()
    file = file_logger(base)
    database = database_logger(file)

    # Example usage
    database.log("This is a log message.")
    database.log("Another log message.")