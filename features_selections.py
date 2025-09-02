""" only Selecting the Essential Features
 For Example: IN House Dataset Selecting the Cost,Bedrooms not Colours"""

import pandas as pd

from Python1 import result

df=pd.DataFrame({ "area":[100,200,300,400],"bedrooms":[10,20,30,40],"price":[100,200,300,500],"colours":["red","green","blue","yellow"]})
print(df)
result=df[["area","bedrooms","price"]]
print(result)