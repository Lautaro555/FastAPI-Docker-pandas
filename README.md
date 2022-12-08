# FastAPI-Docker-pandas

El proyecto consiste en realizar una ingesta de datos desde diversas fuentes, posteriormente aplicar las transformaciones que consideren pertinentes, y luego disponibilizar los datos limpios para su consulta a través de una API. Esta API deberán construirla en un entorno virtual dockerizado.

### Paso 1:

Se cargaron los datasets que se encuentran en \Datasets_original y se realizo limpieza,cambios de columnas y de tipo de datos.

Estos cambios se encuentra detallados en \Data_cleansing\Clean.ipynb.

### Paso 2:

Luego se creo el archivo functions.py en donde se encuentran las funciones que se van a utilizar luego en el archivo main.py.

### Paso 3:

El archivo main.py se configuro para poder crear la app con FastAPI, este archivo a su vez toma las funciones del archivo functions.py. Esto se hizo para mantener el codigo de forma mas ordenada.
