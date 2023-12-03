"""
Задание 1: Работа с директориями

Импортируйте модуль os.
Создайте новую директорию с именем "my_directory" в текущей рабочей директории.
Проверьте существование созданной директории.
Выведите на экран список файлов и директорий в текущей рабочей директории.

Задание 2: Работа с файлами

Создайте новый текстовый файл с именем "my_file.txt" в текущей рабочей директории.
Проверьте существование созданного файла.
Запишите в файл строку "Привет, мир!".
Прочитайте содержимое файла и выведите его на экран.

Задание 3: Переименование и удаление файлов

Переименуйте файл "my_file.txt" в "renamed_file.txt".
Проверьте существование файла "my_file.txt" (он должен отсутствовать).
Удалите файл "renamed_file.txt".
Проверьте его отсутствие.

Задание 4: Работа с путями

Используя функции модуля os.path, создайте абсолютный путь к файлу
"renamed_file.txt" в текущей рабочей директории.
Разделите абсолютный путь на директорию и имя файла, а затем выведите их на экран.
"""

import os
#1
os.mkdir("my_dir")
if os.path.exists("my_dir"):
    print("'my_dir' сущ")
else:
    print("'my_dir' не сущ")
current_files = os.listdir()
print(current_files)
print("-----------------------------")
#2
with open("my_file.txt", "w") as file:
    file.write("Привет, мир!")
if os.path.exists("my_file.txt"):
    print("Файл 'my_file.txt' существует.")
else:
    print("Файл 'my_file.txt' не существует.")
with open("my_file.txt", "r") as file:
    file_content = file.read()
    print("Содержимое файла 'my_file.txt':", file_content)

print("-----------------------------")
#3
os.rename("my_file.txt", "renamed_file.txt")
if not os.path.exists("my_file.txt"):
    print("Файл 'my_file.txt' отсутствует.")
os.remove("renamed_file.txt")
#проверка
if not os.path.exists("renamed_file.txt"):
    print("Файл 'renamed_file.txt' успешно удален.")

#4
absolute_path = os.path.abspath("renamed_file.txt")
directory, filename = os.path.split(absolute_path)
print("Абсолютный путь:", absolute_path)
print("Директория:", directory)
print("Имя файла:", filename)