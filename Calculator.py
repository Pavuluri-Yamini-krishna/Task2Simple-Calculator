def simple_calculator():
    # Function to perform the calculation
    def calculate(num1, num2, operation):
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            if num2 != 0:
                return num1 / num2
            else:
                return "Error: Division by zero is not allowed."
        else:
            return "Error: Invalid operation."

    # Prompt user for inputs
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        # Perform calculation
        result = calculate(num1, num2, operation)

        # Display result
        print(f"The result is: {result}")
    except ValueError:
        print("Error: Invalid input. Please enter numerical values for the numbers.")

# Run the calculator
simple_calculator()