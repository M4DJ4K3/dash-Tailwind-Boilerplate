import dash
from dash import html

dash.register_page(__name__, path='/')

layout = html.Div([
    html.H1('This is our Home page', className="text-2xl"),
    html.Div('This is our Home page content.'),
])