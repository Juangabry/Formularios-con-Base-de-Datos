import reflex as rx
from app.states.auth_state import AuthState


def auth_field(
    label: str, name: str, type: str = "text", placeholder: str = ""
) -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="block text-sm font-medium text-gray-700 mb-1"),
        rx.el.input(
            type=type,
            name=name,
            placeholder=placeholder,
            class_name="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent outline-none transition-all duration-200",
        ),
        class_name="mb-4",
    )


def login_form() -> rx.Component:
    return rx.el.form(
        auth_field("Email Address", "email", "email", "you@example.com"),
        auth_field("Password", "password", "password", "••••••••"),
        rx.el.button(
            "Sign In",
            type="submit",
            class_name="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-2.5 rounded-lg transition-colors duration-200 mt-2",
        ),
        on_submit=AuthState.login,
        reset_on_submit=True,
    )


def signup_form() -> rx.Component:
    return rx.el.form(
        auth_field("Username", "username", "text", "johndoe"),
        auth_field("Email Address", "email", "email", "you@example.com"),
        auth_field("Password", "password", "password", "••••••••"),
        auth_field("Confirm Password", "confirm_password", "password", "••••••••"),
        rx.el.button(
            "Create Account",
            type="submit",
            class_name="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-2.5 rounded-lg transition-colors duration-200 mt-2",
        ),
        on_submit=AuthState.signup,
        reset_on_submit=True,
    )


def auth_page_component() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon("activity", class_name="w-10 h-10 text-indigo-600 mb-2"),
                rx.el.h1("BRPS System", class_name="text-2xl font-bold text-gray-900"),
                rx.el.p(
                    "Psychosocial Risk Assessment", class_name="text-gray-500 text-sm"
                ),
                class_name="flex flex-col items-center mb-8",
            ),
            rx.cond(
                AuthState.error_message != "",
                rx.el.div(
                    rx.icon("badge_alert", class_name="w-5 h-5 mr-2"),
                    rx.el.span(AuthState.error_message),
                    class_name="bg-red-50 text-red-600 p-3 rounded-lg text-sm flex items-center mb-6 border border-red-100 animate-pulse",
                ),
            ),
            rx.el.div(
                rx.el.div(
                    rx.cond(
                        AuthState.is_login_mode,
                        rx.el.h2(
                            "Welcome back",
                            class_name="text-xl font-semibold text-gray-800 mb-6",
                        ),
                        rx.el.h2(
                            "Create account",
                            class_name="text-xl font-semibold text-gray-800 mb-6",
                        ),
                    ),
                    rx.cond(AuthState.is_login_mode, login_form(), signup_form()),
                    class_name="bg-white p-8 rounded-2xl shadow-xl border border-gray-100",
                ),
                rx.el.div(
                    rx.el.p(
                        rx.cond(
                            AuthState.is_login_mode,
                            "Don't have an account? ",
                            "Already have an account? ",
                        ),
                        rx.el.button(
                            rx.cond(AuthState.is_login_mode, "Sign up", "Log in"),
                            on_click=AuthState.toggle_mode,
                            class_name="font-semibold text-indigo-600 hover:text-indigo-500 ml-1 transition-colors",
                        ),
                        class_name="text-center text-sm text-gray-600",
                    ),
                    class_name="mt-6",
                ),
                class_name="w-full max-w-md",
            ),
            class_name="flex flex-col items-center justify-center min-h-screen w-full px-4",
        ),
        class_name="min-h-screen bg-gradient-to-br from-indigo-50 via-white to-purple-50",
    )