#Dash simple example
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from plotly import tools

df = pd.read_csv("DadesSabadell/residus.csv",sep=';')
df.sort_values(by="Anyo",inplace = True)

materials = list(df.NomMaterial.unique())
materials.remove("Resta")

pd.pivot_table(df,columns="Anyo", index = "NomMaterial", values="Quantitat")

minim = 0
maxim = 1000
pas = 100

app = dash.Dash()
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

app.layout = html.Div([html.Div([dcc.Graph(id='residus_graph')],
                                style={'height':'80%','padding': '0px 20px 20px 20px'}),
                                html.Div([html.H5("Materials amb mitjana de tones per any més grans que:"),
                                    dcc.Slider(id='avg-tones',step = pas,min=minim,max=maxim,value=maxim/2,       
                                            marks={ str(tones): {'label':str(tones)} for tones in range(minim,maxim+pas,pas)})],
                       style={'margin':'auto','height':'20%','width': '70%', 'padding': '0px 0px 40px 40px',"display":'inline_block'})])

@app.callback(
    dash.dependencies.Output('residus_graph', 'figure'),
    [dash.dependencies.Input('avg-tones', 'value')])

def update_figure(avg_tones):
    fig = tools.make_subplots(rows=2, cols=1,shared_xaxes=True, vertical_spacing=0.001)
    traces = []
    
    filtered= df[df['NomMaterial'] =="Resta"]
    trace_Resta = go.Scatter(
                            x=filtered['Anyo'],y=filtered['Quantitat'],text="Resta",
                            mode='lines+markers',
                            opacity=0.7,
                            marker={
                                'size': 15,
                                'line': {'width': 0.5, 'color': 'white'}
                            },
                            name="Resta"
                        )  
    
    filtered = df[df['NomMaterial'].isin(materials)].groupby("Anyo").sum()
    trace_Total= go.Scatter(                      
                            x=filtered.index,y=filtered['Quantitat'],text="Total Materials",
                            mode='lines+markers',
                            opacity=0.7,
                            marker={
                                'size': 15,
                                'line': {'width': 0.5, 'color': 'white'}
                            },
                            name="Total Materials",
                            
                        )   
    
    fig.append_trace(trace_Resta, 1, 1)
    fig.append_trace(trace_Total, 1, 1)
    
    for i in materials :
        filtered= df[df['NomMaterial'] == i]
        y=filtered['Quantitat']
        if (y.mean()>avg_tones) :
            x=filtered['Anyo']
            traces.append(go.Scatter(x=x,y=y,text=i,mode='markers',opacity=0.7,
                                marker={
                                    'size': 15,
                                    'line': {'width': 0.5, 'color': 'white'}
                                }, name=i[0:30])) 
    for trace in traces:
        fig.append_trace(trace, 2, 1)


    fig['layout'].update(height=600,title="Residus a Sabadell", margin={'l': 50, 'b': 40, 't': 40, 'r': 50},
              yaxis1={"title":"Totals"}, yaxis2={"title":"Materials"},hovermode="closest")
    return fig


if __name__ == '__main__':
    app.run_server()