from models import Task

class TaskManager:
    """Represents a task manager that houses a to-do list"""

    def __init__(self):
        self.users = []
        self.tasks = []
        self.current_user = None

    def add_task(self):
        name_input = input("What task would you like to add to your to-do list? ")
        while name_input in self.tasks:
            name_input = input("That task is already in you list! Please enter a new one: ")
        description_input = input("Please add a description of your task here:\n==>")
        new_task = Task(name_input, description_input)
        self.tasks.append(new_task)

    def view_all_tasks(self):
        for task in self.tasks:
            task.display_task()
    
    def view_single_task(self):
        id_input = input("What is the ID of the post you would like to see? ")
        for task in self.tasks:
            if task.id == id_input:
                task.display_task()
        else:
            print("That ID does not exist! Please enter another one.")

    def edit_task(self):
        id_input2 = input("What is the ID of the post you would like to edit? ")
        for task in self.tasks:
            if task.id == id_input2:
                new_name = input("If you would like to chnage the name of the task, enter it here. Or enter 'skip': ")
                if new_name.lower() != 'skip':
                    task.task_name = new_name
                
                new_description = input("If you would like to change the description of the task, enter it here or enter 'skip': ")
                if new_description.lower() !='skip':
                    task.description = new_description
                
                print(f"Your {task} has been changed!")
        else:
            print("That task does not exist. Please enter another one")

    def delete_task(self):
        id_input3 = input('What is the id of the task you would like to delete? ')
        for task in self.tasks:
            if task.id == id_input3:
                confirm = input("Are you sure you would like to delete this post (y/n)? ")
                if confirm.lower() == 'y':
                    self.tasks.pop(task)
                else:
                    print("The task has not been removed.")
        else:
            print("That task does not exist. Please enter another one")