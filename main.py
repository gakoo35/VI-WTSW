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



# world map ------------------------------------------------------------------------------

# create basic df 
# dataset link : https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv
df = pd.read_csv('country_dataset.csv')
df = df.drop('GDP (BILLIONS)', axis=1)
print(df.head())
df['livable'] = df['COUNTRY'].isin([None])
df["livable"] = df["livable"].astype(int)
df["livable"] = df["livable"].astype(str)
 # add a non existing country to give basic color to the map
df_color = pd.DataFrame()
df_color['COUNTRY'] = ['Nothing']
df_color['CODE'] = ['NOT']
df_color['livable'] = [1]
df_basic = pd.concat([df_color, df], ignore_index=True)


#temp logic to add content to the slider --> same will be used later with different list of countries
data_slider = []
data_slider.append(df_basic)
temp_country = ['Switzerland', 'France', 'Germany', 'Russia', 'Algeria', 'India', 'Brazil', 'Canada', 'Niger', 'Italy']
for i in range(10):
    df_temp = df.copy()
    df_temp['livable'] = df_temp['COUNTRY'].isin(temp_country[: i+1])
    df_temp["livable"] = df_temp["livable"].astype(int)
    df_temp["livable"] = df_temp["livable"].astype(str)
    df_temp = pd.concat([df_color, df_temp], ignore_index=True)
    data_slider.append(df_temp)

def frame_args(duration):
    return {
            "frame": {"duration": duration},
            "mode": "immediate",
            "fromcurrent": True,
            "transition": {"duration": duration, "easing": "linear"},
        }

# still need to remove the infobar on the right and the trace 0 on the hovertext
@app.callback(
    Output("map", "figure"), 
    Input("dropdown", "value"))
def display_map(dataset):
    frames = []
    for i in range(0, len(data_slider)):
        frame = go.Frame(data=[go.Choropleth(
            locations = data_slider[i]['CODE'],
            z = data_slider[i]['livable'],
            colorscale = 'Greens',
            marker_line_color='darkgray',
            marker_line_width=0.5,
            hovertemplate =
                "<b>"+data_slider[i]['COUNTRY']+" </b><br>" +
                "longitude: "+str(1)+"<br>" + # change values here if needed --> else remove
                "latitude: "+str(2)+"<br>" , # change values here if needed --> else remove
            )],
            name=str(2022+i))
        frames.append(frame)


    fig = go.Figure(
        data=[go.Choropleth(
            locations = data_slider[0]['CODE'],
            z = data_slider[0]['livable'],
            colorscale = 'Greens',
            marker_line_color='darkgray',
            marker_line_width=0.5,
            hovertemplate =
                "<b>"+data_slider[0]['COUNTRY']+" </b><br>" +
                "longitude: "+str(1)+"<br>" + # change values here if needed --> else remove
                "latitude: "+str(2)+"<br>" , # change values here if needed --> else remove
        )],
        frames=frames
    )
    fig.update_geos(
        showocean=True, oceancolor="LightBlue",
    )

    sliders = [{"pad": {"b": 10, "t": 60},
                "len": 0.9,
                "x": 0.1,
                "y": 0,
                "steps": [ {
                        "args": [[f.name], frame_args(0)],
                        "label": str(2022+k),
                        "method": "animate",
                    }
                    for k, f in enumerate(fig.frames)
                ],
            }
        ]

    fig.update_layout(
            title='Map of countries you could live in :',
            #width=1200,
            height=800,
            #autosize=False,
            scene=dict(
                    zaxis=dict(range=[-0.1, 6.8], autorange=True),
                    ),
            updatemenus = [
            {
                "buttons": [
                    {
                        "args": [None, frame_args(1000)],
                        "label": "&#9654;", # play symbol
                        "method": "animate",
                    },
                    {
                        "args": [[None], frame_args(0)],
                        "label": "&#9724;", # pause symbol
                        "method": "animate",
                    },
                ],
                "direction": "left",
                "pad": {"r": 10, "t": 70},
                "type": "buttons",
                "x": 0.1,
                "y": 0,
            }
            ],
            sliders=sliders
    )
    return fig



app.run_server(debug=True)
