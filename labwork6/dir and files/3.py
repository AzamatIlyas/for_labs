import os

def check_path(path):
    if os.path.exists(path):
        print(f"Путь '{path}' существует.")
        directory_name, file_name = os.path.split(path)
        print(f"Часть имени каталога: {directory_name}")
        print(f"Часть имени файла: {file_name}")
    else:
        print(f"Путь '{path}' не существует.")

path = input("Введите путь: ")
check_path(path)