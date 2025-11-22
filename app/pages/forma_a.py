import reflex as rx
from app.states.forma_a_state import FormaAState
from app.components.sidebar import sidebar
from app.components.form_components import form_layout, likert_question


def forma_a_page() -> rx.Component:
    form_content = rx.el.div(
        rx.el.p(
            "Responda las siguientes preguntas usando la escala de 1 (Nunca) a 5 (Siempre).",
            class_name="mb-6 text-gray-600 italic",
        ),
        likert_question(
            "1. ¿Su trabajo le exige hacer mucho esfuerzo físico?",
            FormaAState.q1,
            FormaAState.set_q1,
        ),
        likert_question(
            "2. ¿Tiene que trabajar en posiciones incómodas?",
            FormaAState.q2,
            FormaAState.set_q2,
        ),
        likert_question(
            "3. ¿Su trabajo requiere mucha concentración?",
            FormaAState.q3,
            FormaAState.set_q3,
        ),
        likert_question(
            "4. ¿Tiene que memorizar mucha información?",
            FormaAState.q4,
            FormaAState.set_q4,
        ),
        likert_question(
            "5. ¿Debe atender a muchos clientes o usuarios?",
            FormaAState.q5,
            FormaAState.set_q5,
        ),
        rx.el.div(
            rx.el.label(
                "Sugerencias / Observaciones sobre el cuestionario",
                class_name="block text-sm font-medium text-gray-700 mb-1",
            ),
            rx.el.textarea(
                on_change=FormaAState.update_sugerencias,
                class_name="w-full p-2 border rounded-lg h-24",
                default_value=FormaAState.sugerencias,
            ),
            class_name="mb-8",
        ),
        rx.el.button(
            "Guardar Forma A",
            on_click=FormaAState.submit,
            class_name="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 font-semibold",
        ),
    )
    return form_layout("Cuestionario Forma A", form_content, sidebar())