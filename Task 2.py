def calculator():
    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation = input("Enter the number of the operation (1/2/3/4): ")

    if operation not in ['1', '2', '3', '4']:
        print("Invalid operation choice. Please try again.")
        return

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operation == '1':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}")
    elif operation == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}")

calculator()
