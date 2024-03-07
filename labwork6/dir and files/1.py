import os

def display_directories_and_files(path):
    print("Список каталогов и файлов в указанном пути:")
    for root, dirs, files in os.walk(path):
        # Выводим список каталогов
        print("Каталоги:")
        for directory in dirs:
            print(os.path.join(root, directory))

        # Выводим список файлов
        print("\nФайлы:")
        for file in files:
            print(os.path.join(root, file))

path = input("Введите путь: ")
display_directories_and_files(path)