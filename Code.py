import pandas as pd
import numpy as np
import math
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("movies.csv")
df = df[['Film','Genre','PageID']]
list_of_Genre = []
# To get a set of list of genres
for i in df['Genre']:
    i = str(i)
    m  =list(i.split(sep=', '))
    for j in m:
        list_of_Genre.append(j)
list_of_Genre = list(set(list_of_Genre))
print(list_of_Genre)
#To create a page profile matrix
page_profile_matrix =[]
Genre = df['Genre']
for i in range(len(df['Genre'])):
    page_profile_matrix.append(list())
for i in (range(len(df['PageID']))):
    for j in (range(len(Genre))):
        if str(Genre[len(Genre) - j - 1]) in str(df['Genre'][i]):
            page_profile_matrix[i].append(1)
        else:
            page_profile_matrix[i].append(0)
print(page_profile_matrix)
#To get the cosine similarity of the page profile matrix
cosine_sim = cosine_similarity(page_profile_matrix)
print(cosine_sim)

scores_series = pd.Series(cosine_sim[3]).sort_values(ascending=False)
recommended_pages_index=list(scores_series[0:3].index)
print(recommended_pages_index)
recommended_pages=[]
for i in recommended_pages_index:
    recommended_pages.append(df['Film'][i])
print:(recommended_pages)
