import os
from utils.file_utils import load_json, save_json, get_new_id
from utils.csv_utils import import_csv_to_json, export_json_to_csv

DATE_FORMAT = "%d-%m-%Y"
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
TASKS_FILE = os.path.join(DATA_DIR, "tasks.json")

class TasksController:
    @staticmethod
    def menu():
        while True:
            print("\nУправление задачами:")
            print("1. Добавить новую задачу")
            print("2. Просмотреть задачи")
            print("3. Отметить задачу как выполненную")
            print("4. Редактировать задачу")
            print("5. Удалить задачу")
            print("6. Экспорт задач в CSV")
            print("7. Импорт задач из CSV")
            print("8. Назад")
            choice = input("Выберите действие: ")
            if choice == "1":
                TasksController.add_task()
            elif choice == "2":
                TasksController.view_tasks()
            elif choice == "3":
                TasksController.mark_done()
            elif choice == "4":
                TasksController.edit_task()
            elif choice == "5":
                TasksController.delete_task()
            elif choice == "6":
                fieldnames = ["id","title","description","done","priority","due_date"]
                filename = input("Введите имя CSV-файла для экспорта: ")
                export_json_to_csv(TASKS_FILE, filename, fieldnames)
            elif choice == "7":
                fieldnames = ["id","title","description","done","priority","due_date"]
                filename = input("Введите имя CSV-файла для импорта: ")
                import_csv_to_json(filename, TASKS_FILE, fieldnames)
            elif choice == "8":
                break
            else:
                print("Неверный выбор, попробуйте снова.")

    @staticmethod
    def add_task():
        data = load_json(TASKS_FILE)
        title = input("Введите название задачи: ")
        description = input("Введите описание задачи: ")
        priority = input("Приоритет (Высокий/Средний/Низкий): ")
        due_date = input("Срок (ДД-ММ-ГГГГ): ")
        task_id = get_new_id(data)
        new_task = {
            "id": task_id,
            "title": title,
            "description": description,
            "done": False,
            "priority": priority,
            "due_date": due_date
        }
        data.append(new_task)
        save_json(TASKS_FILE, data)
        print("Задача успешно добавлена!")

    @staticmethod
    def view_tasks():
        data = load_json(TASKS_FILE)
        if not data:
            print("Задач нет.")
        for t in data:
            status = "Выполнена" if t["done"] else "Не выполнена"
            print(f"ID: {t['id']}, Заголовок: {t['title']}, Статус: {status}, Приоритет: {t['priority']}, Срок: {t['due_date']}")

    @staticmethod
    def mark_done():
        task_id = input("Введите ID задачи для отметки о выполнении: ")
        data = load_json(TASKS_FILE)
        for t in data:
            if str(t["id"]) == task_id:
                t["done"] = True
                save_json(TASKS_FILE, data)
                print("Задача отмечена как выполненная!")
                return
        print("Задача не найдена.")

    @staticmethod
    def edit_task():
        task_id = input("Введите ID задачи для редактирования: ")
        data = load_json(TASKS_FILE)
        for t in data:
            if str(t["id"]) == task_id:
                new_title = input(f"Новый заголовок (старый: {t['title']}): ")
                new_description = input(f"Новое описание (старое: {t['description']}): ")
                new_priority = input(f"Новый приоритет (старый: {t['priority']}): ")
                new_due_date = input(f"Новый срок (старый: {t['due_date']}): ")
                if new_title.strip():
                    t["title"] = new_title
                if new_description.strip():
                    t["description"] = new_description
                if new_priority.strip():
                    t["priority"] = new_priority
                if new_due_date.strip():
                    t["due_date"] = new_due_date
                save_json(TASKS_FILE, data)
                print("Задача успешно обновлена!")
                return
        print("Задача не найдена.")

    @staticmethod
    def delete_task():
        task_id = input("Введите ID задачи для удаления: ")
        data = load_json(TASKS_FILE)
        new_data = [x for x in data if str(x["id"]) != task_id]
        if len(new_data) != len(data):
            save_json(TASKS_FILE, new_data)
            print("Задача удалена!")
        else:
            print("Задача не найдена.")