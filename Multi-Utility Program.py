



print('\n===Welcome to the Multi-Utility Program!===\n')
print('Please select a utility')
print('1. Calculator')
print('2. even/odd Checker')    
print('3. unit converter') 
print('4. text-based game')  
print('q. Exit') 
print('------------------------------')

while True:
    user_choice = input('Your choice: ').strip().lower()
    print("\n------------------------------\n")
    
    if user_choice == 'q':
        print('Exiting the Multi-Utility Program. Goodbye!\n')
        break
    
    if user_choice == '1':
        import calculator