"""
MODULO DE FUNCIONES AUXILIARES NECESARIAS PARA LOS CALLBACKS:

ordPosiciones() toma la ultima info de los conductores y los ordena por posicion.
Como el formato de los datos de la API puede no ser constante evalua segun campo 'Position',
sino 'Line' y si esa info no está todavia se da un nº arbitrariamente grande.

infoFila() usa el par devuelto por ordPosiciones de formato {'driver_id' : {timing de conductor}},
junto al diccionario mapeado de conductores de mismo formato pero con sus datos estaticos,
y los usa para armar el diccionario de la info a mostrar en pantalla

crearFila() toma esa info final y arma la estetica de la fila de la tabla
"""

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
        "Catching": eventoTiming.get("IntervalToPositionAhead_Catching", False),
        "GapToLeader": eventoTiming.get("GapToLeader", "--:---"),

        "LastLapTime": eventoTiming.get("LastLapTime_Value", "--:---"),
        "BestLapTime": eventoTiming.get("BestLapTime_Value", "--:---"),
        "PersonalFastest": eventoTiming.get("LastLapTime_PersonalFastest", False),
        "OverallFastest": eventoTiming.get("LastLapTime_OverallFastest", False),

        "S1_Value": eventoTiming.get("Sectors_1_Value", "--:---"),
        "S1_PersonalFastest": eventoTiming.get("Sectors_1_PersonalFastest", False),
        "S1_OverallFastest": eventoTiming.get("Sectors_1_OverallFastest", False),
        "S1_PreviousValue": eventoTiming.get("Sectors_1_PreviousValue", "--:---"),
        "S2_Value": eventoTiming.get("Sectors_2_Value", "--:---"),
        "S2_PersonalFastest": eventoTiming.get("Sectors_2_PersonalFastest", False),
        "S2_OverallFastest": eventoTiming.get("Sectors_2_OverallFastest", False),
        "S2_PreviousValue": eventoTiming.get("Sectors_2_PreviousValue", "--:---"),
        "S3_Value": eventoTiming.get("Sectors_3_Value", "--:---"),
        "S3_PersonalFastest": eventoTiming.get("Sectors_3_PersonalFastest", False),
        "S3_OverallFastest": eventoTiming.get("Sectors_3_OverallFastest", False),
        "S3_PreviousValue": eventoTiming.get("Sectors_3_PreviousValue", "--:---")
    }

def crearFila(info):

    # Fila grisada si el auto está retirado
    estilo_fila = {
        "opacity": 0.5 if info["retirado"] else 1,
        "height": "44px",
        "borderBottom": "1px solid #222",
    }

    estilo_estandar = {
        "padding": "6px",
    }

    estilo_mejora = {
        "color": "#12c43f",
    }

    estilo_superior = {
        "color": "#c412c4",
    }

    def formatoEstilo(es_mejor, es_superior):
        if es_superior:
            return estilo_superior
        elif es_mejor:
            return estilo_mejora
        else:
            return {}

    return html.Tr([
        # BANDA DE COLOR DEL EQUIPO (8px)
        html.Td("", style={
            "backgroundColor": f"#{info['color']}",
            "width": "8px",
            "padding": "0",
        }),

        html.Td(info["posicion"], style=estilo_estandar),
        html.Td(info["corredor"], style=estilo_estandar),
        html.Td([
            html.Div(info["IntervalToPositionAhead"],
                     style={"fontSize": "15px",
                            "fontWeight": "700",
                            "marginBottom": "2px",
                            **formatoEstilo(info["Catching"],{})
                    }),
            html.Div(info["GapToLeader"],
                     style={"fontSize": "11px",
                            "opacity": 0.75
                    }),
        ], style=estilo_estandar),
        html.Td("PIT" if info["enPits"] else "OUT", style=estilo_estandar),
        html.Td(info["paradasPits"], style=estilo_estandar),
        html.Td([
            html.Div(info["LastLapTime"],
                     style={"fontSize": "15px",
                            "fontWeight": "700",
                            **formatoEstilo(info["PersonalFastest"], info["OverallFastest"])
                    }),
            html.Div(info["BestLapTime"],
                     style={"fontSize": "11px",
                            **formatoEstilo({}, info["OverallFastest"])
                    }),
        ], style=estilo_estandar),
        html.Td(info["S1_Value"]), #Despues quiero valor reciente a la izquiera mas grande y antiguo a la derecha mas chiquito y gris
        html.Td(info["S2_Value"]),
        html.Td(info["S3_Value"])
    ], style=estilo_fila)
