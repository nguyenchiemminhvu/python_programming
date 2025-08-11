import os

TEST_FILE = "test.txt"

f = open(TEST_FILE, "w")
f.write("Hello, World!\n") if f else None
f.write("This is a test file.\n") if f else None
f.close() if f else None

# with statement
with open(TEST_FILE, "a") as f:
    f.write("Appending a new line.\n") if f else None

# Reading the file
with open(TEST_FILE, "r") as f:
    content = f.read() if f else None
    print(content) if content else None

os.remove(TEST_FILE) if os.path.exists(TEST_FILE) else None