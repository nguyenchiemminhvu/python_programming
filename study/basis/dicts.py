d1 = dict()
for i in range(0, 26):
    d1[i] = chr(i + 97)
print(d1)

for i in range(0, 26):
    print(i, d1[i])

for k, v in d1.items():
    print(k, v)

d2 = {i : chr(i + 97) for i in range(0, 26)}
print(d2)

print(d1 == d2)
