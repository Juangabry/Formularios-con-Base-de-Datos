import reflex as rx
from app.states.dashboard_state import DashboardState
from app.components.sidebar import sidebar


def results_page() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.main(
            rx.el.div(
                rx.el.h1(
                    "Resultados y Tutorial",
                    class_name="text-2xl font-bold text-gray-900 mb-6",
                ),
                rx.el.div(
                    rx.el.h2(
                        "Tutorial de Interpretación",
                        class_name="text-xl font-semibold mb-4",
                    ),
                    rx.el.p(
                        "Los resultados se calcularán una vez completadas todas las baterías. A continuación se presenta una guía básica de interpretación:",
                        class_name="mb-4 text-gray-600",
                    ),
                    rx.el.ul(
                        rx.el.li("Puntajes 1-2: Riesgo Bajo o Nulo."),
                        rx.el.li("Puntajes 3: Riesgo Medio."),
                        rx.el.li("Puntajes 4-5: Riesgo Alto o Muy Alto."),
                        class_name="list-disc list-inside space-y-2 mb-6",
                    ),
                    class_name="bg-white p-6 rounded-xl shadow-sm border mb-8",
                ),
                rx.el.div(
                    rx.el.h2(
                        "Estado de sus Evaluaciones",
                        class_name="text-xl font-semibold mb-4",
                    ),
                    rx.el.div(
                        rx.el.p(
                            f"Datos Generales: {rx.cond(DashboardState.datos_generales_done, 'Completado', 'Pendiente')}"
                        ),
                        rx.el.p(
                            f"Forma A: {rx.cond(DashboardState.forma_a_done, 'Completado', 'Pendiente')}"
                        ),
                        rx.el.p(
                            f"Forma B: {rx.cond(DashboardState.forma_b_done, 'Completado', 'Pendiente')}"
                        ),
                        rx.el.p(
                            f"Extralaboral: {rx.cond(DashboardState.extralaboral_done, 'Completado', 'Pendiente')}"
                        ),
                        rx.el.p(
                            f"Estrés: {rx.cond(DashboardState.estres_done, 'Completado', 'Pendiente')}"
                        ),
                        class_name="space-y-2",
                    ),
                    class_name="bg-white p-6 rounded-xl shadow-sm border",
                ),
                class_name="max-w-4xl mx-auto",
            ),
            class_name="md:ml-64 min-h-screen bg-gray-50 p-8",
        ),
        class_name="font-['Inter']",
        on_mount=DashboardState.on_load,
    )