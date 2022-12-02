import dash_bootstrap_components as dbc
from .callbacks import *
from dash import dcc, html

investments_inputs = [
    html.Div(
        [
            html.H4("💶 Investissements", className="settings_title"),
            dbc.InputGroup([
                dbc.Col([
                    dbc.Label("Investissement initial"),
                    html.I(className="icon bi bi-question-circle me-2", id="initial_investment_help"),
                    dbc.Tooltip("Montant investi une seule fois, au début", target="initial_investment_help")
                ]),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("CHF"),
                        dbc.Input(
                            id="initial_investment",
                            type="number",
                            min=0,
                            value="500",
                            step=100,
                            required=True
                        ),
                        dbc.InputGroupText(".00"),
                    ],
                ),
            ], className="input_group"),
            dbc.InputGroup([
                dbc.Col([
                    dbc.Label("Investissement par mois"),
                    html.I(className="icon bi bi-question-circle me-2", id="investment_per_month_help"),
                    dbc.Tooltip("Montant investi à intervalles réguliers, chaque mois",
                                target="investment_per_month_help")
                ]),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("CHF"),
                        dbc.Input(
                            id="investment_per_month",
                            type="number",
                            min=0,
                            value="100",
                            step=50,
                            required=True
                        ),
                        dbc.InputGroupText(".00"),
                    ],
                ),
            ], className="input_group"),
            dbc.InputGroup([
                dbc.Col([
                    dbc.Label("Taux d'intérêt"),
                    html.I(className="icon bi bi-question-circle me-2", id="interest_rate_help"),
                    dbc.Tooltip("Taux d'intérêt annuel sur les investissements", target="interest_rate_help")
                ]),
                dbc.InputGroup(
                    [
                        dbc.Input(
                            id="interest_rate",
                            type="number",
                            min=0,
                            max=100,
                            step=".10",
                            value=5.5,
                            required=True
                        ),
                        dbc.InputGroupText("%"),
                    ],
                ),
            ]),
        ]
    )
]

goals_inputs = [
    html.Div(
        [
            html.H4("🎯 Objectifs", className="settings_title"),
            dbc.InputGroup([
                dbc.Col([
                    dbc.Label("Durée de l'indépendance financière"),
                    html.I(className="icon bi bi-question-circle me-2", id="independence_duration_help"),
                    dbc.Tooltip("Après ce temps, l'entièreté de l'argent investi aura été récupéré",
                                target="independence_duration_help")
                ]),
                dbc.InputGroup([
                    dbc.Select(
                        id="independence_duration",
                        options=[
                            {"label": "15 years", "value": "15"},
                            {"label": "30 years", "value": "30"},
                            {"label": "45 years", "value": "45"},
                            {"label": "Endless", "value": "-1"}
                        ],
                        value="30",
                        required=True
                    ),
                ]),
            ]),
        ]
    )
]

slider_inputs = [
    html.Div(
        [
            dbc.Row([
                dbc.Label("Voir l'évolution après"),
                dbc.Col([dcc.Slider(5, 50, 1, value=10, id='my-slider', updatemode='drag'), ], width=11,
                        className="slider_col"),
                dbc.Col([dbc.FormText("années")], width=1, className="slider_col")
            ]),
        ]
    )
]

buttons = html.Div(
    [
        dbc.Button("Réinitialiser", color="warning", className="me-md-2", outline=True, id="reset-button", n_clicks=0),
        dbc.Button("Visualiser", color="success", className="me-md-2", outline=True, id="apply-button", n_clicks=0),
    ],
    className="d-grid gap-2 d-md-flex justify-content-md-end",
)

outputs = [
    html.Div(
        [
            html.H4("💰 Retraits par mois", className="settings_title"),
            dbc.Col([
                dbc.Label("Montant disponible par mois"),
                html.I(className="icon bi bi-question-circle me-2", id="monthly_withdrawals_help"),
                dbc.Tooltip("Ce montant pourra être retiré chaque mois, durant la période objectif choisie",
                            target="monthly_withdrawals_help"),
                html.H4("-- CHF", className="amount", id="monthly-withdrawals")
            ]),
        ]
    )
]

home_layout = dbc.Row([
    dbc.Col([
        dbc.Card([
            dbc.CardBody(investments_inputs),
            dbc.CardBody(goals_inputs),
            dbc.CardBody(buttons)
        ], className="card"),
        dbc.Card([
            dbc.CardBody(outputs)
        ], className="card")
    ], md=12, lg=4, xxl=3, className="settings_card"),
    dbc.Col([
        dbc.Row([
            dbc.CardBody(slider_inputs),
            dbc.CardBody([
                dbc.Label("Parts des investissements et des intérêts au fil du temps :"),
                dcc.Graph(id="barchart"),
            ]),
            dbc.CardBody([
                dbc.Label("Carte des pays où vous pouvez aller vivre :"),
                dcc.Graph(id="map"),
            ]),
        ], className="main_content", id="valid_display")
    ], md=12, lg=8, xxl=9),
])
