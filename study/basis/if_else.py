a = 5
b = 10
if a < b:
    print("a is less than b")
else:
    print("a is greater than or equal to b")

if a == b:
    print("a is equal to b")
elif a < b:
    print("a is less than b")
else:
    print("a is greater than b")

# short form if-else
print("a is less than b" if a < b else "a is greater than or equal to b")

# nested if-else
if a < b:
    print("a is less than b")
    if a < 0:
        print("a is negative")
    else:
        print("a is non-negative")
else:
    print("a is greater than or equal to b")
    if b < 0:
        print("b is negative")
    else:
        print("b is non-negative")

# using logical operators
if a < b and a > 0:
    print("a is less than b and a is positive")
if a < b or b > 15:
    print("Either a is less than b or b is greater than 15")

# using in operator
my_list = [1, 2, 3, 4, 5]
if a in my_list:
    print("a is in the list")
else:
    print("a is not in the list")

# using not operator
if not a == b:
    print("a is not equal to b")
else:
    print("a is equal to b")

# pass statement
if a > b:
    pass  # This block does nothing, but is syntactically correct
