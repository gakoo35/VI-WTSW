import dash_bootstrap_components as dbc

from styles.styles import INPUT_GROUP, CARD, SETTINGS_TITLE, SETTINGS_CARD
from .callbacks import *
from dash import dcc, html

investments_inputs = [
    html.Div(
        [
            html.H3("💶 Investments", style=SETTINGS_TITLE),
            dbc.InputGroup([
                dbc.Label("Initial investment"),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("$"),
                        dbc.Input(
                            id="inital_investment",
                            type="number",
                            min=0,
                            placeholder="Type your initial investment here...",
                            value="500",
                            step=100
                        ),
                        dbc.InputGroupText(".00"),
                    ],
                ),
                dbc.FormText("Amount invested once, at the beginning"),
            ], style=INPUT_GROUP),
            dbc.InputGroup([
                dbc.Label("Investment per month"),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("$"),
                        dbc.Input(
                            id="investment_per_month",
                            type="number",
                            min=0,
                            placeholder="Type your monthly investment here...",
                            value="100",
                            step=50
                        ),
                        dbc.InputGroupText(".00"),
                    ],
                ),
                dbc.FormText("Amount invested each month"),
            ], style=INPUT_GROUP),
            dbc.InputGroup([
                dbc.Label("Interest rate"),
                dbc.InputGroup(
                    [
                        dbc.Input(
                            id="interest_rate",
                            type="number",
                            min=0,
                            max=100,
                            step=".10",
                            value=5.5
                        ),
                        dbc.InputGroupText("%"),
                    ],
                ),
                dbc.FormText("Annual interest rate on investments"),
            ]),
        ]
    )
]

goals_inputs = [
    html.Div(
        [
            html.H3("🎯 Goals", style=SETTINGS_TITLE),
            dbc.InputGroup([
                dbc.Label("Independence duration"),
                dbc.InputGroup([
                    dbc.Select(
                        id="independence_duration",
                        options=[
                            {"label": "15 years", "value": "15"},
                            {"label": "30 years", "value": "30"},
                            {"label": "45 years", "value": "45"},
                            {"label": "Endless", "value": "-1"}
                        ],
                        value="30"
                    ),
                ]),
                dbc.FormText("After this time, the money invested will have been recovered"),
            ], style=INPUT_GROUP),
            dbc.InputGroup([
                dbc.Label("Withdrawals per month"),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("$"),
                        dbc.Input(
                            id="withdrawals_per_month",
                            type="number",
                            min=0,
                            value="2000",
                            step=100
                        ),
                        dbc.InputGroupText(".00"),
                    ],
                ),
                dbc.FormText("Amount withdrawn each month"),
            ]),
        ]
    )
]

buttons = html.Div(
    [
        dbc.Button("Reset defaults", color="warning", className="me-md-2", outline=True, id="reset-button", n_clicks=0),
        dbc.Button("Visualize", color="success", outline=True),
    ],
    className="d-grid gap-2 d-md-flex justify-content-md-end",
)

home_layout = dbc.Row([
    dbc.Col([
        dbc.Card([
            dbc.CardBody(investments_inputs),
            dbc.CardBody(goals_inputs),
            dbc.CardBody(buttons)
        ], style=CARD),
    ], md=12, lg=4, xxl=3, style=SETTINGS_CARD),
    dbc.Col([
        dbc.Row([
            dcc.Slider(10, 80, 10, value=10, id='my-slider'),
            dcc.Graph(id="barchart"),
            dcc.Graph(id="map"),
        ])
    ], md=12, lg=8, xxl=9, )
])