i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print("Loop completed successfully.")

while i < 20:
    print(i)
    i += 1
    if (i == 15):
        print("Breaking the loop at i =", i)
        break
else:
    print("This will not be printed because the loop was broken.")

while i < 25:
    if (i % 2 == 0):
        print(i, "is even")
        i += 1
        continue
    else:
        print(i, "is odd")
        i += 3
else:
    print("This will not be printed because of the continue statement.")