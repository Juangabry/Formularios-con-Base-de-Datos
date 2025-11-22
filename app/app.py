import reflex as rx
import logging
from sqlmodel import SQLModel, create_engine, Session
from app.models import (
    User,
    DatosGenerales,
    FormaA,
    FormaB,
    Extralaboral,
    EvaluacionEstres,
)
from app.pages.login import login_page
from app.pages.registro import registro_page
from app.pages.dashboard import dashboard_page
from app.pages.datos_generales import datos_generales_page
from app.pages.forma_a import forma_a_page
from app.pages.forma_b import forma_b_page
from app.pages.extralaboral import extralaboral_page
from app.pages.estres import estres_page
from app.pages.results import results_page


def init_db():
    try:
        engine = rx.Model.get_db_engine()
        SQLModel.metadata.create_all(engine)
    except Exception as e:
        logging.exception(f"Error initializing database: {e}")


init_db()
app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(login_page, route="/")
app.add_page(registro_page, route="/registro")
app.add_page(dashboard_page, route="/dashboard")
app.add_page(datos_generales_page, route="/datos-generales")
app.add_page(forma_a_page, route="/forma-a")
app.add_page(forma_b_page, route="/forma-b")
app.add_page(extralaboral_page, route="/extralaboral")
app.add_page(estres_page, route="/estres")
app.add_page(results_page, route="/results")