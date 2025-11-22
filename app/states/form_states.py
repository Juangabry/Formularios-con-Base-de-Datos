import reflex as rx
from sqlmodel import select
from typing import Any
from app.models import DatosGenerales, FormaA, FormaB, Extralaboral, EvaluacionEstres
from app.states.auth_state import AuthState


class DatosGeneralesState(rx.State):
    responses: dict[str, str] = {}
    sugerencias: str = ""
    REQUIRED_FIELDS: list[str] = [
        "nombre",
        "edad",
        "sexo",
        "estado_civil",
        "educacion",
        "cargo",
        "area",
        "contrato",
        "antiguedad",
    ]

    @rx.event
    def update_field(self, field: str, value: str):
        self.responses[field] = value

    @rx.event
    def set_sugerencias(self, value: str):
        self.sugerencias = value

    @rx.event
    async def load_data(self):
        user = await self.get_state(AuthState)
        if not user.user:
            return
        with rx.session() as session:
            record = session.exec(
                select(DatosGenerales).where(DatosGenerales.user_id == user.user["id"])
            ).first()
            if record:
                if record.responses:
                    self.responses = record.responses
                if record.sugerencias:
                    self.sugerencias = record.sugerencias

    @rx.event
    async def save_form(self):
        user = await self.get_state(AuthState)
        if not user.user:
            return
        missing_fields = [
            field
            for field in self.REQUIRED_FIELDS
            if not self.responses.get(field)
            or str(self.responses.get(field)).strip() == ""
        ]
        if missing_fields:
            return rx.toast.error(
                f"Por favor complete todos los campos obligatorios: {', '.join(missing_fields)}"
            )
        with rx.session() as session:
            record = session.exec(
                select(DatosGenerales).where(DatosGenerales.user_id == user.user["id"])
            ).first()
            if not record:
                record = DatosGenerales(user_id=user.user["id"])
                session.add(record)
            record.responses = self.responses
            record.sugerencias = self.sugerencias
            record.is_completed = True
            session.add(record)
            session.commit()
        return rx.redirect("/")


class LikertFormState(rx.State):
    """Base state for Likert scale forms."""

    responses: dict[str, str] = {}
    sugerencias: str = ""
    page: int = 1
    total_pages: int = 1
    total_questions: int = 0

    @rx.event
    def get_model(self):
        raise NotImplementedError

    @rx.event
    def set_answer(self, question_idx: str, value: str):
        self.responses[question_idx] = value

    @rx.event
    def set_sugerencias(self, value: str):
        self.sugerencias = value

    @rx.event
    def next_page(self):
        if self.page < self.total_pages:
            self.page += 1
            return rx.scroll_to(id="form-top")

    @rx.event
    def prev_page(self):
        if self.page > 1:
            self.page -= 1
            return rx.scroll_to(id="form-top")

    async def _load_from_db(self, model_class):
        user = await self.get_state(AuthState)
        if not user.user:
            return
        with rx.session() as session:
            record = session.exec(
                select(model_class).where(model_class.user_id == user.user["id"])
            ).first()
            if record:
                if record.responses:
                    self.responses = record.responses
                if record.sugerencias:
                    self.sugerencias = record.sugerencias

    async def _save_to_db(self, model_class, completed: bool = False):
        user = await self.get_state(AuthState)
        if not user.user:
            return
        if completed:
            answered_count = len(self.responses)
            if answered_count < self.total_questions:
                return rx.toast.error(
                    f"Faltan preguntas por responder. ({answered_count}/{self.total_questions})"
                )
        with rx.session() as session:
            record = session.exec(
                select(model_class).where(model_class.user_id == user.user["id"])
            ).first()
            if not record:
                record = model_class(user_id=user.user["id"])
                session.add(record)
            record.responses = self.responses
            record.sugerencias = self.sugerencias
            if completed:
                record.is_completed = True
            session.add(record)
            session.commit()
        if completed:
            return rx.redirect("/")
        else:
            return rx.toast.success("Progreso guardado")


class FormaAState(LikertFormState):
    total_pages: int = 3
    total_questions: int = 123

    @rx.event
    async def load_data(self):
        await self._load_from_db(FormaA)

    @rx.event
    async def save_progress(self):
        await self._save_to_db(FormaA, completed=False)

    @rx.event
    async def finish_form(self):
        await self._save_to_db(FormaA, completed=True)


class FormaBState(LikertFormState):
    total_pages: int = 3
    total_questions: int = 97

    @rx.event
    async def load_data(self):
        await self._load_from_db(FormaB)

    @rx.event
    async def save_progress(self):
        await self._save_to_db(FormaB, completed=False)

    @rx.event
    async def finish_form(self):
        await self._save_to_db(FormaB, completed=True)


class ExtralaboralState(LikertFormState):
    total_pages: int = 2
    total_questions: int = 31

    @rx.event
    async def load_data(self):
        await self._load_from_db(Extralaboral)

    @rx.event
    async def save_progress(self):
        await self._save_to_db(Extralaboral, completed=False)

    @rx.event
    async def finish_form(self):
        await self._save_to_db(Extralaboral, completed=True)


class EstresState(LikertFormState):
    total_pages: int = 2
    total_questions: int = 31

    @rx.event
    async def load_data(self):
        await self._load_from_db(EvaluacionEstres)

    @rx.event
    async def save_progress(self):
        await self._save_to_db(EvaluacionEstres, completed=False)

    @rx.event
    async def finish_form(self):
        await self._save_to_db(EvaluacionEstres, completed=True)