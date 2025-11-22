import reflex as rx
from sqlmodel import select
from app.models import FormaB
from app.states.auth_state import AuthState


class FormaBState(rx.State):
    q1: int = 0
    q2: int = 0
    q3: int = 0
    q4: int = 0
    q5: int = 0
    sugerencias: str = ""

    @rx.event
    def set_q1(self, val: str):
        self.q1 = int(val)

    @rx.event
    def set_q2(self, val: str):
        self.q2 = int(val)

    @rx.event
    def set_q3(self, val: str):
        self.q3 = int(val)

    @rx.event
    def set_q4(self, val: str):
        self.q4 = int(val)

    @rx.event
    def set_q5(self, val: str):
        self.q5 = int(val)

    @rx.event
    def update_sugerencias(self, text: str):
        self.sugerencias = text

    @rx.event
    async def submit(self):
        auth = await self.get_state(AuthState)
        if not auth.user:
            return rx.redirect("/")
        with rx.session() as session:
            existing = session.exec(
                select(FormaB).where(FormaB.user_id == auth.user.id)
            ).first()
            if existing:
                existing.q1 = self.q1
                existing.q2 = self.q2
                existing.q3 = self.q3
                existing.q4 = self.q4
                existing.q5 = self.q5
                existing.sugerencias = self.sugerencias
                existing.completed = True
                session.add(existing)
            else:
                new_record = FormaB(
                    user_id=auth.user.id,
                    q1=self.q1,
                    q2=self.q2,
                    q3=self.q3,
                    q4=self.q4,
                    q5=self.q5,
                    sugerencias=self.sugerencias,
                    completed=True,
                )
                session.add(new_record)
            session.commit()
        return rx.redirect("/dashboard")