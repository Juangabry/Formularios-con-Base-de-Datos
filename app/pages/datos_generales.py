import reflex as rx
from app.states.datos_generales_state import DatosGeneralesState
from app.components.sidebar import sidebar
from app.components.form_components import form_layout


def datos_generales_page() -> rx.Component:
    form_content = rx.el.div(
        rx.el.div(
            rx.el.label(
                "Nombre Completo",
                class_name="block text-sm font-medium text-gray-700 mb-1",
            ),
            rx.el.input(
                on_change=DatosGeneralesState.set_full_name,
                class_name="w-full p-2 border rounded-lg",
                default_value=DatosGeneralesState.full_name,
            ),
            class_name="mb-4",
        ),
        rx.el.div(
            rx.el.label(
                "Edad", class_name="block text-sm font-medium text-gray-700 mb-1"
            ),
            rx.el.input(
                type="number",
                on_change=DatosGeneralesState.set_age,
                class_name="w-full p-2 border rounded-lg",
                default_value=DatosGeneralesState.age,
            ),
            class_name="mb-4",
        ),
        rx.el.div(
            rx.el.label(
                "Género", class_name="block text-sm font-medium text-gray-700 mb-1"
            ),
            rx.el.select(
                rx.el.option("Seleccionar...", value=""),
                rx.el.option("Masculino", value="M"),
                rx.el.option("Femenino", value="F"),
                value=DatosGeneralesState.gender,
                on_change=DatosGeneralesState.set_gender,
                class_name="w-full p-2 border rounded-lg",
            ),
            class_name="mb-4",
        ),
        rx.el.div(
            rx.el.label(
                "Cargo", class_name="block text-sm font-medium text-gray-700 mb-1"
            ),
            rx.el.input(
                on_change=DatosGeneralesState.set_position,
                class_name="w-full p-2 border rounded-lg",
                default_value=DatosGeneralesState.position,
            ),
            class_name="mb-4",
        ),
        rx.el.div(
            rx.el.label(
                "Departamento",
                class_name="block text-sm font-medium text-gray-700 mb-1",
            ),
            rx.el.input(
                on_change=DatosGeneralesState.set_department,
                class_name="w-full p-2 border rounded-lg",
                default_value=DatosGeneralesState.department,
            ),
            class_name="mb-6",
        ),
        rx.el.div(
            rx.el.label(
                "Sugerencias / Comentarios",
                class_name="block text-sm font-medium text-gray-700 mb-1",
            ),
            rx.el.textarea(
                on_change=DatosGeneralesState.set_sugerencias,
                class_name="w-full p-2 border rounded-lg h-24",
                default_value=DatosGeneralesState.sugerencias,
            ),
            class_name="mb-8",
        ),
        rx.el.button(
            "Guardar Datos Generales",
            on_click=DatosGeneralesState.submit,
            class_name="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 font-semibold",
        ),
    )
    return form_layout("Ficha de Datos Generales", form_content, sidebar())