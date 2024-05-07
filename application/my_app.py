from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px

from lib.data_manager import DataManager


dm = DataManager({"logfile_path": "/mnt/c/Users/cyber/AppData/Local/AMD/CN"})
dropdown_values = dm.get_dropdown_values()


app = Dash(__name__)


app.layout = html.Div(
    [
        html.H1(children="Sysem Performance ", style={"textAlign": "center"}),
        dcc.Dropdown(dropdown_values, dropdown_values[0], id="dropdown-selection"),
        dcc.Graph(id="graph-content"),
    ]
)


@callback(Output("graph-content", "figure"), Input("dropdown-selection", "value"))
def update_graph(value):
    dff = dm.filter_data(value=value)
    columns = dff.columns.to_list()
    columns.remove("TIME STAMP")
    print("columns",columns)
    return px.line(dff, x="TIME STAMP", y=columns)


if __name__ == "__main__":
    app.run(debug=True)
