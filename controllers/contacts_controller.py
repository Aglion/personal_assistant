import os
from utils.file_utils import load_json, save_json, get_new_id
from utils.csv_utils import import_csv_to_json, export_json_to_csv

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
CONTACTS_FILE = os.path.join(DATA_DIR, "contacts.json")

class ContactsController:
    @staticmethod
    def menu():
        while True:
            print("\nУправление контактами:")
            print("1. Добавить новый контакт")
            print("2. Поиск контакта")
            print("3. Редактировать контакт")
            print("4. Удалить контакт")
            print("5. Экспорт контактов в CSV")
            print("6. Импорт контактов из CSV")
            print("7. Назад")
            choice = input("Выберите действие: ")
            if choice == "1":
                ContactsController.add_contact()
            elif choice == "2":
                ContactsController.search_contact()
            elif choice == "3":
                ContactsController.edit_contact()
            elif choice == "4":
                ContactsController.delete_contact()
            elif choice == "5":
                fieldnames = ["id","name","phone","email"]
                filename = input("Введите имя CSV-файла для экспорта: ")
                export_json_to_csv(CONTACTS_FILE, filename, fieldnames)
            elif choice == "6":
                fieldnames = ["id","name","phone","email"]
                filename = input("Введите имя CSV-файла для импорта: ")
                import_csv_to_json(filename, CONTACTS_FILE, fieldnames)
            elif choice == "7":
                break
            else:
                print("Неверный выбор, попробуйте снова.")

    @staticmethod
    def add_contact():
        data = load_json(CONTACTS_FILE)
        name = input("Введите имя контакта: ")
        phone = input("Введите телефон: ")
        email = input("Введите email: ")
        contact_id = get_new_id(data)
        new_contact = {
            "id": contact_id,
            "name": name,
            "phone": phone,
            "email": email
        }
        data.append(new_contact)
        save_json(CONTACTS_FILE, data)
        print("Контакт успешно добавлен!")

    @staticmethod
    def search_contact():
        query = input("Введите имя или номер телефона для поиска: ").lower()
        data = load_json(CONTACTS_FILE)
        results = [c for c in data if query in c["name"].lower() or query in c["phone"]]
        if results:
            for r in results:
                print(f"ID: {r['id']}, Имя: {r['name']}, Телефон: {r['phone']}, Email: {r['email']}")
        else:
            print("Контакты не найдены.")

    @staticmethod
    def edit_contact():
        contact_id = input("Введите ID контакта для редактирования: ")
        data = load_json(CONTACTS_FILE)
        for c in data:
            if str(c["id"]) == contact_id:
                new_name = input(f"Новое имя (старое: {c['name']}): ")
                new_phone = input(f"Новый телефон (старый: {c['phone']}): ")
                new_email = input(f"Новый Email (старый: {c['email']}): ")
                if new_name.strip():
                    c["name"] = new_name
                if new_phone.strip():
                    c["phone"] = new_phone
                if new_email.strip():
                    c["email"] = new_email
                save_json(CONTACTS_FILE, data)
                print("Контакт обновлён!")
                return
        print("Контакт не найден.")

    @staticmethod
    def delete_contact():
        contact_id = input("Введите ID контакта для удаления: ")
        data = load_json(CONTACTS_FILE)
        new_data = [x for x in data if str(x["id"]) != contact_id]
        if len(new_data) != len(data):
            save_json(CONTACTS_FILE, new_data)
            print("Контакт удалён!")
        else:
            print("Контакт не найден.")