# All tasks
tasks = []

# Infinite loop
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

    user_choice = int(input("Enter your choice (1-8): "))

    if user_choice == 1:
        print("\n[+] Add subject selected.\n")
        task_number = int(input("How many tasks you want to add: "))

        for i in range(task_number):
            # One task
            task = {}

            subject = input("Enter the subject here: ")
            task["subject"] = subject

            task_name = input("Enter the task here: ")
            task["task_name"] = task_name

            priority = input("Enter the priority here: ")
            task["priority"] = priority

            deadline = input("Enter the deadline here: ")
            task["deadline"] = deadline

            # Add one task to all tasks
            tasks.append(task)

            print("\nTask added successfully!")
            print(task)

    elif user_choice == 2:
        print("\n[+] Add study task selected.\n")

    elif user_choice == 8:
        print("\nExiting... Goodbye!\n")
        break

    else:
        print("\nInvalid choice! Please try again.\n")

    input("Press Enter to go back to the menu...")