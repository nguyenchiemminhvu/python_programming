# arithmetic operators (+, -, *, /, //, %, **)
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 // 5)
print(10 % 5)
print(10 ** 5)

# assignment operators (=, +=, -=, *=, /=, //=, %=, **=)
x = 10
x += 5
print(x)
x -= 3
print(x)
x *= 2
print(x)
x /= 4
print(x)
x //= 2
print(x)
x %= 3
print(x)
x **= 2
print(x)

# comparison operators (==, !=, >, <, >=, <=)
print(10 == 5)
print(10 != 5)
print(10 > 5)
print(10 < 5)
print(10 >= 5)
print(10 <= 5)

# logical operators (and, or, not)
print(True and False)
print(True or False)
print(not True)

# identity operators (is, is not)
a = [1, 2, 3]
b = a
c = a[:]
print(a is b)
print(a is not c)
print(a is c)

# membership operators (in, not in)
print(1 in a)
print(4 in a)
print(1 not in a)
print(4 not in a)

# bitwise operators (&, |, ^, ~, <<, >>)
print(5 & 3)  # bitwise AND
print(5 | 3)  # bitwise OR
print(5 ^ 3)  # bitwise XOR
print(~5)     # bitwise NOT
print(5 << 1)  # left shift
print(5 >> 1)  # right shift

# membership operators (in, not in)
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # True
print(6 in my_list)  # False
print(3 not in my_list)  # False
print(6 not in my_list)  # True

# ternary operator (conditional expression)
x = 10
y = 20
max_value = x if x > y else y
print(max_value)  # 20

# chaining comparison operators
print(5 < 10 < 15)  # True
print(5 < 10 > 15)  # False

# operator precedence
# Arithmetic operators have higher precedence than comparison operators
result = 10 + 5 > 12 * 2
print(result)  # True

# operator precedence with parentheses
result = (10 + 5) > (12 * 2)
print(result)  # True

