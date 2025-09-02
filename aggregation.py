#data transformation: combining all the data into single data without losing the important information so that model gives same result
""" ex:instead of calculating the all the sales per day,calculating the monthly sales """

import pandas as pd
dataset=pd.DataFrame({ "days":["mon"," tues","wed","thurs","fri","sat","sun"],"sales":[10,20,30,40,50,60,70] })
print(dataset)
result=dataset["sales"].sum()
print(" sum of the monthly sales:",result)