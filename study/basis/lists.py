l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]
l3 = l1 + l2
print(l3)
n3 = len(l3)
print(n3)

print(type(l3))

l4 = list(range(1, 11))
print(l4)

for i, v in enumerate(l4):
    print(i, v)

l5 = [v for v in l4 if v % 2 == 0]
print(l5)

l5.reverse()
print(l5)