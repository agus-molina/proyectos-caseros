from livef1.adapters.realtime_client import RealF1Client
from data.data_collections import telemetria

# Initialize client
client = RealF1Client(
    topics=["Heartbeat",
            "SessionInfo",
            "SessionData",
            "TimingDataF1",
            "DriverList",
            "TyreStintSeries"],
    log_file_name="./output.json"
)

def normalizar_datos(data):
    #Devuelve siempre una lista de diccionarios válida.
    if data is None:
        return []
    if isinstance(data, dict):
        return [data]
    if isinstance(data, list):
        # filtrar basura
        return [elem for elem in data if isinstance(elem, dict)]
    return []

# Define multiple handlers
@client.callback("Heartbeat")
async def handle_conn_health(records):
    # Estabilidad de la conexion
    conn_health = normalizar_datos(records.get("Heartbeat"))
    for record in conn_health:
        telemetria["Heartbeat"].append(record)
    if conn_health:
        print("HEARTBEAT OK:", telemetria["Heartbeat"])

@client.callback("SessionInfo")
async def handle_info_sesion(records):
    # Datos estaticos de la sesion
    info = normalizar_datos(records.get("SessionInfo"))
    for record in info:
        telemetria["nombreEvento"] = record.get("Meeting_Name", "")
        telemetria["circuito"] = record.get("Meeting_Circuit_ShortName", "")
        telemetria["SessionInfo"].append(record)

@client.callback("SessionData")
async def handle_session_status(records):
    # Monitorea estado de sesion
    session_status = normalizar_datos(records.get("SessionData"))
    for record in session_status:
        telemetria["SessionData"].append(record)

@client.callback("TimingDataF1")
async def handle_live_timing(records):
    # Datos analiticos de carrera en curso
    updates = normalizar_datos(records.get("TimingDataF1"))

    for record in updates:
        driver = record.get("DriverNo")
        if not driver:
            continue

        # merge incremental
        telemetria["estadoConductores"][driver] = {
            **telemetria["estadoConductores"].get(driver, {}),
            **record
        }

@client.callback("DriverList")
async def handle_drivers_list(records):
    # Lista estatica de corredores
    conductores = normalizar_datos(records.get("DriverList"))
    for record in conductores:
        telemetria["DriverList"].append(record)

@client.callback("TyreStintSeries")
async def handle_tyre_stints(records):
    # Historial de cambio de ruedas
    tyre_stints = normalizar_datos(records.get("TyreStintSeries"))
    for record in tyre_stints:
        telemetria["TyreStintSeries"].append(record)
