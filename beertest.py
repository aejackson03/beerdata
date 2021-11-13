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

#putting the column name in quotation marks and square brackets directly after the data frame calls out that column only, and using pd.to_datetime() on our 'review time' column (with units as #seconds) we can convert the whole column to datetime
df_drop['review_time']=pd.to_datetime(df_drop['review_time'],unit='s')

#printing out the new and updated data types and the column head
print(df_drop.dtypes)
print(df_drop['review_time'].head())

#using the .unique() module we can see the unique variables in the #column 'beer_style'
print(df_drop['beer_style'].unique())

#.value_counts() to return how many different variables are in style column
print(df_drop['beer_style'].value_counts())

#seperate subset from original data frame
ale = df_drop[df_drop['beer_style'].str.contains('Ale')]
IPA = df_drop[df_drop['beer_style'].str.contains('IPA')]

#prin the info on both new data frames
print(ale.info())
print(IPA.info())

#create new data frame titled fav_beer and using pd.concat() to #concatenate them
fav_beer = pd.concat([ale, IPA])

#printing the info to see new data frame
print(fav_beer.info())

#using .duplicated() returns a Boolean Series (True or False) for #our rows, and .value_counts() shows us how many are duplicated
print(fav_beer.duplicated().value_counts())

#create a new data frame and use .drop_duplicates() to remove 
fav_beer_clean = fav_beer.drop_duplicates()

#print out the info on the new data frame
print(fav_beer_clean.info())

#assigning the same variable just overwrites the values, here we are #only selecting the rows that have values equal to or higher than #4.5 in the 'review_overall' columns
fav_beer_clean = fav_beer_clean[fav_beer_clean['review_overall']>=4]

#this is similar to above, except this time we are using the #'beer_abv' column and adding a second conditional statement using #the '&' symbol
fav_beer_clean = fav_beer_clean[(fav_beer_clean['beer_abv']>=5.0)&(fav_beer_clean['beer_abv']<=6.0)]

#printing the value counts of different beers in the beer_name col
print(fav_beer_clean['beer_name'].value_counts())

#putting the number 15 inside the '.head()' module sets the amount #of returned rows to 15, as the value_count is in ascending order it #returns the top 15 most rated beers
print(fav_beer_clean['beer_name'].value_counts().head(20))
