import reflex as rx
from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import datetime


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    password_hash: str
    created_at: datetime = Field(default_factory=datetime.utcnow)


class DatosGenerales(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    full_name: str
    age: int
    gender: str
    position: str
    department: str
    sugerencias: str = ""
    completed: bool = False


class FormaA(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    q1: int = 0
    q2: int = 0
    q3: int = 0
    q4: int = 0
    q5: int = 0
    sugerencias: str = ""
    completed: bool = False


class FormaB(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    q1: int = 0
    q2: int = 0
    q3: int = 0
    q4: int = 0
    q5: int = 0
    sugerencias: str = ""
    completed: bool = False


class Extralaboral(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    q1: int = 0
    q2: int = 0
    q3: int = 0
    q4: int = 0
    q5: int = 0
    sugerencias: str = ""
    completed: bool = False


class EvaluacionEstres(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    q1: int = 0
    q2: int = 0
    q3: int = 0
    q4: int = 0
    q5: int = 0
    sugerencias: str = ""
    completed: bool = False