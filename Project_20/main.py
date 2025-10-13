from pymongo import MongoClient

# 1. Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Change if using Atlas
db = client["NotesDB"]  # Database name
notes_collection = db["Notes"]  # Collection name

# 2. Functions for CRUD operations

def add_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    note = {"title": title, "content": content}
    result = notes_collection.insert_one(note)
    print(f"Note added with ID: {result.inserted_id}")

def view_notes():
    notes = notes_collection.find()
    print("\nAll Notes:")
    for note in notes:
        print(f"ID: {note['_id']}, Title: {note['title']}, Content: {note['content']}")

def update_note():
    note_id = input("Enter the ID of the note to update: ")
    new_title = input("Enter new title: ")
    new_content = input("Enter new content: ")
    result = notes_collection.update_one(
        {"_id": note_id},  # MongoDB IDs are normally ObjectId
        {"$set": {"title": new_title, "content": new_content}}
    )
    print(f"Modified count: {result.modified_count}")

def delete_note():
    note_id = input("Enter the ID of the note to delete: ")
    result = notes_collection.delete_one({"_id": note_id})
    print(f"Deleted count: {result.deleted_count}")

# 3. Main Menu
def menu():
    while True:
        print("\n--- Notes App ---")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Update Note")
        print("4. Delete Note")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            update_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            print("Exiting Notes App...")
            break
        else:
            print("Invalid choice. Try again.")

# Run the app
if __name__ == "__main__":
    menu()
