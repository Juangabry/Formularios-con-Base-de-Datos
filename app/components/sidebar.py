import reflex as rx
from app.states.auth_state import AuthState


def sidebar_item(text: str, icon: str, url: str, enabled: bool = True) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.icon(icon, class_name="w-5 h-5 mr-3"),
            rx.el.span(text),
            class_name=f"flex items-center p-3 rounded-lg transition-colors {('hover:bg-gray-100 text-gray-700' if enabled else 'text-gray-300 cursor-not-allowed')}",
        ),
        href=url if enabled else "#",
    )


def sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.h2(
                "Riesgo Psicosocial",
                class_name="text-xl font-bold text-gray-800 px-4 py-6 border-b",
            ),
            rx.el.nav(
                rx.el.div(
                    sidebar_item("Dashboard", "layout-dashboard", "/dashboard"),
                    sidebar_item("Datos Generales", "user", "/datos-generales"),
                    sidebar_item("Forma A", "file-text", "/forma-a"),
                    sidebar_item("Forma B", "file-text", "/forma-b"),
                    sidebar_item("Extralaboral", "home", "/extralaboral"),
                    sidebar_item("Estrés", "activity", "/estres"),
                    sidebar_item("Resultados", "bar-chart-2", "/results"),
                    class_name="space-y-2 p-4",
                )
            ),
            rx.el.div(
                rx.el.button(
                    rx.el.div(
                        rx.icon("log-out", class_name="w-5 h-5 mr-2"),
                        "Cerrar Sesión",
                        class_name="flex items-center",
                    ),
                    on_click=AuthState.logout,
                    class_name="w-full p-3 text-left text-red-600 hover:bg-red-50 rounded-lg transition-colors",
                ),
                class_name="p-4 border-t mt-auto",
            ),
            class_name="flex flex-col h-full",
        ),
        class_name="w-64 bg-white border-r h-screen fixed left-0 top-0 hidden md:block",
    )