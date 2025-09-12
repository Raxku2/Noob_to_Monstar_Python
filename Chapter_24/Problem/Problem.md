# 📝 Practice Problem – MongoDB with PyMongo

## Problem
Create a Python program that connects to **MongoDB Atlas** using PyMongo and performs the following tasks:

1. Connect to the `schoolDB` database.
2. Create a collection named `teachers`.
3. Insert a teacher document with:
   ```json
   { "name": "Arjun", "subject": "Mathematics", "experience": 5 }
   ````

4. Fetch and print all teachers from the collection.

---

## Expected Output (Example)

```bash
✅ Connected to MongoDB Atlas!
Inserted Teacher: Arjun
All Teachers:
{'_id': ObjectId('...'), 'name': 'Arjun', 'subject': 'Mathematics', 'experience': 5}
```
