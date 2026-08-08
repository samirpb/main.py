from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="API Tareas - Samir Perez")

# Modelo de datos - así se hace en empresa real
class Tarea(BaseModel):
    titulo: str
    hecha: bool = False

tareas_db = [
    {"id": 1, "titulo": "Aprender FastAPI", "hecha": False}
]

@app.get("/")
def inicio():
    return {"mensaje": "¡Bienvenido a mi API!", "autor": "Samir - SENA"}

@app.get("/tareas")
def listar_tareas():
    return tareas_db

@app.post("/tareas")
def crear_tarea(tarea: Tarea):
    nueva_tarea = {
        "id": len(tareas_db) + 1,
        "titulo": tarea.titulo,
        "hecha": tarea.hecha
    }
    tareas_db.append(nueva_tarea)
    return nueva_tarea