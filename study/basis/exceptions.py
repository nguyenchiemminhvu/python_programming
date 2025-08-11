# exception examples

try:
    # This will raise a ZeroDivisionError
    result = 1 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")

try:
    # This will raise a ValueError
    number = int("not a number")
except ValueError as e:
    print(f"Error: {e}")

try:
    # This will raise a KeyError
    my_dict = {"key": "value"}
    value = my_dict["missing_key"]
except KeyError as e:
    print(f"Error: {e}")

try:
    # This will raise an IndexError
    my_list = [1, 2, 3]
    item = my_list[5]
except IndexError as e:
    print(f"Error: {e}")

try:
    # This will raise a TypeError
    result = "string" + 5
except TypeError as e:
    print(f"Error: {e}")

try:
    # This will raise an AttributeError
    my_string = "hello"
    my_string.append(" world")
except AttributeError as e:
    print(f"Error: {e}")

try:
    # This will raise an ImportError
    import non_existent_module
except ImportError as e:
    print(f"Error: {e}")

try:
    # This will raise a FileNotFoundError
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"Error: {e}")

try:
    # This will raise a NameError
    print(undefined_variable)
except NameError as e:
    print(f"Error: {e}")

try:
    # This will raise a RuntimeError
    raise RuntimeError("This is a runtime error")
except RuntimeError as e:
    print(f"Error: {e}")

try:
    # This will raise a NotImplementedError
    def unimplemented_function():
        raise NotImplementedError("This function is not implemented yet")

    unimplemented_function()
except NotImplementedError as e:
    print(f"Error: {e}")

try:
    # This will raise a StopIteration
    iterator = iter([1, 2, 3])
    while True:
        item = next(iterator)
        if item == 3:
            raise StopIteration("End of iteration")
except StopIteration as e:
    print(f"Error: {e}")

try:
    # This will raise a AssertionError
    assert False, "This is an assertion error"
except AssertionError as e:
    print(f"Error: {e}")

try:
    # This will raise a ConnectionError
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("non_existent_host", 80))
except socket.error as e:
    print(f"Error: {e}")

try:
    # This will raise a TimeoutError
    import time
    time.sleep(1)  # Simulating a long operation
    raise TimeoutError("The operation timed out")
except TimeoutError as e:
    print(f"Error: {e}")

try:
    # This will raise a UnicodeError
    invalid_unicode = b'\x80\x81\x82'.decode('utf-8')
except UnicodeError as e:
    print(f"Error: {e}")

try:
    # This will raise a PermissionError
    with open("/root/secret_file.txt", "r") as file:
        content = file.read()
except PermissionError as e:
    print(f"Error: {e}")

try:
    # This will raise a OSError
    import os
    os.remove("non_existent_file.txt")
except OSError as e:
    print(f"Error: {e}")