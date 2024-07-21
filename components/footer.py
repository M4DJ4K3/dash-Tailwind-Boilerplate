from dash import html, dcc, callback, Output, Input

def Footer():

    return html.Div([
        html.Hr(),
        html.Div('Footer', className="mt-5 w-full gap-4 flex flex-col justify-center items-center")
    ], className="w-full mt-5")
