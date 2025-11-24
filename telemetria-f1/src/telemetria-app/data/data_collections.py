from collections import deque

# Buffer para datos recientes
telemetria = {
    "Heartbeat": deque(maxlen=5),
    "SessionInfo": deque(maxlen=1),
    "SessionData": deque(maxlen=100),
    "DriverList": deque(maxlen=25),
    "TyreStintSeries": deque(maxlen=100),
    "nombreEvento": "A definir",
    "circuito": "A definir",
    "estadoConductores": {} 
}