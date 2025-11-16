# task4.py

def parse_input(user_input):
    """
    Розбирає введений рядок на команду та аргументи.
    """
    # Розділяє рядок за пробілами, strip() видаляє зайві пробіли на початку/в кінці
    # lower() переводить команду в нижній регістр
    parts = user_input.strip().split()
    cmd = parts[0].lower() if parts else ""
    args = parts[1:]
    return cmd, args

def add_contact(args, contacts):
    """
    Додає новий контакт до словника.
    """
    if len(args) != 2:
        return "Невірний формат. Використовуйте: add [ім'я] [телефон]"
    
    name, phone = args
    # Перевіряємо, чи контакт вже існує, хоча за ТЗ ми просто перезаписуємо
    if name in contacts:
        return f"Контакт {name} вже існує. Використовуйте 'change' для оновлення."
        
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    """
    Змінює номер телефону існуючого контакту.
    """
    if len(args) != 2:
        return "Невірний формат. Використовуйте: change [ім'я] [новий телефон]"
    
    name, new_phone = args
    if name not in contacts:
        return f"Контакт '{name}' не знайдено."
        
    contacts[name] = new_phone
    return "Contact updated."

def show_phone(args, contacts):
    """
    Показує номер телефону за заданим ім'ям.
    """
    if len(args) != 1:
        return "Невірний формат. Використовуйте: phone [ім'я]"
    
    name = args[0]
    if name not in contacts:
        return f"Контакт '{name}' не знайдено."
        
    return f"{name}: {contacts[name]}"

def show_all(contacts):
    """
    Показує всі збережені контакти.
    """
    if not contacts:
        return "Список контактів порожній."
        
    # Форматуємо вивід
    output = "All contacts:\n"
    for name, phone in contacts.items():
        output += f"{name}: {phone}\n"
    return output.strip() # .strip() щоб видалити останній \n

def main():
    """
    Головний цикл програми, обробка вводу та виклик функцій.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        
        # Використовуємо наш парсер
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
            
        elif command == "hello":
            print("How can I help you?")
            
        elif command == "add":
            print(add_contact(args, contacts))
            
        elif command == "change":
            print(change_contact(args, contacts))
            
        elif command == "phone":
            print(show_phone(args, contacts))
            
        elif command == "all":
            print(show_all(contacts))
            
        else:
            if command: # Якщо користувач щось ввів, а не просто натиснув Enter
                print("Invalid command.")
            # Якщо command порожній (просто Enter), нічого не робимо

if __name__ == "__main__":
    main()
