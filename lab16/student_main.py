from datetime import date, datetime, timedelta

class Task:
    def __init__(self, title, description, due_date, status="Pending", priority="Medium", notes=None, duration=0, recurrence=None, dependencies=[]):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
        self.priority = priority
        self.notes = notes
        self.duration = duration
        self.recurrence = recurrence
        self.dependencies = dependencies

    def is_due_today(self):
        return self.due_date == date.today()

class Schedule:
    def __init__(self):
        self.tasks = []
        self.history = []

    def add_task(self, task):
        self.tasks.append(task)
        self.history.append(("added", task))

    def remove_task(self, task_title):
        task = self.get_task(task_title)
        if task:
            self.tasks.remove(task)
            self.history.append(("removed", task))

    def get_task(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                return task
        return None

    def list_overdue_tasks(self):
        return [task for task in self.tasks if task.due_date < date.today()]

    def list_tasks_due_today(self):
        return [task for task in self.tasks if task.is_due_today()]

    def sort_tasks_by_due_date(self):
        self.tasks.sort(key=lambda task: task.due_date)
        return self.tasks

    def update_task(self, task_title, **kwargs):
        task = self.get_task(task_title)
        if task:
            for attr, value in kwargs.items():
                setattr(task, attr, value)
            self.history.append(("updated", task))

    def weekly_schedule(self, start_date):
        end_date = start_date + timedelta(days=6)
        return [task for task in self.tasks if start_date <= task.due_date <= end_date]

    def monthly_schedule(self, year, month):
        month_start = date(year, month, 1)
        next_month = month + 1 if month < 12 else 1
        next_year = year + 1 if next_month == 1 else year
        month_end = date(next_year, next_month, 1) - timedelta(days=1)
        return [task for task in self.tasks if month_start <= task.due_date <= month_end]

    def list_tasks_by_priority(self, priority):
        return [task for task in self.tasks if task.priority == priority]

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task.title},{task.description},{task.due_date},{task.status},{task.priority},{task.notes},{task.duration},{task.recurrence},{','.join([d.title for d in task.dependencies])}\n")

    def load_from_file(self, filename):
        self.tasks = []
        with open(filename, "r") as file:
            for line in file:
                task_data = line.strip().split(",")
                title = task_data[0]
                description = task_data[1]
                due_date = datetime.strptime(task_data[2], "%Y-%m-%d").date()
                status = task_data[3]
                priority = task_data[4]
                notes = task_data[5] if task_data[5] else None
                duration = int(task_data[6]) if task_data[6] else 0
                recurrence = task_data[7] if task_data[7] else None
                dependencies = [self.get_task(d) for d in task_data[8].split(",")] if task_data[8] else []
                task = Task(title, description, due_date, status, priority, notes, duration, recurrence, dependencies)
                self.add_task(task)

    def list_tasks_with_notes(self):
        return [task for task in self.tasks if task.notes]

    def mark_as_completed(self, task_title):
        task = self.get_task(task_title)
        if task:
            task.status = "Completed"
            self.history.append(("updated", task))

    def list_completed_tasks(self):
        return [task for task in self.tasks if task.status == "Completed"]

    def find_task_by_keyword(self, keyword):
        return [task for task in self.tasks if keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower()]

    def check_deadlines(self):
        return [task for task in self.tasks if (task.due_date - date.today()).days <= 1]

    def list_all_tasks(self):
        return self.tasks

    def list_tasks_by_duration(self, min_duration, max_duration):
        return [task for task in self.tasks if min_duration <= task.duration <= max_duration]

    def task_history(self):
        return self.history

    def clear_completed_tasks(self):
        self.tasks = [task for task in self.tasks if task.status != "Completed"]

    def list_recurring_tasks(self):
        return [task for task in self.tasks if task.recurrence]

    def set_reminder(self, task_title, reminder_date):
        task = self.get_task(task_title)
        if task:
            task.reminder_date = reminder_date

    def completion_percentage(self):
        completed_tasks = len(self.list_completed_tasks())
        total_tasks = len(self.tasks)
        if total_tasks == 0:
            return 0
        return (completed_tasks / total_tasks) * 100