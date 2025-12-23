def even_odd_checker():
    while True:
        print('\n===Even/Odd Checker===\n')
        print('Choose an option\n')
        print('1.Check if even or odd')
        print('q.Exit\n')
        choice = input('Enter your choice: ').strip().lower()   
        if choice == 'q':
            print('Exiting Even/Odd Checker. Goodbye!\n')
            break
        elif choice == '1':
            checker_num = float(input('Enter a number to check if its even or odd:'))
            if checker_num % 2 == 0:
                print(f'{checker_num} is an Even number.\n')
            else:
                print(f'{checker_num} is an Odd number.\n')     

def unit_converter():
    while True:
        print('\n===Unit Converter===\n')
        print('Chosse an Option\n')
        print('1. Convert kilometers to miles')
        print('2. Convert miles to kilometers')
        print('q. Exit\n')
        choice = input('Enter your choice: ').strip().lower()   
        if choice == 'q':
            print('Exiting Unit Converter. Goodbye!\n')
            break
        elif choice == '1':
            km = float(input('Enter distance in kilometers: '))
            miles = km / 1.621371
            print(f'{km} kilometers is equal to {miles:.2f} miles.\n')
        elif choice == '2':
            miles = float(input('Enter distance in miles: '))
            km = miles * 1.621371
            print(f'{miles} miles is equal to {km:.2f} kilometers.\n')


while True:
    print('\n===Welcome to the Multi-Utility Program!===\n')
    print('Please select a utility')
    print('1. Calculator')
    print('2. even/odd Checker')    
    print('3. unit converter')
    print('4. Multi Calculation') 
    print('q. Exit') 
    print('------------------------------')
    user_choice = input('Your choice: ').strip().lower()
    print("\n------------------------------\n")
    
    if user_choice == 'q':
        print('Exiting the Multi-Utility Program. Goodbye!\n')
        break
    
    if user_choice == '1':
        import calculator
    elif user_choice == '2': 
        even_odd_checker()
    elif user_choice == '3':
        unit_converter()
    elif user_choice == '4':
        import MultiUtility
