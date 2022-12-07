#Lista de funciones

#Funcion para obtener duracion maxima por año y plataforma
def get_max_duration(año:int, plataforma:str, duration_type:str):
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

#Funcion para obtener la cantidad de series y peliculas de la plataforma especificada
def get_count_plataform(plataforma):
 if plataforma not in ["netflix","amazon","disney","hulu"]:
        raise ValueError("plataforma should be a platform name")
 else:
    if plataforma=="amazon":
        movies=df[(df["type_amazon"]=="Movie")]["title"].count()
        series=df[(df["type_amazon"]=="TV Show")]["title"].count()
        dict={"Number of series":series,"Number of movies":movies}
    if plataforma=="hulu":
        movies=df[(df["type_hulu"]=="Movie")]["title"].count()
        series=df[(df["type_hulu"]=="TV Show")]["title"].count()
        dict={"Number of series":series,"Number of movies":movies}
    if plataforma=="netflix":
        movies=df[(df["type_netflix"]=="Movie")]["title"].count()
        series=df[(df["type_netflix"]=="TV Show")]["title"].count()
        dict={"Number of series":series,"Number of movies":movies}
    if plataforma=="disney":
        movies=df[(df["type_disney"]=="Movie")]["title"].count()
        series=df[(df["type_disney"]=="TV Show")]["title"].count()
        dict={"Number of series":series,"Number of movies":movies}
    return dict

#se crea la lista de generos para usar en la siguienta funcion
lista_generos=[]
for i in df["listed_in_disney"]:
     if i != 0:
      s=i.split(",")
      for a in range(len(s)):
          if s[a] not in lista_generos:
           lista_generos.append(s[a])
for i in df["listed_in_netflix"]:
     if i != 0:
      s=i.split(",")
      for a in range(len(s)):
          if s[a] not in lista_generos:
           lista_generos.append(s[a])
for i in df["listed_in_hulu"]:
     if i != 0:
      s=i.split(",")
      for a in range(len(s)):
          if s[a] not in lista_generos:
           lista_generos.append(s[a])
for i in df["listed_in_amazon"]:
     if i != 0:
      s=i.split(",")
      for a in range(len(s)):
          if s[a] not in lista_generos:
           lista_generos.append(s[a])


#Funcion para obtener la plataforma en la que mas se repite el genero especificado
def get_listedin(genero:str):
 if genero not in lista_generos:
    raise ValueError("genero introduced is not in list: ",lista_generos)
 else:
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

#Funcion para obtener el actor que mas se repite en la plataforma y año indicado
def get_actor(plataforma:str, año:int):
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
