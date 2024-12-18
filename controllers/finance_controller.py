import os
import csv
from datetime import datetime
from utils.file_utils import load_json, save_json, get_new_id
from utils.csv_utils import import_csv_to_json, export_json_to_csv

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
FINANCE_FILE = os.path.join(DATA_DIR, "finance.json")
DATE_FORMAT = "%d-%m-%Y"

class FinanceController:
    @staticmethod
    def menu():
        while True:
            print("\nУправление финансовыми записями:")
            print("1. Добавить новую запись")
            print("2. Просмотреть все записи")
            print("3. Генерация отчёта")
            print("4. Удалить запись")
            print("5. Экспорт финансовых записей в CSV")
            print("6. Импорт финансовых записей из CSV")
            print("7. Назад")
            choice = input("Выберите действие: ")
            if choice == "1":
                FinanceController.add_record()
            elif choice == "2":
                FinanceController.view_records()
            elif choice == "3":
                FinanceController.generate_report()
            elif choice == "4":
                FinanceController.delete_record()
            elif choice == "5":
                fieldnames = ["id","amount","category","date","description"]
                filename = input("Введите имя CSV-файла для экспорта: ")
                export_json_to_csv(FINANCE_FILE, filename, fieldnames)
            elif choice == "6":
                fieldnames = ["id","amount","category","date","description"]
                filename = input("Введите имя CSV-файла для импорта: ")
                import_csv_to_json(filename, FINANCE_FILE, fieldnames)
            elif choice == "7":
                break
            else:
                print("Неверный выбор, попробуйте снова.")

    @staticmethod
    def add_record():
        data = load_json(FINANCE_FILE)
        amount_str = input("Введите сумму (+ доход, - расход): ")
        try:
            amount = float(amount_str)
        except ValueError:
            print("Некорректная сумма!")
            return
        category = input("Введите категорию: ")
        date_str = input("Введите дату (ДД-ММ-ГГГГ): ")
        description = input("Введите описание: ")
        record_id = get_new_id(data)
        new_record = {
            "id": record_id,
            "amount": amount,
            "category": category,
            "date": date_str,
            "description": description
        }
        data.append(new_record)
        save_json(FINANCE_FILE, data)
        print("Запись успешно добавлена!")

    @staticmethod
    def view_records():
        data = load_json(FINANCE_FILE)
        if not data:
            print("Нет финансовых записей.")
        for r in data:
            print(f"ID: {r['id']}, Сумма: {r['amount']}, Категория: {r['category']}, Дата: {r['date']}, Описание: {r['description']}")

    @staticmethod
    def generate_report():
        start_date_str = input("Введите начальную дату (ДД-ММ-ГГГГ): ")
        end_date_str = input("Введите конечную дату (ДД-ММ-ГГГГ): ")

        data = load_json(FINANCE_FILE)

        def to_date(d_str):
            return datetime.strptime(d_str, DATE_FORMAT)

        try:
            start = to_date(start_date_str)
            end = to_date(end_date_str)
        except ValueError:
            print("Некорректный формат даты!")
            return

        filtered = [r for r in data if start <= to_date(r["date"]) <= end]
        total_income = sum(r["amount"] for r in filtered if r["amount"] > 0)
        total_expense = sum(abs(r["amount"]) for r in filtered if r["amount"] < 0)
        balance = total_income - total_expense

        print(f"Отчёт с {start_date_str} по {end_date_str}:")
        print(f"Доход: {total_income} руб.")
        print(f"Расход: {total_expense} руб.")
        print(f"Баланс: {balance} руб.")

        report_filename = f"report_{start_date_str}_{end_date_str}.csv"
        fieldnames = ["id","amount","category","date","description"]
        with open(report_filename, "w", encoding="utf-8", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for r in filtered:
                writer.writerow(r)
        print(f"Детали сохранены в {report_filename}")

    @staticmethod
    def delete_record():
        record_id = input("Введите ID записи для удаления: ")
        data = load_json(FINANCE_FILE)
        new_data = [x for x in data if str(x["id"]) != record_id]
        if len(new_data) != len(data):
            save_json(FINANCE_FILE, new_data)
            print("Запись удалена!")
        else:
            print("Запись не найдена.")