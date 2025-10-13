from pymongo import MongoClient

# === MongoDB Connection ===
client = MongoClient("URI")  # change if using Atlas
db = client["inventory_db"]
collection = db["items"]

# === Functions ===
def add_item():
    name = input("Enter item name: ").strip().lower()
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))

    item = {"name": name, "quantity": quantity, "price": price}
    collection.insert_one(item)
    print(f"✅ Item '{name}' added successfully!")

def view_items():
    items = list(collection.find())
    if not items:
        print("⚠️ No items found.")
        return
    print("\n--- Inventory List ---")
    for item in items:
        print(f"ID: {item['_id']} | Name: {item['name']} | Qty: {item['quantity']} | Price: ₹{item['price']}")

def update_item():
    name = input("Enter item name to update: ").strip().lower()
    item = collection.find_one({"name": name})
    if not item:
        print("❌ Item not found.")
        return
    new_qty = int(input("Enter new quantity: "))
    collection.update_one({"name": name}, {"$set": {"quantity": new_qty}})
    print(f"🔁 Quantity of '{name}' updated to {new_qty}.")

def delete_item():
    name = input("Enter item name to delete: ").strip().lower()
    result = collection.delete_one({"name": name})
    if result.deleted_count:
        print(f"🗑️ Item '{name}' deleted successfully.")
    else:
        print("❌ Item not found.")

def search_item():
    name = input("Enter item name to search: ").strip().lower()
    item = collection.find_one({"name": name})
    if item:
        print(f"✅ Found: {item['name']} | Qty: {item['quantity']} | Price: ₹{item['price']}")
    else:
        print("❌ Item not found.")

# === CLI Menu ===
def main():
    while True:
        print("\n==== INVENTORY MANAGEMENT SYSTEM ====")
        print("1. Add Item")
        print("2. View All Items")
        print("3. Update Item Quantity")
        print("4. Delete Item")
        print("5. Search Item")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            view_items()
        elif choice == '3':
            update_item()
        elif choice == '4':
            delete_item()
        elif choice == '5':
            search_item()
        elif choice == '6':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, please try again.")

if __name__ == "__main__":
    main()
