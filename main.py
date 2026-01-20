from fastapi import FastAPI, HTTPException
from typing import List
from uuid import UUID, uuid4
from model import Genero, Role, Usuario

app = FastAPI()

db: List[Usuario] = [
    Usuario(
        id=uuid4(),
        primerNombre="Paul",
        apellidos="Dirac",
        genero=Genero.masculino,
        roles=[Role.user]
    ),
    Usuario(
        id=uuid4(),
        primerNombre="George",
        apellidos="Lematrei",
        genero=Genero.masculino,
        roles=[Role.user]
    ),
    Usuario(
        id=uuid4(),
        primerNombre="Marie",
        apellidos="Curie",
        genero=Genero.femenino,
        roles=[Role.user]
    )
]

@app.get("/")
async def root():
    return {"message": "Hola Jones construyendo el futuro"}

@app.get("/api/v1/users")
async def get_users():
    return db

@app.get("/api/v1/users/{user_id}")
async def get_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@app.put("/api/v1/users/{user_id}")
async def update_user(user_id: UUID, updated_user: Usuario):
    for index, user in enumerate(db):
        if user.id == user_id:
            db[index] = updated_user.copy(update={"id": user_id})
            return db[index]
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"message": "Usuario eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
