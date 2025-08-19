import pandas as pd

# Q1
s = pd.Series([1,2,3,4,5]); print(s)

# Q2
s = pd.Series([10,20,30], index=["x","y","z"]); print(s)

# Q3
df = pd.DataFrame({"Name":["Amit","Rahul","Priya"], "Age":[21,22,20]})
print(df)

# Q4
print(df.head(2))

# Q5
print(df.shape)

# Q6
print(df["Name"])

# Q7
print(df.iloc[1])

# Q8
print(df[df["Age"]>20])

# Q9
df["Marks"]=[85,90,88]; print(df)

# Q10
df=df.drop("Age",axis=1); print(df)

# Q11
df.to_csv("students.csv", index=False)

# Q12
df2=pd.read_csv("students.csv"); print(df2)

# Q13
print(df.describe(include="all"))

# Q14
print(df.dtypes)

# Q15
# Series = 1D labeled array, DataFrame = 2D labeled table
