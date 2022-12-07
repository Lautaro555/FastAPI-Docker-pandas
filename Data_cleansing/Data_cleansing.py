#Se importan las librerias
import pandas as pd
import numpy as np

#Se cargan los datasets con pandas
amazon=pd.read_csv("https://github.com/Lautaro555/PI01_DATA05/raw/main/Datasets/amazon_prime_titles.csv", sep=",")
disney=pd.read_csv("https://github.com/Lautaro555/PI01_DATA05/raw/main/Datasets/disney_plus_titles.csv", sep=",")
hulu=pd.read_csv("https://github.com/Lautaro555/PI01_DATA05/raw/main/Datasets/hulu_titles.csv", sep=",")
netflix=pd.read_json("https://github.com/Lautaro555/PI01_DATA05/raw/main/Datasets/netflix_titles.json") 

#Se eliminan posibles duplicados y las columnas "show_id" de cada dataframe,
#luego se agrega una columna con el nombre de la plata forma y se le da el valor 1 
hulu.drop_duplicates(subset=["title"],inplace=True)
hulu.drop_duplicates(inplace=True)
del hulu["show_id"]
hulu["hulu"]=1

netflix.drop_duplicates(subset=["title"],inplace=True)
netflix.drop_duplicates(inplace=True)
del netflix["show_id"]
netflix["netflix"]=1

disney.drop_duplicates(subset=["title"],inplace=True)
disney.drop_duplicates(inplace=True)
del disney["show_id"]
disney["disney"]=1

amazon.drop_duplicates(subset=["title"],inplace=True)
amazon.drop_duplicates(inplace=True)
del amazon["show_id"]
amazon["amazon"]=1

#Se hace un solo dataframe juntando los dataframe de cada plataforma
df = pd.merge(hulu, amazon, on='title',how="outer", suffixes=("_hulu","_amazon"))
df = pd.merge(df, netflix, on='title',how="outer",suffixes=(None,"_netflix"))
df = pd.merge(df, disney, on='title',how="outer",suffixes=(None,"_disney"))
#Se arregla un error con el sufijo en el nombre de la columna 23 a la 32
df.rename(columns=lambda x: x + "_netflix" if x in df.columns.to_list()[23:33] else x, inplace=True)

#Se rellenan los valores nulos con 0 para facilitar el posterior trabajo en las columnas
#y para rellenar los valores de las columnas con el nombre de la plataforma
df.fillna(0,inplace=True)

#Elimino los string para cada valor en las columnas duration
#luego convierto el tipo de dato de duration y release_year a entero.
list_replace=[" min"," Season"," Seasons","s"]
list_value=["","","",""]
df[["duration_amazon","duration_netflix","duration_disney","duration_hulu"]]=df[["duration_amazon","duration_netflix","duration_disney","duration_hulu"]].replace(list_replace,list_value,regex=True)

#Se acomoda el formato de los datos en las columnas cast y las columnas listed_in
df[["cast_amazon","cast_disney","cast_netflix","cast_hulu"]]=df[["cast_amazon","cast_disney","cast_netflix","cast_hulu"]].replace(", ",",",regex=True)
df[["cast_amazon","cast_disney","cast_netflix","cast_hulu"]].head(50)

df[["listed_in_amazon","listed_in_disney","listed_in_netflix","listed_in_hulu"]]=df[["listed_in_amazon","listed_in_disney","listed_in_netflix","listed_in_hulu"]].replace(", ",",",regex=True)
df[["listed_in_amazon","listed_in_disney","listed_in_netflix","listed_in_hulu"]].head(50)

#luego convierto el tipo de dato de duration y release_year a entero.
df[["duration_amazon","duration_netflix","duration_disney","duration_hulu"]]=df[["duration_amazon","duration_netflix","duration_disney","duration_hulu"]].astype(int)
df[["release_year_amazon","release_year_netflix","release_year_disney","release_year_hulu"]]=df[["release_year_amazon","release_year_netflix","release_year_disney","release_year_hulu"]].astype(int)

#convierto el dataset modificado a csv para su posterior carga
df.to_csv(r"df.csv")