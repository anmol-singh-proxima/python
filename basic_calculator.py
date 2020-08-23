
# This program performs the operations of a basic calculator
# It take two numbers as inputs from user and ask what kind of arithmetic operation user want to perform
# And after performing the right operation, it print the result


def basic_calculator():
    """This function acts as basic calculator"""

    num1 = input("Enter first number: ")  # taking input

    # handling the exception of typecasting the value of 'num1' to float
    try:
        num1 = float(num1)
    except ValueError:
        print("Error: Input numeric values.\nTry Again!")
        exit()

    num2 = input("Enter second number: ")  # taking input

    # handling the exception of typecasting the value of 'num2' to float
    try:
        num2 = float(num2)
    except ValueError:
        print("Error: Input numeric values.\nTry Again!")
        exit()

    # Asking user for the operation
    print("Select the operation:")
    print("Type:")
    print("1 for Addition\n2 for Subtraction\n3 for Multiplication\n4 for Division\n5 for Integer Division\n6 for Power")
    choice = input("Enter your choice: ")

    result = 0.0

    # Performing the operation and providing the result
    if choice == '1':
        result = num1 + num2
    elif choice == '2':
        result = num1 - num2
    elif choice == '3':
        result = num1 * num2
    elif choice == '4':
        result = num1 / num2
    elif choice == '5':
        result = num1 // num2
    elif choice == '6':
        result = num1 ** num2
    else:
        print("Wrong Input! Try Again.")
        exit()

    print(f'\nThe result is: {result}')


basic_calculator()