import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 30, 18, 35],
    "City": ["NY", "LA", "Chicago", "Houston"]
}
df = pd.DataFrame(data)
print("Initial DataFrame:\n", df, "\n")

df.to_csv("sample.csv", index=False)
df = pd.read_csv("sample.csv")
print("After Reading CSV:\n", df, "\n")

print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Data Types:\n", df.dtypes)
print("First 3 Rows:\n", df.head(3))
print("Summary Stats:\n", df.describe(), "\n")

print("Single Column:\n", df["Name"])
print("Multiple Columns:\n", df[["Name", "City"]])
print("First Row:\n", df.iloc[0])
print("Specific Value (Row 2, City):", df.loc[2, "City"], "\n")

print("Age > 25:\n", df[df["Age"] > 25], "\n")
print("Age > 20 and City = NY:\n", df[(df["Age"] > 20) & (df["City"] == "NY")], "\n")

df["Age+5"] = df["Age"] + 5
df["Senior"] = df["Age"] > 30
print("After Adding Columns:\n", df, "\n")

df.loc[1, "Age"] = None
print("With Missing Value:\n", df, "\n")
df["Age"].fillna(df["Age"].mean(), inplace=True)
print("After Filling NaN with Mean:\n", df, "\n")

print("Sorted by Age:\n", df.sort_values("Age"))
print("Sorted by Age Descending:\n", df.sort_values("Age", ascending=False), "\n")

grouped = df.groupby("City")["Age"].mean()
print("Grouped by City (Mean Age):\n", grouped, "\n")

df1 = pd.DataFrame({"ID": [1, 2], "Name": ["Alice", "Bob"]})
df2 = pd.DataFrame({"ID": [1, 2], "Salary": [5000, 6000]})
merged = pd.merge(df1, df2, on="ID")
print("Merged DataFrames:\n", merged, "\n")

df["Age_Squared"] = df["Age"].apply(lambda x: x**2)
print("After Apply (Age Squared):\n", df, "\n")

print("Row Indices:", df.index.tolist())
df.set_index("Name", inplace=True)
print("After Setting Name as Index:\n", df, "\n")

pivot = pd.pivot_table(df, values="Age", index="City", aggfunc="mean")
print("Pivot Table (Avg Age by City):\n", pivot, "\n")

df3 = pd.DataFrame({"Name": ["Eve"], "Age": [28], "City": ["Miami"], "Age+5": [33], "Senior": [False], "Age_Squared": [28**2]})
df3.set_index("Name", inplace=True)
concat = pd.concat([df, df3])
print("After Concatenation:\n", concat, "\n")

concat.to_excel("output.xlsx", index=True)
print("✅ Final Data exported to 'output.xlsx'")
