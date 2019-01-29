#Dash simple example
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([html.H1("Hello Dash!"),
                       
              html.Div('''
                Dash: A web application framework for Python.
              '''),
                      
              dcc.Graph(id='exmaple-graph',
                        figure = {
                            'data':[
                                {'x': [1, 2, 3], 'y': [4.2, 1.8, 2.7], 'type': 'bar', 'name': 'Sabadell'},
                                {'x': [1, 2, 3], 'y': [2.8, 4.9, 5.1], 'type': 'bar', 'name': 'Barcelona'},
                            ],
                            'layout':{
                                'title' : 'Dash Data Visualisation'
                            }
              })
])

if __name__ == '__main__':
    app.run_server(debug=True)