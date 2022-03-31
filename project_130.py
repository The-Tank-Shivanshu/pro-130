import pandas as pd
import csv

df=pd.read_csv("total_stars.csv")
print(df.shape)

df = df.rename({
                '': "Sr_name", 
                
            }, axis='columns')

del df["Star_name.1"]
del df["Distance.1"]
del df["Mass.1"]
del df["Radius.1"]
del df["Unnamed: 6"]
del df["Unnamed: 0"]




df.to_csv('main.csv') 
print(df.shape)