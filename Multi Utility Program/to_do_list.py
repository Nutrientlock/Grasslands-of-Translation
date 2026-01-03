task = []

with open('tasks.txt', 'r') as f:
    for line in f:
        task.append(line.strip())
def to_do():
    while True:
        print('\n===Welcome===')
        print('Chosse an Option\n')
        print('1. Add a Task')
        print('2. Veiw all Task')
        print('3. Remove a Task')
        print('q. Exit\n')
        choice = input('Enter your choice: ').strip().lower()   
        if choice == 'q':
            print('Exiting To Do List. Goodbye!\n')
            break
        elif choice == '1':
            new_task = input('Enter Task: ')
            task.append(new_task)
            print("==Task Entered==")
        elif choice == '2':
            if not task:
                print('No Tasks')
            else:
                for item in task:
                    print(f"Task: {item}")
        elif choice == '3':
            if not task:
                print('No Task to Remove')
            else:
                task_to_remove = input('Enter Task to be Removed: ')
                if task_to_remove in task:
                    task.remove(task_to_remove)
                    print('==Task Removed==')
                else:
                    print('Task Does Not Exist')
if __name__ == '__main__':
    to_do()