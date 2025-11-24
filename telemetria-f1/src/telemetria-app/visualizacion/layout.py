from dash import html, dcc

def crear_layout():
    return html.Div(
        style={"margin": "40px"},
        children=[

            # ===== TÍTULOS =====
            html.H1(
                "🏎️ Telemetría F1",
                style={
                    "textAlign": "center",
                    "marginBottom": "10px",
                    "fontWeight": "900",
                    "letterSpacing": "2px",
                    "fontSize": "42px",
                    "color": "#0C0C0C",
                    "fontFamily": "Arial, sans-serif",
                }
            ),

            html.H2(
                id="nombre-evento",
                style={
                    "textAlign": "center",
                    "marginTop": "5px",
                    "marginBottom": "5px",
                    "fontSize": "32px",
                    "color": "#1d1d1d",
                    "textTransform": "uppercase",
                    "fontWeight": "700",
                    "borderBottom": "4px solid #D00000",
                    #"display": "inline-block",
                    "paddingBottom": "6px",
                    "letterSpacing": "1px",
                    "fontFamily": "Arial, sans-serif",
                }
            ),

            html.H4(
                id="nombre-circuito",
                style={
                    "textAlign": "center",
                    "marginTop": "5px",
                    "marginBottom": "25px",
                    "fontSize": "24px",
                    "color": "#2b2b2b",
                    "fontWeight": "500",
                    "letterSpacing": "0.5px",
                    "fontFamily": "Arial, sans-serif",
                }
            ),

            # Intervalo de actualización
            dcc.Interval(
                id="update-interval",
                interval=2000,
                n_intervals=0
            ),

            # ===== TABLA =====
            html.Div(
                id="tabla-container",
                style={"width": "85%", "margin": "auto", "overflowX": "auto"},
                children=[
                    html.Table(
                        id="telemetry-table",
                        style={
                            "width": "100%",
                            "borderCollapse": "collapse",
                            "marginTop": "20px",
                            "backgroundColor": "#131313",
                            "color": "white",
                            "fontFamily": "Arial, sans-serif",
                            "border": "1px solid #222",
                            "borderRadius": "8px",
                            "overflow": "hidden",
                            "textAlign": "center",
                        },
                        children=[

                            # ENCABEZADO
                            html.Thead(
                                html.Tr([
                                    html.Th(""),
                                    html.Th("Posición"),
                                    html.Th("Piloto"),
                                    html.Th("Dif. a Superior"),
                                    html.Th("Dif. al Líder"),
                                    html.Th("En Pits"),
                                    html.Th("Paradas"),
                                    html.Th("Últ. Vuelta"),
                                    html.Th("Mejor Vuelta"),
                                ], style={
                                    "backgroundColor": "#111",
                                    "color": "white",
                                    "textTransform": "uppercase",
                                    "letterSpacing": "0.5px",
                                    "fontSize": "13px",
                                    "height": "40px",
                                    "borderBottom": "2px solid #d00",
                                })
                            ),

                            # CUERPO DE LA TABLA
                            html.Tbody(id="tabla-body")
                        ]
                    )
                ]
            )
        ]
    )