# calculator.py
# Get input from the user for the two numbers and the operator

try:
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /, %, **): ")
    num2 = float(input("Enter the second number: "))

    # Perform the user's calculation based on the operator
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero is undefined and is not allowed."
    elif operator == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            result = "Error! Modulus Dividing by zero is not allowed."
    elif operator == '**':
        result = num1 ** num2
    else:
        result = "Error! Invalid operator."

    # Print the result
    print(f"The result is: {result}")

except ValueError:
    print("Error! Invalid input. Please enter valid numbers.")








