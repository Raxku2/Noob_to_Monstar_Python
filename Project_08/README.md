# 📇 Project_08: Contact Book CLI

A simple **Contact Book CLI** application in Python that stores, retrieves, adds, and deletes contacts using a CSV file as the database.  

---

## ⚙️ Features
- 📌 **Add a new contact** (Name, Phone, City)
- 📖 **View all contacts** in a tabular format
- ❌ **Delete a contact** by serial number
- 💾 **Persistent storage** using `data.csv`
- 🖥️ Runs directly in the terminal (CLI app)

---

## 🛠️ Tech Stack
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/CSV-FCC624?style=for-the-badge&logo=csv&logoColor=black" />
  <img src="https://img.shields.io/badge/CLI-000000?style=for-the-badge&logo=windows-terminal&logoColor=white" />
</p>

---

## 📂 Project Structure
```

.
├── main.py   # Main Python script
├── data.csv          # Contact database (auto-created if missing)
└── README.md         # Project documentation

````

---

## ▶️ How to Run
1. Clone the repo or copy the script:
   ```bash
   git clone https://github.com/yourusername/contact-book-cli.git
   cd contact-book-cli
   ````

2. Run the script:

   ```bash
   python contact_book.py
   ```

3. Interact with the CLI:

   ```
   Sl.  Name                           | Phone                | City
   -----------------------------------------------------------------
   1    John Doe                       | 1234567890           | New York
   2    Jane Smith                     | 9876543210           | London

   Enter 'Q' for Quit, 'a' for add new contacts, 'd' for delete:
   ```

---

## 📝 Example Usage

### ➕ Add a Contact

```
Enter 'a' for add new contacts
Enter Contact er nam: Alice
Number ??: 5551234567
Bari kothay ??: Dhaka
```

### ❌ Delete a Contact

```
Enter 'd' for delete
Delete Sl no: 2
Jane Smith                     | 9876543210           | London | Deleting...
Done..
```

### ✅ Quit

```
Enter 'Q' for Quit
```

---

## 📦 Data Storage

* All contacts are stored in **data.csv**
* Format:

  ```
  Name,Phone,City
  John Doe,1234567890,New York
  Alice,5551234567,Dhaka
  ```
