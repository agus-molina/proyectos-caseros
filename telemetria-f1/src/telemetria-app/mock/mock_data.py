import os, json
import random
import datetime
from copy import deepcopy

def cargar_json(nombre="sample_telemetry.json"):
    # 🔹 Subir un nivel desde /mock hasta /telemetria-app/
    base_dir = os.path.dirname(__file__)  
    ruta = os.path.join(base_dir, "..", "var_non_local", nombre)
    ruta = os.path.abspath(ruta)  # convierte a ruta absoluta
    
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)
    
datos = cargar_json()


def generar_mock_timing_data():
    """Genera una copia del timingdata con pequeñas variaciones en los tiempos."""
    td = deepcopy(datos[2])

    # Lista de pilotos activos
    active_drivers = [
        (int(d["Position"]), driver_id)
        for driver_id, d in td["Lines"].items()
        if not d.get("Retired")
    ]
    active_drivers.sort()  # ordenar por posición

    # 🔹 Simular cambios aleatorios de posición (intercambio)
    if len(active_drivers) > 3 and random.random() < 0.3:  # 30% de probabilidad
        i = random.randint(0, len(active_drivers) - 2)
        j = i + 1
        active_drivers[i], active_drivers[j] = active_drivers[j], active_drivers[i]

        # Reasignar las posiciones
        for pos, (_, driver_id) in enumerate(active_drivers, start=1):
            td["Lines"][driver_id]["Position"] = str(pos)

    # 🔹 Variar los tiempos y sectores
    for driver_id, d in td["Lines"].items():
        if d.get("Retired"):
            continue

        try:
            last_lap = d["LastLapTime"]["Value"]
            min_, sec = last_lap.split(":")
            new_time = float(sec) + random.uniform(-0.300, 0.300)
            d["LastLapTime"]["Value"] = f"{min_}:{new_time:.3f}"
        except Exception:
            d["LastLapTime"]["Value"] = "1:22.000"

        # Flags aleatorios de fastest laps
        d["LastLapTime"]["PersonalFastest"] = random.random() < 0.05
        d["LastLapTime"]["OverallFastest"] = random.random() < 0.01

        # Sectors con pequeñas variaciones
        for s in d.get("Sectors", []):
            try:
                s["Value"] = f"{float(s['Value']) + random.uniform(-0.050, 0.050):.3f}"
                s["PersonalFastest"] = random.random() < 0.05
                s["OverallFastest"] = random.random() < 0.01
            except Exception:
                continue

        # Variar intervalos
        if "IntervalToPositionAhead" in d:
            try:
                val = d["IntervalToPositionAhead"]["Value"]
                if val and val != "":
                    base = float(val.replace("+", ""))
                    d["IntervalToPositionAhead"]["Value"] = f"+{base + random.uniform(-0.2, 0.2):.3f}"
            except Exception:
                pass

    return td


def generar_mock_heartbeat():
    """Devuelve un heartbeat con timestamp actual."""
    return {"Utc": datetime.datetime.utcnow().isoformat() + "Z"}


def mock_update(telemetria):
    """
    Simula una actualización de datos en tiempo real.
    Crea un snapshot con todos los topics y lo agrega al deque.
    """
    snapshot = {
        "sessioninfo": deepcopy(datos[0]),
        "trackstatus": deepcopy(datos[1]),
        "timingdata": generar_mock_timing_data(),
        "driverlist": deepcopy(datos[3]),
        "heartbeat": generar_mock_heartbeat(),
    }

    telemetria.append(snapshot)
    return snapshot


def mock_loop(telemetria, iterations=10):
    """Ejecuta mock_update varias veces (útil para test manual)."""
    for _ in range(iterations):
        mock_update(telemetria)