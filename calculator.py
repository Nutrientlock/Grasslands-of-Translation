#repeated: print result
#repeated:

while True:
    print("===Simple Integer Calculator===\n")
    print("What is your Choice")
    print("1, Addition")
    print("2, Subtraction")
    print("3, Multiplication")
    print("4, Division")
    print("5, Power")
    print("6, Modular")
    print('q, Exit')

    choice = input('Enter your choice: ').strip().lower()

    if choice == 'q':
        break

    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))

    if choice == '1':
        results = num1 + num2
        print("results:", results)

    elif choice == '2':
        results = num1 - num2
        print("results:", results)

    elif choice == '3':
        results = num1 * num2
        print("results:", results)

    elif choice == '4':
        if num2 == 0:
            print("Second number cannot be zero")
        else:
            results = num1 / num2
            print("results:", results)

    elif choice == '5':
        results = num1 ** num2
        print("results:", results)

    elif choice == '6':
        results = num1 % num2
        print("results:", results)

    else:
        print('Invalid input')

    