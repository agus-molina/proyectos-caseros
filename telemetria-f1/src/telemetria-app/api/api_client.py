from livef1.adapters.realtime_client import RealF1Client
import datetime
import json
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

# Initialize client
client = RealF1Client(
    topics=["CarData.z", "SessionInfo", "TrackStatus"],
    log_file_name="session_data.json"
)

# Define multiple handlers
@client.callback("process_telemetry")
async def handle_telemetry(records):
    # Process car telemetry data
    telemetry_data = records.get("CarData.z")
    if telemetry_data:
        for record in telemetry_data:
            process_telemetry_data(record) # this is a placeholder for your code

@client.callback("track_status")
async def handle_track_status(records):
    # Monitor track conditions
    track_data = records.get("TrackStatus")
    if track_data:
        for record in track_data:
            update_track_status(record) # this is a placeholder for your code

@client.callback("log_handler")
async def log_with_timestamp(records):
    with open("data_with_timestamp.log", "a") as f:
        for record in records:
            timestamp = datetime.datetime.now().isoformat()
            f.write(f"{timestamp} - {record}\n")


# Start the client
client.run()"""