import reflex as rx
from sqlmodel import select
from app.models import DatosGenerales, FormaA, FormaB, Extralaboral, EvaluacionEstres
from app.states.auth_state import AuthState


class DashboardState(rx.State):
    datos_generales_status: str = "Pending"
    forma_a_status: str = "Locked"
    forma_b_status: str = "Locked"
    extralaboral_status: str = "Pending"
    estres_status: str = "Pending"
    show_ab_message: bool = False
    completed_count: int = 0
    pending_count: int = 5

    @rx.event
    async def load_progress(self):
        auth_state = await self.get_state(AuthState)
        if not auth_state.user:
            return
        user_id = auth_state.user["id"]
        with rx.session() as session:

            @rx.event
            def check_status(model):
                obj = session.exec(
                    select(model).where(model.user_id == user_id)
                ).first()
                return obj.is_completed if obj else False

            dg_done = check_status(DatosGenerales)
            fa_done = check_status(FormaA)
            fb_done = check_status(FormaB)
            ex_done = check_status(Extralaboral)
            ee_done = check_status(EvaluacionEstres)
            self.datos_generales_status = "Completed" if dg_done else "Pending"
            if dg_done:
                self.forma_a_status = "Completed" if fa_done else "Pending"
                self.forma_b_status = "Completed" if fb_done else "Pending"
                self.show_ab_message = not (fa_done or fb_done)
            else:
                self.forma_a_status = "Locked"
                self.forma_b_status = "Locked"
                self.show_ab_message = False
            self.extralaboral_status = "Completed" if ex_done else "Pending"
            self.estres_status = "Completed" if ee_done else "Pending"
            statuses = [
                self.datos_generales_status,
                self.forma_a_status,
                self.forma_b_status,
                self.extralaboral_status,
                self.estres_status,
            ]
            self.completed_count = statuses.count("Completed")
            self.pending_count = 5 - self.completed_count