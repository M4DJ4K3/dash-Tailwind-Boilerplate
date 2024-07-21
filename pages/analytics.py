# app.py
import pandas as pd
import plotly.express as px
from dash import html, dcc, register_page, dash_table, callback, Input, Output
from components.histogram import Histogram

register_page(
    __name__,
    path='/analytics-dashboard',
    title='Our Analytics Dashboard',
    name='Analytics'
)

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

layout = [
    html.H1(
        className='w-full text-3xl mb-4', 
        children='My First App with Data, Graph, and Controls'),

    html.Div(
        className='grid grid-cols-5 gap-4 flex flex-row gap-4', 
        children=[
            
            html.Div(
                className= "col-span-3", 
                children = [
                    html.H1('Table', className="3xl mb-4 font-bold"),
                    html.Div(className='align-middle', children=[
                        dash_table.DataTable(data=df.to_dict('records'), page_size=14, style_table={'overflowX': 'auto'})
                        ])
                    ]),
            
            html.Div(
                className= 'col-span-2', 
                children = [html.H1('Graphique', className="3xl mb-4 font-bold"),
                    html.Div(
                        className='flex flex-row gap-10 mb-5' , 
                        children=[
                                html.H1(children='Colonne choisie :'),
                                dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'],
                                value='lifeExp',
                                inline=True,
                                id='my-radio-buttons-final')
                        ]),
                                Histogram(df, component_id='histo-chart-final')
                    ]),
                ]),
    ]
