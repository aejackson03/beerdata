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

#cleaning up review data/time convert to seconds
df_drop['review_time']=pd.to_datetime(df_drop['review_time'],unit='s')

#print out new and updated data types and the column head
print(df_drop.dtypes)
print(df_drop['review_time'].head())

#show howm any unique variables are in the #column 'beer_style'
print(df_drop['beer_style'].unique())

#return number of variables in style column
print(df_drop['beer_style'].value_counts())

#seperate from original data frame
ale = df_drop[df_drop['beer_style'].str.contains('Ale')]
IPA = df_drop[df_drop['beer_style'].str.contains('IPA')]

#print info on both new data frames
print(ale.info())
print(IPA.info())

#create new data frame titled fav_beer and using pd.concat() to combine
fav_beer = pd.concat([ale, IPA])

#print info to see new data frame
print(fav_beer.info())

#use .duplicated() to show how many are duplicated
print(fav_beer.duplicated().value_counts())

#create clean  data frame and use .drop_duplicates() to remove 
fav_beer_clean = fav_beer.drop_duplicates()

#print out the info on the new data frame
print(fav_beer_clean.info())

#only show rows with 4 or higher review
fav_beer_clean = fav_beer_clean[fav_beer_clean['review_overall']>=4]

fav_beer_clean = fav_beer_clean[(fav_beer_clean['beer_abv']>=5.0)&(fav_beer_clean['beer_abv']<=6.0)]

#print value counts of different beers in the beer_name col
print(fav_beer_clean['beer_name'].value_counts())

#only show the top 15 most rated beers
print(fav_beer_clean['beer_name'].value_counts().head(20))

#import pandas package pd
import pandas as pd

# read CSV file
results = pd.read_csv('https://query.data.world/s/zhsp6ytp4wfqkqq3vdp2eo5fq255sk')
  
# count no. of lines
print("Number of lines present:", 
      len(results))

#for loop
import pandas as pd
for filename in ['https://query.data.world/s/zhsp6ytp4wfqkqq3vdp2eo5fq255sk']:
    data = pd.read_csv(filename, index_col='beer_name')
    print(filename, data.min())

review_overall = 4.0
if review_overall > 3:
    print('greater')
else:
    print('not greater')
print('done')