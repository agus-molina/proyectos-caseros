from dash import Input, Output

def registrar_callbacks(app, telemetria):

    @app.callback(
        Output("telemetry-table", "data"),
        Input("update-interval", "n_intervals")
    )
    def actualizar_tabla(_):

        if not telemetria:
            return []

        # ✅ Último snapshot
        snapshot = telemetria[-1]
        timing = snapshot["timingdata"]["Lines"]

        filas = []
        for driver_id, info in sorted(timing.items(), key=lambda x: int(x[1]["Position"])):
            filas.append({
                "Position": info.get("Position", "-"),
                "Driver": info.get("RacingNumber", "-"),
                "GapToLeader": info.get("GapToLeader", "-") or "-",
                "LastLapTime": info.get("LastLapTime", {}).get("Value", "-"),
                "BestLapTime": info.get("BestLapTime", {}).get("Value") or "-",
            })

        return filas