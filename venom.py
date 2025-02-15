class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_as_done(self):
        self.completed = True

    def __str__(self):
        status = "✅ всьо" if self.completed else "❌ не всьо"
        return f"{self.title} ({self.deadline}) - {status}\n{self.description}\n"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    def mark_task_as_done(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_as_done()
                break

    def show_tasks(self):
        if not self.tasks:
            print("позор без діла")
        else:
            for task in self.tasks:
                print(task)


# приклад цього шедевру людських мрій та фантазій
manager = TaskManager()
manager.add_task(Task("купити бутилку еаеае пусту бутилку", "піти поплакати в магазині і купити бутилку", "2025-02-16"))
manager.add_task(Task("зробити дз(не треба)", "закінчити укр мову(не треба)", "2025-02-17"))

print("--- спісок завдань ---")
manager.show_tasks()

manager.mark_task_as_done("купити бутиль йоу")
print("--- оновлений список ---")
manager.show_tasks()
