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


while True:
    print('\n===Welcome to the Multi-Utility Program!===\n')
    print('Please select a utility')
    print('1. Calculator')
    print('2. even/odd Checker')    
    print('3. unit converter') 
    print('4. text-based game')  
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