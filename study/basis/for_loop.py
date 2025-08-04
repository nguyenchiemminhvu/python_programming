for i in range(5):
    print(i)
else:
    print("Loop completed successfully.")

for i in range(3, 8):
    print(i)
else:
    print("Loop completed successfully.")

for i in range(2, 10, 2):
    print(i)
else:
    print("Loop completed successfully.")

for i in range(10, 0, -2):
    print(i)
else:
    print("Loop completed successfully.")

items = ['apple', 'banana', 'cherry']
for item in items:
    print(item)
else:
    print("All items printed successfully.")

for i in range(5):
    if i == 3:
        print("Breaking the loop at i =", i)
        break
    print(i)
else:
    print("This will not be printed due to break.")

for item in items:
    if item == 'banana':
        print("Skipping banana")
        continue
    print(item)
else:
    print("All items processed, skipping banana.")

for i in range(1, 6):
    for j in range(1, 4):
        print(f"i: {i}, j: {j}")
else:
    print("Nested loop completed successfully.")

for i in range(1, 11):
    if i % 2 == 0:
        pass
    else:
        print(f"Odd number: {i}")
else:
    print("Loop with pass completed successfully.")