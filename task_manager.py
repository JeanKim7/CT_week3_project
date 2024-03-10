from models import Task, User

class TaskManager:
    """Represents a task manager that houses a to-do list"""

    def __init__(self):
        self.users = []
        self.tasks = []
        self.current_user = None

    def create_new_user(self):
        new_username = input("Enter a username for your account: ")
        while new_username in [u.username for u in self.users]:
            new_username = input("That username is already taken!")
        new_password = input("Enter a password for your account: ")
        new_user = User(new_username, new_password)
        self.users.append(new_user)
        print("Your account has been created!")

    def log_in(self):
        username_login = input("Please enter your username: ")
        password_login = input("Pleaes enter your password: ")
        for user in self.users:    
            if username_login == user.username and user.check_password(password_login):
                self.current_user = user
                print("You have been logged in!")
        else:
            print("The password or username you entered is incorrect.")

    def log_out(self):
        double_check = input("Are you sure you would like to log out (y/n)?" )
        while double_check.lower() not in ['y', 'n']:
            double_check = input("Please enter 'y' or 'n' only. Are you sure you want to log out? ")
        if double_check.lower() == 'y':
            self.current_user = None
            print("You have been logged out!")
         
    def add_task(self):
        name_input = input("What task would you like to add to your to-do list? ")
        description_input = input("Please add a description of your task here:\n==>")
        new_task = Task(name_input, description_input, self.current_user)
        self.tasks.append(new_task)
        print("Your task has been created!")

    def check_off_task(self):
        print("Here are your tasks: ")
        for task in self.tasks:
            if task.author == self.current_user:
                print(f"{task.task_name} | id: {task.id}")
        checkoff_input = input("\nWhat is the id of the task would you like to mark as done? ")
        for task in self.tasks:
            if task.id == int(checkoff_input):
                if self.current_user == task.author:
                    task.status = 'done'
                    print("The task has been marked as done!")
                else: 
                    print("You are not authorized to change this task.")
        else: 
            print("The id you entered does not exist.")
    
    def view_all_tasks(self):
        for task in self.tasks:
            if task.author == self.current_user:
                task.display_task()
    
    def view_single_task(self):
        id_input = input("What is the ID of the post you would like to see? ")
        for task in self.tasks:
            if task.id == int(id_input):
                if task.author == self.current_user:
                    task.display_task()
                else:
                    print("You are not authorized to see this task.")
        else:
            print("That ID does not exist!")

    def edit_task(self):
        id_input2 = input("What is the ID of the post you would like to edit? ")
        for task in self.tasks:
            if task.id == int(id_input2):
                if task.author == self.current_user:
                    new_name = input("If you would like to chnage the name of the task, enter it here. Or enter 'skip': ")
                    if new_name.lower() != 'skip':
                        task.task_name = new_name
                    
                    new_description = input("If you would like to change the description of the task, enter it here or enter 'skip': ")
                    if new_description.lower() !='skip':
                        task.description = new_description
                    
                    print(f"Your {task} has been changed!")
                else:
                    print("You are not auhorized to edit this task.")
        else:
            print("That task does not exist. Please enter another one")

    def delete_task(self):
        id_input3 = input('What is the id of the task you would like to delete? ')
        for task in self.tasks:
            if task.id == int(id_input3):
                if task.author == self.current_user:
                    confirm = input("Are you sure you would like to delete this post (y/n)? ")
                    if confirm.lower() == 'y':
                        self.tasks.pop(task)
                    else:
                        print("The task has not been removed.")
                else:
                    print("You are not authorized to delete this task.")
        else:
            print("That task does not exist. Please enter another one")