import dash_bootstrap_components as dbc
from .callbacks import *
from dash import dcc, html

home_layout = html.Div([
    dbc.Row([
        html.Div([
            html.B("Initial investment (in $):"),
            dcc.Input(
                id="inital_investment",
                type="number",
                min=0,
                placeholder="Ex: 2000"
            ),
        ], className="input"),
        html.Div([
            html.B("Investment per month (in $):"),
            dcc.Input(
                id="investment_per_month",
                type="number",
                placeholder="Ex: 150"
            )
        ], className="input"),
        html.Div([
            html.B("Interest rate (%):"),
            dcc.Input(
                id="interest_rate",
                type="number",
                min=0,
                max=100,
                value="8"
            )
        ], className="input"),
        html.Div([
            html.B("Independence type :"),
            dcc.RadioItems(
                ["Endless", "30 years"], "Endless"
                , className="radios")
        ], className="input")
    ]),
    dbc.Row([
        dbc.Col(dcc.Slider(0, 10, 1, value=0, id='my-slider')),
        dbc.Col(dcc.Graph(id="barchart"), width=9),
        dbc.Col(dcc.Graph(id="map"), width=9),
    ])
])
