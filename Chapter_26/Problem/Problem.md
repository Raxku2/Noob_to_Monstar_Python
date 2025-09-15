# 📝 Practice Problem – Indexing, Aggregations, and Queries

## Problem
1. Create a database `salesDB` and a collection `orders`.
2. Insert at least 5 orders with:
   ```json
   {"customer": "Alice", "amount": 500, "city": "Kolkata"}
   {"customer": "Bob", "amount": 1200, "city": "Delhi"}
   {"customer": "Charlie", "amount": 700, "city": "Kolkata"}
   {"customer": "David", "amount": 900, "city": "Mumbai"}
   {"customer": "Eva", "amount": 1500, "city": "Delhi"}
   ````

3. Create an index on the `city` field.
4. Query all orders with `amount > 800`.
5. Use aggregation to find **total sales per city**.

---

## Expected Output

```bash
✅ Inserted 5 orders
✅ Index created on city
📖 Orders with amount > 800:
{'customer': 'Bob', 'amount': 1200, 'city': 'Delhi'}
{'customer': 'David', 'amount': 900, 'city': 'Mumbai'}
{'customer': 'Eva', 'amount': 1500, 'city': 'Delhi'}

📊 Total Sales Per City:
{'_id': 'Delhi', 'total_sales': 2700}
{'_id': 'Mumbai', 'total_sales': 900}
{'_id': 'Kolkata', 'total_sales': 1200}
  ```
