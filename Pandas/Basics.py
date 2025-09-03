
import pandas as pd
df=pd.DataFrame({ "name":["a","b","c","d","e"],"ages":[10,20,30,40,50]})
print(df.head(2)) # first to two
print(df.tail(2)) # last to first

print(df.shape[0]) # number of rows
print(df.shape[1]) # number of columns

print(df.dtypes) # printing a data types example Strings : objects
print(df["ages"].astype(float)) # converting an DataFrame into Series

print(df.columns.tolist())
print(df.columns.tolist()) # It works well in case of columns names but not for row names

print(df.index.tolist()) # It works for index (index prints from 0 to 4)

print(df[df["ages"]>18]) # printing the ages greater than 18

print(df.sort_values(by="ages",ascending=False)) # sorting in descending order

