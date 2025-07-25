i_var1 = 0
s_var1 = "Hello, World!"
f_var1 = 3.14
b_var1 = True

# type casting
i_var2 = int(f_var1)  # Convert float to int
s_var2 = str(i_var1)  # Convert int to string
f_var2 = float(i_var1)  # Convert int to float
b_var2 = bool(i_var1)  # Convert int to bool

# type checking
def check_type(var):
    if isinstance(var, int):
        return "This is an integer."
    elif isinstance(var, str):
        return "This is a string."
    elif isinstance(var, float):
        return "This is a float."
    elif isinstance(var, bool):
        return "This is a boolean."
    else:
        return "Unknown type."

print(check_type(i_var1))  # Output: This is an integer.
print(check_type(s_var1))  # Output: This is a string.
print(check_type(f_var1))  # Output: This is a float.
print(check_type(b_var1))  # Output: This is a boolean.
print(check_type(i_var2))  # Output: This is an integer.
print(check_type(s_var2))  # Output: This is a string.
print(check_type(f_var2))  # Output: This is a float.
print(check_type(b_var2))  # Output: This is a boolean.

# variable min and max
i_max = 2**31 - 1  # Maximum value for a 32-bit signed integer
i_min = -2**31  # Minimum value for a 32-bit signed integer
f_max = float('inf')  # Maximum float value
f_min = float('-inf')  # Minimum float value
print(f"Integer range: {i_min} to {i_max}")
print(f"Float range: {f_min} to {f_max}")

# variable multiple assignment
i_var3, s_var3, f_var3, b_var3 = 42, "Python", 2.718, False

# variable unpacking
def unpack_variables():
    i, s, f, b = i_var3, s_var3, f_var3, b_var3
    return i, s, f, b
i_unpacked, s_unpacked, f_unpacked, b_unpacked = unpack_variables()
print(i_unpacked, s_unpacked, f_unpacked, b_unpacked)  # Output: 42 Python 2.718 False

# complex type
x_var = 3 + 4j  # Complex number
print(type(x_var))  # Output: <class 'complex'>

# variable scope
def variable_scope_example():
    local_var = "I'm local"
    print(local_var)  # Accessing local variable
    return local_var
global_var = "I'm global"
def access_global_var():
    print(global_var)  # Accessing global variable
access_global_var()  # Output: I'm global
variable_scope_example()  # Output: I'm local