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
        
    elif user_choice == 2:
        print("\n[+] Add study task selected.\n")
        
    elif user_choice == 8:
        print("\nExiting... Goodbye!\n")
        break  
        
    else:
        print("\nInvalid choice! Please try again.\n")

    input("Press Enter to go back to the menu...")