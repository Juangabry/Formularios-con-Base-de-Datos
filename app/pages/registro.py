import reflex as rx
from app.states.auth_state import AuthState


def registro_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Registro de Usuario", class_name="text-3xl font-bold text-center mb-8"
            ),
            rx.el.div(
                rx.el.label(
                    "Usuario", class_name="block text-sm font-medium text-gray-700 mb-1"
                ),
                rx.el.input(
                    placeholder="Elija un nombre de usuario",
                    on_change=AuthState.set_username,
                    class_name="w-full p-2 border rounded-lg mb-4",
                    default_value=AuthState.username,
                ),
                rx.el.label(
                    "Contraseña",
                    class_name="block text-sm font-medium text-gray-700 mb-1",
                ),
                rx.el.input(
                    type="password",
                    placeholder="Elija una contraseña",
                    on_change=AuthState.set_password,
                    class_name="w-full p-2 border rounded-lg mb-6",
                    default_value=AuthState.password,
                ),
                rx.el.button(
                    "Registrarse",
                    on_click=AuthState.register,
                    class_name="w-full bg-green-600 text-white py-2 rounded-lg hover:bg-green-700 transition-colors",
                ),
                rx.cond(
                    AuthState.error_message != "",
                    rx.el.p(
                        AuthState.error_message,
                        class_name="text-red-500 text-sm mt-4 text-center",
                    ),
                    rx.el.div(),
                ),
                rx.el.div(
                    rx.el.a(
                        "¿Ya tienes cuenta? Inicia sesión",
                        href="/",
                        class_name="text-blue-600 hover:underline",
                    ),
                    class_name="text-center mt-6 text-sm",
                ),
                class_name="bg-white p-8 rounded-xl shadow-lg w-full max-w-md",
            ),
            class_name="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4",
        ),
        class_name="font-['Inter']",
    )