l1 = [1, 2, 3, 4, 5]
i1 = iter(l1)
while True:
    try:
        print(next(i1))
    except StopIteration:
        break

print()

for item in l1:
    print(item)

print()

class CustomIterator:
    def __init__(self, list_item):
        self.list_item = list_item
        self.index = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if (self.index < len(self.list_item)):
            val = self.list_item[self.index]
            self.index += 1
            return val
        else:
            self.index = 0  # Reset index for next iteration
            raise StopIteration

i2 = CustomIterator(l1)

while True:
    try:
        print(next(i2))
    except StopIteration:
        break

print()

i3 = CustomIterator(l1)
for item in i3:
    print(item)

print()