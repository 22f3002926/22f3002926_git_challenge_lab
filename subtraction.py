"""
Subtraction Module for Python Calculator
Provides subtraction operations with validation
"""

def subtract_numbers(num1, num2):
    """
    Subtract second number from first number
    
    Args:
        num1 (float): First number (minuend)
        num2 (float): Second number (subtrahend)
    
    Returns:
        float: Difference between the two numbers
    """
    return num1 - num2

def subtract_multiple(base_number, *numbers):
    """
    Subtract multiple numbers from base number
    
    Args:
        base_number (float): Starting number
        *numbers: Numbers to subtract from base
    
    Returns:
        float: Result after all subtractions
    """
    result = base_number
    for num in numbers:
        result -= num
    return result

# Test the functions
if __name__ == "__main__":
    print("Testing subtraction module:")
    print(f"10 - 3 = {subtract_numbers(10, 3)}")
    print(f"20 - 2 - 3 - 1 = {subtract_multiple(20, 2, 3, 1)}")