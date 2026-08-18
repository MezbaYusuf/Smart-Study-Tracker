# All tasks
tasks = []

# Infinite loop

#fucntion for showing task
def show_task():
    print(tasks)

#fucntion to add tasks : 
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
            
            #task status
            task["completed"] = False

            tasks.append(task)

            return task
#fucntion to mark task as complete : 
def complete_task():
        complete_task_number = int(input(f"Which task you want to complete (1 - {len(tasks)}) : "))
        complete_task_number -= 1 

        new_complete_task = tasks[complete_task_number]
        new_complete_task["completed"] = True
#functions to delete tasks : 

while True:
    print('''========== SMART STUDY PLANNER ==========

1. Add subject
2. Add study task
3. View today's tasks
4. Complete a task
8. Save & Exit
''')



    user_choice = int(input("Enter your choice (1-8): "))

    if user_choice == 1:
        print("\n[+] Add subject selected.\n")
        task_number = int(input("How many tasks you want to add: "))

        for i in range(task_number):
            # One task
            task = add_tasks()
            print("\nTask added successfully!")
            print(task)



    elif user_choice == 2:
        print("\n[+] Add study task selected.\n")
        add_tasks()        

    elif user_choice == 3:
        print("\n[+] View Tasks slected .\n")
        show_task()

    elif user_choice == 4:
        print("\n[+] Complete task selected.\n")
        task_complete_number = int(input("How many tasks you want to complete : "))
        for i in range(task_complete_number):
            complete_task()


    elif user_choice == 8:
        print("\nExiting... Goodbye!\n")
        break

    else:
        print("\nInvalid choice! Please try again.\n")

    input("Press Enter to go back to the menu...")