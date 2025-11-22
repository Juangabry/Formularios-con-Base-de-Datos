import reflex as rx
from app.states.forma_b_state import FormaBState
from app.components.sidebar import sidebar
from app.components.form_components import form_layout, likert_question


def forma_b_page() -> rx.Component:
    form_content = rx.el.div(
        rx.el.p(
            "Responda las siguientes preguntas usando la escala de 1 (Nunca) a 5 (Siempre).",
            class_name="mb-6 text-gray-600 italic",
        ),
        likert_question(
            "1. ¿El ruido en su lugar de trabajo es molesto?",
            FormaBState.q1,
            FormaBState.set_q1,
        ),
        likert_question(
            "2. ¿Siente frío o calor extremo en su trabajo?",
            FormaBState.q2,
            FormaBState.set_q2,
        ),
        likert_question(
            "3. ¿El aire en su lugar de trabajo es fresco?",
            FormaBState.q3,
            FormaBState.set_q3,
        ),
        likert_question(
            "4. ¿La iluminación es adecuada para trabajar?",
            FormaBState.q4,
            FormaBState.set_q4,
        ),
        likert_question(
            "5. ¿Se siente seguro en su lugar de trabajo?",
            FormaBState.q5,
            FormaBState.set_q5,
        ),
        rx.el.div(
            rx.el.label(
                "Sugerencias / Observaciones sobre el cuestionario",
                class_name="block text-sm font-medium text-gray-700 mb-1",
            ),
            rx.el.textarea(
                on_change=FormaBState.update_sugerencias,
                class_name="w-full p-2 border rounded-lg h-24",
                default_value=FormaBState.sugerencias,
            ),
            class_name="mb-8",
        ),
        rx.el.button(
            "Guardar Forma B",
            on_click=FormaBState.submit,
            class_name="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 font-semibold",
        ),
    )
    return form_layout("Cuestionario Forma B", form_content, sidebar())