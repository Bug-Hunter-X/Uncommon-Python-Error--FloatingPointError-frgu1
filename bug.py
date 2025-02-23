def function_with_uncommon_error(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Type error"

# Uncommon error: FloatingPointError
# This can occur if you attempt certain operations on floating point numbers that are not valid
# For example, taking the square root of a negative number
# If your code doesn't handle such scenarios, a FloatingPointError may raise unexpectedly.
# The specific error message would describe the nature of the issue

# Example showing FloatingPointError in specific cases
import cmath
import math

print(math.sqrt(-1))  # This will raise ValueError
print(cmath.sqrt(-1)) # This will return a complex number (1j)

#Another example where a small change could easily lead to a floating point error
# This is especially relevant in scientific computing with very small/large numbers
num = 1e-300
print(1 + num) # Prints 1.0
