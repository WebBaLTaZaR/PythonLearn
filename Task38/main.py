
from os import path

file_base = "base.txt" # Файл БД
last_id = 0
all_data = []

if not path.exists(file_base): # если указанного выше пути нет, создать пустую папку
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global last_id, all_data  # Изменяем глобальные переменные

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f] # strip Возвращает копию строки с удаленными начальными и конечными пробелами
        if all_data: # Если база не пустая
            last_id = int(all_data[-1].split()[0]) # берём последний элемент БД, разъединяем по пробелам и помещаем в переменную ID эл.
            return all_data # возвращаем БД
    return []


def show_all():
    if all_data:
        print(*all_data, sep="\n") # Вывести на экран с переносом строки
    else:
        print("Empty data")


def add_new_contact(): # Добавить новый контакт
    global last_id
    array = ["surname", "name", "patronymic", "phone_number"] # Фамилия, имя, отчество, номер телефона
    string = ""
    for i in array:
        string += input(f"Enter {i}: ") + " "
    last_id += 1

    with open(file_base, "a", encoding="utf-8") as f:
        f.write(f"{last_id} {string}\n") # добавить к каждом контакту индивидуальный идентификатор


def search_record(): # Поиск по записям
    search_text = input("Enter text to search: ").lower() # просим ввести то, что надо найти и переводим в ниж рег

    results = []
    for entry in all_data: # пробегаемся по БД
        if search_text in entry.lower(): # проверяем совпадения инпута и слов в БД
            results.append(entry) # результат записываем в переменную

    if results: 
        print("Matching records found:")
        print(*results, sep="\n") # выводим искомый ответ
    else:
        print("No matching records found.")


def change_record():
    record_id = int(input("Enter the ID of the record to change: ")) # спрашиваем, какую запись собираемся изменить
    new_data = input("Enter new data for the record: ") # что хотим записать на старом месте

    for i, entry in enumerate(all_data): # пробегаемся по БД используя индек и содержимое
        if entry.startswith(str(record_id)): # проверяем, есть ли в списке введенный идентификатор 
            all_data[i] = f"{record_id} {new_data}" # соединяем ID и нову информацию 
            break

    with open(file_base, "w", encoding="utf-8") as f:
        f.write("\n".join(all_data)) # обновляем БД


def delete_record():
    record_id = int(input("Enter the ID of the record to delete: ")) # спрашиваем, какую запись мы хотим удалить

    for i, entry in enumerate(all_data):
        if entry.startswith(str(record_id)):
            del all_data[i] # удаляем найденный ID
            break

    with open(file_base, "w", encoding="utf-8") as f:
        f.write("\n".join(all_data)) # обновляем БД


def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change a record\n"
                       "5. Delete a record\n"
                       "6. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                search_record()
            case "4":
                change_record()
            case "5":
                delete_record()
            case "6":
                play = False
            case _:
                print("Try again!\n")


main_menu()
