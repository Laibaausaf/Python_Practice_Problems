a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

while True:
    print("Enter which operation you want to perform?")
    print("a. addition")
    print("b. subtraction")
    print("c. divison")
    print("d. multiplication")
    print("e. exit")
    c = input("Enter your choice: ")

    if c == 'a':
        sum = a + b
        print(f"Sum of {a} + {b} is:{sum}")
    elif c == 'b':
        sub = a - b
        print(f"Difference of {a} and {b} is:{sub}")
    elif c == 'c':
        if b != 0:
            div = a / b
            print(f"Division of {a} and {b} is:{div}")
        else:
            print("integer cannot be divided by zero")
    elif c == 'd':
        mul = a * b
        print(f"Multiplication of {a} and {b} is: {mul}")
    elif c == 'e':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
