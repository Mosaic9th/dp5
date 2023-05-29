#dash
from dash import dcc, html

#plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.graph_objects import Layout

#dash-bootstrap-components
import dash_bootstrap_components as dbc

#dash-bootstrap-templates

#dash_mantine_components
import dash_mantine_components as dmc

#dash-iconify
from dash_iconify import DashIconify

#paginas

#modulos

#callbacks / layouts

#outros
import numpy as np

botao_reenviar_verificacao =  dbc.Button("Reenviar e-mail de verificação", size="lg", id = 'btn_reenvio_email_confirmacao', color="info", outline=True, className="d-grid gap-2 col-10 mx-auto p-2 mb-2", n_clicks=0, style = {'width':'340px'}),

msg = html.Div(children = None, id = 'mensagem_email_confirmacao')


alerts = html.Div(
            [
                    
                
            
            ])

reenvio_1  =html.Div(

        [
        html.Div(
                [
            dmc.Space(h=100),
            
            dbc.Row(
            [
                msg,

            ]
            ),

            dmc.Space(h=30),

            
      

            dbc.Row(

                [
                dbc.Col (
                   html.A(dbc.Button("Já abri o e-mail de verificação", size="lg", id="local-button", color="info", outline=True, n_clicks=0, style = {'width':'340px'},),href='/'),
                md = 6
                ),
                dbc.Col (

                    botao_reenviar_verificacao,

                md = 6
                )
                ], className="flex-grow-1" 
            ),

            dmc.Space(h=60),

            #alerts,
            dbc.Alert(
                [
                    html.I(className="bi bi-check-circle-fill me-4", 
                    ), "E-mail de confirmação enviado!", 
                ],
                color="success",
                className="d-flex align-items-center",
                id= "success_reenvio_email_verificacao_1",
                is_open = False,  

                ),
                
                dbc.Alert(
                [
                    #html.I(className="bi bi-x-octagon-fill me-4", 
                    #), "Quantidade se envios excedida, tente novamente mais tarde", 
                ],
                color="danger",
                className="d-flex align-items-center",
                id= "danger_reenvio_email_verificacao_1",
                is_open = False,  

                ),

            dmc.Space(h=100),
        ]
        )

        ]
)

reenvio_2  = html.Div(

        [
        html.Div(
                [
            dmc.Space(h=100),

            
            
            dbc.Row(
            [
                msg,

            ]
            ),

            dmc.Space(h=30),

            dbc.Row(

                [
                dbc.Col (
                    dbc.Button("Refazer login", size="lg", id="btn_logar_novamente_email_maior", color="info", outline=True, className="d-grid gap-2 col-10 mx-auto p-2 mb-2", n_clicks=0, style = {'width':'340px'}),
                md = 6
                ),
                dbc.Col (

                    botao_reenviar_verificacao,

                md = 6
                )
                ], className="flex-grow-1" 
            ),

            dmc.Space(h=60),

            #alerts,
            dbc.Alert(
                [
                    html.I(className="bi bi-check-circle-fill me-4", 
                    ), "E-mail de confirmação enviado!", 
                ],
                color="success",
                className="d-flex align-items-center",
                id= "success_reenvio_email_verificacao_2",
                is_open = False,  

                ),
                
                dbc.Alert(
                [
                    #html.I(className="bi bi-x-octagon-fill me-4", 
                    #), "Quantidade se envios excedida, tente novamente mais tarde", 
                ],
                color="danger",
                className="d-flex align-items-center",
                id= "danger_reenvio_email_verificacao_2",
                is_open = False,  

                ),

            dmc.Space(h=100),
        ]
        )

        ]
)


def create_modulo_content_r_1():
    
    modulo  = html.Div(

        [

        html.Div(
        [
    
        dbc.Container(
        [
            html.Div(
            [
                html.Hr(),

                dmc.Space(h=50), 

                html.H3("Resultados:", className="p-4 mb-4 text-md-center", style = {'text-align': 'center'}, ), 
                dmc.Space(h=10),

                

                                

                dbc.Row(
                [

                    dbc.Col(
                        [
                    
                        html.Div([

                            dbc.Row(
                                [
                                

                                #### RESUMO
                                html.H4("QUADRO RESUMO:", className="p-4 mb-4 text-md-center", style = {'text-align': 'center'}, ), 
                                #dmc.Space(h=10),
                                dbc.Card([
                                    
                                    
                                    dbc.CardBody([
                                        html.Div([
                                            


                                            #html.H5("RETORNO DA CARTEIRA (R$):", className="card-title"),
                                            dmc.Space(h=15),

                                            dbc.Row(
                                            [
                                                dbc.Col(

                                                [
                                                    
                                                    html.Div([

                                                        html.H6('Valor da carteira:'),
                                                        dmc.Space(h=5),
                                                        html.H6(id='leg_1', style = {'color': '#3498db'}),

                                                    ],
                                                    style={
                                                        #'border-right': 'thin white solid',
                                                        #'border-left': 'thin white solid',
                                                        #'border-top': 'thin white solid',
                                                        #'border-bottom': 'thin white solid',
                                                        #'height':'250px',
                                                        'text-align': 'center',
                                                        'background-color': '#222222',
                                                        "padding-top": '20px',
                                                        "padding-bottom": '20px',      
                                                    },
                                                   
                                                    ),
                                                ], md = 4,
                                                
                                                ),

                                                dbc.Col(
    
                                                [
        
                                                    html.Div([
                                                        html.H6('Soma dos aportes:'),
                                                        dmc.Space(h=5),
                                                        html.H6(id='leg_2', style = {'color': '#f39c12'}),

                                                    ],
                                                    style={
                                                        #'border-right': 'thin white solid',
                                                        #'border-left': 'thin white solid',
                                                        #'height':'250px',
                                                        'text-align': 'center',
                                                        'background-color': '#222222',
                                                        "padding-top": '20px',
                                                        "padding-bottom": '20px',    
                                                    },

                                                    ),
                                                        
                                                ], md = 4,
                                                
                                                ),

                                                dbc.Col(
                                                [
                                                    
                                                    html.Div([

                                                        html.H6('Rendimento:'),
                                                        dmc.Space(h=5),
                                                        html.Div(
                                                            [
                                                            dcc.Graph(
                                                                config = {'displaylogo': False,
                                                                    'scrollZoom': False,
                                                                    'displayModeBar': False,
                                                                    'editable': False,
                                                                    'showLink':False,

                                                                    },
                                                                id='leg_3',
                                                                figure = go.Figure()
                                                            ),

                                                        
                                                            ]
                                                        ),

                                                    ],
                                                    style={
                                                        #'border-right': 'thin white solid',
                                                        #'border-left': 'thin white solid',
                                                        #'height':'250px',
                                                        'text-align': 'center',
                                                        'background-color': '#222222',
                                                        "padding-top": '20px',
                                                        "padding-bottom": '27px',    
                                                    },
                                                    ),
                                                    
                                                ], md = 4,
                                               
                                                ),
                                                
                                            ], className="p-3 mb-2 text-md-center"
                                            ),

                                            

                                            dbc.Row(
                                            [
    
                                                dbc.Col(

                                                [
                                                    
                                                    html.Div([
                                                        
                                                        html.H6('Rebaixamento máximo vs início:'),
                                                        dmc.Space(h=5),
                                                        html.H6(id='rmi_txt', style = {'color': 'rgb(222,61,130)'}),

                                                    ],
                                                    style={
                                                        #'border-right': 'thin white solid',
                                                        #'border-left': 'thin white solid',
                                                        #'height':'250px',
                                                        'text-align': 'center',
                                                        'background-color': '#222222',
                                                        "padding-top": '20px',
                                                        "padding-bottom": '20px',    
                                                    },
                                                    )
                                                   
                                                    
                                                ], md = 4,
                                                
                                                ),

                                                dbc.Col(
                                                [
                                                    html.Div([
        
                                                        html.H6('Elevação máxima vs início:'),
                                                        dmc.Space(h=5),
                                                        html.H6(id='emi_txt', style = {'color': 'rgb(126,132,250)'}),

                                                    ],
                                                    style={
                                                        #'border-right': 'thin white solid',
                                                        #'border-left': 'thin white solid',
                                                        #'height':'250px',
                                                        'text-align': 'center',
                                                        'background-color': '#222222',
                                                        "padding-top": '20px',
                                                        "padding-bottom": '20px',    
                                                    },

                                                    )
                                                    
                                                ], md = 4,
                                                
                                                ),

                                                dbc.Col(
                                                [
                                                    
                                                    html.Div([

                                                        html.H6('Rentabilidade:'),
                                                        dmc.Space(h=5),
                                                        html.Div(
                                                            [
                                                            dcc.Graph(
                                                                config = {'displaylogo': False,
                                                                    'scrollZoom': False,
                                                                    'displayModeBar': False,
                                                                    'editable': False,
                                                                    'showLink':False,

                                                                    },
                                                                id='leg_4',
                                                                figure = go.Figure()
                                                            ),

                                                        
                                                            ]
                                                        ),

                                                    ],
                                                    style={
                                                        #'border-right': 'thin white solid',
                                                        #'border-left': 'thin white solid',
                                                        #'height':'250px',
                                                        'text-align': 'center',
                                                        'background-color': '#222222',
                                                        "padding-top": '20px',
                                                        "padding-bottom": '27px',    
                                                    },
                                                    ),
                                                    
                                                ], md = 4,
                                               
                                                ),

                                                
                                                
                                            ], className="p-3 mb-2 text-md-center"
                                            ),
                                            #dmc.Space(h=15),

                                            dbc.Row(
                                            [
                                                dbc.Col(

                                                [
                                                    
                                                    html.Div([
                                                        
                                                        html.H6('Ação com menor rentabilidade:'),
                                                        dmc.Space(h=5),
                                                        html.H6(id='pior_acao', style = {'color': 'rgb(222,61,130)'}),

                                                    ],
                                                    style={
                                                        #'border-right': 'thin white solid',
                                                        #'border-left': 'thin white solid',
                                                        #'height':'250px',
                                                        'text-align': 'center',
                                                        'background-color': '#222222',
                                                        "padding-top": '20px',
                                                        "padding-bottom": '20px',    
                                                    },
                                                    )
                                                   
                                                    
                                                ], md = 6,
                                                
                                                ),

                                                dbc.Col(
                                                [
                                                    html.Div([
        
                                                        html.H6('Ação com maior rentabilidade:'),
                                                        dmc.Space(h=5),
                                                        html.H6(id='melhor_acao', style = {'color': 'rgb(126,132,250)'}),

                                                    ],
                                                    style={
                                                        #'border-right': 'thin white solid',
                                                        #'border-left': 'thin white solid',
                                                        #'height':'250px',
                                                        'text-align': 'center',
                                                        'background-color': '#222222',
                                                        "padding-top": '20px',
                                                        "padding-bottom": '20px',    
                                                    },

                                                    )
                                                    
                                                ], md = 6,
                                                
                                                ),

                                                
                                                
                                            ], className="p-3 mb-2 text-md-center"
                                            ),

                                            #dmc.Space(h=15),

                                            dbc.Row(
                                            [
                                                dbc.Col(

                                                [
                                                    html.Div([
        
                                                        html.H6('Setor econômico com menor rentabilidade:'),
                                                        dmc.Space(h=5),
                                                        html.H6(id='pior_setor', style = {'color':'rgb(222,61,130)'}),
                                                   
                                                    ],
                                                    style={
                                                        #'border-right': 'thin white solid',
                                                        #'border-left': 'thin white solid',
                                                        #'height':'250px',
                                                        'text-align': 'center',
                                                        'background-color': '#222222',
                                                        "padding-top": '20px',
                                                        "padding-bottom": '20px',    
                                                    },

                                                    )
                                                    
                                                ], md = 6,
                                                
                                                ),

                                                dbc.Col(
                                                [
                                                    html.Div([

                                                        html.H6('Setor econômico com maior rentabilidade:'),
                                                        dmc.Space(h=5),
                                                        html.H6(id='melhor_setor', style = {'color': 'rgb(126,132,250)'}),
        
                                                        

                                                    ],
                                                    style={
                                                        #'border-right': 'thin white solid',
                                                        #'border-left': 'thin white solid',
                                                        #'height':'250px',
                                                        'text-align': 'center',
                                                        'background-color': '#222222',
                                                        "padding-top": '20px',
                                                        "padding-bottom": '20px',    
                                                    },

                                                    )
                                                    
                                                ], md = 6,
                                                
                                                ),

                                                
                                                
                                            ], className="p-3 mb-2 text-md-center"
                                            ),
                                                    
                                           
                                            
                                            
                                            ],

                                        ),
                                    ], 
                                    ),

                                    
                                    
                                ],color="dark", inverse=True, style = {"min-height": "500px"}
                                ),

                                dmc.Space(h=50),


                                
                                #### GRAFICO_1

                                html.H4("GRÁFICOS:", className="p-4 mb-4 text-md-center",  ), 
                                dbc.Card([
                                    
                                    dbc.CardBody([
                                        html.Div([
                                            #html.H5("HISTÓRICO DO RENDIMENTO DA CARTEIRA:", className="card-title"),
                                            dmc.Space(h=15),
                                            #html.H5("RENDIMENTO DA CARTEIRA E APORTES:", className="card-title"),
                                            dcc.Graph(
                                                config = {'displaylogo': False,
                                                    'displayModeBar': False,
                                                    'scrollZoom': False,
                                                    'editable': False,
                                                    'showLink':False,
                                                    },
                                                id='grafico_1f',
                                                figure = go.Figure(layout = Layout(paper_bgcolor='rgba(0,0,0,0)')),
                                                
                                                ),
                                            
                                            ],

                                        ),

                                    ], 
                                    ),

                                    
                                    
                                ],color="dark", inverse=True, style = {"max-height": "600px","min-height": "500px"}
                                ),

                                dmc.Space(h=50),
                
                                #### GRAFICO_2
                                dbc.Card([
                                    
                                    dbc.CardBody([
                                        html.Div([
                                            #html.H5("HISTÓRICO DO RENDIMENTO DA CARTEIRA:", className="card-title"),
                                            dmc.Space(h=15),
                                            #html.H5("RENDIMENTO DA CARTEIRA E APORTES:", className="card-title"),
                                            dcc.Graph(
                                                config = {'displaylogo': False,
                                                    'displayModeBar': False,
                                                    'scrollZoom': False,
                                                    'editable': False,
                                                    'showLink':False,
                                                    },
                                                id='grafico_2f',
                                                figure = go.Figure(layout = Layout(paper_bgcolor='rgba(0,0,0,0)')),
                                                
                                                ),
                                            
                                            ],

                                        ),

                                    ], 
                                    ),

                                    
                                    
                                ],color="dark", inverse=True, style = {"max-height": "600px","min-height": "500px"}
                                ),

                                dmc.Space(h=50),

                                #### GRAFICO_3
                                dbc.Card([
                                    
                                    dbc.CardBody([
                                        html.Div([
                                            #html.H5("HISTÓRICO DO RENDIMENTO DA CARTEIRA:", className="card-title"),
                                            dmc.Space(h=15),
                                            #html.H5("RENDIMENTO DA CARTEIRA E APORTES:", className="card-title"),
                                            dcc.Graph(
                                                config = {'displaylogo': False,
                                                    'displayModeBar': False,
                                                    'scrollZoom': False,
                                                    'editable': False,
                                                    'showLink':False,
                                                    },
                                                id='grafico_3f',
                                                figure = go.Figure(layout = Layout(paper_bgcolor='rgba(0,0,0,0)')),
                                                
                                                ),
                                            
                                            ],

                                        ),

                                    ], 
                                    ),

                                    
                                    
                                ],color="dark", inverse=True, style = {"max-height": "600px","min-height": "500px"}
                                ),

                                dmc.Space(h=50),

                                #### GRAFICO_4
                                dbc.Card([
                                    
                                    dbc.CardBody([
                                        html.Div([
                                            #html.H5("HISTÓRICO DO RENDIMENTO DA CARTEIRA:", className="card-title"),
                                            dmc.Space(h=15),
                                            #html.H5("RENDIMENTO DA CARTEIRA E APORTES:", className="card-title"),
                                            dcc.Graph(
                                                config = {'displaylogo': False,
                                                    'displayModeBar': False,
                                                    'scrollZoom': False,
                                                    'editable': False,
                                                    'showLink':False,
                                                    },
                                                id='grafico_4f',
                                                figure = go.Figure(layout = Layout(paper_bgcolor='rgba(0,0,0,0)')),
                                                
                                                ),
                                            
                                            ],

                                        ),

                                    ], 
                                    ),

                                    
                                    
                                ],color="dark", inverse=True, style = {"max-height": "600px","min-height": "500px"}
                                ),

                                dmc.Space(h=50),

                                #### GRAFICO_5
                                dbc.Card([
                                    
                                    dbc.CardBody([
                                        html.Div([
                                            #html.H5("HISTÓRICO DO RENDIMENTO DA CARTEIRA:", className="card-title"),
                                            dmc.Space(h=15),
                                            #html.H5("RENDIMENTO DA CARTEIRA E APORTES:", className="card-title"),
                                            dcc.Graph(
                                                config = {'displaylogo': False,
                                                    'displayModeBar': False,
                                                    'scrollZoom': False,
                                                    'editable': False,
                                                    'showLink':False,
                                                    },
                                                id='grafico_5f',
                                                figure = go.Figure(layout = Layout(paper_bgcolor='rgba(0,0,0,0)')),
                                                
                                                ),
                                            
                                            ],

                                        ),

                                    ], 
                                    ),

                                    
                                    
                                ],color="dark", inverse=True, style = {"max-height": "600px","min-height": "500px"}
                                ),

                                dmc.Space(h=50),

                                #### GRAFICO_6
                                dbc.Card([
                                    
                                    dbc.CardBody([
                                        html.Div([
                                            #html.H5("HISTÓRICO DO RENDIMENTO DA CARTEIRA:", className="card-title"),
                                            dmc.Space(h=15),
                                            #html.H5("RENDIMENTO DA CARTEIRA E APORTES:", className="card-title"),
                                            dcc.Graph(
                                                config = {'displaylogo': False,
                                                    'displayModeBar': False,
                                                    'scrollZoom': False,
                                                    'editable': False,
                                                    'showLink':False,
                                                    },
                                                id='grafico_6f',
                                                figure = go.Figure(layout = Layout(paper_bgcolor='rgba(0,0,0,0)')),
                                                
                                                ),
                                            
                                            ],

                                        ),

                                    ], 
                                    ),

                                    
                                    
                                ],color="dark", inverse=True, style = {"max-height": "600px","min-height": "500px"}, id = 'card_dividendos'
                                ),

                                dmc.Space(h=50),

                                #### GRAFICO_7
                                dbc.Card([
                                    
                                    dbc.CardBody([
                                        html.Div([
                                            #html.H5("HISTÓRICO DO RENDIMENTO DA CARTEIRA:", className="card-title"),
                                            dmc.Space(h=15),
                                            #html.H5("RENDIMENTO DA CARTEIRA E APORTES:", className="card-title"),
                                            dcc.Graph(
                                                config = {'displaylogo': False,
                                                    'displayModeBar': False,
                                                    'scrollZoom': False,
                                                    'editable': False,
                                                    'showLink':False,
                                                    },
                                                id='grafico_7f',
                                                figure = go.Figure(layout = Layout(paper_bgcolor='rgba(0,0,0,0)')),
                                                
                                                ),
                                            
                                            ],

                                        ),

                                    ], 
                                    ),

                                    
                                    
                                ],color="dark", inverse=True, style = {"max-height": "600px","min-height": "500px"}, id = 'card_benchmarks_1'
                                ),

                                dmc.Space(h=50),

                                #### GRAFICO_8
                                dbc.Card([
                                    
                                    dbc.CardBody([
                                        html.Div([
                                            #html.H5("HISTÓRICO DO RENDIMENTO DA CARTEIRA:", className="card-title"),
                                            dmc.Space(h=15),
                                            #html.H5("RENDIMENTO DA CARTEIRA E APORTES:", className="card-title"),
                                            dcc.Graph(
                                                config = {'displaylogo': False,
                                                    'displayModeBar': False,
                                                    'scrollZoom': False,
                                                    'editable': False,
                                                    'showLink':False,
                                                    },
                                                id='grafico_8f',
                                                figure = go.Figure(layout = Layout(paper_bgcolor='rgba(0,0,0,0)')),
                                                
                                                ),
                                            
                                            ],

                                        ),

                                    ], 
                                    ),

                                    
                                    
                                ],color="dark", inverse=True, style = {"max-height": "600px","min-height": "500px"}, id = 'card_benchmarks_2'
                                ),

                                

                                

                                dmc.Space(h=50),

                                

                                

                            
                            ]
                            ),

                        ],
                        
                        className="p-2 mb-2 ",
                        )

                    ], md = 8
                    ),

                    dbc.Col(
                    [
                        html.H6("coluna de anúncios"),
                        #html.A(html.Button('Refresh Data'),href='/'), 
                    ], md = 4
                    ),

                    html.Div(
                    [
                        html.A(dbc.Button("RECONFIGURAR CARTEIRA", size="lg", id="reload", n_clicks=0, color="info", outline=True,    style = {'width':'340px'},),href='/'), 
        
                    ], style = {'text-align':'center'},
                    ),

                    dmc.Space(h=100),

                    
                ]
                
                ),
                ],style = {"display": "block"}, id = "relatorio_graphs",
                
                ),
                
            ],style = {"display": "none"}, id = "exibir"
            )      
        ], 
    
        
        ), 

        html.Div(
        [
        
        #valide seu e-mail
        dbc.Container(
        
        [
        
            html.Div(
            [
            html.Div(
            [
                html.Hr(),

                dmc.Space(h=50), 

                html.H3("Valide seu e-mail", className="p-4 mb-4 text-md-center", style = {'text-align': 'center'}, ), 
                dmc.Space(h=10),
                html.Div(
                    [
                        #html.A(dbc.Button("CONFIRMAR", size="lg", id="btn_confirmar_email", color="info", outline=True, n_clicks=0, style = {'width':'340px'},),href='/')
        
                    ], style = {'text-align':'center'},
                    ),

                reenvio_1,



            ], 
            ),

            ],
            ),

            
        ],id = 'container_valide_seu_email', style = {"display": "none"}
        ),

        #logar novamente
        dbc.Container(
        
        [
        
            html.Div(
            [
            html.Div(
            [
                html.Hr(),

                dmc.Space(h=50), 

                html.H3("div_logar_novamente", className="p-4 mb-4 text-md-center", style = {'text-align': 'center'}, ), 
                dmc.Space(h=10),
                html.Div(
                    [

                        #dbc.Button("div_logar_novamente", size="lg", id="btn_logar_novamente_email_maior", color="info", outline=True, n_clicks=0, style = {'width':'340px'})
                       
                    ], style = {'text-align':'center'},
                    ),

                reenvio_2,

            ], 
            )

            ], 
            )
        ], id = 'container_logar_novamente', style = {"display": "none"}
        )

        ],id = 'div_validacao', style = {"display": "none"}
        )

    ]
        
    )


    return modulo