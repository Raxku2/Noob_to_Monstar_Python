# 📘 Chapter 25 – CRUD Operations with PyMongo

Now that we can connect to MongoDB, let’s perform the **CRUD operations**:  
- **C → Create** (insert documents)  
- **R → Read** (find documents)  
- **U → Update** (modify documents)  
- **D → Delete** (remove documents)  

---

## 🔹 Create (Insert Data)
```python
coll.insert_one({
    "name": "Rakesh",
    "roll": 6737843267,
    "phone": 6296386131
})
````

---

## 🔹 Read (Fetch Data)

```python
# Fetch all
for data in coll.find():
    print(data)

# Fetch one
student = coll.find_one({"name": "Rakesh"})
print(student)
```

---

## 🔹 Update (Modify Data)

```python
coll.update_one({"name": "Rakesh"}, {"$set": {"name": "Rakesh Kundu"}})
```

---

## 🔹 Delete (Remove Data)

```python
coll.delete_one({"name": "Rakesh Kundu"})
```

---

## 🔑 Summary

* `insert_one()` → Add new data
* `find()` / `find_one()` → Read data
* `update_one()` → Modify existing data
* `delete_one()` → Remove data

