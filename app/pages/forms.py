import reflex as rx
from app.components.sidebar import sidebar
from app.states.auth_state import AuthState
from app.states.form_states import (
    DatosGeneralesState,
    FormaAState,
    FormaBState,
    ExtralaboralState,
    EstresState,
)


def form_layout(title: str, content: rx.Component) -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.main(
            rx.el.header(
                rx.el.div(
                    rx.el.h1(title, class_name="text-2xl font-bold text-gray-800"),
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
                id="form-top",
            ),
            rx.el.div(content, class_name="max-w-4xl mx-auto"),
            class_name="md:ml-64 p-8 min-h-screen bg-gray-50",
        ),
        class_name="min-h-screen font-['Inter']",
    )


def input_field(label: str, key: str, placeholder: str = "") -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="block text-sm font-medium text-gray-700 mb-1"),
        rx.el.input(
            placeholder=placeholder,
            on_change=lambda val: DatosGeneralesState.update_field(key, val),
            class_name="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent outline-none",
            default_value=DatosGeneralesState.responses[key],
        ),
        class_name="mb-4",
    )


def select_field(label: str, key: str, options: list[str]) -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="block text-sm font-medium text-gray-700 mb-1"),
        rx.el.select(
            rx.el.option(
                "Seleccione una opción", value="", disabled=True, selected=True
            ),
            rx.foreach(options, lambda opt: rx.el.option(opt, value=opt)),
            value=DatosGeneralesState.responses[key],
            on_change=lambda val: DatosGeneralesState.update_field(key, val),
            class_name="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent outline-none bg-white",
        ),
        class_name="mb-4",
    )


def suggestions_section(state_class) -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Comentarios y Sugerencias",
            class_name="text-lg font-semibold text-gray-800 mb-4",
        ),
        rx.el.p(
            "Si tiene alguna observación adicional o sugerencia sobre este formulario, por favor escríbala a continuación:",
            class_name="text-sm text-gray-600 mb-4",
        ),
        rx.el.textarea(
            placeholder="Escriba sus comentarios aquí...",
            on_change=state_class.set_sugerencias,
            class_name="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent outline-none min-h-[120px] resize-y",
            default_value=state_class.sugerencias,
        ),
        class_name="bg-white p-8 rounded-xl border border-gray-200 shadow-sm mb-6 mt-6",
    )


def datos_generales_page():
    return rx.fragment(
        rx.script("window.scrollTo(0, 0);"),
        form_layout(
            "Datos Generales",
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Información Personal y Laboral",
                        class_name="text-xl font-semibold text-gray-800 mb-6",
                    ),
                    rx.el.div(
                        input_field("Nombre Completo", "nombre", "Juan Pérez"),
                        input_field("Edad", "edad", "30"),
                        select_field("Sexo", "sexo", ["Masculino", "Femenino"]),
                        select_field(
                            "Estado Civil",
                            "estado_civil",
                            [
                                "Soltero/a",
                                "Casado/a",
                                "Unión Libre",
                                "Separado/a",
                                "Viudo/a",
                            ],
                        ),
                        select_field(
                            "Nivel Educativo",
                            "educacion",
                            [
                                "Primaria",
                                "Secundaria",
                                "Técnico",
                                "Tecnólogo",
                                "Profesional",
                                "Postgrado",
                            ],
                        ),
                        input_field("Cargo Actual", "cargo", "Analista"),
                        input_field("Área / Departamento", "area", "Sistemas"),
                        select_field(
                            "Tipo de Contrato",
                            "contrato",
                            [
                                "Fijo",
                                "Indefinido",
                                "Obra/Labor",
                                "Prestación de Servicios",
                            ],
                        ),
                        input_field("Antigüedad (años)", "antiguedad", "2"),
                        class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
                    ),
                    class_name="bg-white p-8 rounded-xl border border-gray-200 shadow-sm mb-6",
                ),
                suggestions_section(DatosGeneralesState),
                rx.el.button(
                    "Guardar y Continuar",
                    on_click=DatosGeneralesState.save_form,
                    class_name="w-full md:w-auto px-8 py-3 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition-colors font-medium shadow-sm",
                ),
                class_name="pb-12",
            ),
        ),
        on_mount=DatosGeneralesState.load_data,
    )


LIKERT_OPTIONS = ["Siempre", "Casi siempre", "Algunas veces", "Casi nunca", "Nunca"]


def likert_question(index: int, text: str, state_class) -> rx.Component:
    key = f"q{index}"
    return rx.el.div(
        rx.el.p(
            f"{index}. {text}", class_name="text-sm font-medium text-gray-800 mb-2"
        ),
        rx.el.select(
            rx.el.option("Seleccione...", value="", disabled=True),
            rx.foreach(LIKERT_OPTIONS, lambda opt: rx.el.option(opt, value=opt)),
            value=state_class.responses[key],
            on_change=lambda val: state_class.set_answer(key, val),
            class_name="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none text-sm bg-white",
        ),
        class_name="bg-white p-4 rounded-lg border border-gray-100 hover:border-indigo-100 transition-colors",
    )


def likert_page_content(
    questions: list[str], start_index: int, state_class
) -> rx.Component:
    return rx.el.div(
        rx.foreach(
            questions, lambda q, i: likert_question(start_index + i, q, state_class)
        ),
        class_name="space-y-4 grid gap-4",
    )


def navigation_buttons(state_class) -> rx.Component:
    return rx.el.div(
        rx.cond(
            state_class.page > 1,
            rx.el.button(
                "Anterior",
                on_click=state_class.prev_page,
                class_name="px-6 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-colors font-medium",
            ),
            rx.el.div(),
        ),
        rx.el.div(
            rx.el.span(
                f"Página {state_class.page} de {state_class.total_pages}",
                class_name="text-sm text-gray-500 font-medium mr-4",
            ),
            rx.cond(
                state_class.page < state_class.total_pages,
                rx.el.button(
                    "Siguiente",
                    on_click=state_class.next_page,
                    class_name="px-6 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition-colors font-medium",
                ),
                rx.el.div(
                    rx.el.button(
                        "Guardar progreso",
                        on_click=state_class.save_progress,
                        class_name="px-4 py-2 text-indigo-600 hover:bg-indigo-50 rounded-lg mr-2 text-sm font-medium transition-colors",
                    ),
                    rx.el.button(
                        "Guardar Formulario",
                        on_click=state_class.finish_form,
                        class_name="px-6 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition-colors font-medium shadow-sm",
                    ),
                    class_name="flex items-center",
                ),
            ),
            class_name="flex items-center",
        ),
        class_name="flex justify-between items-center mt-8 pt-6 border-t border-gray-200",
    )


FORMA_A_QUESTIONS = [
    f"Pregunta sobre liderazgo y condiciones laborales {i}" for i in range(1, 124)
]


def forma_a_page():
    return rx.fragment(
        rx.script("window.scrollTo(0, 0);"),
        form_layout(
            "Forma A - Cuestionario de Factores de Riesgo Psicosocial",
            rx.el.div(
                rx.cond(
                    FormaAState.page == 1,
                    likert_page_content(FORMA_A_QUESTIONS[0:30], 1, FormaAState),
                ),
                rx.cond(
                    FormaAState.page == 2,
                    likert_page_content(FORMA_A_QUESTIONS[30:60], 31, FormaAState),
                ),
                rx.cond(
                    FormaAState.page == 3,
                    rx.el.div(
                        likert_page_content(FORMA_A_QUESTIONS[60:123], 61, FormaAState),
                        suggestions_section(FormaAState),
                    ),
                ),
                navigation_buttons(FormaAState),
                class_name="pb-12",
            ),
        ),
        on_mount=FormaAState.load_data,
    )


FORMA_B_QUESTIONS = [f"Pregunta sobre condiciones laborales {i}" for i in range(1, 98)]


def forma_b_page():
    return rx.fragment(
        rx.script("window.scrollTo(0, 0);"),
        form_layout(
            "Forma B - Cuestionario de Factores de Riesgo Psicosocial",
            rx.el.div(
                rx.cond(
                    FormaBState.page == 1,
                    likert_page_content(FORMA_B_QUESTIONS[0:33], 1, FormaBState),
                ),
                rx.cond(
                    FormaBState.page == 2,
                    likert_page_content(FORMA_B_QUESTIONS[33:66], 34, FormaBState),
                ),
                rx.cond(
                    FormaBState.page == 3,
                    rx.el.div(
                        likert_page_content(FORMA_B_QUESTIONS[66:97], 67, FormaBState),
                        suggestions_section(FormaBState),
                    ),
                ),
                navigation_buttons(FormaBState),
                class_name="pb-12",
            ),
        ),
        on_mount=FormaBState.load_data,
    )


EXTRALABORAL_QUESTIONS = [
    f"Pregunta sobre condiciones extralaborales {i}" for i in range(1, 32)
]


def extralaboral_page():
    return rx.fragment(
        rx.script("window.scrollTo(0, 0);"),
        form_layout(
            "Cuestionario de Factores de Riesgo Psicosocial Extralaboral",
            rx.el.div(
                rx.cond(
                    ExtralaboralState.page == 1,
                    likert_page_content(
                        EXTRALABORAL_QUESTIONS[0:15], 1, ExtralaboralState
                    ),
                ),
                rx.cond(
                    ExtralaboralState.page == 2,
                    rx.el.div(
                        likert_page_content(
                            EXTRALABORAL_QUESTIONS[15:31], 16, ExtralaboralState
                        ),
                        suggestions_section(ExtralaboralState),
                    ),
                ),
                navigation_buttons(ExtralaboralState),
                class_name="pb-12",
            ),
        ),
        on_mount=ExtralaboralState.load_data,
    )


ESTRES_QUESTIONS = [f"Síntoma de estrés {i}" for i in range(1, 32)]


def estres_page():
    return rx.fragment(
        rx.script("window.scrollTo(0, 0);"),
        form_layout(
            "Evaluación de Estrés",
            rx.el.div(
                rx.cond(
                    EstresState.page == 1,
                    likert_page_content(ESTRES_QUESTIONS[0:15], 1, EstresState),
                ),
                rx.cond(
                    EstresState.page == 2,
                    rx.el.div(
                        likert_page_content(ESTRES_QUESTIONS[15:31], 16, EstresState),
                        suggestions_section(EstresState),
                    ),
                ),
                navigation_buttons(EstresState),
                class_name="pb-12",
            ),
        ),
        on_mount=EstresState.load_data,
    )