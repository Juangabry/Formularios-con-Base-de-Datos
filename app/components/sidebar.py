import reflex as rx
from app.states.auth_state import AuthState


def sidebar_item(text: str, icon: str, href: str) -> rx.Component:
    return rx.el.a(
        rx.icon(icon, class_name="w-5 h-5 mr-3"),
        text,
        href=href,
        class_name="flex items-center px-6 py-3 text-gray-600 hover:bg-indigo-50 hover:text-indigo-600 transition-colors cursor-pointer",
    )


def sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.icon("activity", class_name="w-8 h-8 text-indigo-600"),
                rx.el.span("BRPS", class_name="text-xl font-bold ml-2"),
                class_name="flex items-center px-6 h-16 border-b border-gray-100",
            ),
            rx.el.nav(
                sidebar_item("Dashboard", "layout-dashboard", "/"),
                rx.el.div(
                    rx.el.span(
                        "Instrumento BRPS",
                        class_name="px-6 py-2 text-xs font-semibold text-gray-400 uppercase tracking-wider",
                    ),
                    sidebar_item("Datos Generales", "user", "/form/datos-generales"),
                    sidebar_item("Forma A", "file-text", "/form/forma-a"),
                    sidebar_item("Forma B", "file-text", "/form/forma-b"),
                    sidebar_item("Extralaboral", "sun", "/form/extralaboral"),
                    sidebar_item("Evaluación de Estrés", "heart-pulse", "/form/estres"),
                    class_name="flex flex-col mt-2",
                ),
                rx.el.div(
                    rx.el.span(
                        "Análisis",
                        class_name="px-6 py-2 text-xs font-semibold text-gray-400 uppercase tracking-wider",
                    ),
                    sidebar_item("Resultados", "bar-chart-2", "/results"),
                    class_name="flex flex-col mt-2",
                ),
                class_name="flex flex-col py-4",
            ),
            class_name="flex flex-col h-full bg-white border-r border-gray-200",
        ),
        class_name="hidden md:block w-64 h-screen fixed left-0 top-0 z-10",
    )