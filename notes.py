import argparse
import datetime
import json
import os

NOTES_FILE = "notes.json"

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            return json.load(f)
    return []

def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=4)

def add_note(title, message):
    notes = load_notes()
    if notes:
        note_id = max(note["id"] for note in notes) + 1
    else:
        note_id = 1
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": note_id,
        "title": title,
        "message": message,
        "timestamp": now
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена")

def list_notes(date_filter=None):
    notes = load_notes()
    if date_filter:
        filtered_notes = [note for note in notes if note["timestamp"].startswith(date_filter)]
    else:
        filtered_notes = notes
    
    if filtered_notes:
        for note in filtered_notes:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Создана: {note['timestamp']}")
            print(f"Тело заметки: {note['message']}")
            print("-" * 30)
    else:
        print("Заметок не найдено")

def edit_note(note_id, title, message):
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            note["title"] = title
            note["message"] = message
            note["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно отредактирована")
            return
    print("Заметка с указанным ID не найдена")

def delete_note(note_id):
    notes = load_notes()
    notes = [note for note in notes if note["id"] != note_id]
    save_notes(notes)
    print("Заметка успешно удалена")

def main():
    parser = argparse.ArgumentParser(description="Консольное приложение заметок")
    parser.add_argument("command", choices=["add", "list", "edit", "delete"], help="Команда: add, list, edit, delete")
    parser.add_argument("--id", type=int, help="ID заметки для редактирования или удаления")
    parser.add_argument("--title", help="Заголовок заметки")
    parser.add_argument("--msg", help="Тело заметки")
    parser.add_argument("--date", help="Дата для фильтрации списка заметок (гггг-мм-дд)")
    args = parser.parse_args()

    if args.command == "add":
        if not args.title or not args.msg:
            print("Для добавления заметки требуется указать заголовок и текст")
            return
        add_note(args.title, args.msg)
    elif args.command == "list":
        list_notes(args.date)
    elif args.command == "edit":
        if not args.id or not args.title or not args.msg:
            print("Для редактирования заметки требуется указать ID, заголовок и текст")
            return
        edit_note(args.id, args.title, args.msg)
    elif args.command == "delete":
        if not args.id:
            print("Для удаления заметки требуется указать ID")
            return
        delete_note(args.id)
    else:
        print("Недопустимая команда")

if __name__ == "__main__":
    main()
