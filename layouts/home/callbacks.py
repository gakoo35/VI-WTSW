import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Input, Output

from app import app

# world map ------------------------------------------------------------------------------

# create basic df
# dataset link : https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv
df = pd.read_csv('datasets/country_dataset.csv')
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

# temp logic to add content to the slider --> same will be used later with different list of countries
data_slider = []
data_slider.append(df_basic)
temp_country = ['Switzerland', 'France', 'Germany', 'Russia', 'Algeria', 'India', 'Brazil', 'Canada', 'Niger', 'Italy']
for i in range(10):
    df_temp = df.copy()
    df_temp['livable'] = df_temp['COUNTRY'].isin(temp_country[: i + 1])
    df_temp["livable"] = df_temp["livable"].astype(int)
    df_temp["livable"] = df_temp["livable"].astype(str)
    df_temp = pd.concat([df_color, df_temp], ignore_index=True)
    data_slider.append(df_temp)

# ------------------- bar chart -----------------
barchartDF = pd.DataFrame()
barchartDF['years'] = [2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032]
barchartDF['investissement'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
barchartDF['interet'] = [0, 0, 0, 1, 1, 2, 4, 6, 10, 15, 18]


@app.callback(
    Output("map", "figure"),
    Input("my-slider", "value"))
def display_map(year):
    fig = go.Figure(
        data=[go.Choropleth(
            locations=data_slider[year]['CODE'],
            z=data_slider[year]['livable'],
            colorscale='Greens',
            marker_line_color='darkgray',
            marker_line_width=0.5,
            hovertemplate=
            "<b>" + data_slider[year]['COUNTRY'] + " </b><br>" +
            "longitude: " + str(1) + "<br>" +  # change values here if needed --> else remove
            "latitude: " + str(2) + "<br>",  # change values here if needed --> else remove
        )]
    )
    fig.update_geos(
        showocean=True, oceancolor="LightBlue",
    )

    fig.update_layout(
        title='Map of countries you could live in :',
        # width=1200,
        height=800,
        # autosize=False,
    )
    return fig


@app.callback(
    Output("barchart", "figure"),
    Input("my-slider", "value"))
def display_map(year):
    # still need to figure out what is displayed when hover
    data1 = barchartDF[barchartDF["years"] == 2022 + year]
    data2 = barchartDF[barchartDF["years"] != 2022 + year]
    fig1 = px.bar(data1,
                  x="years",
                  y=["investissement", "interet"],
                  title="Coumpound interest",
                  color_discrete_sequence=["#0D0CB5", "#BECBFF"]
                  )
    fig2 = px.bar(data2,
                  x="years",
                  y=["investissement", "interet"],
                  title="Coumpound interest",
                  color_discrete_sequence=['#00441B', '#C6EBC5']
                  )

    fig3 = go.Figure(data=fig1.data + fig2.data)
    fig3.update_layout(barmode='relative')
    print(year)
    return fig3