import pandas as pd
#Lista de funciones
type={"cast_hulu": "object","cast_amazon": "object", "hulu": "int64", "amazon": "int64", "netflix": "int64", "disney": "int64",
      "listed_in_amazon":str,"listed_in_netflix":str,"listed_in_disney":str,"listed_in_hulu":str}
df=pd.read_csv("https://github.com/Lautaro555/FastAPI-Docker-pandas/raw/main/Data_cleansing/Clean_dataset/df.csv",sep=",",dtype=type).drop('Unnamed: 0', axis=1)

def get_max_duration2(año:int, plataforma:str, duration_type:str):
   if duration_type not in ["min","season"]:
        raise ValueError("duration_type should be 'min' or 'season'")
   elif plataforma not in ["netflix","amazon","disney","hulu"]:
        raise ValueError("plataforma should be a platform name")
   else:
    if plataforma=="amazon":
        if duration_type=="min":
            max_duration_id=df[(df["release_year_amazon"]==año) & (df["type_amazon"]=="Movie")].duration_amazon.idxmax()
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

def get_count_plataform2(plataforma):
    if plataforma=="amazon":
        movies=df[(df["type_amazon"]=="Movie")]["title"].count()
        series=df[(df["type_amazon"]=="TV Show")]["title"].count()
        dict={"Number of series":int(series),"Number of movies":int(movies)}
    if plataforma=="hulu":
        movies=df[(df["type_hulu"]=="Movie")]["title"].count()
        series=df[(df["type_hulu"]=="TV Show")]["title"].count()
        dict={"Number of series":int(series),"Number of movies":int(movies)}
    if plataforma=="netflix":
        movies=df[(df["type_netflix"]=="Movie")]["title"].count()
        series=df[(df["type_netflix"]=="TV Show")]["title"].count()
        dict={"Number of series":int(series),"Number of movies":int(movies)}
    if plataforma=="disney":
        movies=df[(df["type_disney"]=="Movie")]["title"].count()
        series=df[(df["type_disney"]=="TV Show")]["title"].count()
        dict={"Number of series":int(series),"Number of movies":int(movies)}
    return dict

def get_listedin2(genero:str):
    amazon_count=0
    hulu_count=0
    disney_count=0
    netflix_count=0
    for i in df["listed_in_amazon"]:
        if genero in i.split(","):
            amazon_count+=1
    for i in df["listed_in_netflix"]:
        if genero in i.split(","):
            netflix_count+=1
    for i in df["listed_in_hulu"]:
        if genero in i.split(","):
            hulu_count+=1
    for i in df["listed_in_disney"]:
        if genero in i.split(","):
            disney_count+=1
    dict_count={"Amazon":amazon_count,"netflix":netflix_count,"hulu":hulu_count,"disney":disney_count}
    max_value=max(dict_count.values())
    max_platform=key = [key for key, val in dict_count.items() if val == max_value][0]
    return max_platform , max_value

def get_actor2(plataforma:str, año:int):
    c=0
    dict={}
    lista_actores=[]
    if plataforma=="netflix":
        for i in df[(df["release_year_netflix"]==año)]["cast_netflix"]:
         if i != 0:
          s=i.split(",")
          for a in range(len(s)):
           if s[a] not in lista_actores and s[a] != "0":
            lista_actores.append(s[a])
        for i in lista_actores:
            c=0
            for n in df[(df["release_year_netflix"]==año)]["cast_netflix"]:
                if i in n.split(","):
                    c+=1
            dict[i]=c
    if plataforma=="hulu":
        for i in df[(df["release_year_hulu"]==año)]["cast_hulu"]:
         if i != 0:
          s=i.split(",")
          for a in range(len(s)):
           if s[a] not in lista_actores and s[a] != "0":
            lista_actores.append(s[a])
        for i in lista_actores:
            c=0
            for n in df[(df["release_year_hulu"]==año)]["cast_hulu"]:
                if i in n.split(","):
                    c+=1
            dict[i]=c
    if plataforma=="amazon":
        for i in df[(df["release_year_amazon"]==año)]["cast_amazon"]:
         if i != 0:
          s=i.split(",")
          for a in range(len(s)):
           if s[a] not in lista_actores and s[a] != "0":
            lista_actores.append(s[a])
        for i in lista_actores:
            c=0
            for n in df[(df["release_year_amazon"]==año)]["cast_amazon"]:
                if i in n.split(","):
                    c+=1
            dict[i]=c
    if plataforma=="disney":
        for i in df[(df["release_year_disney"]==año)]["cast_disney"]:
         if i != 0:
          s=i.split(",")
          for a in range(len(s)):
           if s[a] not in lista_actores and s[a] != "0":
            lista_actores.append(s[a])
        for i in lista_actores:
            c=0
            for n in df[(df["release_year_disney"]==año)]["cast_disney"]:
                if i in n.split(","):
                    c+=1
            dict[i]=c
    max_value=max(dict.values())
    max_actor= [key for key, val in dict.items() if val == max_value][0]
    return max_actor , max_value