import reflex as rx
from app.states.results_state import ResultsState
from app.components.sidebar import sidebar
from app.states.auth_state import AuthState

TOOLTIP_PROPS = {
    "content_style": {
        "background": "white",
        "borderColor": "#E8E8E8",
        "borderRadius": "0.75rem",
        "boxShadow": "0px 24px 12px 0px light-dark(rgba(28, 32, 36, 0.02), rgba(0, 0, 0, 0.00)), 0px 8px 8px 0px light-dark(rgba(28, 32, 36, 0.02), rgba(0, 0, 0, 0.00)), 0px 2px 6px 0px light-dark(rgba(28, 32, 36, 0.02), rgba(0, 0, 0, 0.00))",
        "fontFamily": "sans-serif",
        "fontSize": "0.875rem",
        "lineHeight": "1.25rem",
        "fontWeight": "500",
        "minWidth": "8rem",
        "padding": "0.375rem 0.625rem",
        "position": "relative",
    },
    "item_style": {
        "display": "flex",
        "paddingBottom": "0px",
        "position": "relative",
        "paddingTop": "2px",
    },
    "label_style": {"color": "black", "fontWeight": "500", "alignSelf": "flex-end"},
    "separator": "",
}


def stat_card(title: str, value: int | str, icon: str, color: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon(icon, class_name=f"w-6 h-6 text-{color}-600"),
                class_name=f"p-3 bg-{color}-100 rounded-lg",
            ),
            rx.el.div(
                rx.el.p(title, class_name="text-sm text-gray-500 font-medium"),
                rx.el.p(value, class_name="text-2xl font-bold text-gray-900"),
            ),
            class_name="flex items-center gap-4",
        ),
        class_name="bg-white p-6 rounded-xl border border-gray-200 shadow-sm",
    )


def tutorial_card() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(
                "Interpretación de Resultados",
                class_name="text-lg font-semibold text-gray-800 mb-4 flex items-center",
            ),
            rx.el.p(
                "Esta sección presenta un resumen estadístico de sus respuestas en los diferentes formularios de la batería de riesgo psicosocial. Aquí podrá visualizar:",
                class_name="text-gray-600 mb-4",
            ),
            rx.el.ul(
                rx.el.li(
                    "El progreso general de diligenciamiento de los instrumentos.",
                    class_name="mb-2 flex items-center before:content-['•'] before:mr-2 before:text-indigo-500",
                ),
                rx.el.li(
                    "La distribución de sus respuestas por escala (Siempre, Casi siempre, etc.).",
                    class_name="mb-2 flex items-center before:content-['•'] before:mr-2 before:text-indigo-500",
                ),
                rx.el.li(
                    "Indicadores de completitud por cada formulario específico.",
                    class_name="mb-2 flex items-center before:content-['•'] before:mr-2 before:text-indigo-500",
                ),
                class_name="text-sm text-gray-600 bg-indigo-50 p-4 rounded-lg",
            ),
            rx.el.p(
                "Recuerde que este tablero es informativo. El diagnóstico y análisis detallado de riesgo psicosocial será realizado por profesionales especializados basándose en sus respuestas completas.",
                class_name="text-xs text-gray-500 mt-4 italic",
            ),
            class_name="p-6",
        ),
        class_name="bg-white rounded-xl border border-gray-200 shadow-sm mb-8",
    )


def results_page():
    return rx.fragment(
        rx.el.div(
            sidebar(),
            rx.el.main(
                rx.el.header(
                    rx.el.div(
                        rx.el.h1(
                            "Resultados y Estadísticas",
                            class_name="text-2xl font-bold text-gray-800",
                        ),
                        rx.el.div(
                            rx.el.span(
                                f"User: {AuthState.user['username']}",
                                class_name="text-sm font-medium text-gray-600 mr-4",
                            ),
                            class_name="flex items-center",
                        ),
                        class_name="flex justify-between items-center mb-8",
                    ),
                    class_name="mb-8",
                ),
                rx.el.div(
                    rx.el.div(
                        tutorial_card(),
                        rx.el.div(
                            stat_card(
                                "Formularios Completados",
                                ResultsState.completed_forms_count,
                                "check_check",
                                "green",
                            ),
                            stat_card(
                                "Preguntas Respondidas",
                                ResultsState.total_questions_answered,
                                "list-checks",
                                "blue",
                            ),
                            class_name="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8",
                        ),
                        class_name="col-span-1 lg:col-span-2",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.h3(
                                "Distribución de Respuestas",
                                class_name="text-lg font-semibold text-gray-800 mb-6",
                            ),
                            rx.recharts.bar_chart(
                                rx.recharts.cartesian_grid(
                                    horizontal=True,
                                    vertical=False,
                                    class_name="opacity-25",
                                ),
                                rx.recharts.graphing_tooltip(**TOOLTIP_PROPS),
                                rx.recharts.bar(
                                    data_key="value",
                                    fill="#4F46E5",
                                    bar_size=40,
                                    radius=[4, 4, 0, 0],
                                ),
                                rx.recharts.x_axis(
                                    data_key="name",
                                    axis_line=False,
                                    tick_line=False,
                                    custom_attrs={"fontSize": "12px"},
                                ),
                                rx.recharts.y_axis(
                                    axis_line=False,
                                    tick_line=False,
                                    custom_attrs={"fontSize": "12px"},
                                ),
                                data=ResultsState.response_distribution,
                                width="100%",
                                height=300,
                            ),
                            class_name="bg-white p-6 rounded-xl border border-gray-200 shadow-sm h-full",
                        ),
                        class_name="col-span-1 lg:col-span-3",
                    ),
                    class_name="grid grid-cols-1 lg:grid-cols-5 gap-8 mb-8",
                ),
                rx.el.div(
                    rx.el.h3(
                        "Progreso por Instrumento",
                        class_name="text-lg font-semibold text-gray-800 mb-6",
                    ),
                    rx.recharts.area_chart(
                        rx.recharts.cartesian_grid(
                            horizontal=True, vertical=False, class_name="opacity-25"
                        ),
                        rx.recharts.graphing_tooltip(**TOOLTIP_PROPS),
                        rx.recharts.area(
                            data_key="progress",
                            stroke="#8B5CF6",
                            fill="#8B5CF6",
                            fill_opacity=0.2,
                        ),
                        rx.recharts.x_axis(
                            data_key="name",
                            axis_line=False,
                            tick_line=False,
                            custom_attrs={"fontSize": "12px"},
                        ),
                        rx.recharts.y_axis(
                            axis_line=False,
                            tick_line=False,
                            custom_attrs={"fontSize": "12px"},
                            domain=[0, 100],
                        ),
                        data=ResultsState.completion_data,
                        width="100%",
                        height=300,
                        margin={"left": 0, "right": 0, "top": 10, "bottom": 0},
                    ),
                    class_name="bg-white p-6 rounded-xl border border-gray-200 shadow-sm",
                ),
                class_name="md:ml-64 p-8 min-h-screen bg-gray-50",
            ),
            class_name="min-h-screen font-['Inter']",
        ),
        on_mount=ResultsState.load_stats,
    )