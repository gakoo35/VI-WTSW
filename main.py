import pandas as pd
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    dcc.Markdown('''
        # 🏖 When to stop working ?
        
        🎯 **Objectives :** Explain the power of compound interest and give an overview of the wealth to accumulate 
        in order to achieve financial independence in a country.
        
        👨‍💻**Authors :** `Alexis Allemann`, `Corpataux Sam`, `Koch Gaël` 
         
         
         ## 💰 Investment configuration
        '''),
    dcc.Markdown('''
        ## 📈 Compound interest over time
        '''),
    dcc.Markdown('''
        ## 🌏 Where you can go live
        '''),
    dcc.Dropdown(
        id="dropdown",
        options=['Gold', 'MediumTurquoise', 'LightGreen'],
        value='Gold',
        clearable=False,
    ),
    dcc.Graph(id="graph"),
    dcc.Graph(id="map")
], className='markdown-body')


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
        locations=df['CODE'],
        z=df['livable'],
        text=df['COUNTRY'],
        colorscale='Greens',
        marker_line_color='darkgray',
        marker_line_width=0.5,
    ))
    fig.update_geos(
        showocean=True, oceancolor="LightBlue",
    )
    return fig


app.run_server(debug=True)
