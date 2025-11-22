import reflex as rx
from datetime import datetime, timezone
from typing import Optional
import sqlmodel
from sqlalchemy import Column, JSON


def get_utc_now():
    return datetime.now(timezone.utc)


class User(sqlmodel.SQLModel, table=True):
    """User model for authentication."""

    id: Optional[int] = sqlmodel.Field(default=None, primary_key=True)
    username: str
    email: str = sqlmodel.Field(unique=True, index=True)
    password_hash: str
    created_at: datetime = sqlmodel.Field(default_factory=get_utc_now)


class DatosGenerales(sqlmodel.SQLModel, table=True):
    """Formulario de Datos Generales."""

    id: Optional[int] = sqlmodel.Field(default=None, primary_key=True)
    user_id: int = sqlmodel.Field(foreign_key="user.id")
    created_at: datetime = sqlmodel.Field(default_factory=get_utc_now)
    is_completed: bool = False
    responses: dict[str, str | int | float | bool | None] = sqlmodel.Field(
        default={}, sa_column=Column(JSON)
    )
    sugerencias: Optional[str] = sqlmodel.Field(default=None)


class FormaA(sqlmodel.SQLModel, table=True):
    """Formulario A."""

    id: Optional[int] = sqlmodel.Field(default=None, primary_key=True)
    user_id: int = sqlmodel.Field(foreign_key="user.id")
    created_at: datetime = sqlmodel.Field(default_factory=get_utc_now)
    is_completed: bool = False
    responses: dict[str, str | int | float | bool | None] = sqlmodel.Field(
        default={}, sa_column=Column(JSON)
    )
    sugerencias: Optional[str] = sqlmodel.Field(default=None)


class FormaB(sqlmodel.SQLModel, table=True):
    """Formulario B."""

    id: Optional[int] = sqlmodel.Field(default=None, primary_key=True)
    user_id: int = sqlmodel.Field(foreign_key="user.id")
    created_at: datetime = sqlmodel.Field(default_factory=get_utc_now)
    is_completed: bool = False
    responses: dict[str, str | int | float | bool | None] = sqlmodel.Field(
        default={}, sa_column=Column(JSON)
    )
    sugerencias: Optional[str] = sqlmodel.Field(default=None)


class Extralaboral(sqlmodel.SQLModel, table=True):
    """Formulario Extralaboral."""

    id: Optional[int] = sqlmodel.Field(default=None, primary_key=True)
    user_id: int = sqlmodel.Field(foreign_key="user.id")
    created_at: datetime = sqlmodel.Field(default_factory=get_utc_now)
    is_completed: bool = False
    responses: dict[str, str | int | float | bool | None] = sqlmodel.Field(
        default={}, sa_column=Column(JSON)
    )
    sugerencias: Optional[str] = sqlmodel.Field(default=None)


class EvaluacionEstres(sqlmodel.SQLModel, table=True):
    """Evaluación de Estrés."""

    id: Optional[int] = sqlmodel.Field(default=None, primary_key=True)
    user_id: int = sqlmodel.Field(foreign_key="user.id")
    created_at: datetime = sqlmodel.Field(default_factory=get_utc_now)
    is_completed: bool = False
    responses: dict[str, str | int | float | bool | None] = sqlmodel.Field(
        default={}, sa_column=Column(JSON)
    )
    sugerencias: Optional[str] = sqlmodel.Field(default=None)