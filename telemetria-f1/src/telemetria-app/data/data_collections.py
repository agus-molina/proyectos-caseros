from collections import deque

# buffer para datos recientes
telemetria = {
    "heartbeat": deque(maxlen=5),
    "session_info": deque(maxlen=1),
    "session_data": deque(maxlen=100),
    "live_timing": deque(maxlen=4000),
    "drivers_list": deque(maxlen=1),
    "tyre_series": deque(maxlen=100)
} # guarda los últimos eventos

nombreEvento = "São Paulo Grand Prix"
circuito = "Interlagos"
