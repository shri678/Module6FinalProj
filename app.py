import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

url1 = 'https://raw.githubusercontent.com/shri678/DataViz1/master/Module6IPL%20(1).csv'
df3 = pd.read_csv(url1, index = 'teams')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div([
    html.H3("IPL Team level Statistics"),
        html.Div([
        dcc.Dropdown(
            id='IPLStat', clearable=False,
            value='toss_Matchwins', options=[
                {'label': c, 'value': c}
                for c in df3.columns
            ], multi = False),
    ],style={'display': 'inline', 'width': '15%'}),
        
        html.Div([
        dcc.Graph(id='graph'),
    ],style={'display': 'inline-block', 'width': '45%'}),
        
        html.Div([
       dcc.Graph(id='graph_2'),
    ],style={'display': 'inline-block', 'width': '55%'})
])


@app.callback(
    [dash.dependencies.Output('graph', 'figure'),dash.dependencies.Output('graph_2', 'figure')],
    [dash.dependencies.Input("IPLStat", "value")]
)


def multi_output(IPLStat):

    #fig1 = px.pie(df3, x=df3.index, y=teams)
    fig1 = px.pie(df3, values= IPLStat, names=df3.index, title='IPL pie chart')
    fig2 = px.bar(df3, x=df3.index, y=IPLStat)
    
  
    
    fig2.update_layout(
    legend_title_text='Teams',
    yaxis_title=IPLStat,
    )


    return fig1, fig2

if __name__ == '__main__':
    app.run_server()
