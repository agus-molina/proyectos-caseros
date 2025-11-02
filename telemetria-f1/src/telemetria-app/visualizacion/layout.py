from dash import html
import livef1

# Intentamos cargar los datos de una sesión
try:
    session = livef1.get_session(
        season=2024,
        meeting_identifier="Spa",
        session_identifier="Race"
    )
    data = session.get_data("Car_Data")

    # Convertimos los datos a texto legible
    data_text = str(data)[:1500]  # solo mostramos los primeros caracteres
except Exception as e:
    data_text = f"⚠️ Error al cargar datos: {e}"

# Layout del dashboard
layout = html.Div(
    style={"textAlign": "center", "marginTop": "50px", "fontFamily": "monospace"},
    children=[
        html.H1("🏎️ Telemetría F1 Dashboard", style={"color": "#d32f2f"}),
        html.P("Datos obtenidos de la API de LiveF1:"),
        html.Pre(data_text, style={
            "backgroundColor": "#f4f4f4",
            "padding": "10px",
            "textAlign": "left",
            "maxWidth": "80%",
            "margin": "auto",
            "borderRadius": "8px",
            "whiteSpace": "pre-wrap"
        }),
    ]
)