import pandas as pd

# Series
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print("Series:\n", s)

# DataFrame
data = {"Name":["Amit","Rahul","Priya"], "Age":[21,22,20]}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# Info about DataFrame
print("\nShape:", df.shape)
print("Head:\n", df.head())
print("Describe:\n", df.describe(include="all"))

# Selecting
print("\nSelect column:\n", df["Name"])
print("Row using loc:\n", df.loc[0])
print("Row using iloc:\n", df.iloc[1])

# Filtering
print("\nAge > 21:\n", df[df["Age"] > 21])

# Add new column
df["Marks"] = [85, 90, 88]
print("\nAfter adding column:\n", df)

# Drop column
df = df.drop("Age", axis=1)
print("\nAfter dropping Age:\n", df)
