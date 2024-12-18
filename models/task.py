class Task:
    def __init__(self, task_id, title, description, done, priority, due_date):
        self.id = task_id
        self.title = title
        self.description = description
        self.done = done
        self.priority = priority
        self.due_date = due_date