import reflex as rx
from typing import Optional
from sqlmodel import select
from app.models import User
import hashlib


class AuthState(rx.State):
    username: str = ""
    password: str = ""
    user: Optional[User] = None
    error_message: str = ""

    @rx.event
    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    @rx.event
    def login(self):
        with rx.session() as session:
            user = session.exec(
                select(User).where(User.username == self.username)
            ).first()
            if user and user.password_hash == self.hash_password(self.password):
                self.user = user
                self.error_message = ""
                return rx.redirect("/dashboard")
            else:
                self.error_message = "Credenciales inválidas"

    @rx.event
    def register(self):
        if not self.username or not self.password:
            self.error_message = "Complete todos los campos"
            return
        with rx.session() as session:
            existing_user = session.exec(
                select(User).where(User.username == self.username)
            ).first()
            if existing_user:
                self.error_message = "El usuario ya existe"
                return
            new_user = User(
                username=self.username, password_hash=self.hash_password(self.password)
            )
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
            self.user = new_user
            return rx.redirect("/dashboard")

    @rx.event
    def logout(self):
        self.user = None
        return rx.redirect("/")

    @rx.var
    def is_authenticated(self) -> bool:
        return self.user is not None