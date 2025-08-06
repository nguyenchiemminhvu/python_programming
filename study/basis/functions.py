def print_wrapper(s = "Default String"):
    print(f"Function called with argument: {s}")

def print_wrapper_positional(s, /):
    print(f"Function called with positional arguments: {s}")

def print_wrapper_keyword(*, s="Default Keyword String"):
    print(f"Function called with keyword argument: {s}")

def print_wrapper_args(*args, **kwargs):
    if args:
        print(f"Function called with positional arguments: {args}")
        if (1 in args) or (2 in args):
            print("Special condition met: 1 or 2 is in the arguments.")
    if kwargs:
        print(f"Function called with keyword arguments: {kwargs}")
        if ("key1" in kwargs) or ("key2" in kwargs):
            print("Special condition met: key1 or key2 is in the keyword arguments.")

def do_something(*args, **kwargs):
    print_wrapper_args(*args, **kwargs)

def return_constant():
    return 42

print_wrapper()
print_wrapper("Hello, World!")
print_wrapper(s="Python is great!")
print_wrapper_positional("Positional Argument")
print_wrapper_keyword(s="Keyword Argument")
print_wrapper_args(1, 2, 3, key1="value1", key2="value2")

do_something(5, 6, 7, key="example")

print(return_constant())

