import json

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Input, Output

from app import app


@app.callback(
    Output("map", "figure"),
    [Input("my-slider", "value"), Input("map_df", "data")])
def display_map(year, map_df):
    if map_df is None:
        return

    map_df = json.loads(map_df)
    temp = []
    for i in map_df:
        temp.append(pd.read_json(i, orient='split'))
    map_df = temp

    fig = go.Figure(
        data=[go.Choropleth(

            locations=map_df[year]['CODE'],
            z=map_df[year]['livable'],
            colorscale='Greens',
            marker_line_color='darkgray',
            marker_line_width=0.5,
            hovertemplate=
            "<b>" + map_df[year]['COUNTRY'] + " </b><br>" +
            "longitude: " + str(1) + "<br>" +  # change values here if needed --> else remove
            "latitude: " + str(2) + "<br>",  # change values here if needed --> else remove
        )]
    )
    fig.update_geos(
        showlakes=False,
        projection_type="orthographic"
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
    [Input("my-slider", "value"), Input("bar_chart_df", "data")])
def display_bar_chart(year, bar_chart_df):
    if bar_chart_df is None:
        return

    bar_chart_df = pd.read_json(bar_chart_df, orient='split')

    # still need to figure out what is displayed when hover
    data1 = bar_chart_df[bar_chart_df["years"] == 2022 + year]
    data2 = bar_chart_df[bar_chart_df["years"] != 2022 + year]
    fig1 = px.bar(data1,
                  x="years",
                  y=["investment", "interest"],
                  title="Coumpound interest",
                  color_discrete_sequence=["#0D0CB5", "#BECBFF"]
                  )
    fig2 = px.bar(data2,
                  x="years",
                  y=["investment", "interest"],
                  title="Compound interest",
                  color_discrete_sequence=['#00441B', '#C6EBC5']
                  )

    fig3 = go.Figure(data=fig1.data + fig2.data)
    fig3.update_layout(barmode='relative')
    fig3.update_layout(
        title='Parts of interests and investments over time :',
    )

    return fig3


@app.callback(
    [Output("initial_investment", "value"), Output("investment_per_month", "value"), Output("interest_rate", "value"),
     Output("independence_duration", "value"), Output("withdrawals_per_month", "value")],
    [Input("reset-button", "n_clicks")]
)
def on_button_click(_):
    return 500, 100, 5.5, 30, 2000


def is_valid(initial_investment, investment_per_month, interest_rate, independence_duration, withdrawals_per_month):
    return initial_investment is not None and investment_per_month is not None and interest_rate is not None and independence_duration is not None and withdrawals_per_month is not None


@app.callback(
    [Output("valid_display", "style")],
    [Input("initial_investment", "value"), Input("investment_per_month", "value"), Input("interest_rate", "value"),
     Input("independence_duration", "value"), Input("withdrawals_per_month", "value")]
)
def valid_display(initial_investment, investment_per_month, interest_rate, independence_duration,
                  withdrawals_per_month):
    return [{"display": "visible"}] if is_valid(initial_investment, investment_per_month, interest_rate,
                                                independence_duration,
                                                withdrawals_per_month) else [{"display": "none"}]


@app.callback(
    Output("bar_chart_df", "data"),
    [Input("initial_investment", "value"), Input("investment_per_month", "value"), Input("interest_rate", "value"),
     Input("independence_duration", "value"), Input("withdrawals_per_month", "value")]
)
def barchart_df(initial_investment, investment_per_month, interest_rate, independence_duration,
                withdrawals_per_month):
    if not is_valid(initial_investment, investment_per_month, interest_rate, independence_duration,
                    withdrawals_per_month):
        return
    bar_chart_df = pd.DataFrame()
    temp = []
    for i in range(5, 65, 5):
        temp.append(2022 + i)
    bar_chart_df['years'] = temp
    bar_chart_df['investment'] = range(5 + initial_investment, 65 + initial_investment, 5)
    bar_chart_df['interest'] = range(5 + initial_investment, 65 + initial_investment, 5)
    return bar_chart_df.to_json(date_format='iso', orient='split')


@app.callback(
    Output("map_df", "data"),
    [Input("initial_investment", "value"), Input("investment_per_month", "value"), Input("interest_rate", "value"),
     Input("independence_duration", "value"), Input("withdrawals_per_month", "value")]
)
def barchart_df(initial_investment, investment_per_month, interest_rate, independence_duration,
                withdrawals_per_month):
    if not is_valid(initial_investment, investment_per_month, interest_rate, independence_duration,
                    withdrawals_per_month):
        return

    df = pd.read_csv('datasets/country_dataset.csv')
    df = df.drop('GDP (BILLIONS)', axis=1)
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
    map_df = []
    temp_country = ['Switzerland', 'France', 'Germany', 'Russia', 'Algeria', 'India', 'Brazil', 'Canada', 'Niger',
                    'Italy',
                    'Marshall Islands', 'Paraguay', 'Cuba', 'Wallis and Futuna', 'Nicaragua', 'Malta', 'Jersey',
                    'Western Sahara', 'South Korea', 'Monaco', 'Panama', 'Kyrgyzstan', 'Burkina Faso', 'Holy See',
                    'Iran',
                    'Latvia', 'Mexico', 'Saint Pierre and Miquelon', 'Democratic Republic of the Congo', 'Montenegro',
                    'Zimbabwe', 'India', 'Nauru', 'Turkmenistan', 'Tonga', 'Cape Verde', 'Yemen', 'Saint Lucia',
                    'Bermuda',
                    'Croatia', 'The Gambia', 'Aruba', 'Faroe Islands', 'Bolivia', 'Bangladesh', 'Reunion', 'Norway',
                    'Maldives', 'Pitcairn Islands', 'Pakistan', 'Slovakia', 'Hong Kong', 'Djibouti',
                    'Republic of Ireland',
                    'Sierra Leone', 'Albania', 'Isle of Man', 'Estonia', 'Uzbekistan', 'Canada']

    for i in range(60):
        df_temp = df.copy()
        df_temp['livable'] = df_temp['COUNTRY'].isin(temp_country[: i + 1])
        df_temp["livable"] = df_temp["livable"].astype(int)
        df_temp["livable"] = df_temp["livable"].astype(str)
        df_temp = pd.concat([df_color, df_temp], ignore_index=True)
        map_df.append(df_temp.to_json(date_format='iso', orient='split'))

    return json.dumps(map_df)
