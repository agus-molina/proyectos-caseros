import os
import json
import random
import datetime
from copy import deepcopy


# ======================================================
# 🔹 CARGA DE ARCHIVO BASE DE DATOS ESTÁTICOS
# ======================================================
def cargar_json(nombre="sample_telemetry.json"):
    """
    Carga el archivo JSON local de datos simulados.
    """
    base_dir = os.path.dirname(__file__)  # carpeta actual (/mock)
    ruta = os.path.join(base_dir, "..", "data", nombre)
    ruta = os.path.abspath(ruta)

    if not os.path.exists(ruta):
        raise FileNotFoundError(f"No se encontró el archivo JSON en: {ruta}")

    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)


# Carga inicial del JSON base (estructura completa)
datos = cargar_json()


# ======================================================
# 🔹 FUNCIONES DE MOCK POR TOPIC
# ======================================================
def generar_mock_timing_data():
    """Genera una copia del TimingData con pequeñas variaciones simuladas."""
    td = deepcopy(datos[2])  # índice 2 = TimingData

    # Lista de pilotos activos
    active_drivers = [
        (int(d["Position"]), driver_id)
        for driver_id, d in td["Lines"].items()
        if not d.get("Retired")
    ]
    active_drivers.sort()  # ordenar por posición

    # 🔹 Simular cambios aleatorios de posición
    if len(active_drivers) > 3 and random.random() < 0.3:
        i = random.randint(0, len(active_drivers) - 2)
        j = i + 1
        active_drivers[i], active_drivers[j] = active_drivers[j], active_drivers[i]

        # Reasignar posiciones actualizadas
        for pos, (_, driver_id) in enumerate(active_drivers, start=1):
            td["Lines"][driver_id]["Position"] = str(pos)

    # 🔹 Variar tiempos y sectores
    for driver_id, d in td["Lines"].items():
        if d.get("Retired"):
            continue

        # Última vuelta
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

        # Sectores
        for s in d.get("Sectors", []):
            try:
                s["Value"] = f"{float(s['Value']) + random.uniform(-0.050, 0.050):.3f}"
                s["PersonalFastest"] = random.random() < 0.05
                s["OverallFastest"] = random.random() < 0.01
            except Exception:
                continue

        # Intervalo con el piloto anterior
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
    """Devuelve un Heartbeat con timestamp actual."""
    return {"Utc": datetime.datetime.utcnow().isoformat() + "Z"}


# ======================================================
# 🔹 FUNCIÓN PRINCIPAL MOCK
# ======================================================
def mock_update(telemetria):
    """
    Simula una actualización de datos en tiempo real.
    Inserta los datos en cada topic del diccionario 'telemetria'.
    """
    telemetria["heartbeat"].append(generar_mock_heartbeat())
    telemetria["session_info"].append(deepcopy(datos[0]))      # SessionInfo
    telemetria["session_data"].append(deepcopy(datos[1]))      # TrackStatus / SessionData
    telemetria["live_timing"].append(generar_mock_timing_data())  # TimingDataF1
    telemetria["drivers_list"].append(deepcopy(datos[3]))       # DriverList
    # Podrías simular más adelante TyreStintSeries:
    # telemetria["tyre_series"].append(deepcopy(datos[4]))

    return telemetria


def mock_loop(telemetria, iterations=10, delay=2):
    """
    Ejecuta mock_update() varias veces para simular flujo en tiempo real.
    """
    import time
    for _ in range(iterations):
        mock_update(telemetria)
        time.sleep(delay)