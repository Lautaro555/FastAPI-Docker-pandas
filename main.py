from fastapi import FastAPI, Path, UploadFile, File
import pandas as pd

app=FastAPI()

@app.get("/")
async def index():
    return {'name':'First Data'}
'''
get = get an information 
post = create something new
put = update
delete = delete something
'''
type={"cast_hulu": "object", "hulu": "int64", "amazon": "int64", "netflix": "int64", "disney": "int64"}
df=pd.read_csv("https://github.com/Lautaro555/FastAPI-Docker-pandas/raw/main/ETL/df.csv",sep=",",dtype=type).drop('Unnamed: 0', axis=1)


@app.get("/get-alumno/{alumno_id}")
async def get_alumno(alumno_id:int=Path(None,description='Necesitamos que coloque el número de alumno',gt=0,lt=6)):
    return alumnos[alumno_id]

@app.get('/get-by-name/{alumno_id}')
async def get_alumno(*, alumno_id:Optional[int], name:Optional[str] = None):#, test : int):
    for alumno_id in alumnos:
        if alumnos[alumno_id]['name']==name:
            return alumnos[alumno_id]
    return {'Datos no encotrados'}

@app.post('/crear-alumno/{alumno_id}')
async def create_alumno(alumno_id : int, alumno : Alumno): #creamos un objeto llamado alumno con la forma de la clase Alumno
    if alumno_id in alumnos:
        return  {'Error - El Alumno ya existe'}

    alumnos[alumno_id]=alumno
    return alumnos[alumno_id]

@app.put('/actualizar-alumno/{alumno_id}')
async def update_alumno(alumno_id: int, alumno: ActualizarAlumno):
    if alumno_id not in alumnos:
        return {'Error - El Alumno no existe'}
    
    if alumno.name != None:
        alumnos[alumno_id].name = alumno.name

    if alumno.skill != None:
        alumnos[alumno_id].skill = alumno.skill 

    if alumno.children != None:
        alumnos[alumno_id].children = alumno.children

    alumnos[alumno_id] = alumno
    return alumnos[alumno_id]

@app.delete('/borar-alumno/{alumno_id}')
async def delete_alumno(alumno_id : int):
    if alumno_id not in alumnos:
        return {'Error - El Alumno no existe'}

    del alumnos[alumno_id]
    return {'Se ha borrado el Alumno exitosamente'}


'''
@app.post('/upload-file/{filename}')
async def upload_file(file: UploadFile =File(...)):
    with open('test.csv','wb') as buffer:
        shutil.copyfileobj(file.file,buffer)

    return {'file_name':file.filename}
'''
@app.post('/upload-file/{filename}')
async def upload_file(file: UploadFile =File(...)):
    with open(f'{file.filename}','wb') as buffer:
        shutil.copyfileobj(file.file,buffer)

    return {'file_name':file.filename}


@app.post('/upload-manyfile')
async def upload_manyfile(files: List[UploadFile] =File(...)):
    for fi in files: 
        with open(f'{fi.filename}','wb') as buffer:
            shutil.copyfileobj(fi.file,buffer)
    return {'file_name':'sus archivos cargaron correctamente'}