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
            id='teams', clearable=False,
            value='toss_Matchwins', options=[
                {'label': c, 'value': c}
                for c in df3.columns
            ], multi = True),
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
    [dash.dependencies.Input("teams", "value")]
)


def multi_output(teams):

    #fig1 = px.pie(df3, x=df3.index, y=teams)
    fig1 = px.pie(df3, values= df3.index, names='teams', title='IPL pie chart')
    fig2 = px.bar(df3, x=df3.index, y=teams)
    
    fig1.update_layout(
    yaxis_title= df3.column,
    showlegend = False
    )
    
    fig2.update_layout(
    legend_title_text='teams',
    yaxis_title='IPL',
    )

    fig1.update_xaxes(showspikes=True)
    fig1.update_yaxes(showspikes=True)

    return fig1, fig2

if __name__ == '__main__':
    app.run_server()
