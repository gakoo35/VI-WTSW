import json

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Input, Output

from app import app

@app.callback(
    [Output("initial_investment", "value"), Output("investment_per_month", "value"), Output("interest_rate", "value"),
     Output("independence_duration", "value"), Output("withdrawals_per_month", "value")],
    [Input("reset-button", "n_clicks")]
)
def on_button_click(_):
    return 500, 100, 5.5, 30, 2000

@app.callback(
    Output("barchart", "figure"),
    [Input("apply-button", "n_clicks"), Input("my-slider", "value")]
)
def barchart_df(nb_clicks, year):
    # TODO : Add barchart code
    return

@app.callback(
    Output("map", "figure"),
    [Input("apply-button", "n_clicks"), Input("my-slider", "value")]
)
def barchart_df(nb_clicks, year):
    # TODO : Add map code
    return