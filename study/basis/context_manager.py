import os
with open("test.txt", "w") as f:
    f.write("Hello, World!")
    os.remove("test.txt") if os.path.exists("test.txt") else None

class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        if exc_type:
            print(f"An exception occurred: {exc_value}")

with MyContextManager() as cm:
    print("Inside the context")

