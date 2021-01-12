import dash  
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.express as px 
import plotly.graph_objects as go
import pandas as pd

app = dash.Dash(__name__)
server = app.server

df = pd.read_csv('pred1.csv')
dff = pd.read_csv('pred5.csv')


app.layout = html.Div([
    
    html.H1("Friday January 8th, 2021",style={'text-align':'center'}),
    html.H5("Training: 12/27/1950 - 12/24/2020",style={'text-align':'center'}),

    dcc.Dropdown(id="slct_year",
                options=[
                    {'label':'1 day','value':'1 day'},
                    {'label':'5 days','value':'5 days'}],
                multi=False,
                value='1 day',
                style={'width':'50%'},
                clearable = False,
                ),
    html.Br(),
    html.Div(id='output_container'),
    html.Br(),
    
    dcc.Graph(id='my_graph')
])



@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_graph', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)


def update_output(option_slctd):

    
    
    if option_slctd =='1 day':
        container = "Monday January 11th, 2020: {}".format('$3637.29')

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['time'], y=df['true'], name = 'True Price',
                                 line=dict(color='navy', width=2)))
        fig.add_trace(go.Scatter(x=df['time'], y=df['pred'], name = 'Predicted Price',
                                 line=dict(color='lime', width=2)))
    else:
        container = "Friday January 15th, 2020: {}".format('$3323.00')
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dff['time'], y=dff['true'], name = 'True Price',
                                 line=dict(color='navy', width=2)))
        fig.add_trace(go.Scatter(x=dff['time'], y=dff['pred'], name = 'Predicted Price',
                                 line=dict(color='coral', width=2)))
    return container, fig



if __name__ == '__main__':
    app.run_server(debug=True,use_reloader=False)