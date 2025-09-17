"""
Python Arithmetic Calculator
A modular calculator demonstrating Git workflow
"""

# Import all operation modules
try:
    from addition import add_numbers, add_multiple
    from subtraction import subtract_numbers, subtract_multiple
    from multiplication import multiply_numbers, multiply_multiple, power_operation
    MODULES_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Some modules not available: {e}")
    MODULES_AVAILABLE = False

def display_menu():
    """Display calculator menu options"""
    print("\n=== Python Arithmetic Calculator ===")
    print("1. Addition (two numbers)")
    print("2. Addition (multiple numbers)")
    print("3. Subtraction (two numbers)")
    print("4. Subtraction (multiple numbers)")
    print("5. Multiplication (two numbers)")
    print("6. Multiplication (multiple numbers)")
    print("7. Power operation (base^exponent)")
    print("8. Exit")

def get_numbers(count=2):
    """Get specified number of inputs from user"""
    numbers = []
    for i in range(count):
        while True:
            try:
                num = float(input(f"Enter number {i+1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Please enter a valid number.")
    return numbers

def get_multiple_numbers():
    """Get variable number of inputs from user"""
    numbers = []
    print("Enter numbers (press Enter with empty input to finish):")
    while True:
        try:
            user_input = input(f"Number {len(numbers)+1}: ")
            if user_input.strip() == "":
                break
            numbers.append(float(user_input))
        except ValueError:
            print("Please enter a valid number or press Enter to finish.")
    return numbers

def main():
    """Main calculator interface"""
    if not MODULES_AVAILABLE:
        print("Calculator modules are not available. Please ensure all module files are present.")
        return
    
    while True:
        display_menu()
        
        try:
            choice = int(input("\nSelect operation (1-8): "))
        except ValueError:
            print("Please enter a valid number (1-8).")
            continue
        
        if choice == 8:
            print("Thank you for using the calculator!")
            break
        elif choice == 1:
            nums = get_numbers(2)
            result = add_numbers(nums[0], nums[1])
            print(f"Result: {nums[0]} + {nums[1]} = {result}")
        elif choice == 2:
            nums = get_multiple_numbers()
            if nums:
                result = add_multiple(*nums)
                print(f"Result: {' + '.join(map(str, nums))} = {result}")
            else:
                print("No numbers entered.")
        elif choice == 3:
            nums = get_numbers(2)
            result = subtract_numbers(nums[0], nums[1])
            print(f"Result: {nums[0]} - {nums[1]} = {result}")
        elif choice == 4:
            nums = get_multiple_numbers()
            if nums:
                base = nums[0]
                others = nums[1:]
                result = subtract_multiple(base, *others)
                print(f"Result: {base} - {' - '.join(map(str, others))} = {result}")
            else:
                print("Need at least one number.")
        elif choice == 5:
            nums = get_numbers(2)
            result = multiply_numbers(nums[0], nums[1])
            print(f"Result: {nums[0]} × {nums[1]} = {result}")
        elif choice == 6:
            nums = get_multiple_numbers()
            if nums:
                result = multiply_multiple(*nums)
                print(f"Result: {' × '.join(map(str, nums))} = {result}")
            else:
                print("No numbers entered.")
        elif choice == 7:
            print("Power operation: base^exponent")
            nums = get_numbers(2)
            result = power_operation(nums[0], nums[1])
            print(f"Result: {nums[0]}^{nums[1]} = {result}")
        else:
            print("Invalid choice. Please select 1-8.")

if __name__ == "__main__":
    main()