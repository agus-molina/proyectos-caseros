from dash import html, dcc, dash_table

def crear_layout(nombre_evento: str, circuito: str):
    return html.Div(
        style={"margin": "40px"},
        children=[
            html.H1("🏎️ Telemetría F1 (Mock Real-Time)", style={"textAlign": "center"}),
            html.H4(f"{nombre_evento} — {circuito}", style={"textAlign": "center"}),

            dcc.Interval(id="update-interval", interval=2000, n_intervals=0),

            dash_table.DataTable(
                id="telemetry-table",
                columns=[
                    {"name": "Pos", "id": "Position"},
                    {"name": "Auto", "id": "Driver"},
                    {"name": "Gap Líder", "id": "GapToLeader"},
                    {"name": "Últ. Vuelta", "id": "LastLapTime"},
                    {"name": "Mejor Vuelta", "id": "BestLapTime"},
                ],
                style_table={"width": "80%", "margin": "auto"},
                style_cell={"textAlign": "center"},
                style_header={"backgroundColor": "#111", "color": "white"},
                style_data={"backgroundColor": "#222", "color": "white"},
                page_size=20,
            )
        ]
    )