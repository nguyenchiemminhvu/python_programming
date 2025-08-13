a = 5  # 0b0101
b = 3  # 0b0011

# &
c = a & b  # 0b0001

# |
d = a | b  # 0b0111

# ^
e = a ^ b  # 0b0110

# ~
f = ~a  # 0b1010 (in Python, this is -6 due to two's complement representation)

# << left shift
g = a << 1  # 0b1010 (10 in decimal)

# >> right shift
h = a >> 1  # 0b0010 (2 in decimal)


# Print results
print(f"a: {a} (0b{a:04b})")
print(f"b: {b} (0b{b:04b})")
print(f"a & b: {c} (0b{c:04b})")
print(f"a | b: {d} (0b{d:04b})")
print(f"a ^ b: {e} (0b{e:04b})")
print(f"~a: {f} (0b{f & 0b1111:04b})") 
print(f"a << 1: {g} (0b{g:04b})")
print(f"a >> 1: {h} (0b{h:04b})")