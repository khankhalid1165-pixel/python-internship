# calculator.py

def add(a, b):
    """Addition operation"""
    return a + b

def subtract(a, b):
    """Subtraction operation"""
    return a - b

def multiply(a, b):
    """Multiplication operation"""
    return a * b

def divide(a, b):
    """Division operation with zero division check"""
    if b == 0:
        raise ValueError("Error: Cannot divide by zero!")
    return a / b

def get_number_input(prompt):
    """Get valid number input from user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def display_menu():
    """Display the calculator menu"""
    print("\n" + "="*40)
    print("          CALCULATOR CLI APP")
    print("="*40)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("="*40)

def main():
    """Main calculator function"""
    print("Welcome to the Calculator CLI App!")
    
    while True:
        display_menu()
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '5':
            print("Thank you for using the Calculator! Goodbye!")
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice! Please select 1-5.")
            continue
        
        try:
            # Get numbers from user
            num1 = get_number_input("Enter first number: ")
            num2 = get_number_input("Enter second number: ")
            
            # Perform calculation based on user choice
            if choice == '1':
                result = add(num1, num2)
                operator = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operator = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operator = "*"
            elif choice == '4':
                result = divide(num1, num2)
                operator = "/"
            
            # Display result
            print(f"\nResult: {num1} {operator} {num2} = {result}")
            
        except ValueError as e:
            print(f"\n{e}")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
        
        # Ask if user wants to continue
        continue_calc = input("\nDo you want to perform another calculation? (y/n): ").strip().lower()
        if continue_calc not in ['y', 'yes']:
            print("Thank you for using the Calculator! Goodbye!")
            break

# Advanced calculator with additional features
def advanced_calculator():
    """Advanced version with more operations"""
    operations = {
        '1': ('Addition', add),
        '2': ('Subtraction', subtract),
        '3': ('Multiplication', multiply),
        '4': ('Division', divide),
        '5': ('Power', lambda a, b: a ** b),
        '6': ('Modulo', lambda a, b: a % b)
    }
    
    while True:
        print("\n" + "="*50)
        print("          ADVANCED CALCULATOR")
        print("="*50)
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        print("7. Exit")
        print("="*50)
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == '7':
            print("Goodbye!")
            break
        
        if choice not in operations:
            print("Invalid choice! Please select 1-7.")
            continue
        
        try:
            num1 = get_number_input("Enter first number: ")
            num2 = get_number_input("Enter second number: ")
            
            operation_name, operation_func = operations[choice]
            result = operation_func(num1, num2)
            
            operators = {
                '1': '+', '2': '-', '3': '*', '4': '/',
                '5': '^', '6': '%'
            }
            
            print(f"\n{operation_name}: {num1} {operators[choice]} {num2} = {result}")
            
        except (ValueError, ZeroDivisionError) as e:
            print(f"\nError: {e}")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    # Run the basic calculator
    main()
    
    