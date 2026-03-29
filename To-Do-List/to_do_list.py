def add_task(tasks, task_name):
    """Adds a new task to the task list.

    Args:
        tasks (list): The current list of tasks.
        task_name (str): The description of the task to add.
    """
    tasks.append({"name": task_name, "completed": False})
    print(f"Task '{task_name}' added successfully.")

def view_tasks(tasks):
    """Displays all tasks with their status.

    Args:
        tasks (list): The list of tasks to display.
    """
    if not tasks:
        print("\nYour to-do list is empty.")
        return

    print("\n--- Your To-Do List ---")
    for idx, task in enumerate(tasks, 1):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{idx}. {status} {task['name']}")
    print("-----------------------")

def mark_completed(tasks, index):
    """Marks a specific task as completed.

    Args:
        tasks (list): The current list of tasks.
        index (int): The 1-based index of the task.
    """
    if 0 < index <= len(tasks):
        tasks[index - 1]["completed"] = True
        print(f"Task {index} marked as completed.")
    else:
        print("Invalid task number.")

def main():
    """Main entry point for the To-Do List application."""
    tasks = []
    while True:
        print("\n--- Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")

        if choice == '1':
            name = input("Enter task description: ")
            add_task(tasks, name)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            view_tasks(tasks)
            try:
                idx = int(input("Enter the task number to mark complete: "))
                mark_completed(tasks, idx)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid selection, please try again.")

if __name__ == "__main__":
    main()