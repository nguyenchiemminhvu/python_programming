import sys

if __name__ == "__main__":
    # Print the number of arguments passed
    print(f"Number of arguments: {len(sys.argv)}")

    # Print the arguments passed
    print("Arguments:", sys.argv)

    # Print the first argument (script name)
    print("First argument (script name):", sys.argv[0])

    # Print the second argument if it exists
    if len(sys.argv) > 1:
        print("Second argument:", sys.argv[1])
    else:
        print("No second argument provided.")