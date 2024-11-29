def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def calculator():
    print("Welcome to the Calculator!")
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    while True:
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "5":
            print("Thank you for using the Calculator. Goodbye!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice! Please select a valid operation.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        if choice == "1":
            print(f"The result is: {add(num1, num2)}")
        elif choice == "2":
            print(f"The result is: {subtract(num1, num2)}")
        elif choice == "3":
            print(f"The result is: {multiply(num1, num2)}")
        elif choice == "4":
            print(f"The result is: {divide(num1, num2)}")

if __name__ == "__main__":
    calculator()
