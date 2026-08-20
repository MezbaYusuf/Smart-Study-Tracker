# All tasks
tasks = []


# function for showing task
def show_task():
    print(tasks)


# function to add tasks
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

    # task status
    task["completed"] = False

    tasks.append(task)

    return task


# function to mark task as complete
def complete_task():
    while True:
        try:
            complete_task_number = int(
                input(f"Which task you want to complete (1 - {len(tasks)}) : ")
            )

            if complete_task_number < 1 or complete_task_number > len(tasks):
                print("Invalid Task Number")
                continue

            break

        except ValueError:
            print("Please enter a valid number!")

    complete_task_number -= 1

    new_complete_task = tasks[complete_task_number]
    new_complete_task["completed"] = True


# function to delete tasks
def delete_task(delete_task_number):
    delete_task_number -= 1
    tasks.pop(delete_task_number)


# function to view progress
def view_progress():
    total_task = len(tasks)
    total_complete_task_number = 0


    for i in tasks:
        if i["completed"] == True:
            total_complete_task_number += 1

    total_incomplete_task_number = total_task - total_complete_task_number

    print("Total tasks:", total_task)
    print("Completed tasks:", total_complete_task_number)
    print("Incomplete tasks:", total_incomplete_task_number)
    print(f"{(total_complete_task_number / total_task) * 100} is the percentance")

# Infinite loop
while True:
    print('''========== SMART STUDY PLANNER ==========

1. Add subject
2. Add study task
3. View today's tasks
4. Complete a task
5. Delete a task
6. View progress
7. Save & Exit
''')

    while True:
        try:
            user_choice = int(input("Enter your choice (1-8): "))
            break

        except ValueError:
            print("Please Enter Valid Number : ")

    if user_choice == 1:
        print("\n[+] Add subject selected.\n")

        while True:
            try:
                task_number = int(input("How many tasks you want to add: "))
                break

            except ValueError:
                print("Please enter a number please : ")

        for i in range(task_number):
            task = add_tasks()

            print("\nTask added successfully!")
            print(task)

    elif user_choice == 2:
        print("\n[+] Add study task selected.\n")
        add_tasks()

    elif user_choice == 3:
        print("\n[+] View Tasks selected.\n")
        show_task()

    elif user_choice == 4:
        print("\n[+] Complete task selected.\n")

        while True:
            try:
                task_complete_number = int(
                    input("How many tasks you want to complete : ")
                )
                break

            except ValueError:
                print("Enter a number please ! ")

        for i in range(task_complete_number):
            complete_task()

    elif user_choice == 5:
        print("\n[+] Delete task selected.\n")

        while True:
            try:
                delete_task_number = int(
                    input("Enter the task number you want to delete : ")
                )
                break

            except ValueError:
                print("Please provide us a valid number.")

        delete_task(delete_task_number)

    elif user_choice == 6:
        print("\n[+] View progress selected.\n")
        view_progress()



    elif user_choice == 7:
        print("\nExiting... Goodbye!\n")
        break

    else:
        print("\nInvalid choice! Please try again.\n")

    input("Press Enter to go back to the menu...")