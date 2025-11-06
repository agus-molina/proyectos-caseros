from dash import Dash, Output, Input
from collections import deque
import threading, time
from visualizacion.layout import crear_layout
from visualizacion.callbacks import registrar_callbacks
from mock.mock_data import mock_update
from data.data_collections import nombreEvento, circuito, telemetria

app = Dash(__name__)
app.layout = crear_layout(nombreEvento, circuito)
registrar_callbacks(app, telemetria)

# 🔹 Hilo que simula datos en tiempo real
def simular_datos():
    while True:
        mock_update(telemetria)
        time.sleep(3)  # cada 3 segundos una nueva actualización

# 🔹 Lanzar el hilo simulador al iniciar la app
threading.Thread(target=simular_datos, daemon=True).start()

if __name__ == "__main__":
    app.run(debug=True)