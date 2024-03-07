import string

def create_files():
    # Получаем список всех букв алфавита от A до Z
    alphabet = string.ascii_uppercase
    
    # Создаем текстовый файл для каждой буквы
    for letter in alphabet:
        file_name = f"{letter}.txt"
        with open(file_name, 'w') as file:
            file.write(f"Это файл {file_name}")

create_files()