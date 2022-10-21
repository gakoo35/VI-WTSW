from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

app = Dash(__name__)


app.layout = html.Div([
    html.H4('Interactive color selection with simple Dash example'),
    html.P("Select color:"),
    dcc.Dropdown(
        id="dropdown",
        options=['Gold', 'MediumTurquoise', 'LightGreen'],
        value='Gold',
        clearable=False,
    ),
    dcc.Graph(id="graph"),
    dcc.Graph(id="map")
])


@app.callback(
    Output("graph", "figure"), 
    Input("dropdown", "value"))
def display_color(color):
    fig = go.Figure(
        data=go.Bar(y=[2, 3, 1], # replace with your own data source
                    marker_color=color))
    return fig

@app.callback(
    Output("map", "figure"), 
    Input("dropdown", "value"))
def display_map(dataset):
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')
    df = df.drop('GDP (BILLIONS)', axis=1)
    df['livable'] = df['COUNTRY'].isin(['Switzerland'])
    df["livable"] = df["livable"].astype(int)
    df["livable"] = df["livable"].astype(str)

    fig = go.Figure(data=go.Choropleth(
        locations = df['CODE'],
        z = df['livable'],
        text = df['COUNTRY'],
        colorscale = 'Greens',
        marker_line_color='darkgray',
        marker_line_width=0.5,
    ))
    fig.update_geos(
        showocean=True, oceancolor="LightBlue",
    )
    return fig



app.run_server(debug=True)