from dash import html

def ordPosiciones(eventoTiming):
    return sorted(
        eventoTiming.items(),
        key=lambda item: int(item[1].get("Position", item[1].get("Line", 999)))
    )

def infoFila(driver_id, eventoTiming, conductores):
    datos_conductor = conductores.get(driver_id, {})
    return {
        "posicion": eventoTiming.get("Position", "--"),
        "corredor": datos_conductor.get("Tla", "---"),
        "color": datos_conductor.get("TeamColour", "FFFFFF"),

        "retirado": eventoTiming.get("Retired", False) or not eventoTiming.get("ShowPosition", True),
        "enPits": eventoTiming.get("InPit", False),
        "paradasPits": eventoTiming.get("NumberOfPitStops", 0),

        "IntervalToPositionAhead": eventoTiming.get("IntervalToPositionAhead_Value", "--:---"),
        "GapToLeader": eventoTiming.get("GapToLeader", "--:---"),

        "LastLapTime": eventoTiming.get("LastLapTime", {}).get("Value", "--:---"),
        "BestLapTime": eventoTiming.get("BestLapTime", {}).get("Value", "--:---"),
    }
    """return {
        "posicion": eventoTiming.get("Position", "--"),
        "corredor": datos_conductor.get("Tla", "---"),
        "color": datos_conductor.get("TeamColour", "FFFFFF"),
        "retirado": eventoTiming.get("Retired", False),
        "enPits": eventoTiming.get("InPit", False),
        "paradasPits": eventoTiming.get("NumberOfPitStops", 0),
        "IntervalToPositionAhead": eventoTiming.get("IntervalToPositionAhead", {}).get("Value", "-- ---"),
        "Catching": eventoTiming.get("IntervalToPositionAhead", {}).get("Catching", False),
        "GapToLeader": eventoTiming.get("GapToLeader", "-- ---"),
        "LastLapTime": eventoTiming.get("LastLapTime", {}).get("Value", "-- ---"),
        "BestLapTime": eventoTiming.get("BestLapTime", {}).get("Value", "-- ---"),
        "PersonalFastest": eventoTiming.get("LastLapTime", {}).get("PersonalFastest", False),
        "OverallFastest": eventoTiming.get("LastLapTime", {}).get("OverallFastest", False)
    }
"""
def crearFila(info):
    # Fila grisada si el auto está retirado
    estilo_fila = {
        "opacity": 0.5 if info["retirado"] else 1,
        "height": "38px",
        "borderBottom": "1px solid #222",
    }

    return html.Tr([
        # BANDA DE COLOR DEL EQUIPO (8px)
        html.Td("", style={
            "backgroundColor": f"#{info['color']}",
            "width": "8px",
            "padding": "0",
        }),

        html.Td(info["posicion"], style={"padding": "6px"}),
        html.Td(info["corredor"], style={"padding": "6px"}),
        html.Td(info["IntervalToPositionAhead"], style={"padding": "6px"}),
        html.Td(info["GapToLeader"], style={"padding": "6px"}),
        html.Td("PIT" if info["enPits"] else "OUT", style={"padding": "6px"}),
        html.Td(info["paradasPits"], style={"padding": "6px"}),
        html.Td(info["LastLapTime"], style={"padding": "6px"}),
        html.Td(info["BestLapTime"], style={"padding": "6px"}),
    ], style=estilo_fila)
