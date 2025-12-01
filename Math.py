def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract_numbers(a, b):
    """Return the difference of two numbers."""
    return a - b

def main():
    print("Welcome! Do you want to do addition or subtraction?")
    choice = input("Type 'add' for addition or 'subtract' for subtraction: ").strip().lower()

    # Ask for two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Perform the chosen operation
    if choice == "add":
        result = add_numbers(num1, num2)
        print(f"The result of adding {num1} and {num2} is {result}.")
    elif choice == "subtract":
        result = subtract_numbers(num1, num2)
        print(f"The result of subtracting {num2} from {num1} is {result}.")
    else:
        print("Invalid choice. Please restart and type 'add' or 'subtract'.")

if __name__ == "__main__":
    main()