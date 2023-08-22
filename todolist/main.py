# Define a class to represent a Task
class Task:
    def __init__(self, desc, done=False):
        self.desc = desc
        self.done = done

# Define a To-Do List class
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_desc):
        task = Task(task_desc)
        self.tasks.append(task)

    def mark_as_done(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].done = True

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks):
                status = " [X]" if task.done else " [ ]"
                print(f"{index+1}. {task.desc}{status}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Mark Task as done")
        print("3. Display Tasks")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            task_desc = input("Enter task desc: ")
            todo_list.add_task(task_desc)
        elif choice == "2":
            todo_list.display_tasks()
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            todo_list.mark_as_done(task_index)
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
