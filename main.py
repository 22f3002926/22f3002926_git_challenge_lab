"""
Python Arithmetic Calculator
A modular calculator demonstrating Git workflow
"""

def main():
    """Main calculator interface"""
    print("=== Python Arithmetic Calculator ===")
    print("Welcome to the modular calculator!")
    
    # Basic calculator functionality
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    print(f"\nNumbers entered: {num1} and {num2}")
    print("More operations will be added through feature branches!")
    
    # Basic addition as starter
    result = num1 + num2
    print(f"Basic addition result: {result}")

if __name__ == "__main__":
    main()