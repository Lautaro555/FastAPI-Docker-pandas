from fastapi import FastAPI, Path, UploadFile, File
import pandas as pd

app=FastAPI()

type={"cast_hulu": "object","cast_amazon": "object", "hulu": "int64", "amazon": "int64", "netflix": "int64", "disney": "int64",
      "listed_in_amazon":str,"listed_in_netflix":str,"listed_in_disney":str,"listed_in_hulu":str}
df=pd.read_csv("https://github.com/Lautaro555/FastAPI-Docker-pandas/raw/main/ETL/df.csv",sep=",",dtype=type).drop('Unnamed: 0', axis=1)


@app.get("/get-max-duration/{año:int}")
async def get_max_duration(año:int, plataforma:str, duration_type:str):
   if duration_type not in ["min","season"]:
        raise ValueError("duration_type should be 'min' or 'season'")
   elif plataforma not in ["netflix","amazon","disney","hulu"]:
        raise ValueError("plataforma should be a platform name")
   else:
    if plataforma=="amazon":
        if duration_type=="min":
            max_duration_id=df[(df["release_year_amazon"]==2021) & (df["type_amazon"]=="Movie")].duration_amazon.idxmax()
            return df.loc[max_duration_id, 'title']
        if duration_type=="season":
            max_duration_id=df[(df["release_year_amazon"]==año) & (df["type_amazon"]=="TV Show")].duration_amazon.idxmax()
            return df.loc[max_duration_id, 'title']
    if plataforma=="netflix":
        if duration_type=="min":
            max_duration_id=df[(df["release_year_netflix"]==año) & (df["type_netflix"]=="Movie")].duration_netflix.idxmax()
            return df.loc[max_duration_id, 'title']
        if duration_type=="season":
            max_duration_id=df[(df["release_year_netflix"]==año) & (df["type_netflix"]=="TV Show")].duration_netflix.idxmax()
            return df.loc[max_duration_id, 'title']
    if plataforma=="hulu":
        if duration_type=="min":
            max_duration_id=df[(df["release_year_hulu"]==año) & (df["type_hulu"]=="Movie")].duration_hulu.idxmax()
            return df.loc[max_duration_id, 'title']
        if duration_type=="season":
            max_duration_id=df[(df["release_year_hulu"]==año) & (df["type_hulu"]=="TV Show")].duration_hulu.idxmax()
            return df.loc[max_duration_id, 'title']
    if plataforma=="disney":
        if duration_type=="min":
            max_duration_id=df[(df["release_year_disney"]==año) & (df["type_disney"]=="Movie")].duration_disney.idxmax()
            return df.loc[max_duration_id, 'title']
        if duration_type=="season":
            max_duration_id=df[(df["release_year_disney"]==año) & (df["type_disney"]=="TV Show")].duration_disney.idxmax()
            return df.loc[max_duration_id, 'title']