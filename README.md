# FastAPI-Docker-pandas

El proyecto consiste en realizar una ingesta de datos desde diversas fuentes, posteriormente aplicar las transformaciones  pertinentes, y luego disponibilizar los datos limpios para su consulta a través de una API. Para esta API se utilizo FastAPI y luego se creo un entorno virtual con docker para su uso.

---

### Paso 1:

Se cargaron los datasets que se encuentran en \Datasets_original y se realizo limpieza, cambios de columnas y de tipo de datos. Estos cambios se encuentran detallados en \Data_cleansing\Clean.ipynb

Los cuatro datasets fueron combinados en un solo archivo para su posterior ingesta y uso.

### Paso 2:

Luego se creo el archivo functions.py en donde se encuentran las funciones que se van a utilizar luego en el archivo main.py. Dichas funciones utilizan un dataframe creado con el archivo df.csv previamente generado en el paso 1.

### Paso 3:

El archivo main.py se configuro para poder crear la app con FastAPI, este archivo a su vez toma las funciones del archivo functions.py. Esto se hizo para mantener el codigo de forma mas ordenada.

### Paso 4:

Se crea un dockerfile con la configuracion para crear la imagen de docker, luego se ejecuta el comando para crear la imagen de docker, en este caso llamada "fastapi"

```
docker build -t fastapi .
```

### Paso 5:

La imagen se ejecuta usando `docker run -d --name container -p 8000:8000 fastapi `y se abre en el navegador `localhost:8000/docs` desde donde se podran ejecutar las consultas requeridas.

---

## Conclusiones

Para esta API elegi utilizar solo pandas y funciones basicas de python como el loop for, etc. para evitar añadirle mas complejidad a herramientas como FastAPI o Docker, las cuales utilizo por primera vez, y evitar futuros errores. De todas formas con este proyecto aprendi el uso basico de estas herramientas, como utilizarlas conjuntamente y su utilidad para futuras API.
