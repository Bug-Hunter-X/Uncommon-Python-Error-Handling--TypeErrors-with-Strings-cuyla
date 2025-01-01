def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        if isinstance(a, str) or isinstance(b, str):
            return "Type error: String cannot be divided"
        else:
            return "Unknown type error"

# Example usage:
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: Division by zero
print(function_with_uncommon_error(10, "hello")) # Output: Type error: String cannot be divided
print(function_with_uncommon_error([1,2],2)) # Output: Unknown type error