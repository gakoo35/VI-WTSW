import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

from app import app
from layouts.about.about import about_layout
from layouts.concepts.concepts import concepts_layout
from layouts.errors.errors import not_found_layout
from layouts.home.home import home_layout
from styles.styles import CONTENT_STYLE

appbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/", active="exact")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Visualisation concepts", href="concepts"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("About", href="about"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="When to stop working ?",
    brand_href="",
    color="secondary",
    dark=True,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    appbar,
    content
])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return home_layout
    elif pathname == "/concepts":
        return concepts_layout
    elif pathname == "/about":
        return about_layout
    return not_found_layout


if __name__ == "__main__":
    app.run_server(port=8989, debug=True)
