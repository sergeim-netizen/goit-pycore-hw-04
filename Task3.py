# task3.py

import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізуємо colorama, щоб кольори автоматично скидались після кожного print
init(autoreset=True)

def display_directory_structure(directory_path, indent=''):
    """
    Рекурсивно обходить директорію та виводить її структуру з кольорами.

    Args:
        directory_path (Path): Об'єкт Path до директорії.
        indent (str): Відступ для візуалізації вкладеності.
    """
    try:
        # Отримуємо список елементів, сортуємо (спочатку директорії, потім файли)
        items = sorted(list(directory_path.iterdir()), key=lambda p: (not p.is_dir(), p.name))
        
        for item in items:
            if item.is_dir():
                # Виводимо директорію синім кольором
                print(f"{indent}📂 {Fore.BLUE}{item.name}{Style.RESET_ALL}")
                # Рекурсивний виклик для піддиректорії
                display_directory_structure(item, indent + "    ")
            elif item.is_file():
                # Виводимо файл зеленим кольором
                print(f"{indent}📜 {Fore.GREEN}{item.name}{Style.RESET_ALL}")

    except PermissionError:
        print(f"{indent}🚫 {Fore.RED}Немає доступу{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{indent}❓ {Fore.RED}Директорію не знайдено{Style.RESET_ALL}")

def main():
    # Перевіряємо, чи передано аргумент
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Помилка: Потрібно вказати шлях до директорії.")
        print(f"Використання: python {sys.argv[0]} /шлях/до/вашої/директорії")
        sys.exit(1)

    # Отримуємо шлях до директорії з аргументів
    dir_path_str = sys.argv[1]
    dir_path = Path(dir_path_str)

    # Перевіряємо, чи шлях існує
    if not dir_path.exists():
        print(f"{Fore.RED}Помилка: Шлях '{dir_path_str}' не існує.{Style.RESET_ALL}")
        sys.exit(1)
    
    # Перевіряємо, чи є це директорія
    if not dir_path.is_dir():
        print(f"{Fore.RED}Помилка: Шлях '{dir_path_str}' не є директорією.{Style.RESET_ALL}")
        sys.exit(1)

    # Виводимо корінь директорії (з повним шляхом для ясності)
    print(f"\n{Fore.YELLOW}📦 Структура для: {dir_path.resolve()}{Style.RESET_ALL}\n")
    # Починаємо рекурсивний обхід
    display_directory_structure(dir_path)

if __name__ == "__main__":
    main()
