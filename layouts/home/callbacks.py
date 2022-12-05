import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import maths_functions as math
from dash import Input, Output
from app import app

# ------------------- world map chart -----------------

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
temp_country = ['']
for i in range(50):
    df_temp = df.copy()
    df_temp['livable'] = df_temp['COUNTRY'].isin(temp_country[: i + 1])
    df_temp["livable"] = df_temp["livable"].astype(int)
    df_temp["livable"] = df_temp["livable"].astype(str)
    df_temp = pd.concat([df_color, df_temp], ignore_index=True)
    data_slider.append(df_temp)

# ------------------- bar chart -----------------
barchartDF = pd.DataFrame()
temp = []
for i in range(0, 51):
    temp.append(2022 + i)
barchartDF['years'] = temp
barchartDF['investment'] = [10000, 16000, 22000, 28000, 34000, 40000, 46000, 52000, 58000, 64000, 70000, 76000,
                                82000, 88000, 94000, 100000, 106000, 112000, 118000, 124000, 130000, 136000, 142000,
                                148000, 154000, 160000, 166000, 172000, 178000, 184000, 190000, 196000, 202000, 208000,
                                214000, 220000, 226000, 232000, 238000, 244000, 250000, 256000, 262000, 268000, 274000,
                                280000, 286000, 292000, 298000, 304000, 310000]

barchartDF['interest'] = [0, 677, 1695, 3072, 4827, 6978, 9547, 12554, 16021, 19973, 24435, 29431, 34990, 41141, 47913,
                         55338, 63451, 72285, 81879, 92270, 103500, 115611, 128649, 142661, 157696, 173808, 191052,
                         209484, 229167, 250163, 272541, 296370, 321726, 348686, 377332, 407750, 440032, 474273, 510572,
                         549035, 589773, 632903, 678546, 726831, 777893, 831875, 888926, 949202, 1012870, 1080101,
                         1151080]


@app.callback(
    # [Output("barchart", "figure"), Output("monthly_withdrawals", "children")],
    [Output("barchart", "figure"), Output("monthly_withdrawals", "value")],
    [Input("my-slider", "value"), Input("initial_investment", "value"), Input("investment_per_month", "value"),
     Input("interest_rate", "value"), Input("independence_duration", "value")]
)
def barchart_df(year, ia, ma, ir, independence_duration):
    global data_slider
    print("independence duration = ")
    print(independence_duration)
    print(independence_duration)
    # still need to figure out what is displayed when hover
    data1 = barchartDF[barchartDF["years"] == 2022 + year]
    data2 = barchartDF[barchartDF["years"] != 2022 + year]
    fig1 = px.bar(data1,
                  x="years",
                  y=["investment", "interest"],
                  title="Compound interest",
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
    print("Year : ")
    print(year)

    total_wealth = math.get_total_wealth(ia, ma, year, ir)
    monthly_income = math.get_monthly_income(total_wealth, independence_duration)
    eligible_countries = math.filter_countries(monthly_income)

    list_of_eligible_countries = []
    for country in eligible_countries:
        list_of_eligible_countries.append(country)

    every_year_eligible_countries = []
    data_slider = []
    data_slider.append(df_basic)

    for actual_year in range(50):
        total_wealth = math.get_total_wealth(ia, ma, actual_year, ir)
        monthly_income = math.get_monthly_income(total_wealth, independence_duration)
        actual_eligible_countries = math.filter_countries(monthly_income)

        actual_year_eligible_countries = []
        for country in actual_eligible_countries:
            actual_year_eligible_countries.append(country)

        df_temp_2 = df.copy()
        df_temp_2['livable'] = df_temp_2['COUNTRY'].isin(actual_year_eligible_countries)
        df_temp_2["livable"] = df_temp_2["livable"].astype(int)
        df_temp_2["livable"] = df_temp_2["livable"].astype(str)
        df_temp_2 = pd.concat([df_color, df_temp_2], ignore_index=True)
        data_slider.append(df_temp_2)

    actual_total_wealth = math.get_total_wealth(ia, ma, year, ir)
    actual_monthly_income = math.get_monthly_income(actual_total_wealth, independence_duration)

    return fig3, actual_monthly_income


@app.callback(
    Output("map", "figure"),
    [Input("apply-button", "n_clicks"), Input("my-slider", "value")]
)
def display_map(nb_clicks, year):
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
        showlakes=False,
        projection_type="orthographic"
    )
    fig.update_layout(
        # width=1200,
        height=800,
        # autosize=False,
    )
    return fig


@app.callback(
    [Output("initial_investment", "value"), Output("investment_per_month", "value"), Output("interest_rate", "value"),
     Output("independence_duration", "value")],
    [Input("reset-button", "n_clicks")]
)
def on_button_click(_):
    return 10000, 500, 5, 30


@app.callback(
    Output("dummy1", "children"),
    [Input("initial_investment", "value"), Input("investment_per_month", "value"), Input("interest_rate", "value"),
     Input("apply-button", "n_clicks")]
)
def on_button_click(ia, ma, ir, _):
    global barchartDF
    # Calculate total wealth per year (value invested + cmpi)
    total_value_with_cmpi = []
    for i in range(51):
        total_value_with_cmpi.append(math.get_total_wealth(ia, ma, i, ir))
    print("total_value_with_cmpi : ")
    print(total_value_with_cmpi)

    # Calculate total value invested (without cmpi)
    total_value_invested_per_year = []
    for i in range(51):
        total_value_invested_per_year.append(math.get_total_ma(ia, ma, i))
    print("total_value_invested_per_year : ")
    print(total_value_invested_per_year)
    barchartDF['investment'] = total_value_invested_per_year

    # Calculate total compound value per year
    total_only_cmpi = []
    for i in range(51):
        total_only_cmpi.append(math.get_compound_interest_added_value(total_value_invested_per_year[i],
                                                                      total_value_with_cmpi[i]))
    print("total_only_cmpi : ")
    print(total_only_cmpi)
    barchartDF['interest'] = total_only_cmpi
    return
