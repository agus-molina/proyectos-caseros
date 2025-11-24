from dash import Dash
import threading
from visualizacion.layout import crear_layout
from visualizacion.callbacks import registrar_callbacks
from data.data_collections import telemetria
from api.api_client import client

app = Dash(__name__)
app.layout = crear_layout()
registrar_callbacks(app, telemetria)

# --- INICIAR CLIENTE EN THREAD ---
def iniciar_cliente():
    try:
        client.run()
    except Exception as e:
        print(f"Error loading data: {e}")

threading.Thread(target=iniciar_cliente, daemon=True).start()

if __name__ == "__main__":
    app.run(debug=True)
