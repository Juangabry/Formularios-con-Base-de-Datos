import reflex as rx
from app.states.estres_state import EstresState
from app.components.sidebar import sidebar
from app.components.form_components import form_layout, likert_question


def estres_page() -> rx.Component:
    form_content = rx.el.div(
        rx.el.p(
            "Indique la frecuencia de los siguientes síntomas (1=Nunca, 5=Siempre).",
            class_name="mb-6 text-gray-600 italic",
        ),
        likert_question(
            "1. ¿Siente dolores de cabeza frecuentes?",
            EstresState.q1,
            EstresState.set_q1,
        ),
        likert_question(
            "2. ¿Tiene dificultades para dormir?", EstresState.q2, EstresState.set_q2
        ),
        likert_question(
            "3. ¿Se siente irritable o de mal genio?",
            EstresState.q3,
            EstresState.set_q3,
        ),
        likert_question(
            "4. ¿Siente cansancio excesivo?", EstresState.q4, EstresState.set_q4
        ),
        likert_question(
            "5. ¿Tiene problemas digestivos?", EstresState.q5, EstresState.set_q5
        ),
        rx.el.div(
            rx.el.label(
                "Sugerencias / Comentarios sobre su salud",
                class_name="block text-sm font-medium text-gray-700 mb-1",
            ),
            rx.el.textarea(
                on_change=EstresState.update_sugerencias,
                class_name="w-full p-2 border rounded-lg h-24",
                default_value=EstresState.sugerencias,
            ),
            class_name="mb-8",
        ),
        rx.el.button(
            "Guardar Evaluación de Estrés",
            on_click=EstresState.submit,
            class_name="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 font-semibold",
        ),
    )
    return form_layout("Evaluación de Estrés", form_content, sidebar())