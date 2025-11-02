import dash
from components.layout import layout  # importás el layout

app = dash.Dash(__name__)
app.layout = layout  # lo asignás

if __name__ == "__main__":
    app.run(debug=True)