import reflex as rx
from app.states.extralaboral_state import ExtralaboralState
from app.components.sidebar import sidebar
from app.components.form_components import form_layout, likert_question


def extralaboral_page() -> rx.Component:
    form_content = rx.el.div(
        rx.el.p(
            "Responda sobre su tiempo fuera del trabajo (1=Nunca, 5=Siempre).",
            class_name="mb-6 text-gray-600 italic",
        ),
        likert_question(
            "1. ¿Tiene tiempo suficiente para descansar?",
            ExtralaboralState.q1,
            ExtralaboralState.set_q1,
        ),
        likert_question(
            "2. ¿Comparte tiempo con su familia?",
            ExtralaboralState.q2,
            ExtralaboralState.set_q2,
        ),
        likert_question(
            "3. ¿Tiene buenas relaciones con sus vecinos?",
            ExtralaboralState.q3,
            ExtralaboralState.set_q3,
        ),
        likert_question(
            "4. ¿El transporte a su trabajo es fácil?",
            ExtralaboralState.q4,
            ExtralaboralState.set_q4,
        ),
        likert_question(
            "5. ¿Su situación económica es estable?",
            ExtralaboralState.q5,
            ExtralaboralState.set_q5,
        ),
        rx.el.div(
            rx.el.label(
                "Sugerencias / Observaciones personales",
                class_name="block text-sm font-medium text-gray-700 mb-1",
            ),
            rx.el.textarea(
                on_change=ExtralaboralState.update_sugerencias,
                class_name="w-full p-2 border rounded-lg h-24",
                default_value=ExtralaboralState.sugerencias,
            ),
            class_name="mb-8",
        ),
        rx.el.button(
            "Guardar Extralaboral",
            on_click=ExtralaboralState.submit,
            class_name="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 font-semibold",
        ),
    )
    return form_layout("Factores Extralaborales", form_content, sidebar())