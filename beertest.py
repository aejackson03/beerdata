#import pandas package as alias pd
import pandas as pd
#use pandas '.read_csv()' module to read file as df
df=pd.read_csv('https://query.data.world/s/zhsp6ytp4wfqkqq3vdp2eo5fq255sk')

#print first 5 rows in the data frame df
print(df.head())

#shows the table dimensions
print(df.shape)

#shows data type and # the amount of missing values for each column
print(df.info())

#create new data frame (df_drop) remove all rows with missing data
df_drop=df.dropna()
#print info of the new dataframe
print(df_drop.info())

