import os

def check_path_access(path):
    # Проверка существования пути
    if not os.path.exists(path):
        print(f"Путь '{path}' не существует.")
        return

    # Проверка читаемости пути
    if os.access(path, os.R_OK):
        print(f"Путь '{path}' доступен для чтения.")
    else:
        print(f"Нет доступа к чтению для пути '{path}'.")

    # Проверка записи в путь
    if os.access(path, os.W_OK):
        print(f"Путь '{path}' доступен для записи.")
    else:
        print(f"Нет доступа к записи для пути '{path}'.")

    # Проверка исполнимости пути (для *nix систем)
    if os.name == 'posix':
        if os.access(path, os.X_OK):
            print(f"Путь '{path}' доступен для исполнения.")
        else:
            print(f"Нет доступа к исполнению для пути '{path}'.")

path = input("Введите путь: ")
check_path_access(path)