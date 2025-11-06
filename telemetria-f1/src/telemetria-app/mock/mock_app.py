from collections import deque
from mock_data import mock_update
import time

telemetria = deque(maxlen=10)

for _ in range(5):
    snapshot = mock_update(telemetria)
    print("Top 3 posiciones:")
    lines = snapshot["timingdata"]["Lines"]
    top = sorted(lines.values(), key=lambda x: int(x["Position"]))[:3]
    for d in top:
        print(f"{d['Position']} - {d['RacingNumber']} - {d['LastLapTime']['Value']}")
    time.sleep(2)