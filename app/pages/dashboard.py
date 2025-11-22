import reflex as rx
from app.states.dashboard_state import DashboardState
from app.components.sidebar import sidebar


def status_card(
    title: str, description: str, status: bool, url: str, locked: bool = False
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(title, class_name="text-lg font-semibold text-gray-900"),
            rx.el.p(description, class_name="text-sm text-gray-500 mt-1"),
            class_name="flex-1",
        ),
        rx.el.div(
            rx.cond(
                status,
                rx.el.span(
                    "Completado",
                    class_name="bg-green-100 text-green-800 text-xs font-medium px-2.5 py-0.5 rounded-full",
                ),
                rx.cond(
                    locked,
                    rx.el.span(
                        "Bloqueado",
                        class_name="bg-gray-100 text-gray-800 text-xs font-medium px-2.5 py-0.5 rounded-full",
                    ),
                    rx.el.span(
                        "Pendiente",
                        class_name="bg-yellow-100 text-yellow-800 text-xs font-medium px-2.5 py-0.5 rounded-full",
                    ),
                ),
            ),
            class_name="mt-4",
        ),
        rx.cond(
            locked,
            rx.el.button(
                "Bloqueado",
                disabled=True,
                class_name="mt-4 w-full py-2 bg-gray-200 text-gray-400 rounded-lg cursor-not-allowed",
            ),
            rx.el.a(
                rx.el.button(
                    rx.cond(~status, "Ir al Formulario", "Ver/Editar"),
                    class_name=f"mt-4 w-full py-2 rounded-lg transition-colors {rx.cond(status, 'bg-green-600 hover:bg-green-700 text-white', 'bg-blue-600 hover:bg-blue-700 text-white')}",
                ),
                href=url,
            ),
        ),
        class_name="bg-white p-6 rounded-xl border shadow-sm hover:shadow-md transition-shadow flex flex-col",
    )


def dashboard_page() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.main(
            rx.el.div(
                rx.el.h1(
                    "Dashboard de Evaluación",
                    class_name="text-2xl font-bold text-gray-900 mb-2",
                ),
                rx.el.p(
                    "Gestione sus evaluaciones de riesgo psicosocial.",
                    class_name="text-gray-600 mb-8",
                ),
                rx.el.div(
                    status_card(
                        "Datos Generales",
                        "Información demográfica básica.",
                        DashboardState.datos_generales_done,
                        "/datos-generales",
                        False,
                    ),
                    status_card(
                        "Cuestionario Forma A",
                        "Para jefes y profesionales.",
                        DashboardState.forma_a_done,
                        "/forma-a",
                        rx.cond(DashboardState.datos_generales_done, False, True),
                    ),
                    status_card(
                        "Cuestionario Forma B",
                        "Para personal operativo.",
                        DashboardState.forma_b_done,
                        "/forma-b",
                        rx.cond(DashboardState.datos_generales_done, False, True),
                    ),
                    status_card(
                        "Cuestionario Extralaboral",
                        "Condiciones fuera del trabajo.",
                        DashboardState.extralaboral_done,
                        "/extralaboral",
                        rx.cond(DashboardState.datos_generales_done, False, True),
                    ),
                    status_card(
                        "Evaluación de Estrés",
                        "Síntomas y nivel de estrés.",
                        DashboardState.estres_done,
                        "/estres",
                        rx.cond(DashboardState.datos_generales_done, False, True),
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6",
                ),
                class_name="max-w-6xl mx-auto",
            ),
            class_name="md:ml-64 min-h-screen bg-gray-50 p-8",
        ),
        class_name="font-['Inter']",
        on_mount=DashboardState.on_load,
    )