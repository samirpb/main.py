from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="API Tareas - Samir Perez")
app.add_middleware( CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.delete("/tareas/{tarea_id}")
def borrar_tarea(tarea_id: int):
    for tarea in tareas_db:
        if tarea["id"] == tarea_id:
            tareas_db.remove(tarea)
            return {"mensaje": f"Tarea {tarea_id} borrada correctamente"}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")