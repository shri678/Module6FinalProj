
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
bowlscount = df_bowler.TEAM.value_counts().reset_index().rename(columns = {'index': 'Country', 'TEAM': 'Number of players in top 100'})


df3 = df3.set_index('teams')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
css_stylesheets = ['https://www.w3schools.com/w3css/4/w3.css']


app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

server = app.server

app.layout = html.Div([
    html.Div([
              html.Img(src = "https://raw.githubusercontent.com/shri678/DataViz1/master/Daco_4377152.png",style={'height':'10%', 'width':'5%', 'display': 'inline-block','text-align': 'left'}),
              html.H1("Cricket Statistics",style={'height':'5%', 'width':'95%', 'display': 'inline-block', 'text-align': 'center', 'vertical-align': 'middle'}),
            ],style={'background-color':'DodgerBlue', 'text-align':'center', 'color' : 'White'}),
    

    

    #html.H3('Indian Premier League Statistics'),
    # https://www.britannica.com/topic/Indian-Premier-League

    html.Details([
        html.Summary('Indian Premier League Statistics',style={'background-color':'DeepSkyBlue','color' : 'White', 'text-indent': '0%', 'font-size': '120%'}),

        html.P('Indian Premier League (IPL), Indian professional Twenty20 (T20) cricket league established in 2008. The league, which is based on a round-robin group and knockout format, has teams in major Indian cities. Matches generally begin in late afternoon or evening so that at least a portion of them are played under floodlights at night to maximize the television audience for worldwide broadcasts. The top four teams contest three play-off matches, with one losing team being given a second chance to reach the final, a wrinkle aimed at maximizing potential television revenue. The play-off portion of the tournament involves the four teams that finished at the top of the tables in a series of knockout games that allows one team that lost its first-round game a second chance to advance to the final match'),

        html.P('With the advent of the IPL, almost overnight the world’s best cricketers—who had seldom made the kind of money earned by their counterparts in other professional sports—became millionaires. The owners of the IPL franchises, who included major companies, Bollywood film stars, and media moguls, bid for the best players in auctions organized by the league. The eight founding franchises were the Mumbai Indians, the Chennai Super Kings, the Royal Challengers Bangalore, the Deccan Chargers (based in Hyderabad), the Delhi Daredevils, the Punjab XI Kings (Mohali), the Kolkata Knight Riders, and the Rajasthan Royals (Jaipur). In late 2010 two franchises, Rajasthan and Punjab, were expelled from the league by the BCCI for breeches of ownership policy, but they were later reinstated in time for the 2011 tournament. Two new franchises, the Pune Warriors India and the Kochi Tuskers Kerala, joined the IPL for the 2011 tournament. The Kochi club played just one year before the BCCI terminated its contract. In 2013 the Deccan Chargers were replaced in the IPL by the Sunrisers Hyderabad.'),
  
        html.Div([
          html.H6("Select Metric for graph ", style={'display':'inline', 'text-indent': '2%', 'color':'Black', 'background-color':'White'}),
          dcc.Dropdown(
            id='IPLStat', clearable=False,
            value='Total Matches Played', options=[
                {'label': c, 'value': c}
                for c in df3.columns
            ], multi = False),
        ],style={'display': 'inline', 'width': '60%', 'color': 'black', 'text-indent': '0%'}),
        
        html.Div([
        dcc.Graph(id='graph'), 
          ],style={'display': 'inline-block', 'width': '50%'}),
        
        html.Div([
          dcc.Graph(id='graph_2'),    
        ],style={'display': 'inline-block', 'width': '50%'}),
        
        html.Div([
          dcc.Graph(id='graph_3'),
        ],style={'display': 'inline-block', 'width': '80%'}),
        
    ],style={'display': 'inline-block', 'width': '100%', 'background-color':'DeepSkyBlue', 'color': 'White', 'text-indent': '5%'}),
        
        
       
       

        html.Details([
        html.Summary('One Day International',style={'color' : 'White', 'text-indent': '0%', 'font-size': '120%'}),

        html.P('A One Day International (ODI) is a form of limited overs cricket, played between two teams with international status, in which each team faces a fixed number of overs, currently 50 (used to be 60 overs until 1983), with the game lasting up to 8 hours. The Cricket World Cup, generally held every four years, is played in this format. One Day International matches are also called Limited Overs Internationals (LOI), although this generic term may also refer to Twenty20 International matches. They are major matches and considered the highest standard of List A, limited-overs competition.'),

        html.Div([
            dcc.Graph(id='graph_4'),
          ],style={'display': 'inline-block', 'width': '50%'}),
        
        html.Div([
            dcc.Graph(id='graph_5'),
          ],style={'display': 'inline-block', 'width': '50%'}),
        
        html.Div([
            dcc.Graph(id='graph_6'),
          ],style={'display': 'inline-block', 'width': '50%'}),

        html.Div([
            dcc.Graph(id='graph_7'),
          ],style={'display': 'inline-block', 'width': '50%'}),


    ],style={'display': 'inline-block', 'width': '100%', 'background-color':'SkyBlue', 'color': 'White', 'text-indent': '5%'}),


    html.Details([
      html.Summary('Data Sources',style={'color' : 'Black', 'text-indent': '0%', 'font-size': '120%'}),
      dcc.Link('IPL Data', href='https://www.kaggle.com/nowke9/ipldata'),
      html.Br(),
      dcc.Link('One Day International data for batsmen and bowlers', href = 'https://www.icc-cricket.com/rankings/mens/overview')
    ],style={'display': 'inline-block', 'width': '100%', 'background-color':'White', 'color': 'Black'}),
], style={'background-color':'DeepSkyBlue','color' : 'white','margin-left':'1%'})


@app.callback(
    [dash.dependencies.Output('graph', 'figure'),dash.dependencies.Output('graph_2', 'figure'),
     dash.dependencies.Output('graph_3', 'figure'), dash.dependencies.Output('graph_4', 'figure'),
     dash.dependencies.Output('graph_7', 'figure'), dash.dependencies.Output('graph_6', 'figure'),
     dash.dependencies.Output('graph_5', 'figure')
     ],

    [dash.dependencies.Input("IPLStat", "value")]
)


def multi_output(IPLStat):

  
    fig1 = px.pie(df3, values= IPLStat, names=df3.index, title=IPLStat, hole = 0.4)
    fig1.update_layout(title_x = .5, plot_bgcolor = 'coral')


    fig2 = px.bar(df3, x=df3.index, y=IPLStat)
    fig2.update_layout(title = IPLStat + " by every IPL team",title_x = .5, xaxis_title ='IPL Teams', yaxis_title=IPLStat)
    
    max_x = df3['Win by Wickets'].max()+20
    max_y = df3['Win by Runs'].max()+20

    fig3 = px.scatter(df3, x = 'Win by Wickets', y = 'Win by Runs', size = 'Matches won',
                color = df3.index, hover_name = df3.index, size_max = 100, title = 'Total Wins by Runs vs Wins by Wickets of all IPL teams',
                 range_x = [0,max_x], range_y = [0,max_y])
    fig3.update_layout(title_x = .5)
  
    fig4 = px.bar(batscount, x=batscount['Country'], y=batscount['Number of players in top 100'])
    fig4.update_layout(title =  'Number of Batsmen in Top 100 for each Nation ',title_x = .5, yaxis_title = 'Number of batsmen in top 100')



    df_bowler_top20 = df_bowler.query('Pos < 21')
    df_bowler_top20.drop(columns = ['TEAM', 'Team against', 'Date', 'Pos'], inplace=True, axis= 1)
    df_bowlers_top20 = df_bowler_top20.melt(['Name'], var_name='Rating type', value_name='Rating value')
    df_bowlers_top20.replace({'RATING': 'Current Rating'}, inplace=True)

    fig5 = px.line(df_bowlers_top20, x="Name", y="Rating value", title='Rating Comparison of Top 20 Bowlers (Highest vs Present)', color = 'Rating type')
    fig5.update_layout(
        title_x = .5
    )
    
    fig6 = px.bar(bowlscount, x=bowlscount['Country'], y=bowlscount['Number of players in top 100'])
    fig6.update_layout(title =  'Number of Bowlers in Top 100 for each Nation ',title_x = .5, yaxis_title = 'Number of bowlers in top 100')


    df_batsman_top20 = df_batsman.query('POS < 21')
    df_batsman_top20.drop(columns = ['TEAM', 'Team against', 'Date', 'POS'], inplace=True, axis= 1)
    df_batsmen_top20 = df_batsman_top20.melt(['PLAYER'], var_name='Rating type', value_name='Rating value')
    df_batsmen_top20.replace({'RATING': 'Current Rating'}, inplace=True)

    fig7 = px.line(df_batsmen_top20, x="PLAYER", y="Rating value", title='Rating Comparison of Top 20 Batsmen (Highest vs Present)', color = 'Rating type')
    fig7.update_layout(
        title_x = .5
    )

    return fig1, fig2, fig3, fig4, fig5, fig6, fig7

if __name__ == '__main__':
    app.run_server()
