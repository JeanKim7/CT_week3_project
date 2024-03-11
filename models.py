class Task:
    """Represents a task in the to-do list"""
    id_counter = 1
    
    def __init__(self, task_name, description, author):
        self.id = Task.id_counter
        Task.id_counter += 1
        self.task_name = task_name
        self.description = description
        self.status = "not done"
        self.author = author
    
    def __str__(self):
        return self.task_name

    def __repr__(self):
        return f"< id: {self.id} | {self.task_name} >"
    
    def display_task(self):

        if self.status == 'done':
            print(f"\n[X] {self.task_name} | id: {self.id}\n    =>{self.description}\n\n")
        elif self.status == 'not done':
            print(f"\n[ ] {self.task_name} | id: {self.id}\n    =>{self.description}\n\n")

class User:
    """Represents a user of the task manager"""
    id_counter = 1

    def __init__(self, username, password):
        self.id = Task.id_counter
        Task.id_counter+=1
        self.username = username
        self.__password = password

    def __str__(self):
        return self.username

    def __repr__(self):
        return f"< {self.id} | {self.username} >"
    
    def check_password(self, pw_guess):
        return self.__password == pw_guess