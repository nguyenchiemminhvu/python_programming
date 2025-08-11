mi = min(1, 2, 3, 4, 5)
ma = max(1, 2, 3, 4, 5)
print(f"Minimum: {mi}, Maximum: {ma}")
print(abs(-10))  # Absolute value
print(pow(2, 3))  # 2 raised to the power of 3
print(round(3.14159, 2))  # Round to 2 decimal places
print(sum([1, 2, 3, 4, 5]))  # Sum of a list

# Using math module for more advanced operations
import math
print(math.sqrt(16))  # Square root of 16
print(math.factorial(5))  # Factorial of 5
print(math.pi)  # Value of pi
print(math.e)  # Value of e

# Using random module for generating random numbers
import random
print(random.randint(1, 10))  # Random integer between 1 and 10
print(random.uniform(1.0, 10.0))  # Random float between 1.0 and 10.0

# Using statistics module for statistical operations
import statistics
data = [1, 2, 3, 4, 5]
print(statistics.mean(data))  # Mean of the data
print(statistics.median(data))  # Median of the data
print(statistics.stdev(data))  # Standard deviation of the data
print(statistics.variance(data))  # Variance of the data
print(statistics.pstdev(data))  # Population standard deviation
print(statistics.pvariance(data))  # Population variance

# Using cmath for complex number operations
import cmath
z = complex(2, 3)  # Create a complex number
print(cmath.sqrt(z))  # Square root of the complex number
print(cmath.polar(z))  # Polar coordinates of the complex number
print(cmath.rect(5, cmath.pi/4))  # Rectangular coordinates from polar form

# Using fractions for rational number operations
from fractions import Fraction
f = Fraction(1, 3)  # Create a fraction
print(f + Fraction(1, 6))  # Add two fractions
print(f * Fraction(2, 5))  # Multiply two fractions

# Using decimal for high precision arithmetic
from decimal import Decimal, getcontext
getcontext().prec = 28  # Set precision for Decimal operations
d = Decimal('1.1') + Decimal('2.2')  # High precision addition
print(d)  # Output: 3.3
