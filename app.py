import pandas as pd
import numpy as np
df = pd.read_csv("D:\DS Course\Scripts\proyecto_int_1\proyecto_int_1\games.csv")
df.columns = df.columns.str.lower() #Se pasan los nombres de las columnas a minusculas
df['year_of_release'] = df['year_of_release'].astype('Int64') #Paso year_of_release a int64
df['user_score'] = df['user_score'].replace("tbd", np.nan) #paso los valores tbd a NaN para conservas la columna como un float64
df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')
df[['critic_score', 'rating']] = df[['critic_score', 'rating']].replace("", np.nan)#Hago los valores en blanco a NaN para las columnas critics_score y rating

df['total_sales'] = df[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']].sum(axis=1) #sumo los todas las ventas en una nueva columna


