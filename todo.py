# To-Do List CLI Application

# List to store tasks
tasks = []

# Function to add a task
def add_task(task_description):
    tasks.append({"description": task_description, "completed": False})
    print("Task added successfully!")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        for i, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{i + 1}. {task['description']} - {status}")


def complete_task(task_number):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number.")


def delete_task(task_number):
    if 0 < task_number <= len(tasks):
        tasks.pop(task_number - 1)
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")


def main():
    while True:
        print("\nTo-Do List App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task_description = input("Enter task description: ")
            add_task(task_description)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            try:
                task_number = int(input("Enter task number to mark as completed: "))
                complete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            try:
                task_number = int(input("Enter task number to delete: "))
                delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
