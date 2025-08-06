add = lambda x, y: x + y

print(add(2, 3))  # Output: 5

def multiplier(factor):
    return lambda x: x * factor

double = multiplier(2)
triple = multiplier(3)

print(double(5))
print(triple(5))