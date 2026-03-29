import os

# --- CONFIGURATION ---
# The file where tasks will be saved
filename = "todo.txt"

# --- FUNCTIONS ---

def load_tasks():
    """Reads tasks from the file into a list."""
    tasks = []
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            # .strip() removes the invisible newline character at the end
            tasks = [line.strip() for line in f.readlines()]
    return tasks

def save_tasks(tasks):
    """Writes the current list of tasks back to the file."""
    with open(filename, 'w') as f:
        for task in tasks:
            f.write(task + "\n")

def view_tasks(tasks):
    """Prints the list of tasks with numbers."""
    print("\n--- YOUR TASKS ---")
    if not tasks:
        print("Your list is empty.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    print("------------------")

def add_task(tasks):
    """Adds a new task."""
    item = input("Enter the task to add: ")
    tasks.append(item)
    save_tasks(tasks)
    print(f"Added: '{item}'")

def remove_task(tasks):
    """Removes a task by its number."""
    view_tasks(tasks)
    if not tasks:
        return

    try:
        num = int(input("Enter the number of the task to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Removed: '{removed}'")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

# --- MAIN PROGRAM LOOP ---
def main():
    tasks = load_tasks()
    
    while True:
        print("\n--- MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()