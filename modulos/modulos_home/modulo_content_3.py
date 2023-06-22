#dash
from dash import dcc, html

#plotly
import plotly.graph_objs as go
from plotly.graph_objects import Layout

#dash-bootstrap-components
import dash_bootstrap_components as dbc

#dash-bootstrap-templates

#dash_mantine_components
import dash_mantine_components as dmc

#dash-iconify

#paginas

#modulos
from modulos.modulos_banner.banner_05 import banner_05
from modulos.modulos_banner.banner_05_mob import banner_05_mob
from modulos.modulos_banner.banner_06 import banner_06
from modulos.modulos_banner.banner_07 import banner_07


#callbacks / layouts

#outros

#fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 1, 2])])
fig = go.Figure()

def create_modulo_content_3():
    
    modulo = html.Div(
    
    dbc.Container(
        [
        html.Div(
        [
            dmc.Space(h=40), 
            dbc.Row(
            [
            
                dbc.Col([

                    html.Div(
                    [
                        dmc.Space(h=20),
                        dbc.Card([           
                            dbc.CardBody([  
                                html.Div([
                                    #html.H5("Percentual alocado por setor econômico:", className="card-title text-md-center"),
                                    dcc.Graph(
                                        config = {'displaylogo': False,
                                            'displayModeBar': False},
                                        id='graph_acoes',
                                        #figure = go.Figure(data=[go.Pie(labels=None, values=None, hoverinfo="label+percent", hole=.3 )], layout_showlegend=True,)
                                        figure = go.Figure(layout = Layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', xaxis= dict(visible=False), yaxis= dict(visible=False), font_color = 'rgba(0,0,0,0)', autosize=True, width=810, height=460, ), )#margin=dict(l=50, r=50, t=50, b=50))),
                                    ),
                                ],         
                                ),   
                            ], 
                            ),                  
                        ],id = 'card_div_graph3', color="dark",
                        ),
                    ],id = "div_graph3", style={'display':'none'}
                    ),

                    html.Div(
                    [
                        dbc.Card([
                                        
                            dbc.CardBody([

                            dmc.Space(h=180),
                                    
                            html.Div(
                                    dbc.Spinner(spinner_style={"width": "100px", "height": "100px"},color="info", id = "spinner_grafico2"),
                                    #id ="div_spinner_grafico2", className= 'text-md-center',style = {"max-height": "500px", "padding-top": "175px"} 
                                ),  
                            dmc.Space(h=180),

                            ],style = {"text-align": "center"},
                            ),
                        ],id = 'card_div_spinner_grafico3', color="dark", style = {"height": "500px"}, 
                        ),

                    ],id ="div_spinner_grafico3"
                    ),

                    

                  
                    #banner_5
                    html.Div(
                    [  
                        html.Div(
                            dmc.Text("PUBLICIDADE", size="xs", color="gray",align="center"),
                        style = {'height':'20px',
                        'margin-top':'30px',
                        },
                        id = 'banner_5_p', 
                        ),
                        html.Div(
                            banner_05(),
                        style={             
                        'height':'250px',
                        #'width': '728px',
                        },       
                        id = 'banner_5', 
                        ),
    
                    ], id = 'div_content_banner_5', 
                    ),
                    
                    #banner_5_mobile
                    html.Div(
                    [
                        html.Div(
                            dmc.Text("PUBLICIDADE", size="xs", color="gray",align="center"),
                        style = {'height':'20px',
                        'margin-top':'30px',
                                                },
                        id = 'banner_5_p_mobile', 
                        
                        ),
                        html.Div(
                            banner_05_mob(),
                        style={             
                        
                        'height':'300px',
                        },       
                        id = 'banner_5_mobile', 
                        ),
    
                        #dmc.Space(h=20),

                    ], id = 'div_content_banner_5_mobile', 
                    style = {'display': 'none'}
                    ),

                    html.Div(
                    [
                        dmc.Space(h=50),
                        dbc.Card([           
                            dbc.CardBody([  
                                html.Div([
                                    #html.H5("Percentual alocado por setor econômico:", className="card-title text-md-center"),
                                    dcc.Graph(
                                        config = {'displaylogo': False,
                                            'displayModeBar': False},
                                        id='graph_setor',
                                        #figure = go.Figure(data=[go.Pie(labels=None, values=None, hoverinfo="label+percent", hole=.3 )], layout_showlegend=True,)
                                        figure = go.Figure(layout = Layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', xaxis= dict(visible=False), yaxis= dict(visible=False), font_color = 'rgba(0,0,0,0)', autosize=True, width=810, height=460, ), )#margin=dict(l=50, r=50, t=50, b=50))),
                                    ),
                                ],         
                                ),   
                            ], 
                            ),                  
                        ],id = 'card_div_graph2', color="dark", #style = {"min-width": "650px"},
                        ),
                    ],id = "div_graph2", style={'display':'none'}
                    ),

                    html.Div(
                    [
                        dmc.Space(h=50),
                        dbc.Card([
                                        
                            dbc.CardBody([
                            
                            dmc.Space(h=180),
                                    
                            html.Div(
                                    dbc.Spinner(spinner_style={"width": "100px", "height": "100px"},color="info", id = "spinner_grafico2"),
                                    #id ="div_spinner_grafico2", className= 'text-md-center',style = {"max-height": "500px", "padding-top": "175px"} 
                                ),  
                            dmc.Space(h=180),  
                            ],style = {"text-align": "center"},
                            ),
                        ],id = 'card_div_spinner_grafico2', color="dark", style = {"height": "500px"},
                        ),

                    ],id ="div_spinner_grafico2"
                    ),
                    

                ],md=8, id = 'col_acoes_setor',
                ),

                dbc.Col([

                #banner_6
                html.Div(
                [
                    
                    html.Div(
                        dmc.Text("PUBLICIDADE", size="xs", color="gray",align="center"),
                    style = {'height':'20px',
                    #'margin-top':'30px',
                    },
                    id = 'banner_6_p', 
                     ),
                    html.Div(
                        banner_06(),
                    style={             
                    'text-align': 'center',
                    'height':'711px',
                    'width': '400px',
                    },       
                    id = 'banner_6', 
                    ),
   
                    

                ], id = 'div_content_banner_6'
                ),
                   
           

                #banner_7
                html.Div(
                [
                    
                    html.Div(
                        dmc.Text("PUBLICIDADE", size="xs", color="gray",align="center"),
                    style = {'height':'20px',
                    'margin-top':'30px',
                    },
                    id = 'banner_7_p', 
                     ),
                    html.Div(
                        banner_07(),
                    style={             
                    'text-align': 'center',
                    'height':'580px',
                    'width': '400px',
                    },       
                    id = 'banner_7', 
                    ),
   
                    

                ], id = 'div_content_banner_7'
                ),

                    
                ],md=4, id = 'col_banner'
                ),

                
            
            ],className="gx-5",
            ),
            dbc.Row(
            [
                html.Div(
                [
                    dmc.Modal(
                    
                        title="Olá, Visitante!",
                  
                        centered=True,
                        #children=[dmc.Text("This is a vertically centered modal.")],
                        id="modal"
                    ),
                ]
                )

                

            ]),

            dbc.Row(
            [
                dmc.Space(h=50),
                html.Div(
                [
                    dbc.Button("RODAR BACKTEST", size="lg", id="btn_ainda_nao_logou", n_clicks=0, color="success", outline=True, style = {'display':'none'}, href = '/login' ),
                    dbc.Button("RODAR BACKTEST", size="lg", id="btn_rodar", n_clicks=0, color="success", outline=True,    style = {'display':'none'},),
                    dbc.Button("RODAR BACKTEST", size="lg", id="btn_ainda_nao_verificou_email", n_clicks=0, color="success", outline=True,    style = {'display':'none'},),
                    #dbc.Button("RODAR BACKTEST_logado+email+não_verificado+3vezes", size="lg", id="btn_ainda_nao_verificou_email_3vezes", n_clicks=0, color="success", outline=True,    style = {'display':'block'},),
                ],  #className="d-grid gap-2 col-4 mx-auto", 
                style = {'text-align':'center'},
                id = "div_btn_modal"
                ),
            dmc.Space(h=50),
            
                                        


            

            #dcc.Graph(figure=fig, id='graph_r_11'),

           
           
            ]
            )


        ], style={
        #'border': 'thin grey solid',
        }),#divisao_1
        dmc.Space(h=50),
    ]
    ),#className="p-xl-5", 
    id =  "modulo_content_3",
    #style = {'display':'none',}
    
    )




    return modulo