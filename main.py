from fastapi import FastAPI

app = FastAPI(title='API Tareas - Samir Perez')

@app.get("/")
def inicio(): 
    return {"mensaje": "¡Bienvenido a mi API!"} 

@app.get("/tareas")
def listar_tareas():
    return [{"id":1, "titulo": 'Aprender FastAPI','hecha': False}]