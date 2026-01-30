"""
Modelos de datos para la aplicación.
"""

from enum import Enum
from typing import List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel


class Genero(str, Enum):
    """Enum para el género del usuario."""

    MASCULINO = "Hombre"
    FEMENINO = "Mujer"
    OTRO = "Otro"


class Role(str, Enum):
    """Enum para los roles del usuario."""

    ADMIN = "admin"
    USER = "user"


class Usuario(BaseModel):  # pylint: disable=too-few-public-methods
    """Modelo de usuario."""

    id: Optional[UUID] = uuid4()
    primerNombre: str
    apellidos: str
    genero: Genero
    roles: List[Role]
