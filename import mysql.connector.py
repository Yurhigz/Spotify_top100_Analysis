import mysql.connector 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

mydb = mysql.connector.connect(
    host= 'localhost',
    user='root',
    password='Benben123,',
    database='spotify_top_100'
)

mycursor = mydb.cursor()


# Which artists had the most Top 100 songs? 

request_1 =  "SELECT  artists,  count(*) AS nb_top100_songs FROM top2018 GROUP BY 1 ORDER BY 2 DESC LIMIT 1;"

mycursor.execute(request_1)

myresult = mycursor.fetchall()

print(myresult)

# Are there more artists in the Top 100 with 'Lil' in their name, or with 'DJ' in their name? 

request_2 = " SELECT \
COUNT(CASE WHEN artists LIKE '{}' THEN artists ELSE NULL END) AS lil_in_name, \
COUNT(CASE WHEN artists LIKE '{}' THEN artists ELSE NULL END) AS DJ_in_name \
FROM \
top2018;"
args = [('%'+'Lil'+'%'),'%DJ%']

print(args)
print(request_2.format(*args))

mycursor.execute(request_2.format(*args))

myresult2 = mycursor.fetchall()

print(myresult2)

# Which song attributes are most strongly correlated? What attributes seem to have very little correlation?

request_3 = 'SELECT * FROM top2018;'

mycursor.execute(request_3)

myresult3 = mycursor.fetchall()

header=[]

for element in mycursor.description:
    header.append(element[0])


df = pd.DataFrame(myresult3,columns=header)

df_attributes = df.loc[:,'danceability':]

df_attributes_corr = df_attributes.corr(method='pearson')

mask = np.triu(df_attributes_corr,0)


plt.figure(figsize=(15,8))
sns.heatmap(df_attributes_corr,mask=mask,linewidths=1,cmap='RdYlGn',annot=True)
plt.show()

## the most correlated attributes according to pearson correlation are loudness and energy , then we'll find the valence/danceability and valence/loudness couples followed closely by valence/energy
## the least correlated attributes are acousticness/energy, loudness/acousticness and speechiness/loudness



# Which attributes have the most variability? Which tend to be the most similar among the Top 100 songs? 
# to study the variability of an attributes I will compare their range, their mean, standard deviation and their variance, I will use the same df to obtain these informations
# df_attributes.duration_ms = (df_attributes.duration_ms / 1000)/60
print(df_attributes.describe())
plt.figure(figsize=(15,8))
sns.heatmap(df_attributes.describe(),linewidths=1,cmap='RdYlGn',annot=True)
plt.show()


#print(df_attributes.describe())

# https://study.com/academy/lesson/variability-in-statistics-definition-measures-quiz.html