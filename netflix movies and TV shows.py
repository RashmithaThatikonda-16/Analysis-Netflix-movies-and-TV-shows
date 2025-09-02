#load the dataset in python
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv(r"C:/Users/DELL/Downloads/archive/netflix_titles.csv")
print(df)
df.head()
#explore the dataset
print(df.info())
print(df.isnull().sum())
print(df.describe(include='all'))
#cleaning the data
df['director']=df['director'].fillna("unknown")
df['cast']=df['cast'].fillna("unknown")
df=df.dropna(subset=['release_year','rating'])
df.groupby('type')['show_id'].count()
df['date_added']=pd.to_datetime(df['date_added'],errors='coerce')
df['year_added']=df['date_added'].dt.year
print(df['year_added'].isnull().sum())                                
df['year_added'].value_counts().sort_index().plot(kind='bar',figsize=(10,5))
plt.xlabel("year")
plt.ylabel("number of titles added")
plt.title("number of titles added to netflix over time")
plt.show()
#most common movie genres
from collections import Counter
all_genres=','.join(df['listed_in']).split(',')
genre_counts=Counter(all_genres)
genre_df=pd.DataFrame(genre_counts.items(),columns=['Genre','Count'])
genre_df=genre_df.sort_values(by='Count',ascending=False)
plt.figure(figsize=(12,6))
genre_df.iloc[:10].plot(kind='bar',x='Genre',y='Count',color='red',legend=False)
plt.xticks(rotation=45)
plt.ylabel("Count")
plt.title("Top 10 most common netflix genres")
plt.show()
top_directors=df[df['director'] !="unknown"]['director'].value_counts().head(10)
top_directors.plot(kind='bar',figsize=(10,5),color='green')
plt.xlabel("director")
plt.ylabel("number of titles")
plt.title("top 10 most popular directors on netflix")
plt.xticks(rotation=45)
plt.show()
df['rating'].value_counts().plot(kind='bar',figsize=(8,5),color='purple')
plt.xlabel("rating")
plt.ylabel("count")
plt.title("distribution of netflix content rating")
plt.xticks(rotation=45)
plt.show()
df.to_csv("cleaned_netflix_data.csv",index=False)











