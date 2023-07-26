import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks, 1):
                print(f"{index}. {task}")
                
    def save_tasks_to_file(self, file_path):
        with open(file_path, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def load_tasks_from_file(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
    
    def clear_tasks(self):
        self.tasks = []

def main():
    clear()
    
    todo_list = ToDoList()
    file_path = "tasks.txt"

    todo_list.load_tasks_from_file(file_path)

    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Show Tasks")
        print("4. Clear All Tasks")
        print("5. Save and Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            clear()
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print("Task added successfully!")
        elif choice == "2":
            clear()
            task = input("Enter the task to remove: ")
            try:
                todo_list.remove_task(task)
                clear()
                print("Task removed successfully!")
            except ValueError:
                print("Task not found in the list.")
        elif choice == "3":
            clear()
            todo_list.show_tasks()
        elif choice == "4":
            clear()
            todo_list.clear_tasks()
            print("All tasks cleared.")
        elif choice == "5":
            print("Exiting the To-Do List.")
            todo_list.save_tasks_to_file(file_path)
            break
        else:
            clear()
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()