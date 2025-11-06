from livef1.adapters.realtime_client import RealF1Client
from data.data_collections import nombreEvento, circuito, telemetria
import datetime

"""
try:
    session = livef1.get_session(
        season=2024,
        meeting_identifier="Spa",
        session_identifier="Race"
    )
    data = session.get_data("Car_Data")
except Exception as e:
    print(f"Error loading data: {e}")
"""
# Initialize client
client = RealF1Client(
    topics=["Heartbeat", "SessionInfo", "SessionData", "TimingData", "DriverList", "TyreStintSeries"],
)

# Define multiple handlers
@client.callback("salud_conexion")
async def handle_conn_health(records):
    # Estabilidad de la conexion
    conn_health = records.get("Heartbeat")
    if conn_health:
        for record in conn_health:
            telemetria["heartbeat"].append(record)

@client.callback("info_sesion")
async def handle_info_sesion(records):
    # Datos estaticos de la sesion
    nombreEvento = records.get("SessionInfo", {}).get("Name", "")
    locacion = records.get("SessionInfo", {}).get("Circuit", {}).get("ShortName", "")     

@client.callback("sesion_status")
async def handle_track_status(records):
    # Monitorea estado de sesion
    session_status = records.get("SessionData")
    if session_status:
        for record in session_status:
            telemetria["sesion_data"].append(record)

@client.callback("timing_data")
async def handle_track_status(records):
    # Datos analiticos de carrera en curso
    timing_data = records.get("TimingData")
    if timing_data:
        for record in timing_data:
            telemetria["live_timing"].append(record)

@client.callback("driver_list")
async def handle_track_status(records):
    # Lista estatica de corredores
    drivers = records.get("DriverList")
    if drivers:
        for record in drivers:
            telemetria["drivers_list"].append(record)

@client.callback("series_ruedas")
async def handle_track_status(records):
    # Historial de cambio de ruedas
    tyre_stints = records.get("TyreStintSeries")
    if tyre_stints:
        for record in tyre_stints:
            telemetria["tyre_series"].append(record)

@client.callback("log_handler")
async def log_with_timestamp(records):
    with open("data_with_timestamp.log", "a") as f:
        for record in records:
            timestamp = datetime.datetime.now().isoformat()
            f.write(f"{timestamp} - {record}\n")

# Start the client
client.run()