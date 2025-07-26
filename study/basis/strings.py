s = "Nguyen Chiem Minh Vu"

print(s.upper())  # Convert to uppercase
print(s.lower())  # Convert to lowercase
print(s.lower().title())  # Convert to title case
print(s.capitalize())  # Capitalize the first letter
print(s.swapcase())  # Swap case of all letters

# string is an array/iterable
print(s[0])  # Access the first character
temp = ''
for c in s:
    temp += c
print(temp)  # Reconstruct the string from characters

print("length:", len(s))  # Get the length of the string
print("Vu in s" if "Vu" in s else "Vu not in s")  # Check if substring exists

# slicing
print(s[0:6])  # Get substring from index 0 to 5
print(s[7:])  # Get substring from index 7 to the end
print(s[-1::-1])  # Reverse the string
print(s[::2])  # Get every second character

# replace
print(s.replace("e", "E"))  # Replace "Vu" with "V"

# split and join
words = s.split()  # Split the string into words
print(words)  # Print the list of words
print(" ".join(words))  # Join the words back into a string

# concatenation
print(s + " is a developer.")  # Concatenate strings

# formatting
print("My name is {} and I am a {}".format(s, "developer"))  # Old formatting
print(f"My name is {s} and I am a developer")  # New formatting (f-string)

# place holders
holder = f"{s} is a developer"
print(holder)  # Format using a placeholder
print(holder.format(s=s))  # Format using a placeholder

# escape characters
print("This is a backslash: \\")  # Print a backslash
print("This is a double quote: \"")  # Print a double quote
print("This is a single quote: \'")  # Print a single quote
print("This is a tab:\t")  # Print a tab character
print("This is a newline:\n")  # Print a newline character
print("This is a backspace:\band we lost the : character") # Print a backspace character

# C-style formatting
print("My name is %s and I am a %s" % (s, "developer"))  # C-style formatting

# searching
print(s.find("Vu"))  # Find the index of "Vu"
print(s.index("Vu"))  # Find the index of "Vu" (raises error if not found)
print(s.count("e"))  # Count occurrences of "e"
print(s.startswith("Nguyen"))  # Check if string starts with "Nguyen"
print(s.endswith("Vu"))  # Check if string ends with "Vu"