from collections import deque

# buffer para datos recientes
telemetria = {
    "Heartbeat": deque(maxlen=5),
    "SessionInfo": deque(maxlen=1),
    "SessionData": deque(maxlen=100),
    #"TimingDataF1": deque(maxlen=4000),
    "DriverList": deque(maxlen=25),
    "TyreStintSeries": deque(maxlen=100),
    "nombreEvento": "A definir",
    "circuito": "A definir",
    "estadoConductores": {} 
} # guarda los últimos eventos