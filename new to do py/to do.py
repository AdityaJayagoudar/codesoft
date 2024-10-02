# Simple To-Do List Application

# Initialize an empty dictionary to store tasks
tasks = {}

# Display the menu options
def show_menu():
    print("\n-- To-Do List Menu --")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

# View all tasks
def view_tasks():
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for task_id, task_details in tasks.items():
            status = "✔️" if task_details['completed'] else "❌"
            print(f"{task_id}. {task_details['name']} - {status}")

# Add a new task
def add_task():
    task_name = input("\nEnter the task: ").strip()
    if task_name:
        task_id = len(tasks) + 1
        tasks[task_id] = {"name": task_name, "completed": False}
        print(f"Task '{task_name}' added.")
    else:
        print("Task cannot be empty!")

# Mark a task as completed
def mark_task_completed():
    if not tasks:
        print("\nYour to-do list is empty.")
        return
    view_tasks()
    task_num = input("\nEnter the number of the task to mark as completed: ")
    
    try:
        task_id = int(task_num)
        if task_id in tasks:
            tasks[task_id]['completed'] = True
            print(f"Task '{tasks[task_id]['name']}' marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task
def delete_task():
    if not tasks:
        print("\nYour to-do list is empty.")
        return
    view_tasks()
    task_num = input("\nEnter the number of the task to delete: ")
    
    try:
        task_id = int(task_num)
        if task_id in tasks:
            removed_task = tasks.pop(task_id)
            print(f"Task '{removed_task['name']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main function to run the to-do list application
def main():
    while True:
        show_menu()
        choice = input("\nChoose an option: ")
        
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_task_completed()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("\nExiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
