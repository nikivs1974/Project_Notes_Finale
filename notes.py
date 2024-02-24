import json
import datetime
import os


# Функция для создания новой заметки
def create_note():
    notes = load_notes()
    new_note = {}
    new_note["id"] = len(notes) + 1
    new_note["date"] = datetime.datetime.now().strftime("%Y-%m-%d")
    new_note["title"] = input("Введите заголовок: ")
    new_note["text"] = input("Введите текст: ")
    notes.append(new_note)
    save_notes(notes)
    print("Заметка создана")


# Функция для загрузки списка заметок
def load_notes():
    if os.path.exists("notes.json"):
        with open("notes.json", "r", encoding="utf-8") as file:
            notes = json.load(file)
        return notes
    else:
        return []


# Функция для сохранения списка заметок
def save_notes(notes):
    with open("notes.json", "w", encoding="utf-8") as file:
        json.dump(notes, file, indent=4)


# Функция для вывода списка всех заметок
def list_notes():
    notes = load_notes()
    for note in notes:
        print(f"{note['id']}. {note['date']}. {note['title']}: {note['text']}")


# Функция для вывода заметки по id
def show_note_id(notes, note_id):
    for note in notes:
        if note["id"] == note_id:
            print(f"{note['id']}. {note['date']}. {note['title']}: {note['text']}")
            break
    else:
        print("Заметка с этим id не существует")


# Функция для вывода заметки по дате
def show_note_date(notes, note_date):
    temp = 0
    for note in notes:
        if note["date"] == note_date:
            print(f"{note['id']}. {note['date']}. {note['title']}: {note['text']}")
            temp += 1
    if temp == 0:
        print("Заметок с этой датой не существует, или формат ввода не совпадает с требуемым")


# Функция для редактирования заметки
def edit_note(note_id):
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            note["title"] = input("Введите новый заголовок заметки: ")
            note["text"] = input("Введите новый текст заметки: ")
            note["date"] = datetime.datetime.now().strftime("%Y-%m-%d")
            save_notes(notes)
            print("Заметка отредактирована")
            return
    print("Заметка с таким id не найдена")


# Функция для удаления заметки
def delete_note(note_id):
    notes = load_notes()
    notes = [note for note in notes if note["id"] != note_id]
    save_notes(notes)
    print("Заметка удалена")


# Программа
def program():
    while True:
        print("Выбрать:")
        print("--------")
        print("1 - Создать заметку")
        print("2 - Вывести все заметки")
        print("3 - Вывести заметку по id")
        print("4 - Вывести заметку по дате")
        print("5 - Редактировать")
        print("6 - Удалить")
        print("7 - Выход")
        print("--------")
        choice = input("Enter: ")

        if choice == "1":
            create_note()
        elif choice == "2":
            list_notes()
        elif choice == "3":
            note_id = int(input("Введите id заметки для вывода: "))
            notes = load_notes()
            show_note_id(notes, note_id)
        elif choice == "4":
            note_date = input("Введите дату заметки для вывода в формате год-месяц-день (XXXX-XX-XX): ")
            notes = load_notes()
            show_note_date(notes, note_date)
        elif choice == "5":
            note_id = int(input("Введите id заметки для редактирования: "))
            edit_note(note_id)
        elif choice == "6":
            note_id = int(input("Введите id заметки для удаления: "))
            delete_note(note_id)
        elif choice == "7":
            break
        else:
            print("Такой опции не существует. Сделайте выбор еще раз")


program()
