class Calculator:
    @staticmethod
    def menu():
        while True:
            print("\nКалькулятор:")
            expr = input("Введите выражение (или 'назад' для выхода): ")
            if expr.lower() == "назад":
                break
            # Простейшая проверка символов
            allowed_chars = "0123456789+-*/.() "
            if any(ch not in allowed_chars for ch in expr):
                print("Ошибка: недопустимые символы!")
                continue
            try:
                result = eval(expr)
                print("Результат:", result)
            except ZeroDivisionError:
                print("Ошибка: деление на ноль!")
            except Exception:
                print("Ошибка в выражении!")