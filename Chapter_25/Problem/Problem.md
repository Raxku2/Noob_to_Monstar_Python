# 📝 Practice Problem – CRUD Operations with PyMongo

## Problem
Write a Python program using PyMongo that does the following:

1. Create a database called `libraryDB` and a collection `books`.
2. Insert three books:
   - {"title": "Python 101", "author": "Guido", "year": 2020}
   - {"title": "Learning MongoDB", "author": "Dwight", "year": 2021}
   - {"title": "Data Science", "author": "Smith", "year": 2019}
3. Fetch and print all books.
4. Update the year of "Python 101" to 2023.
5. Delete the book "Data Science".

---

## Expected Output (Example)
```bash
✅ Inserted 3 books
📖 All Books:
{'_id': ObjectId('...'), 'title': 'Python 101', 'author': 'Guido', 'year': 2020}
{'_id': ObjectId('...'), 'title': 'Learning MongoDB', 'author': 'Dwight', 'year': 2021}
{'_id': ObjectId('...'), 'title': 'Data Science', 'author': 'Smith', 'year': 2019}

✏️ Updated Python 101 year → 2023
🗑️ Deleted Data Science
