from task_manager import TaskManager

def run_task_manager():

    print("Welcome to Jean's notes app to keep track of tasks you have to do!")
    task_manager1 = TaskManager()

    while True: 
        if task_manager1.current_user == None:
            print("1. Sign Up\n2. Log In\n3. Quit")
            option = input("Enter what you would like to do (1, 2 or 3): ")
            while option not in ['1', '2', '3']:
                option = input("Please enter only 1, 2 or 3: ")
            if option == '3':
                print("Thanks for using our program!")
                break
            elif option == '1':
                task_manager1.create_new_user()
            elif option == '2':
                task_manager1.log_in()
                print(f"Hello {task_manager1.current_user}! Thanks for joining us.")
        else:
            print("1. Log Out\n2. Add a task\n3. Mark a task as done\n4. View all tasks\n5. View a single task\n6. Edit a task\n 7. Delete a task")
            option2 = input("What would you like to do (enter only 1 through 7: ")
            while option2 not in ['1', '2', '3', '4','5', '6', '7']:
                option2 = input('Please only enter a number from 1 to 7: ')
            if option2 == '1':
                task_manager1.log_out()
            elif option2 == '2':
                task_manager1.add_task()
            elif option2 == '3':
                task_manager1.check_off_task()
            elif option2 == '4':
                task_manager1.view_all_tasks()
            elif option2 == '5':
                task_manager1.view_single_task()
            elif option2 == '6':
                task_manager1.edit_task()
            elif option2 == '7':
                task_manager1.delete_task()
        
        print(task_manager1.users)
        print(task_manager1.tasks)

run_task_manager()