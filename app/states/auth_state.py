import reflex as rx
import bcrypt
from typing import Optional
from sqlmodel import select
from app.models import User


class AuthState(rx.State):
    user: Optional[dict] = None
    is_login_mode: bool = True
    error_message: str = ""

    @rx.event
    def toggle_mode(self):
        self.is_login_mode = not self.is_login_mode
        self.error_message = ""

    @rx.event
    async def login(self, form_data: dict):
        """Handle user login."""
        email = form_data.get("email")
        password = form_data.get("password")
        if not email or not password:
            self.error_message = "Please fill in all fields."
            return
        with rx.session() as session:
            query = select(User).where(User.email == email)
            user = session.exec(query).first()
            if user and bcrypt.checkpw(
                password.encode("utf-8"), user.password_hash.encode("utf-8")
            ):
                self.user = user.model_dump()
                self.error_message = ""
                return rx.redirect("/")
            else:
                self.error_message = "Invalid email or password."

    @rx.event
    async def signup(self, form_data: dict):
        """Handle user registration."""
        username = form_data.get("username")
        email = form_data.get("email")
        password = form_data.get("password")
        confirm_password = form_data.get("confirm_password")
        if not username or not email or (not password):
            self.error_message = "Please fill in all fields."
            return
        if password != confirm_password:
            self.error_message = "Passwords do not match."
            return
        with rx.session() as session:
            existing_user = session.exec(
                select(User).where(User.email == email)
            ).first()
            if existing_user:
                self.error_message = "Email already registered."
                return
            hashed_pw = bcrypt.hashpw(
                password.encode("utf-8"), bcrypt.gensalt()
            ).decode("utf-8")
            new_user = User(username=username, email=email, password_hash=hashed_pw)
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
            self.user = new_user.model_dump()
            self.error_message = ""
            return rx.redirect("/")

    @rx.event
    def logout(self):
        """Handle user logout."""
        self.user = None
        return rx.redirect("/login")

    @rx.event
    def check_auth(self):
        """Check if user is authenticated on page load."""
        if self.user is None:
            return rx.redirect("/login")