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
from modulos.modulos_banner.banner_08 import banner_08
from modulos.modulos_banner.banner_09 import banner_09
from modulos.modulos_banner.banner_09_mob import banner_09_mob
from modulos.modulos_banner.banner_10 import banner_10
from modulos.modulos_banner.banner_11 import banner_11
from modulos.modulos_banner.banner_12 import banner_12
from modulos.modulos_banner.banner_13 import banner_13
from modulos.modulos_banner.banner_13_mob import banner_13_mob
from modulos.modulos_banner.banner_14 import banner_14
from modulos.modulos_banner.banner_14_mob import banner_14_mob
from modulos.modulos_banner.banner_15 import banner_15
from modulos.modulos_banner.banner_15_mob import banner_15_mob

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


def create_modulo_backtest():
    
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

                    html.H4("QUADRO RESUMO:", className="p-4 mb-4 text-md-center", style = {'text-align': 'center'}, ), 

                dbc.Row(
                [

                    dbc.Col(
            
                    [
                    
                    html.Div(
                        
                        style = {'height':'20px'}
                        ),

                    html.Div(

                            #quadro_resumo

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

                                                
                                                
                                            ],className="p-3 mb-2 text-md-center" 
                                            ),
                                                    
                                           
                                            
                                            
                                            ],

                                        ),
                                    ], 
                                    ),

                                    
                                    
                                ],color="dark", inverse=True, 
                                style = {
                                    #"height": "600px", 
                                    #'min-width:': '2000px'
                                    }
                                ),

                        style={
                        #'border': 'thin grey solid',
                        #'height': '608px',
                        }
                        

                        ),

                    ],md=8, id = 'col_quadro_resumo'
                    
                    
                    
                    ),
                            
                    dbc.Col(
                    [
                        #banner_8
                        html.Div(
                        [
                            html.Div(
                                dmc.Text("PUBLICIDADE", size="xs", color="gray",align="center"),
                            style = {'height':'24px'},
                            id = 'banner_8_p', 
                            ),
                            html.Div(
                                banner_08(),
                            style={             
                            'text-align': 'center',
                            'height': '600px',
                            'width': '400px',
                            #'border': 'thin grey solid',    
                            },                  
                            id = 'banner_8', 
                        ),
                        ], id = 'div_content_banner_8'
                        ),
                    ],md=4, 
                    ),

                ],className="gx-5",
                ),

            ], 
        ),

        dmc.Space(h=50), 
        
        html.Div(
        [

            html.H4("GRÁFICOS:", className="p-4 mb-4 text-md-center", style = {'text-align': 'center'}, ), 

            dbc.Row(
                [
                        
                #### GRAFICO_1
                html.Div(
                [
        
                    dbc.Card([
                                    
                        dbc.CardBody([
                            html.Div([
                                dmc.Space(h=15),
                                dcc.Graph(
                                    config = {'displaylogo': False,
                                        'displayModeBar': False,
                                        'scrollZoom': False,
                                        'editable': False,
                                        'showLink':False,
                                    },
                                    id='grafico_1f',
                                    figure = go.Figure(layout = Layout(paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=50, r=50, t=50, b=50), autosize = False, height= 600)),
                                ),
                            ],
                            ),

                        ], 
                        ),
   
                    ],color="dark", inverse=True, id = 'card_grafico_1f'
                    ),
                ],id = "div_grafico_1f"
                )

            ]
            ),

            #banner_9
            html.Div(
            [
                dmc.Space(h=50),
                ###


                html.Div(
                        dmc.Text("PUBLICIDADE", size="xs", color="gray",align="center"),
                        style = {'height':'24px'},
                        id = 'banner_9_p', 
                        ),
                        html.Div(
                            banner_09(),

                            style={             
                            #'text-align': 'center',
                            'min-height':'250px'
                            },       
                           
                                    
                        id = 'banner_9', 
                        ),

            ], id = 'div_content_banner_9'
            ),

            #banner_9_mobile
                    html.Div(
                    [
                        html.Div(
                            dmc.Text("PUBLICIDADE", size="xs", color="gray",align="center"),
                        style = {'height':'20px',
                        'margin-top':'30px',
                                                },
                        id = 'banner_9_p_mobile', 
                        
                        ),
                        html.Div(
                            banner_09_mob(),
                        style={             
                        
                        'height':'300px',
                        },       
                        id = 'banner_9_mobile', 
                        ),
    
                        

                    ], id = 'div_content_banner_9_mobile', 
                    style = {'display': 'none'}
                    ),
            dmc.Space(h=50),

            dbc.Row(
            [
                #### GRAFICO_2
                html.Div(
                [
                    
                    dbc.Card([
                                    
                        dbc.CardBody([
                            html.Div([
                                dmc.Space(h=15),
                                dcc.Graph(
                                    config = {'displaylogo': False,
                                            'displayModeBar': False,
                                            'scrollZoom': False,
                                            'editable': False,
                                            'showLink':False,
                                    },
                                    id='grafico_2f',
                                    figure = go.Figure(layout = Layout(paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=50, r=50, t=50, b=50), autosize = False, height= 600)),
                                ),
                            ],
                            ),
                        ], 
                        ),

                    ],color="dark", inverse=True, id = 'card_grafico_2f'
                    ),
                ],id = "div_grafico_2f"
                )
            ]
            ),

            dmc.Space(h=50),

            dbc.Row(
            [

                dbc.Col(
            
                    [
                    #### GRAFICO_3
                    html.Div(
                    [
                        dbc.Card([
                            dbc.CardBody([
                                html.Div([
                                    dmc.Space(h=15),
                                    dcc.Graph(
                                        config = {'displaylogo': False,
                                            'displayModeBar': False,
                                            'scrollZoom': False,
                                            'editable': False,
                                            'showLink':False,
                                        },
                                        id='grafico_3f',
                                        figure = go.Figure(layout = Layout(paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=50, r=50, t=50, b=50), autosize = False, height= 500)),
                                    ),
                                ],
                                ),
                            ], 
                            ),
                        ],color="dark", inverse=True, id = 'card_grafico_3f'
                        ),
                    ],id = "div_grafico_3f"
                    ),

                    dmc.Space(h=50),

                    #### GRAFICO_4
                    html.Div(
                    [
                        dbc.Card([
                            dbc.CardBody([
                                html.Div([
                                    dmc.Space(h=15),
                                    dcc.Graph(
                                        config = {'displaylogo': False,
                                            'displayModeBar': False,
                                            'scrollZoom': False,
                                            'editable': False,
                                            'showLink':False,
                                        },
                                        id='grafico_4f',
                                        figure = go.Figure(layout = Layout(paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=50, r=50, t=50, b=50), autosize = False, height= 500)),
                                    ),
                                ],
                                ),
                            ], 
                            ),
                        ],color="dark", inverse=True,id = 'card_grafico_4f'
                        ),
                    ],id = "div_grafico_4f"
                    ),

                    dmc.Space(h=50),

                    #### GRAFICO_5
                    html.Div(
                    [
                        dbc.Card([
                            dbc.CardBody([
                                html.Div([
                                    dmc.Space(h=15),
                                    dcc.Graph(
                                        config = {'displaylogo': False,
                                            'displayModeBar': False,
                                            'scrollZoom': False,
                                            'editable': False,
                                            'showLink':False,
                                        },
                                        id='grafico_5f',
                                        figure = go.Figure(layout = Layout(paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=50, r=50, t=50, b=50), autosize = False, height= 600)),
                                    ),
                                ],
                                ),
                            ], 
                            ),
                        ],color="dark", inverse=True, id = 'card_grafico_5f'
                        ),
                    ],id = "div_grafico_5f"
                    )
                
                ],md = 8, id = 'col_bk_graphs',
                ),

                dbc.Col(
            
                [
                    #banner_10_11_12
                    html.Div(
                    [

                        html.Div(
                            dmc.Text("PUBLICIDADE", size="xs", color="gray",align="center"),
                            style = {'height':'20px'},
                            id = 'banner_10_p', 
                            ),
                            html.Div(
                                banner_10(),

                                style={             
                                'text-align': 'center',
                                'height':'711px',
                                'width':'400px'
                                },       
                            
                                        
                            id = 'banner_10', 
                            ),

                        dmc.Space(h=30),

                        html.Div(
                            dmc.Text("PUBLICIDADE", size="xs", color="gray",align="center"),
                            style = {'height':'20px'},
                            id = 'banner_11_p', 
                            ),
                            html.Div(
                                banner_11(),

                                style={             
                                'text-align': 'center',
                                'height':'300px',
                                'width':'400px'
                                },       
                            
                                        
                            id = 'banner_11', 
                            ),
                        
                                        

                        dmc.Space(h=30),

                        html.Div(
                            dmc.Text("PUBLICIDADE", size="xs", color="gray",align="center"),
                            style = {'height':'20px'},
                            id = 'banner_12_p', 
                            ),
                            html.Div(
                                banner_12(),

                                style={             
                                'text-align': 'center',
                                'height':'711px',
                                'width':'400px'
                                },       
                            
                                        
                            id = 'banner_12', 
                            ),

                    ], id = 'div_content_banner_10_11_12'
                    ),              

                ],md = 4
                )
            ],className="gx-5",
            ),

            
            

            dbc.Row(
            [
                dmc.Space(h=50),
                #### GRAFICO_6
                html.Div(   
                [
                    dbc.Card([
                        dbc.CardBody([
                            html.Div([
                                dmc.Space(h=15),
                                dcc.Graph(
                                    config = {'displaylogo': False,
                                        'displayModeBar': False,
                                        'scrollZoom': False,
                                        'editable': False,
                                        'showLink':False,
                                    },
                                    id='grafico_6f',
                                    figure = go.Figure(layout = Layout(paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=50, r=50, t=50, b=50), autosize = False, height= 600)),
                                ),                      
                            ],
                            ),
                        ], 
                        ),
                    ],color="dark", inverse=True, id = 'card_grafico_6f'
                    ),
                ],id = "div_grafico_6f"
                ),
                #dmc.Space(h=50),
            ], id = 'row_dividendos'
            ),

            

            

            dbc.Row(
            [
                #banner_13
                html.Div(
                [
                    
                    html.Div(
                        dmc.Text("PUBLICIDADE", size="xs", color="gray",align="center"),
                    style = {'height':'20px',
                    'margin-top':'30px',
                    },
                    id = 'banner_13_p', 
                     ),
                    html.Div(
                        banner_13(),
                    style={             
                       'min-height':'250px'
                    },       
                    id = 'banner_13', 
                    ),
   
                    

                ], id = 'div_content_banner_13'
                ),

                #banner_13_mobile
                    html.Div(
                    [
                        html.Div(
                            dmc.Text("PUBLICIDADE", size="xs", color="gray",align="center"),
                        style = {'height':'20px',
                        'margin-top':'30px',
                                                },
                        id = 'banner_13_p_mobile', 
                        
                        ),
                        html.Div(
                            banner_13_mob(),
                        style={             
                        
                        'height':'300px',
                        },       
                        id = 'banner_13_mobile', 
                        ),
    
                        

                    ], id = 'div_content_banner_13_mobile', 
                    style = {'display': 'none'}
                    ),

                dmc.Space(h=50),
                #### GRAFICO_7
                html.Div(
                [
                    dbc.Card([        
                        dbc.CardBody([
                            html.Div([
                                dmc.Space(h=15),
                                dcc.Graph(
                                    config = {'displaylogo': False,
                                        'displayModeBar': False,
                                        'scrollZoom': False,
                                        'editable': False,
                                        'showLink':False,
                                    },
                                    id='grafico_7f',
                                    figure = go.Figure(layout = Layout(paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=50, r=50, t=50, b=50), autosize = False, height= 600)),
                                ),                    
                            ],
                            ),
                        ], 
                        ),
                    ],color="dark", inverse=True, id = 'card_grafico_7f'
                    ),
                ],id = "div_grafico_7f"
                ),

               
            ],id = 'row_benchmarks_1'
            ),

       

            

            dbc.Row(
            [
                #banner_14
                html.Div(
                [
                    html.Div(
                        dmc.Text("PUBLICIDADE", size="xs", color="gray",align="center"),
                        style = {'height':'20px',
                        'margin-top':'30px',
                        },
                        id = 'banner_14_p', 
                        ),
                    html.Div(
                        banner_14(),
                        style={             
                        'min-height':'250px'
                        },       
                           
                                    
                        id = 'banner_14', 
                    ),
                        
                    

                ], id = 'div_content_banner_14'
                ),

                #banner_14_mobile
                    html.Div(
                    [
                        html.Div(
                            dmc.Text("PUBLICIDADE", size="xs", color="gray",align="center"),
                        style = {'height':'20px',
                        'margin-top':'30px',
                                                },
                        id = 'banner_14_p_mobile', 
                        
                        ),
                        html.Div(
                            banner_14_mob(),
                        style={             
                        
                        'height':'300px',
                        },       
                        id = 'banner_14_mobile', 
                        ),
    
                        

                    ], id = 'div_content_banner_14_mobile',
                    style = {'display': 'none'}
                    ),

                dmc.Space(h=50),

                #### GRAFICO_8
                html.Div(
                [
                    dbc.Card([
                        dbc.CardBody([
                            html.Div([
                                dmc.Space(h=15),
                                dcc.Graph(
                                    config = {'displaylogo': False,
                                        'displayModeBar': False,
                                        'scrollZoom': False,
                                        'editable': False,
                                        'showLink':False,
                                    },
                                    id='grafico_8f',
                                    figure = go.Figure(layout = Layout(paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=50, r=50, t=50, b=50), autosize = False, height= 600)),
                                ),
                            ],
                            ),
                        ], 
                        ),
                    ],color="dark", inverse=True, id = 'card_grafico_8f'
                    ),
                ],id = "div_grafico_8f"
                ),
            
            
            
            ], id = 'row_benchmarks_2'
            ),

        ],
        ),

        
        #banner_15
        html.Div(
        [
                
            html.Div(
                dmc.Text("PUBLICIDADE", size="xs", color="gray",align="center"),
            style = {'height':'20px',
                     'margin-top':'30px',
            },
            id = 'banner_15_p', 
            ),
            
            html.Div(
                banner_15(),
            style={             
                'min-height':'250px'
            },       
            id = 'banner_15', 
                    ),
        ],id = 'div_content_banner_15'
        ),

        #banner_15_mobile
                    html.Div(
                    [
                        html.Div(
                            dmc.Text("PUBLICIDADE", size="xs", color="gray",align="center"),
                        style = {'height':'20px',
                        'margin-top':'30px',
                                                },
                        id = 'banner_15_p_mobile', 
                        
                        ),
                        html.Div(
                            banner_15_mob(),
                        style={             
                        
                        'height':'300px',
                        },       
                        id = 'banner_15_mobile', 
                        ),
    
                        

                    ], id = 'div_content_banner_15_mobile', 
                    style = {'display': 'none'}
                    ),


        dmc.Space(h=50),

        dbc.Row(
        [

            html.Div(
            [
                html.A(dbc.Button("RECONFIGURAR CARTEIRA", size="lg", id="reload", n_clicks=0, color="info", outline=True,    style = {'width':'300px'},),href='/'), 
        
            ], style = {'text-align':'center'},
            ),


            
        ]
        ),

        
        dmc.Space(h=100),

            ##########################################################################################
            ##########################################################################################
            ##########################################################################################

            
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