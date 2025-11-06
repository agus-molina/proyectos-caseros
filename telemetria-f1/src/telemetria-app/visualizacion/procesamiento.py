from dash import html
import json


def cargar_json(ruta="data/sample_telemetry.json"):
    """Carga los datos desde un archivo JSON local."""
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)


def generar_filas_telemetria(datos):
    """Crea las filas de la tabla Dash a partir de datos de telemetría."""
    drivers = []

    timing = datos.get("timingdata", {}).get("Lines", {})
    driverlist = datos.get("driverlist", {})

    for num, info in timing.items():
        pos = int(info.get("Position", 999))
        driver_info = driverlist.get(num, {})
        sectores = info.get("Sectors", [])

        def sec(i):
            try:
                s = sectores[i]
                return {
                    "Value": s.get("Value", "-"),
                    "PersonalFastest": s.get("PersonalFastest", False),
                    "OverallFastest": s.get("OverallFastest", False)
                }
            except IndexError:
                return {"Value": "-", "PersonalFastest": False, "OverallFastest": False}

        s1, s2, s3 = sec(0), sec(1), sec(2)

        drivers.append({
            "Position": pos,
            "RacingNumber": num,
            "Driver": driver_info.get("BroadcastName", "N/A"),
            "TeamName": driver_info.get("TeamName", ""),
            "TeamColour": f"#{driver_info.get('TeamColour', 'FFFFFF')}",
            "IntervalToPositionAhead": info.get("IntervalToPositionAhead", {}).get("Value", "-"),
            "Catching": info.get("IntervalToPositionAhead", {}).get("Catching", False),
            "GapToLeader": info.get("GapToLeader", "-"),
            "LastLapTime": info.get("LastLapTime", {}).get("Value", "-"),
            "BestLapTime": info.get("BestLapTime", {}).get("Value", "-"),
            "PersonalFastest": info.get("LastLapTime", {}).get("PersonalFastest", False),
            "OverallFastest": info.get("LastLapTime", {}).get("OverallFastest", False),
            "Retired": info.get("Retired", False),
            "S1": s1,
            "S2": s2,
            "S3": s3
        })

    drivers.sort(key=lambda x: x["Position"])

    def color_sector(s):
        if s["OverallFastest"]:
            return "#AA00FF"  # violeta brillante
        elif s["PersonalFastest"]:
            return "#00FF00"  # verde brillante
        return "#FFF"

    def estilo_fila(d):
        if d["Retired"]:
            return {"backgroundColor": "#333", "color": "#777"}
        return {"backgroundColor": "#111", "color": "#FFF"}

    filas = []
    for d in drivers:
        catching_color = "#00FF00" if d["Catching"] else "#FFF"
        lap_color = "#00FF00" if d["PersonalFastest"] else "#AA00FF" if d["OverallFastest"] else "#FFF"

        fila = html.Tr(
            style=estilo_fila(d),
            children=[
                html.Td(d["Position"]),
                html.Td(d["RacingNumber"]),
                html.Td(d["Driver"]),
                html.Td(d["TeamName"], style={"color": d["TeamColour"]}),
                html.Td(html.Div([
                    html.Span(d["IntervalToPositionAhead"], style={"color": catching_color}),
                    html.Br(),
                    html.Small(d["GapToLeader"])
                ])),
                html.Td(html.Div([
                    html.Span(d["LastLapTime"], style={"color": lap_color}),
                    html.Br(),
                    html.Small(d["BestLapTime"])
                ])),
                html.Td(html.Span(d["S1"]["Value"], style={"color": color_sector(d["S1"])})),
                html.Td(html.Span(d["S2"]["Value"], style={"color": color_sector(d["S2"])})),
                html.Td(html.Span(d["S3"]["Value"], style={"color": color_sector(d["S3"])})),
            ]
        )
        filas.append(fila)

    return filas