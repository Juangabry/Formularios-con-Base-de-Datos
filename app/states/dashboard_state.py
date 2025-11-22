import reflex as rx
from sqlmodel import select
from app.models import DatosGenerales, FormaA, FormaB, Extralaboral, EvaluacionEstres
from app.states.auth_state import AuthState


class DashboardState(rx.State):
    datos_generales_done: bool = False
    forma_a_done: bool = False
    forma_b_done: bool = False
    extralaboral_done: bool = False
    estres_done: bool = False

    @rx.event
    async def on_load(self):
        auth = await self.get_state(AuthState)
        if not auth.user:
            return
        with rx.session() as session:
            dg = session.exec(
                select(DatosGenerales).where(DatosGenerales.user_id == auth.user.id)
            ).first()
            self.datos_generales_done = dg.completed if dg else False
            fa = session.exec(
                select(FormaA).where(FormaA.user_id == auth.user.id)
            ).first()
            self.forma_a_done = fa.completed if fa else False
            fb = session.exec(
                select(FormaB).where(FormaB.user_id == auth.user.id)
            ).first()
            self.forma_b_done = fb.completed if fb else False
            ex = session.exec(
                select(Extralaboral).where(Extralaboral.user_id == auth.user.id)
            ).first()
            self.extralaboral_done = ex.completed if ex else False
            es = session.exec(
                select(EvaluacionEstres).where(EvaluacionEstres.user_id == auth.user.id)
            ).first()
            self.estres_done = es.completed if es else False