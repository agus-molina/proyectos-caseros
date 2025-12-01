from dash import html, dcc

def crear_layout():
    return html.Div(  
        style={
            "backgroundColor": "#15151E",
            "margin": "0px",
            "padding": "0px",
            "minHeight": "100vh",
            "overflow": "hidden",
        },
        children=[
            # Importación de la fuente
            html.Link(
                rel="stylesheet",
                href="https://fonts.googleapis.com/css2?family=Sansation:wght@300;400;700&display=swap"
            ),
            # ===== TITULO PRINCIPAL =====
            html.Div(
                style={
                    "width": "100%",
                    "backgroundColor": "#15151E",
                    "padding": "18px 0",
                    "boxSizing": "border-box",
                    "borderBottom": "2px solid #3A3A3A",
                    "borderTop": "2px solid #3A3A3A",
                    "textAlign": "center",
                },
                children=[
                    html.H1(
                        "TELEMETRÍA F1",
                        style={
                            "margin": "0",
                            "fontFamily": "Sansation, sans-serif",
                            "fontWeight": "900",
                            "letterSpacing": "1px",
                            "fontSize": "38px",
                            "color": "#FFFFFF",
                        }
                    )
                ]
            ),
            # ===== CONTENEDOR HEADER =====
            html.Div(
                style={
                    "width": "100%",
                    "backgroundColor": "#1C1C25",
                    "padding": "20px 25px",
                    "boxSizing": "border-box",
                },
                children=[
                    # ----- INFO DE CARRERA DINAMICA
                    html.Div(
                        style={
                            "display": "flex",
                            "justifyContent": "space-between",
                            "alignItems": "center",
                            "padding": "8px 0"
                        },
                        children=[
                            # ----- COLUMNA IZQUIERDA
                            html.Div(
                                children=[
                                    # ===== NOMBRE EVENTO =====
                                    html.H2(
                                        id="nombre-evento",
                                        style={
                                            "margin": "0 0 4px 0",
                                            "fontSize": "26px",
                                            "fontWeight": "800",
                                            "color": "#CCCCCC",
                                            "paddingBottom": "4px",
                                            "borderBottom": "3px solid #D00000",
                                            "display": "inline-block",
                                            "fontFamily": "Sansation, sans-serif"
                                        }
                                    ),
                                    # ===== NOMBRE CIRCUITO =====
                                    html.H4(
                                        id="nombre-circuito",
                                        style={
                                            "margin": "2px 0 0 0",
                                            "fontSize": "18px",
                                            "color": "#BEBEBE",
                                            "fontWeight": "400",
                                            "fontFamily": "Sansation, sans-serif"
                                        }
                                    )
                                ]
                            ),
                            # ----- COLUMNA CENTRAL VACIA
                            html.Div(style={"flex": "1"}),
                            # ----- COLUMNA DERECHA (HUD estado)
                            html.Div(
                                style={
                                    "backgroundColor": "#47464C",
                                    "padding": "12px 18px",
                                    "borderRadius": "10px",
                                    "minWidth": "180px",
                                    "color": "white",
                                    "fontFamily": "Sansation, sans-serif",
                                    "textAlign": "right",
                                    "boxShadow": "0 2px 8px rgba(0,0,0,0.35)",
                                },
                                children=[
                                    html.Div("ALL CLEAR",id="estado-carrera"),
                                    html.Div("-- / --", id="vueltas"),
                                    html.Div("Banderita", id="bandera-estado"), #bandera segun logo en carpeta public
                                ]
                            ),
                        ]
                    ),
                ]
            ),
            # ===== CONTENEDOR TABLA =====
            html.Div(
                style={
                    "maxWidth": "1600px",
                    "margin": "0 auto",
                    "padding": "10px 25px 10px 25px",
                    "minHeight": "100vh",
                    "boxSizing": "border-box",
                },
                children=[
                    # Intervalo de refresco
                    dcc.Interval(
                        id="update-interval",
                        interval=2000,
                        n_intervals=0
                    ),
                    # ===== TABLA =====
                    html.Div(
                        id="tabla-container",
                        style={"width": "100%", "margin": "auto", "overflowX": "auto"},
                        children=[
                            html.Table(
                                id="telemetry-table",
                                style={
                                    "width": "100%",
                                    "borderCollapse": "collapse",
                                    "marginTop": "10px",
                                    "backgroundColor": "#000000",
                                    "color": "white",
                                    "border": "1px solid #222",
                                    "borderRadius": "8px",
                                    "overflow": "hidden",
                                    "textAlign": "center",
                                    "boxShadow": "0 4px 12px rgba(0,0,0,0.35)",
                                    "fontFamily": "Sansation, sans-serif",
                                },
                                children=[
                                    html.Thead(
                                        html.Tr([
                                            html.Th(""),
                                            html.Th("Posición"),
                                            html.Th("Piloto"),
                                            html.Th("Brecha"),
                                            html.Th("En Pits"),
                                            html.Th("Paradas"),
                                            html.Th("Vuelta"),
                                            html.Th("Sector 1"),
                                            html.Th("Sector 2"),
                                            html.Th("Sector 3"),
                                        ],
                                        style={
                                            "backgroundColor": "#000000",
                                            "color": "#BEBEBE",
                                            "textTransform": "uppercase",
                                            "letterSpacing": "1px",
                                            "fontSize": "12px",
                                            "height": "32px",
                                            "borderBottom": "2px solid #D00000",
                                        })
                                    ),
                                    html.Tbody(id="tabla-body")
                                ]
                            )
                        ]
                    )
                ]
            )
        ]
    )