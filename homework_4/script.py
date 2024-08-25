import csv
import json

from homework_4 import CSV_BOOKS_FILE_PATH, JSON_USERS_FILE_PATH, JSON_RESULT_FILE_PATH

with open(CSV_BOOKS_FILE_PATH, 'r') as f:
    reader = csv.DictReader(f)
    books = list(reader)

with open(JSON_USERS_FILE_PATH, 'r') as f:
    users = json.load(f)

books_per_user = len(books) // len(users)
remaining_books = len(books) % len(users)

book_index = 0
result = []
for user in users:
    new_user = {
        'name': user['name'],
        'gender': user['gender'],
        'address': user['address'],
        'age': user['age'],
        'books': []
    }
    for _ in range(books_per_user):
        new_user['books'].append(books[book_index])
        book_index += 1
    if remaining_books > 0:
        new_user['books'].append(books[book_index])
        book_index += 1
        remaining_books -= 1
    result.append(new_user)

with open(JSON_RESULT_FILE_PATH, 'w') as f:
    json.dump(result, f, indent=4)
