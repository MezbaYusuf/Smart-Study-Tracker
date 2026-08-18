# All tasks list to store task dictionaries
tasks = []

# Function for showing tasks
def show_task():
    if not tasks:
        print("\nNo tasks available!\n")
        return
    print("\n--- Task List ---")
    for index, task in enumerate(tasks, 1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index}. Subject: {task['subject']} | Task: {task['task_name']} | Priority: {task['priority']} | Deadline: {task['deadline']} | Status: {status}")
    print("-" * 30)

# Function to add tasks 
def add_tasks():
    task = {}
    subject = input("Enter the subject here: ")
    task["subject"] = subject

    task_name = input("Enter the task here: ")
    task["task_name"] = task_name

    priority = input("Enter the priority here: ")
    task["priority"] = priority

    deadline = input("Enter the deadline here: ")
    task["deadline"] = deadline
    
    # Default task status is False (not completed)
    task["completed"] = False

    tasks.append(task)

    return task

# Function to mark task as complete 
def complete_task():
    if not tasks:
        print("\nNo tasks to complete!\n")
        return
    
    while True:
        try:
            complete_task_number = int(input(f"Which task you want to complete (1 - {len(tasks)}) : "))
            if 1 <= complete_task_number <= len(tasks):
                complete_task_number -= 1 
                new_complete_task = tasks[complete_task_number]
                new_complete_task["completed"] = True
                print("\nTask marked as completed successfully!")
                break
            else:
                print(f"Please enter a valid number between 1 and {len(tasks)}.")
        except ValueError:
            print("Please enter a valid integer!")

# Function to delete tasks 
def delete_task():
    if not tasks:
        print("\nNo tasks to delete!\n")
        return
    
    while True:
        try:
            delete_task_number = int(input(f"Which task you want to delete (1 - {len(tasks)}) : "))
            if 1 <= delete_task_number <= len(tasks):
                deleted = tasks.pop(delete_task_number - 1)
                print(f"\nTask '{deleted['task_name']}' deleted successfully!")
                break
            else:
                print(f"Please enter a valid number between 1 and {len(tasks)}.")
        except ValueError:
            print("Please enter a valid integer!")

# Main infinite loop for the application menu
while True:
    print('''========== SMART STUDY PLANNER ==========

1. Add subject
2. Add study task
3. View today's tasks
4. Complete a task
5. Delete a task
6. View progress
7. Search tasks
8. Save & Exit
''')

    # Error handling for main menu choice input
    while True: 
        try:
            user_choice = int(input("Enter your choice (1-8): "))
            break
        except ValueError: 
            print("Please Enter Valid Number : ")

    if user_choice == 1:
        print("\n[+] Add subject selected.\n")
        # Error handling for number of tasks to add
        while True: 
            try:
                task_number = int(input("How many tasks you want to add: "))
                if task_number > 0:
                    break
                else:
                    print("Please enter a number greater than 0.")
            except ValueError: 
                print("Please enter a number please : ")

        for i in range(task_number):
            # Add each task
            task = add_tasks()
            print("\nTask added successfully!")
            print(task)

    elif user_choice == 2:
        print("\n[+] Add study task selected.\n")
        add_tasks()
        print("\nTask added successfully!")

    elif user_choice == 3:
        print("\n[+] View Tasks selected .\n")
        show_task()

    elif user_choice == 4:
        print("\n[+] Complete task selected.\n")
        if not tasks:
            print("No tasks available!")
        else:
            show_task()
            # Error handling for how many tasks to complete
            while True: 
                try:  
                    task_complete_number = int(input("How many tasks you want to complete : "))
                    if task_complete_number > 0:
                        break
                    else:
                        print("Please enter a number greater than 0.")
                except ValueError: 
                    print("Enter a number please ! ")
            for i in range(task_complete_number):
                complete_task()

    elif user_choice == 5:
        print("\n[+] Delete task selected.\n")
        if not tasks:
            print("No tasks available to delete!")
        else:
            show_task()
            delete_task()

    elif user_choice == 6:
        print("\n[+] View progress selected.\n")
        if not tasks:
            print("No progress data available.")
        else:
            completed_count = sum(1 for t in tasks if t["completed"])
            print(f"Total Tasks: {len(tasks)} | Completed: {completed_count} | Pending: {len(tasks) - completed_count}")

    elif user_choice == 7:
        print("\n[+] Search tasks selected.\n")
        if not tasks:
            print("No tasks to search!")
        else:
            search_query = input("Enter subject or task name to search: ").lower()
            found = False
            for index, task in enumerate(tasks, 1):
                if search_query in task['subject'].lower() or search_query in task['task_name'].lower():
                    status = "Completed" if task["completed"] else "Pending"
                    print(f"{index}. Subject: {task['subject']} | Task: {task['task_name']} | Status: {status}")
                    found = True
            if not found:
                print("No matching tasks found.")

    elif user_choice == 8:
        print("\nExiting... Goodbye!\n")
        break

    else:
        print("\nInvalid choice! Please try again.\n")

    input("Press Enter to go back to the menu...")