# components/my_component.py
from dash import html, dcc, callback, Input, Output
import plotly.express as px

def Histogram(df, component_id):
    @callback(
        Output(component_id, 'figure'),
        Input('my-radio-buttons-final', 'value')
    )
    def update_graph(col_chosen):
        fig = px.histogram(df, x="continent", y=col_chosen, histfunc='avg')
        return fig

    return html.Div(className='six columns', children=[
        dcc.Graph(id=component_id)
    ])
