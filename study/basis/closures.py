# examples of closures in Python

def make_multiplier_of(n):
    """Returns a function that multiplies its input by n."""
    def multiplier(x):
        return x * n
    return multiplier

# Example usage
double = make_multiplier_of(2)
triple = make_multiplier_of(3)
print(double(5))  # Output: 10
print(triple(5))  # Output: 15