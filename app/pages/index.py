import reflex as rx
from app.states.auth_state import AuthState
from app.states.dashboard_state import DashboardState
from app.components.sidebar import sidebar


def dashboard_card(title: str, status: str, icon: str, url: str) -> rx.Component:
    is_locked = status == "Locked"
    is_completed = status == "Completed"
    return rx.el.div(
        rx.el.div(
            rx.icon(
                icon,
                class_name=rx.cond(
                    is_locked, "w-6 h-6 text-gray-400", "w-6 h-6 text-indigo-600"
                ),
            ),
            rx.el.span(
                status,
                class_name=rx.cond(
                    is_completed,
                    "text-xs font-medium px-2 py-1 bg-green-100 text-green-700 rounded-full",
                    rx.cond(
                        is_locked,
                        "text-xs font-medium px-2 py-1 bg-gray-100 text-gray-500 rounded-full",
                        "text-xs font-medium px-2 py-1 bg-amber-100 text-amber-700 rounded-full",
                    ),
                ),
            ),
            class_name="flex justify-between items-start mb-4",
        ),
        rx.el.h3(
            title,
            class_name=rx.cond(
                is_locked,
                "font-semibold text-gray-400 mb-1",
                "font-semibold text-gray-800 mb-1",
            ),
        ),
        rx.el.p(
            "Required assessment form",
            class_name=rx.cond(
                is_locked, "text-sm text-gray-400", "text-sm text-gray-500"
            ),
        ),
        rx.cond(
            is_locked,
            rx.el.button(
                rx.icon("lock", class_name="w-4 h-4 mr-2"),
                "Locked",
                disabled=True,
                class_name="mt-4 w-full py-2 px-4 border border-gray-200 text-gray-400 rounded-lg bg-gray-50 flex items-center justify-center text-sm font-medium cursor-not-allowed",
            ),
            rx.el.a(
                rx.cond(is_completed, "Review", "Start"),
                href=url,
                class_name=rx.cond(
                    is_completed,
                    "mt-4 w-full block text-center py-2 px-4 border border-green-600 text-green-600 rounded-lg hover:bg-green-50 transition-colors text-sm font-medium",
                    "mt-4 w-full block text-center py-2 px-4 border border-indigo-600 text-indigo-600 rounded-lg hover:bg-indigo-50 transition-colors text-sm font-medium",
                ),
            ),
        ),
        class_name=rx.cond(
            is_locked,
            "bg-gray-50 p-6 rounded-xl border border-gray-200 shadow-none opacity-80",
            "bg-white p-6 rounded-xl border border-gray-200 shadow-sm hover:shadow-md transition-shadow",
        ),
    )


def index() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.main(
            rx.el.header(
                rx.el.div(
                    rx.el.h1(
                        "Dashboard", class_name="text-2xl font-bold text-gray-800"
                    ),
                    rx.el.div(
                        rx.el.span(
                            f"Welcome, {AuthState.user['username']}",
                            class_name="text-sm font-medium text-gray-600 mr-4",
                        ),
                        rx.el.button(
                            rx.icon("log-out", class_name="w-5 h-5"),
                            on_click=AuthState.logout,
                            class_name="text-gray-500 hover:text-red-600 transition-colors",
                        ),
                        class_name="flex items-center",
                    ),
                    class_name="flex justify-between items-center mb-8",
                ),
                rx.cond(
                    DashboardState.show_ab_message,
                    rx.el.div(
                        rx.el.div(
                            rx.icon("info", class_name="w-6 h-6 text-blue-600 mr-3"),
                            rx.el.div(
                                rx.el.h3(
                                    "Next Step Required",
                                    class_name="font-semibold text-blue-800",
                                ),
                                rx.el.p(
                                    "You have completed 'Datos Generales'. Please choose to fill out either 'Forma A' or 'Forma B' to proceed.",
                                    class_name="text-blue-600 text-sm",
                                ),
                            ),
                            class_name="flex items-start",
                        ),
                        class_name="mb-8 bg-blue-50 border border-blue-200 rounded-xl p-4 animate-pulse",
                    ),
                ),
                class_name="mb-8",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.p("Total Forms", class_name="text-sm text-gray-500 mb-1"),
                    rx.el.p("5", class_name="text-2xl font-bold text-gray-900"),
                    class_name="bg-white p-6 rounded-xl border border-gray-200 shadow-sm",
                ),
                rx.el.div(
                    rx.el.p("Completed", class_name="text-sm text-gray-500 mb-1"),
                    rx.el.p(
                        DashboardState.completed_count,
                        class_name="text-2xl font-bold text-indigo-600",
                    ),
                    class_name="bg-white p-6 rounded-xl border border-gray-200 shadow-sm",
                ),
                rx.el.div(
                    rx.el.p("Pending", class_name="text-sm text-gray-500 mb-1"),
                    rx.el.p(
                        DashboardState.pending_count,
                        class_name="text-2xl font-bold text-amber-600",
                    ),
                    class_name="bg-white p-6 rounded-xl border border-gray-200 shadow-sm",
                ),
                class_name="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8",
            ),
            rx.el.h2(
                "Your Assessments", class_name="text-lg font-bold text-gray-800 mb-4"
            ),
            rx.el.div(
                dashboard_card(
                    "Datos Generales",
                    DashboardState.datos_generales_status,
                    "user",
                    "/form/datos-generales",
                ),
                dashboard_card(
                    "Forma A",
                    DashboardState.forma_a_status,
                    "file-text",
                    "/form/forma-a",
                ),
                dashboard_card(
                    "Forma B",
                    DashboardState.forma_b_status,
                    "file-text",
                    "/form/forma-b",
                ),
                dashboard_card(
                    "Extralaboral",
                    DashboardState.extralaboral_status,
                    "sun",
                    "/form/extralaboral",
                ),
                dashboard_card(
                    "Evaluación Estrés",
                    DashboardState.estres_status,
                    "heart-pulse",
                    "/form/estres",
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6",
            ),
            class_name="md:ml-64 p-8 min-h-screen bg-gray-50",
        ),
        class_name="min-h-screen font-['Inter']",
    )