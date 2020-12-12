
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

url1 = 'https://raw.githubusercontent.com/shri678/DataViz1/master/Module6IPL%20(5).csv'
df3 = pd.read_csv(url1)

urlbowler = 'https://raw.githubusercontent.com/shri678/DataViz1/master/ODI_rankings%20-%20Bowlers.csv'
urlbatsman = 'https://raw.githubusercontent.com/shri678/DataViz1/master/ODI_rankings%20-%20Batsman.csv'
df_bowler = pd.read_csv(urlbowler)
df_batsman = pd.read_csv(urlbatsman)

batscount = df_batsman.TEAM.value_counts().reset_index().rename(columns = {'index': 'Country', 'TEAM': 'Number of players in top 100'})


df3 = df3.set_index('teams')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
css_stylesheets = ['https://www.w3schools.com/w3css/4/w3.css']


app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

server = app.server

app.layout = html.Div([
    html.Div([
              html.Img("https://raw.githubusercontent.com/shri678/DataViz1/master/Daco_4377152.png"),
              html.H1("Cricket Statistics"),
    ],style={'background-color':'lightblue', 'text-align':'center', 'color' : 'darkorange'}),
    

    html.H3('Indian Premier League Statistics'),
    html.Details([
        html.Summary('Background'),
        html.P('The Indian Premier League (IPL) is a professional Twenty20 cricket league in India usually contested between March and May of every year by eight teams representing eight different cities or states in India.'),
    ],style={'display': 'inline-block', 'width': '100%', 'background-color':'grey', 'color': 'white'}),
        html.P("Select Metric for graph"),
        html.Div([
        dcc.Dropdown(
            id='IPLStat', clearable=False,
            value='Total Matches Played', options=[
                {'label': c, 'value': c}
                for c in df3.columns
            ], multi = False),
    ],style={'display': 'inline', 'width': '5%'}),
        
        html.Div([
        dcc.Graph(id='graph'), 
    ],style={'display': 'inline-block', 'width': '50%', 'bgcolor': 'gray'}),
        
        html.Div([
       dcc.Graph(id='graph_2'),
        
    ],style={'display': 'inline-block', 'width': '50%'}),
        
        html.Div([
       dcc.Graph(id='graph_3'),
    ],style={'display': 'inline-block', 'width': '50%'}),
        
        
        html.H3("One Day International Statistics"),
       

        html.Details([
        html.Summary('Background'),
        html.P('ODI is a form of limited overs cricket, played between two teams with international status, in which each team faces a fixed number of overs, currently 50, with the game lasting up to 8 hours.'),
    ],style={'display': 'inline-block', 'width': '100%', 'background-color':'grey', 'color': 'white'}),
        
        html.Div([
       dcc.Graph(id='graph_4'),
    ],style={'display': 'inline-block', 'width': '50%'})
], style={'background-color':'lightblue','color' : 'darkorange'})


@app.callback(
    [dash.dependencies.Output('graph', 'figure'),dash.dependencies.Output('graph_2', 'figure'),dash.dependencies.Output('graph_3', 'figure'), dash.dependencies.Output('graph_4', 'figure')],

    [dash.dependencies.Input("IPLStat", "value")]
)


def multi_output(IPLStat):

  
    fig1 = px.pie(df3, values= IPLStat, names=df3.index, title=IPLStat, hole = 0.1)

    #fig1.update_traces(textinfo='percent+label')
    fig1.update_layout(title_x = .5, legend=dict(orientation="h",yanchor="bottom",y=-0.7,xanchor="left",x=0))


    fig2 = px.bar(df3, x=df3.index, y=IPLStat)
    fig2.update_layout(title = IPLStat + " by every IPL team",title_x = .5, legend_title_text='IPL Teams', yaxis_title=IPLStat)
    
    max_x = df3['Win by Wickets'].max()+20
    max_y = df3['Win by Runs'].max()-20

    fig3 = px.scatter(df3, x = 'Win by Wickets', y = 'Win by Runs', size = 'Matches won',
                color = df3.index, hover_name = df3.index, size_max = 60, title = 'Total Wins by Runs vs Wins by Wickets of all IPL teams',
                 range_x = [0,max_x], range_y = [0,max_y])
    fig3.update_layout(title_x = .5)
  
    fig4 = px.bar(batscount, x=batscount['Country'], y=batscount['Number of players in top 100'])
    fig4.update_layout(title =  'One Day International Rankings for Batsman ',title_x = .5)


    return fig1, fig2, fig3, fig4

if __name__ == '__main__':
    app.run_server()
