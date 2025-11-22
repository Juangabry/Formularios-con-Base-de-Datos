import reflex as rx


def likert_question(question_text: str, state_var, set_event) -> rx.Component:
    return rx.el.div(
        rx.el.p(question_text, class_name="mb-2 font-medium text-gray-700"),
        rx.el.div(
            rx.foreach(
                ["1", "2", "3", "4", "5"],
                lambda val: rx.el.label(
                    rx.el.input(
                        type="radio",
                        name=question_text,
                        value=val,
                        on_change=set_event,
                        checked=state_var.to_string() == val,
                        class_name="mr-2",
                    ),
                    rx.el.span(val),
                    class_name="flex items-center mr-4 cursor-pointer",
                ),
            ),
            class_name="flex flex-row flex-wrap gap-4",
        ),
        class_name="mb-6 p-4 bg-gray-50 rounded-lg",
    )


def form_layout(
    title: str, content: rx.Component, sidebar_component: rx.Component
) -> rx.Component:
    return rx.el.div(
        sidebar_component,
        rx.el.main(
            rx.el.div(
                rx.el.h1(title, class_name="text-2xl font-bold mb-6 text-gray-900"),
                content,
                class_name="max-w-4xl mx-auto bg-white p-8 rounded-xl shadow-sm border",
            ),
            class_name="md:ml-64 min-h-screen bg-gray-50 p-8",
        ),
        class_name="min-h-screen font-['Inter']",
    )