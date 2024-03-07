import os

def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            os.remove(file_path)
            print(f"Файл '{file_path}' успешно удален.")
        else:
            print(f"Недостаточно прав для удаления файла '{file_path}'.")
    else:
        print(f"Файл '{file_path}' не существует.")

file= input()
delete_file(file)