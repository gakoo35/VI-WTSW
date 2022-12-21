import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import maths_functions as math
from dash import Input, Output, State
from app import app

# ------------------- world map chart -----------------

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
df_basic['monthly_cost'] = [0, 664.9499999999999, 1255.6499999999999, 903.65, 0, 0,
 0, 0, 0, 1212.1999999999998, 1289.75, 0,
 3221.35, 2775.3, 1071.4, 0, 2353.45, 1081.8500000000001,
 3265.9, 1155.55, 2786.8500000000004, 1799.05, 0, 6809.0,
 0, 1278.2, 0, 1436.6, 1184.6999999999998, 0,
 0, 1355.2, 0, 0, 0, 0,
 1839.1999999999998, 1332.1, 2937.0, 0, 0, 0,
 1631.3, 1646.15, 991.6500000000001, 0, 0, 0,
 0, 1752.85, 0, 1774.8500000000001, 1999.8, 0,
 2301.2000000000003, 1883.7500000000002, 3314.3, 0, 0,
 1467.3999999999999, 1381.6000000000001, 1012.5500000000001, 1636.25,
 0, 0, 1990.45, 1822.7, 0, 0, 1719.3,
 2807.7499999999995, 2819.2999999999997, 0, 0, 0,
 1120.3500000000001, 2627.9, 1555.3999999999999, 0,
 1969.5500000000002, 0, 0, 0, 1673.1000000000001,
 3835.15, 0, 0, 0, 0, 1447.05, 4280.65,
 1494.8999999999999, 3852.75, 850.85, 1300.75, 1531.7500000000002,
 1280.95, 3307.15, 0, 3447.9500000000003, 2472.25, 1840.3,
 2917.2, 4373.05, 1675.3, 1081.3, 1216.05, 0, 0,
 0, 0, 2229.7, 0, 0, 1719.3,
 2673.5499999999997, 0, 0, 1745.15, 0, 1720.95,
 3901.15, 0, 0, 0, 0, 1335.95, 2462.9,
 0, 2748.35, 0, 0, 1570.2500000000002,
 1356.3000000000002, 0, 1111.0, 0, 1304.6, 1469.6,
 1219.9, 0, 0, 928.9499999999999, 3140.5000000000005,
 0, 3065.15, 1382.1499999999999, 1818.85, 0, 0,
 0, 3842.3, 1876.0500000000002, 683.1, 0,
 2063.0499999999997, 0, 1141.25, 1239.7, 1329.8999999999999,
 1510.3, 1935.45, 2418.35, 3077.7999999999997, 1291.95,
 1367.8500000000001, 1333.75, 0, 0, 0, 0,
 0, 0, 0, 0, 1773.75, 2060.2999999999997,
 1283.1499999999999, 2760.4500000000003, 0, 4166.25, 0,
 1720.95, 2035.55, 0, 1143.45, 1657.7, 0, 2121.9,
 1126.4, 0, 1763.3, 0, 2762.6499999999996, 4984.1,
 973.5, 2278.1, 0, 1277.65, 1641.2, 0, 0,
 0, 0, 951.5000000000001, 998.25, 0, 0,
 1215.5, 1169.85, 2820.4, 2856.15, 3133.8999999999996,
 1880.4499999999998, 1037.3, 0, 1519.6499999999999, 1436.05,
 0, 0, 1725.8999999999999, 1204.4999999999998,
 1560.3500000000001]

# temp logic to add content to the slider --> same will be used later with different list of countries
data_slider = []
data_slider.append(df_basic)
temp_country = ['']
for i in range(50):
    df_temp = df.copy()
    df_temp['livable'] = df_temp['COUNTRY'].isin(temp_country[: i + 1])
    df_temp["livable"] = df_temp["livable"].astype(int)
    df_temp["livable"] = df_temp["livable"].astype(str)
    df_temp['monthly_cost'] = ''
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
    Output("barchart", "figure"),
    [Input("my-slider", "value"), Input("dummy1", "value")] # [Input("my-slider", "value"), Input("initial_investment", "value"), Input("investment_per_month", "value"), Input("interest_rate", "value"), Input("independence_duration", "value")]
)
def barchart_df(year, dummy):
    global data_slider
    # still need to figure out what is displayed when hover
    data1 = barchartDF[barchartDF["years"] == 2022 + year]
    data2 = barchartDF[barchartDF["years"] != 2022 + year]
    fig1 = px.bar(data1,
                  x="years",
                  y=["initial", "investment", "interest"],
                  title="Compound interest",
                  color_discrete_sequence=['#285430', '#5F8D4E', '#A4BE7B']
                  )
    fig2 = px.bar(data2,
                  x="years",
                  y=["initial", "investment", "interest"],
                  title="Compound interest",
                  color_discrete_sequence=['#14397d', '#77b5d9', '#d7eaf3']
                  )

    fig3 = go.Figure(data=fig1.data + fig2.data)
    fig3.update_layout(barmode='relative')
    return fig3


@app.callback(
    Output("map", "figure"),
    [Input("my-slider", "value"), Input("dummy1", "value")]
)
def display_map(year, dummy):
    data_slider[year] = data_slider[year].round(2)
    data_slider[year]["monthly_cost"] = data_slider[year]["monthly_cost"].astype(str)
    fig = go.Figure(
        data=[go.Choropleth(

            locations=data_slider[year]['CODE'],
            z=data_slider[year]['livable'],
            colorscale='Greens',
            marker_line_color='darkgray',
            marker_line_width=0.5,
            hovertemplate=
            "<b>" + data_slider[year]['COUNTRY'] + " </b><br>" +
            "Monthly cost: " + data_slider[year]['monthly_cost'],  # change values here if needed --> else remove
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
    Output("piechart", "figure"),
    [Input("my-slider", "value"), Input("dummy1", "value")] 
)
def display_pie_chart(year, dummy):
    data = barchartDF[barchartDF["years"] == 2022 + year]
    investissement = data['investment'].values[0]
    interet = data['interest'].values[0]
    initial = data['initial'].values[0]
    annee = data['years'].values[0]
    temp_df = pd.DataFrame(data={'CHF': [investissement, interet, initial], 'col2': [annee, annee, annee], 'Type': ['investment', 'interest', 'initial']})
    fig = px.pie(temp_df, values='CHF', names='Type', color_discrete_map={'interest':'#A4BE7B', 'investment':'#5F8D4E', 'initial':'#285430'}, color='Type')
    
    return fig

@app.callback(
    [Output("initial_investment", "value"), Output("investment_per_month", "value"), Output("interest_rate", "value"),
     Output("independence_duration", "value")],
    [Input("reset-button", "n_clicks")]
)
def on_button_click_res(_):
    return 10000, 500, 5, 30


@app.callback(
    Output("dummy1", "value"),
    [State("initial_investment", "value"), State("investment_per_month", "value"), State("interest_rate", "value"), State("independence_duration", "value"), State("my-slider", "value"),
     Input("apply-button", "n_clicks")]
)
def on_button_click_update(ia, ma, ir, independence_duration, year, _):
    if(ia == None or ma == None or ir == None or int(ia) <= 0 or int(ma) <= 0 or int(ir) <= 0):
        print('INPUT GOOD VALUES')
        return
    ia = int(ia)
    ma = int(ma)
    ir = float(ir)
    global barchartDF
    # Calculate total wealth per year (value invested + cmpi)
    total_value_with_cmpi = []
    for i in range(51):
        total_value_with_cmpi.append(math.get_total_wealth(ia, ma, i, ir))

    # Calculate total value invested (without cmpi)
    total_value_invested_per_year = []
    for i in range(51):
        total_value_invested_per_year.append(math.get_total_ma(ma, i))
    barchartDF['investment'] = total_value_invested_per_year

    # Calculate total compound value per year
    total_only_cmpi = []
    for i in range(51):
        total_only_cmpi.append(math.get_compound_interest_added_value(ia, total_value_invested_per_year[i],
                                                                      total_value_with_cmpi[i]))
    barchartDF['interest'] = total_only_cmpi
    barchartDF['initial'] = ia

    # FOR THE COUNTRIES : 
    global data_slider
    total_wealth = math.get_total_wealth(ia, ma, year, ir)
    monthly_income = math.get_monthly_income(total_wealth, independence_duration)
    eligible_countries = math.filter_countries(monthly_income)

    list_of_eligible_countries = []
    for country in eligible_countries:
        list_of_eligible_countries.append(country)

    every_year_eligible_countries = []
    data_slider = []
    #data_slider.append(df_basic)

    for actual_year in range(51):
        total_wealth = math.get_total_wealth(ia, ma, actual_year, ir)
        monthly_income = math.get_monthly_income(total_wealth, independence_duration)
        actual_eligible_countries, clean_df = math.filter_countries(monthly_income)

        actual_year_eligible_countries = []
        for country in actual_eligible_countries:
            actual_year_eligible_countries.append(country)

        df_temp_2 = df.copy()
        df_temp_2['livable'] = df_temp_2['COUNTRY'].isin(actual_year_eligible_countries)
        df_temp_2["livable"] = df_temp_2["livable"].astype(int)
        df_temp_2["livable"] = df_temp_2["livable"].astype(str)
        temp_monthly_cost = []
        for index, row in df_temp_2.iterrows():
            if(row['COUNTRY'] in clean_df['Country'].values):
                #print(str(clean_df.loc[clean_df['Country'] == row['COUNTRY']]['Cost of Living Plus Rent Index in dollars'].values[0]))
                temp_monthly_cost.append(clean_df.loc[clean_df['Country'] == row['COUNTRY']]['Cost of Living Plus Rent Index in dollars'].values[0])
            else:
                temp_monthly_cost.append(0)

        df_temp_2['monthly_cost'] = temp_monthly_cost
        df_temp_2 = pd.concat([df_color, df_temp_2], ignore_index=True)
        data_slider.append(df_temp_2)

    return 10


@app.callback(
    [Output("monthly_withdrawals", "value"),
    Output("total_capital", "value")],
    [State("initial_investment", "value"), State("investment_per_month", "value"), State("interest_rate", "value"), State("independence_duration", "value"), Input("my-slider", "value"), 
    Input("apply-button", "n_clicks")]
)
def cal_withdrawal(ia, ma, ir, independence_duration, year, _):
    if(ia == None or ma == None or ir == None or int(ia) <= 0 or int(ma) <= 0 or int(ir) <= 0):
        return
    ia = int(ia)
    ma = int(ma)
    ir = float(ir)
    actual_total_wealth = math.get_total_wealth(ia, ma, year, ir)
    actual_monthly_income = math.get_monthly_income(actual_total_wealth, independence_duration)

    return actual_monthly_income, actual_total_wealth