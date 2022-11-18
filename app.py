import dash
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP], suppress_callback_exceptions=True)
load_figure_template('BOOTSTRAP')
