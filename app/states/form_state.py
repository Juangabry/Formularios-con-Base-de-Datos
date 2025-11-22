import reflex as rx
from app.states.auth_state import AuthState


class FormState(rx.State):
    sugerencias: str = ""

    @rx.event
    def update_sugerencias(self, text: str):
        self.sugerencias = text

    @rx.event
    def check_auth(self):
        pass