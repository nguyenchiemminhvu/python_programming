t1 = (1, 2, 3)
# t1[0] = 4  # This will raise a TypeError because tuples are immutable

t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)  # Output: (1, 2, 3, 4, 5, 6)

n3 = len(t3)
print(n3)  # Output: 6

print(type(t3))  # Output: <class 'tuple'>

t4 = tuple(range(10))
print(t4)  # Output: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

for i, v in enumerate(t4):
    print(i, v)

print(t4.count(5))  # Output: 1