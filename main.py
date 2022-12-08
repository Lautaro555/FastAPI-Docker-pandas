from fastapi import FastAPI
from functions import *

app=FastAPI()


#Funcion para obtener duracion maxima por año y plataforma
@app.get("/get-max-duration/{year-platform-duration}")
async def get_max_duration(año:int, plataforma:str, duration_type:str):
    return get_max_duration2(año,plataforma,duration_type)

@app.get("/get-count-plataform/{plataforma}")
async def get_count_plataform(plataforma):
    return get_count_plataform2(plataforma)

@app.get("/get-listedin/{genero}")
async def get_listedin(genero:str):
    return get_listedin2(genero)

@app.get("/get_actor/{platform-year}")
async def get_actor(plataforma:str, año:int):
    return get_actor2(plataforma,año)