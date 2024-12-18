import os
from datetime import datetime
from utils.file_utils import load_json, save_json, get_new_id
from utils.csv_utils import import_csv_to_json, export_json_to_csv

DATE_FORMAT_DATETIME = "%d-%m-%Y %H:%M:%S"

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
NOTES_FILE = os.path.join(DATA_DIR, "notes.json")

class NotesController:
    @staticmethod
    def menu():
        while True:
            print("\nУправление заметками:")
            print("1. Создать новую заметку")
            print("2. Просмотреть список заметок")
            print("3. Просмотреть подробности заметки")
            print("4. Редактировать заметку")
            print("5. Удалить заметку")
            print("6. Экспорт заметок в CSV")
            print("7. Импорт заметок из CSV")
            print("8. Назад")
            choice = input("Выберите действие: ")
            if choice == "1":
                NotesController.create_note()
            elif choice == "2":
                NotesController.list_notes()
            elif choice == "3":
                NotesController.view_note_detail()
            elif choice == "4":
                NotesController.edit_note()
            elif choice == "5":
                NotesController.delete_note()
            elif choice == "6":
                filename = input("Введите имя CSV-файла для экспорта: ")
                fieldnames = ["id","title","content","timestamp"]
                export_json_to_csv(NOTES_FILE, filename, fieldnames)
            elif choice == "7":
                filename = input("Введите имя CSV-файла для импорта: ")
                fieldnames = ["id","title","content","timestamp"]
                import_csv_to_json(filename, NOTES_FILE, fieldnames)
            elif choice == "8":
                break
            else:
                print("Неверный выбор, попробуйте снова.")

    @staticmethod
    def create_note():
        data = load_json(NOTES_FILE)
        title = input("Введите заголовок заметки: ")
        content = input("Введите содержимое заметки: ")
        timestamp = datetime.now().strftime(DATE_FORMAT_DATETIME)
        note_id = get_new_id(data)
        new_note = {
            "id": note_id,
            "title": title,
            "content": content,
            "timestamp": timestamp
        }
        data.append(new_note)
        save_json(NOTES_FILE, data)
        print("Заметка успешно создана!")

    @staticmethod
    def list_notes():
        data = load_json(NOTES_FILE)
        if not data:
            print("Нет заметок для отображения.")
        for note in data:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата: {note['timestamp']}")

    @staticmethod
    def view_note_detail():
        note_id = input("Введите ID заметки: ")
        data = load_json(NOTES_FILE)
        for note in data:
            if str(note["id"]) == note_id:
                print("Заголовок:", note["title"])
                print("Содержимое:", note["content"])
                print("Дата/время:", note["timestamp"])
                return
        print("Заметка не найдена.")

    @staticmethod
    def edit_note():
        note_id = input("Введите ID заметки для редактирования: ")
        data = load_json(NOTES_FILE)
        for note in data:
            if str(note["id"]) == note_id:
                title = input(f"Новый заголовок (старый: {note['title']}): ")
                content = input(f"Новое содержимое (старое: {note['content']}): ")
                if title.strip():
                    note["title"] = title
                if content.strip():
                    note["content"] = content
                note["timestamp"] = datetime.now().strftime(DATE_FORMAT_DATETIME)
                save_json(NOTES_FILE, data)
                print("Заметка успешно обновлена!")
                return
        print("Заметка не найдена.")

    @staticmethod
    def delete_note():
        note_id = input("Введите ID заметки для удаления: ")
        data = load_json(NOTES_FILE)
        new_data = [n for n in data if str(n["id"]) != note_id]
        if len(new_data) != len(data):
            save_json(NOTES_FILE, new_data)
            print("Заметка успешно удалена!")
        else:
            print("Заметка не найдена.")