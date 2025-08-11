print("Enter your name:")
name = input()
print("Hello, " + name + "!")

name = input("Enter your name: ")
print("Hello, " + name + "!")

# validate input

validated = False
while not validated:
    f = input("Enter a number: ")
    try:
        f = float(f)
        validated = True
    except ValueError:
        print("Invalid input, please enter a number.")
print("You entered:", f)