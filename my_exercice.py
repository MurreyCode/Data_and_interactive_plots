#Dash exercice
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from plotly import tools
import numpy as np

df = pd.read_csv("DadesBarcelona/2017_naixements_sexe.csv",sep=',')
pv = pd.pivot_table(df, columns="Sexe", index = "Nom_Districte", values="Nombre",  aggfunc='sum')

app = dash.Dash()
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

app.layout = html.Div([html.Div(
    [dcc.Graph(id='birth_bcn',figure = {
                                    'data':[
                                        {'x': pv.index, 'y': pv['Nenes'], 'type': 'bar', 'name': 'Nenes'},
                                        {'x': pv.index, 'y': pv['Nens'], 'type': 'bar', 'name': 'Nens'},
                                        {'x': pv.index, 'y': pv['Nenes'], 'type': 'lines+markers', 'name': 'Nenes'},
                                        {'x': pv.index, 'y': pv['Nens'], 'type': 'lines+markers', 'name': 'Nens'},
                                        ],
                                        'layout':{
                                            'title' : 'Niñas y niños nacidos en Barcelona por distrito'
                                                }
                                      } )
                                ],
                                style={'height':'80%','padding': '0px 20px 20px 20px'},
                                
                               )])




if __name__ == '__main__':
    app.run_server(debug=True)


if __name__ == '__main__':
    app.run_server()