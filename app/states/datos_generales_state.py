import reflex as rx
from sqlmodel import select
from app.models import DatosGenerales
from app.states.auth_state import AuthState


class DatosGeneralesState(rx.State):
    full_name: str = ""
    age: int = 0
    gender: str = ""
    position: str = ""
    department: str = ""
    sugerencias: str = ""

    @rx.event
    async def submit(self):
        auth = await self.get_state(AuthState)
        if not auth.user:
            return rx.redirect("/")
        with rx.session() as session:
            existing = session.exec(
                select(DatosGenerales).where(DatosGenerales.user_id == auth.user.id)
            ).first()
            if existing:
                existing.full_name = self.full_name
                existing.age = self.age
                existing.gender = self.gender
                existing.position = self.position
                existing.department = self.department
                existing.sugerencias = self.sugerencias
                existing.completed = True
                session.add(existing)
            else:
                new_record = DatosGenerales(
                    user_id=auth.user.id,
                    full_name=self.full_name,
                    age=self.age,
                    gender=self.gender,
                    position=self.position,
                    department=self.department,
                    sugerencias=self.sugerencias,
                    completed=True,
                )
                session.add(new_record)
            session.commit()
        return rx.redirect("/dashboard")