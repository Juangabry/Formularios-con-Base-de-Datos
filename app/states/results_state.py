import reflex as rx
from sqlmodel import select
from app.models import DatosGenerales, FormaA, FormaB, Extralaboral, EvaluacionEstres
from app.states.auth_state import AuthState


class ResultsState(rx.State):
    completed_forms_count: int = 0
    total_questions_answered: int = 0
    response_distribution: list[dict[str, str | int]] = []
    completion_data: list[dict[str, str | int]] = [
        {"name": "Datos Generales", "progress": 0},
        {"name": "Forma A", "progress": 0},
        {"name": "Forma B", "progress": 0},
        {"name": "Extralaboral", "progress": 0},
        {"name": "Estrés", "progress": 0},
    ]

    @rx.event
    async def load_stats(self):
        user = await self.get_state(AuthState)
        if not user.user:
            return
        user_id = user.user["id"]
        with rx.session() as session:
            dg = session.exec(
                select(DatosGenerales).where(DatosGenerales.user_id == user_id)
            ).first()
            fa = session.exec(select(FormaA).where(FormaA.user_id == user_id)).first()
            fb = session.exec(select(FormaB).where(FormaB.user_id == user_id)).first()
            ex = session.exec(
                select(Extralaboral).where(Extralaboral.user_id == user_id)
            ).first()
            es = session.exec(
                select(EvaluacionEstres).where(EvaluacionEstres.user_id == user_id)
            ).first()
            forms = [dg, fa, fb, ex, es]
            self.completed_forms_count = sum((1 for f in forms if f and f.is_completed))
            total_responses = 0
            dist = {
                "Siempre": 0,
                "Casi siempre": 0,
                "Algunas veces": 0,
                "Casi nunca": 0,
                "Nunca": 0,
            }
            form_names = [
                "Datos Generales",
                "Forma A",
                "Forma B",
                "Extralaboral",
                "Estrés",
            ]
            form_counts = [0, 123, 97, 31, 31]
            for i, form in enumerate(forms):
                if form and form.responses:
                    count = len(form.responses)
                    total_responses += count
                    if i == 0:
                        progress = 100 if form.is_completed else 50 if count > 0 else 0
                    else:
                        total_q = form_counts[i]
                        progress = (
                            min(100, int(count / total_q * 100)) if total_q > 0 else 0
                        )
                    self.completion_data[i]["progress"] = (
                        100 if form.is_completed else progress
                    )
                    for val in form.responses.values():
                        if isinstance(val, str) and val in dist:
                            dist[val] += 1
            self.total_questions_answered = total_responses
            self.response_distribution = [
                {"name": k, "value": v} for k, v in dist.items()
            ]