print("Select an operation to do.")
operation = input("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")

if operation == "1":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    x = num1 + num2
    print(f"The sum is {x}")
elif operation == "2":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    x = num1 - num2
    print(f"The difference is {x}")
elif operation == "3":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    x = num1 * num2
    print(f"The product is {x}")
elif operation == "4":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    x = num1 / num2
    print(f"The result is {x}")
else: 
    print("Unrecognized command.")