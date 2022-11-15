import dash
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
load_figure_template('BOOTSTRAP')