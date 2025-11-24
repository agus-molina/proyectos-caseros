from dash import Input, Output
from visualizacion.procesamiento import ordPosiciones, infoFila, crearFila

def registrar_callbacks(app, telemetria):

    @app.callback(
        Output("nombre-evento", "children"),
        Output("nombre-circuito", "children"),
        Input("update-interval", "n_intervals")
    )
    def actualizar_titulos(_):
        return telemetria["nombreEvento"], telemetria["circuito"]

    @app.callback(
        Output("tabla-body", "children"),
        Input("update-interval", "n_intervals")
    )
    def actualizar_tabla(_):

        ultimoTiming = telemetria["estadoConductores"]
        if not ultimoTiming:
            return []

        if not telemetria["DriverList"]:
            return []

        lista_conductores = [
            elem for elem in telemetria["DriverList"] if isinstance(elem, dict)
        ]

        conductores = {
            elem["RacingNumber"]: elem for elem in lista_conductores
        }

        filas = []
        for driver_id, timing in ordPosiciones(ultimoTiming):
            filas.append(crearFila(infoFila(driver_id, timing, conductores)))
        return filas
