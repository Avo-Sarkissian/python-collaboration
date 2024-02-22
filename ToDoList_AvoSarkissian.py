class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})

    def view_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                status = "Completed" if task['completed'] else "Not Completed"
                print(f"{idx}. {task['task']} - {status}")

    def mark_completed(self, task_index):
        if 0 < task_index <= len(self.tasks):
            self.tasks[task_index - 1]['completed'] = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 0 < task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
            print("Task deleted.")
        else:
            print("Invalid task index.")


def main():
    todo_list = ToDoList()

    while True:
        print("\n--- To-Do List ---")
        print("1. Add new task")
        print("2. View all tasks")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Please enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_index = int(input("Please enter the index of the task to mark as completed: "))
            todo_list.mark_completed(task_index)
        elif choice == '4':
            task_index = int(input("Please enter the index of the task to delete: "))
            todo_list.delete_task(task_index)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()
