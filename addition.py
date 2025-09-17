def add_numbers(num1, num2):
    """
    Add two numbers together
    
    Args:
        num1 (float): First number
        num2 (float): Second number
    
    Returns:
        float: Sum of the two numbers
    """
    return num1 + num2

def add_multiple(*numbers):
    """
    Add multiple numbers together
    
    Args:
        *numbers: Variable number of numeric arguments
    
    Returns:
        float: Sum of all numbers
    """
    return sum(numbers)

# Test the functions
if __name__ == "__main__":
    print("Testing addition module:")
    print(f"5 + 3 = {add_numbers(5, 3)}")
    print(f"1 + 2 + 3 + 4 = {add_multiple(1, 2, 3, 4)}")
