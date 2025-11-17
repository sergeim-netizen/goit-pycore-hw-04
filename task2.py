# task2.py

def get_cats_info(path):
    """
    Читає файл з даними про котів та повертає список словників.

    Args:
        path (str): Шлях до файлу з даними про котів.

    Returns:
        list: Список словників, де кожен словник - це інфо про одного кота.
              Повертає порожній список у разі помилки.
    """
    cats_info = []
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue  # Пропускаємо порожні рядки

                try:
                    # Розділяємо рядок на три частини
                    cat_id, name, age = line.split(',')
                    
                    # Створюємо словник та додаємо до списку
                    cats_info.append({
                        "id": cat_id,
                        "name": name,
                        "age": age  # Залишаємо вік як рядок, згідно з очікуваним результатом
                    })

                except ValueError:
                    # Спрацює, якщо split(',') повернув не 3 елементи
                    print(f"Помилка: Некоректний формат даних у рядку: '{line}'")
                except IndexError:
                    print(f"Помилка: Неповні дані у рядку: '{line}'")

        return cats_info

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return []  # Повертаємо порожній список, як логічний результат "котів не знайдено"
    except Exception as e:
        print(f"Сталася непередбачена помилка: {e}")
        return []

# --- Приклад використання ---
# Створіть файл "cats_file.txt" з таким вмістом:
# 60b90c1c13067a15887e1ae1,Tayson,3
# 60b90c2413067a15887e1ae2,Vika,1
# 60b90c2e13067a15887e1ae3,Barsik,2
# 60b90c3b13067a15887e1ae4,Simon,12
# 60b90c4613067a15887e1ae5,Tessi,5

# cats_info = get_cats_info("cats_file.txt")
# print(cats_info)
