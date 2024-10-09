def main():
    tasks = []

    while True:
        print("\n===== To-Do List =====")
        print("1. Add New Event")
        print("2. Edit Event")
        print("3. Show Events")
        print("4. Mark Event as Done")
        print("5. Remove Event")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            n_tasks = int(input("How many tasks you want to add? "))

            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print("Task added!")

        elif choice == '2':
            task_index = int(input("Enter the task number to edit: ")) - 1
            if 0 <= task_index < len(tasks):

                print("Task updated.")
            else:
                print("Invalid task number.")

        elif choice == '3':
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

        elif choice == '4':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done.")
            else:
                print("Invalid task number.")

        elif choice == '5':
            task_index = int(input("Enter the task number to remove: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks.remove(task_index[])
                print("Task removed.")
            else:
                print("Invalid task number.")

        elif choice == '6':
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()