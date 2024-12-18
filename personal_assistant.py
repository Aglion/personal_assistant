from controllers.notes_controller import NotesController
from controllers.tasks_controller import TasksController
from controllers.contacts_controller import ContactsController
from controllers.finance_controller import FinanceController
from controllers.calculator import Calculator

def main_menu():
    while True:
        print("\nДобро пожаловать в Персональный помощник!")
        print("Выберите действие:")
        print("1. Управление заметками")
        print("2. Управление задачами")
        print("3. Управление контактами")
        print("4. Управление финансовыми записями")
        print("5. Калькулятор")
        print("6. Выход")
        choice = input("Выбор: ")
        if choice == "1":
            NotesController.menu()
        elif choice == "2":
            TasksController.menu()
        elif choice == "3":
            ContactsController.menu()
        elif choice == "4":
            FinanceController.menu()
        elif choice == "5":
            Calculator.menu()
        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main_menu()