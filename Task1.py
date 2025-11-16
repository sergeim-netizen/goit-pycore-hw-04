# task1.py

def total_salary(path):
    """
    Обчислює загальну та середню заробітну плату з файлу.

    Args:
        path (str): Шлях до файлу з даними про зарплати.

    Returns:
        tuple: Кортеж із двох значень (загальна сума, середня зарплата).
               Повертає (0, 0), якщо файл не знайдено, він порожній, 
               або дані некоректні.
    """
    total_sum = 0
    count = 0
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                # Видаляємо зайві пробіли та переходи рядків
                line = line.strip()
                if not line:
                    continue  # Пропускаємо порожні рядки

                try:
                    # Розділяємо рядок на ім'я та зарплату
                    name, salary_str = line.split(',')
                    salary = float(salary_str)  # Перетворюємо зарплату на число
                    
                    total_sum += salary
                    count += 1
                
                except ValueError:
                    # Цей except спрацює, якщо:
                    # 1. line.split(',') повернув не 2 елементи
                    # 2. float(salary_str) не зміг перетворити рядок на число
                    print(f"Помилка: Некоректний формат даних у рядку: '{line}'")
                except IndexError:
                    # На випадок, якщо split(',') повернув менше 2 елементів
                    print(f"Помилка: Неповні дані у рядку: '{line}'")

        if count == 0:
            # Якщо файл був порожній або не містив коректних даних
            return 0, 0
            
        average_salary = total_sum / count
        
        # Повертаємо загальну суму та середню (можна округлити за бажанням)
        return total_sum, average_salary

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Сталася непередбачена помилка: {e}")
        return 0, 0

# --- Приклад використання ---
# Спершу створіть файл "salary_file.txt" з таким вмістом:
# Alex Korp,3000
# Nikita Borisenko,2000
# Sitarama Raju,1000
# Invalid Line (для перевірки помилок)
# John Doe,5000.50

# total, average = total_salary("salary_file.txt")
# print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

# --- Тест з прикладу в завданні ---
# Якщо у файлі лише:
# Alex Korp,3000
# Nikita Borisenko,2000
# Sitarama Raju,1000
#
# total, average = total_salary("salary_file.txt")
# print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
# Очікуваний результат: Загальна сума заробітної плати: 6000.0, Середня заробітна плата: 2000.0