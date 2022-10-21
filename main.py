from dash import Dash, dcc, html

app = Dash(__name__)

app.layout = html.Div([
    html.Div([
        dcc.Markdown('''
        # 🏖 When to stop working ?
        
        🎯 **Objectives :** Explain the power of compound interest and give an overview of the wealth to accumulate 
        in order to achieve financial independence in a country.
        
        👨‍💻**Authors :** `Alexis Allemann`, `Corpataux Sam`, `Koch Gaël` 
         
         
         ## 💰 Investment configuration
        '''),
        [],
        dcc.Markdown('''
        ## 📈 Compound interest over time
        '''),
        [],
        dcc.Markdown('''
        ## 🌏 Where you can go live
        ''')
    ], className='markdown-body'),
])

app.run_server(debug=True)
