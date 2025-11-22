import reflex as rx
import logging
from sqlmodel import SQLModel
from app.pages.index import index
from app.components.auth import auth_page_component
from app.states.auth_state import AuthState
from app.states.dashboard_state import DashboardState
from app.pages.forms import (
    datos_generales_page,
    forma_a_page,
    forma_b_page,
    extralaboral_page,
    estres_page,
)
from app.models import (
    User,
    DatosGenerales,
    FormaA,
    FormaB,
    Extralaboral,
    EvaluacionEstres,
)
from app.pages.results import results_page
from app.states.results_state import ResultsState


def protected_page(component: rx.Component):
    return rx.fragment(rx.cond(AuthState.user, component, rx.el.div()))


def protected_index():
    return protected_page(index())


try:
    SQLModel.metadata.create_all(rx.model.get_engine())
except Exception as e:
    logging.exception(f"Database initialization error: {e}")
app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(auth_page_component, route="/login")
app.add_page(
    protected_index,
    route="/",
    on_load=[AuthState.check_auth, DashboardState.load_progress],
)
app.add_page(
    lambda: protected_page(datos_generales_page()),
    route="/form/datos-generales",
    on_load=AuthState.check_auth,
)
app.add_page(
    lambda: protected_page(forma_a_page()),
    route="/form/forma-a",
    on_load=AuthState.check_auth,
)
app.add_page(
    lambda: protected_page(forma_b_page()),
    route="/form/forma-b",
    on_load=AuthState.check_auth,
)
app.add_page(
    lambda: protected_page(extralaboral_page()),
    route="/form/extralaboral",
    on_load=AuthState.check_auth,
)
app.add_page(
    lambda: protected_page(estres_page()),
    route="/form/estres",
    on_load=AuthState.check_auth,
)
app.add_page(
    lambda: protected_page(results_page()),
    route="/results",
    on_load=[AuthState.check_auth, ResultsState.load_stats],
)