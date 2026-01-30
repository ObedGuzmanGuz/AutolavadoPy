"""
API principal de usuarios con FastAPI.
"""

from typing import List
from uuid import UUID, uuid4

from fastapi import FastAPI, HTTPException

from model import Genero, Role, Usuario

app = FastAPI()

db: List[Usuario] = [
    Usuario(
        id=uuid4(),
        primerNombre="Paul",
        apellidos="Dirac",
        genero=Genero.MASCULINO,
        roles=[Role.USER],
    ),
    Usuario(
        id=uuid4(),
        primerNombre="George",
        apellidos="Lemaitre",
        genero=Genero.MASCULINO,
        roles=[Role.USER],
    ),
    Usuario(
        id=uuid4(),
        primerNombre="Marie",
        apellidos="Curie",
        genero=Genero.FEMENINO,
        roles=[Role.USER],
    ),
]


@app.get("/")
async def root():
    """Endpoint raíz."""
    return {"message": "Hola Jones construyendo el futuro"}


@app.get("/api/v1/users")
async def get_users():
    """Obtiene todos los usuarios."""
    return db


@app.get("/api/v1/users/{user_id}")
async def get_user(user_id: UUID):
    """Obtiene un usuario por ID."""
    for user in db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


@app.put("/api/v1/users/{user_id}")
async def update_user(user_id: UUID, updated_user: Usuario):
    """Actualiza un usuario existente."""
    for index, user in enumerate(db):
        if user.id == user_id:
            db[index] = updated_user.copy(update={"id": user_id})
            return db[index]
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    """Elimina un usuario."""
    for index, user in enumerate(db):
        if user.id == user_id:
            db.pop(index)
            return {"message": "Usuario eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
