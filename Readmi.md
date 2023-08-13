Команды для работы с заметками:

1. Для того чтобы добавить заметку:

```python
python notes.py add --title "новая заметка_" --msg "тело новой заметки_"
```

2. Чтобы посмотреть список заметок (без фильтрации по дате):

```python
python notes.py list
```

3. Чтобы посмотреть список заметок с фильтрацией по дате (например, за 2023-08-13):

```python
python notes.py list --date "2023-08-13"
```

4. Чтобы редактировать заметку с определенным ID:

```python
python notes.py edit --id 1 --title "отредактированная заметка" --msg "измененное тело"
```

5. Чтобы удалить заметку с определенным ID:

```python
python notes.py delete --id 1
```

Примечание:

Для того чтобы не создавались заметки с одинаковым ID - в коде на этот случай есть проверка:

```python
    if notes:
        note_id = max(note["id"] for note in notes) + 1
    else:
        note_id = 1
```

Я удалил заметки под 5 и 13 ID и при этом нумерация ID не сбилась.
Таким образом можно даже проследить с каким ID заметки были удалены (те ID которые отсутствуют в списке – те и были удалены).