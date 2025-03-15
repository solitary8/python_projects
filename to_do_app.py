

class Task:
    def __init__(self, title, due_date, completed):
        self.title = title
        self.due_date = due_date
        self.completed = completed

    def mark_completed(self):
        self.completed = True

        
    def add_tasks(self):
        global task_number
        self.title = input("Enter title : ")
        self.due_date = int(input("Enter 1:"))
        self.completed = int(input("Enter 1 for task completed else enter 0:"))

    def edit_task(self, new_title, new_due_date):
        self.title = new_title
        self.due_date = new_due_date

    def __str__(self):
        return f"Task : {self.title} | Due Date : {self.due_date} | Completed : {self.completed}"
    

    def to_string(self):
        return f"{self.title} {self.due_date} {self.completed}"
    

    @classmethod
    def from_to_string(cls, task_string):
        title, due_date, completed = task_string.strip().split(",")
        return cls(title, due_date, completed == 'True')
    
class To_Do_List:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def show_tasks(self):
        if self.tasks:
            for task in self.tasks:
                print(task)

        else: 
            print("No Tasks in the list")


    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(task.to_string() + '\n')

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    task = Task.from_to_string(line)
                    self.add_task(task)
        except FileNotFoundError:
            print(f"{filename} does not exist check any typos or file extension before trying again.")


def add_new_task(to_do_list):
    title = input("Enter title : ")
    due_date = input('Enter the due date (YYYY-MM-DD) :')
    completed = input('Is the task completed ?(yes/no) :').lower()

    completed = True if completed == 'yes' else False
    new_task = Task(title, due_date, completed)
    to_do_list.add_task(new_task)
    print(f"Task {title} succesfully added !")

def main():
    to_do_list = To_Do_List()
    to_do_list.load_from_file('tasks.txt')

    while True:
        print('\n To-Do List Menu')
        print("1. View Tasks")
        print("2.Add Task")
        print("3.Remove Task")
        print("4.Save and Exit")
        choice = int(input("Enter your choice : "))
        if choice == 1:
            print('\n All Tasks')
            to_do_list.show_tasks()

        elif choice == 2:
            add_new_task(to_do_list)

        elif choice == 3:
            to_do_list.remove_task()

        elif choice == 4:
            to_do_list.save_to_file('tasks.txt')
            print("\n Task(s) Saved to file Exiting...")
            break

        else:
            print("Invalid choice. Try Again !")

main()