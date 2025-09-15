# 📘 Chapter 26 – Indexing, Aggregations, and Queries in MongoDB

In this chapter, we explore **advanced database operations** in MongoDB:
- **Indexes** → Make queries faster  
- **Queries** → Filter data with conditions  
- **Aggregations** → Process and transform data

---

## 🔹 Indexing
An **index** is like an index in a book:  
Instead of reading every page, MongoDB looks up the index to quickly find documents.

```python
coll.create_index("name")
````

Now queries using `name` will be much faster.

---

## 🔹 Queries

Queries allow filtering results.

```python
# Find students with age > 20
coll.find({"age": {"$gt": 20}})

# Find students in Kolkata
coll.find({"city": "Kolkata"})
```

---

## 🔹 Aggregations

Aggregation pipelines allow **grouping, filtering, and calculating** over data.

```python
pipeline = [
    {"$group": {"_id": "$city", "total": {"$sum": 1}}},
    {"$sort": {"total": -1}}
]
coll.aggregate(pipeline)
```

---

## 🔹 Visual Diagram

```
[Collection] ---> [Match/Filter] ---> [Group] ---> [Sort] ---> [Result]
```

Example:

```
Students ---> age > 20 ---> group by city ---> sort desc ---> Report
```

---

## 🧠 Summary

* Indexes = Faster queries
* Queries = Fetch filtered data
* Aggregations = Data analysis inside MongoDB

