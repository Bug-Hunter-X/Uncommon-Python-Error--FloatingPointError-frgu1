def function_with_uncommon_error_solution(x, y):
    try:
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            if y == 0:
                return "Division by zero"
            elif y < 0 and x > 0 and isinstance(x, (int, float)) and isinstance(y, (int, float)):
                return "Cannot calculate sqrt of negative number for positive numbers"
            else:
                result = x / y
                return result
        else:
            return "Type error"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Example demonstrating improved handling
print(function_with_uncommon_error_solution(10, 0))
print(function_with_uncommon_error_solution(10, 2))
print(function_with_uncommon_error_solution(10, -2)) #This will return the error
print(function_with_uncommon_error_solution(10, "hello"))

import cmath
import math

try:
    print(math.sqrt(-1)) #ValueError
except ValueError:
    print("This will be caught")

print(cmath.sqrt(-1))

num = 1e-300
print(1 + num) # Prints 1.0