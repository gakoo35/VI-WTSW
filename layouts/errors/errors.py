from dash import html

not_found_layout = html.Div(
    [
        html.H1("404: Not found", className="text-danger"),
        html.Hr(),
        html.P(f"The pathname was not recognised..."),
    ],
    className="p-3 rounded-3",
)
