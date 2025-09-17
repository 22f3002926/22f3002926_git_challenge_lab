"""
Multiplication Module for Python Calculator
Provides multiplication operations
"""

def multiply_numbers(num1, num2):
    """
    Multiply two numbers
    
    Args:
        num1 (float): First number
        num2 (float): Second number
    
    Returns:
        float: Product of the two numbers
    """
    return num1 * num2

def multiply_multiple(*numbers):
    """
    Multiply multiple numbers together
    
    Args:
        *numbers: Variable number of numeric arguments
    
    Returns:
        float: Product of all numbers
    """
    result = 1
    for num in numbers:
        result *= num
    return result

def power_operation(base, exponent):
    """
    Calculate base raised to the power of exponent
    
    Args:
        base (float): Base number
        exponent (float): Exponent
    
    Returns:
        float: Result of base^exponent
    """
    return base ** exponent

# Test the functions
if __name__ == "__main__":
    print("Testing multiplication module:")
    print(f"4 * 5 = {multiply_numbers(4, 5)}")
    print(f"2 * 3 * 4 = {multiply_multiple(2, 3, 4)}")
    print(f"2^8 = {power_operation(2, 8)}")