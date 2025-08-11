def generating_numbers():
    """Generator function that yields numbers from 0 to 9."""
    for i in range(10):
        yield i

def generating_numbers_with_condition():
    """Generator function that yields even numbers from 0 to 9."""
    for i in range(10):
        if i % 2 == 0:
            yield i

if __name__ == "__main__":
    iter = generating_numbers()
    for number in iter:
        print(number)

    print()
    
    iter = generating_numbers_with_condition()
    for number in iter:
        print(number)