# Chapter 19: Pandas (Python Data Analysis Library)

## 📌 What is Pandas?
- Pandas is a **data analysis and manipulation library**.
- Provides two main data structures:
  - **Series** → 1D labeled array
  - **DataFrame** → 2D labeled table

---

## 📥 Installation
```bash
pip install pandas
```

🔹 Creating Series
```python
import pandas as pd

s = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
print(s)
```
🔹 Creating DataFrame
```python
import pandas as pd

data = {"Name":["Amit","Rahul","Priya"], "Age":[21,22,20]}
df = pd.DataFrame(data)
print(df)
```


🔹 Useful DataFrame Methods
```python
head(), tail(), shape, info(), describe()
```

Selecting data: df["col"], df.loc[], df.iloc[]

Filtering: df[df["Age"] > 21]

Adding new column: df["Marks"] = [85,90,88]

Drop column: df.drop("Age", axis=1, inplace=True)

Read/Write:
```python
pd.read_csv("file.csv")

df.to_csv("file.csv", index=False)
```
