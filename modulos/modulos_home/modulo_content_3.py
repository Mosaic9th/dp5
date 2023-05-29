#dash
from dash import dcc, html

#plotly
import plotly.graph_objs as go

#dash-bootstrap-components
import dash_bootstrap_components as dbc

#dash-bootstrap-templates

#dash_mantine_components
import dash_mantine_components as dmc

#dash-iconify

#paginas

#modulos

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
                    dbc.Card([
                                
                        dbc.CardBody([
                            
                            html.Div([
                               #html.H5("Percentual alocado por ativo:", className="card-title text-md-center"),
                                dcc.Graph(
                                    config = {'displaylogo': False,
                                        'displayModeBar': False},
                                    id='graph_acoes',
                                    figure = go.Figure(data=[go.Pie(labels=None, values=None, hoverinfo="label+percent", hole=.3,)], layout_showlegend=True,)
                                    ),
                                      
                            ],
                            id = "div_graph3",
                            #style={"display":"none"}
                                          
                            ),
                            html.Div(
                                dbc.Spinner(spinner_style={"width": "100px", "height": "100px"},color="info", id = "spinner_grafico3"),
                                id ="div_spinner_grafico3", className= 'text-md-center',style = {"max-height": "500px", "padding-top": "175px"} 
                            ),  
                            
                        ], 
                        ),
                                
                    ],color="dark", inverse=True, style = {"max-height": "600px","min-height": "500px"}, id = 'div_certa3',className="p-2 mb-2"
                    ),#style = {"padding-bottom": "50px"}, #className="p-2 mb-2 "    
                    ),

                    dmc.Space(h=30), 

                    html.Div(
                            html.Img(src=r'assets/images/banner.png', width="300px", height="200px", 
                                #className="p-3 mb-2",
                                style={
                                    'maxWidth': '100%',
                                    'maxHeight': '100%',
                                },
                            ),style={'text-align':'center'}
                        ),

                    dmc.Space(h=30),

                    html.Div(
                    dbc.Card([
                                
                        dbc.CardBody([
                            
                            html.Div([
                                #html.H5("Percentual alocado por setor econômico:", className="card-title text-md-center"),
                                dcc.Graph(
                                    config = {'displaylogo': False,
                                        'displayModeBar': False},
                                    id='graph_setor',
                                    figure = go.Figure(data=[go.Pie(labels=None, values=None, hoverinfo="label+percent", hole=.3 )], layout_showlegend=True,)
                                    ),
                                
                            ],
                            id = "div_graph2",
                            #style={"display":"none"}          
                            ),
                            html.Div(
                                dbc.Spinner(spinner_style={"width": "100px", "height": "100px"},color="info", id = "spinner_grafico2"),
                                id ="div_spinner_grafico2", className= 'text-md-center',style = {"max-height": "500px", "padding-top": "175px"} 
                            ),  
                            
                        ], 
                        ),
                                
                    ],color="dark", inverse=True, style = {"max-height": "600px","min-height": "500px"}, id = 'div_certa2', className="p-2 mb-2"
                    ),#style = {"padding-bottom": "50px"}, #className="p-2 mb-2 "
                    ),

                ],md=8
                ),

                dbc.Col([
                    html.Div(
                        html.Img(src=r'assets/images/banner.png', width="425px", height="600px", 
                        #className="p-3 mb-2",
                        style={
                            'maxWidth': '100%',
                            'maxHeight': '100%',
                            },
                        ),style={'text-align':'center'}
                        
                    ),
                    dmc.Space(h=30),

                    html.Div(
                        html.Img(src=r'assets/images/banner.png', width="425px", height="600px", 
                        #className="p-3 mb-2",
                        style={
                            'maxWidth': '100%',
                            'maxHeight': '100%',
                            },
                        ),style={'text-align':'center'}
                        
                    ),

                    dmc.Space(h=30),

                    #html.Div(
                            #html.Img(src=r'assets/images/banner.png', width="300px", height="300px", 
                                #lassName="p-3 mb-2",
                                #style={
                                    #'maxWidth': '100%',
                                    #'maxHeight': '100%',
                                #},
                            #),style={'text-align':'center'}
                        #),

                ],md=4
                ),

                
            
            ]),
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
                    #dbc.Button("Open modal", id="open", n_clicks=0),
                    
                    #login_modal
                   
                        #dbc.ModalHeader(dbc.ModalTitle("Faça o login para continuar...")),
                        #dbc.ModalBody("Para realizar o backtest do seu portfólio crie uma conta gratuita agora.", className="p-2 mb-2"),
                        #dbc.ModalBody("Caso já tenha uma conta, por favor, faça o login.", className="p-2 mb-2"),
                        #dbc.ModalBody(
                            #id = 'modal_body'),
                        #dbc.ModalFooter(
                            
                            #dbc.Row(

                            #[
                                #dbc.Col (
                                    #dbc.Button(
                                        #"Ainda não tenho cadastro?", id="close", n_clicks=0, className="d-grid gap-2 col-10 mx-auto p-2 mb-2", href='/cadastro'), md = 6
                                #),
                                 #dbc.Col (
                                    #dbc.Button(
                                        #"Esqueci minha senha.", id="close", n_clicks=0, className="d-grid gap-2 col-10 mx-auto p-2 mb-2", href='/login'),  md = 6
                                #)
                            #], className="flex-grow-1" 
                            #)
                       #)
                    #],
                    #id="modal",
                    #size="lg",
                    #is_open=False,
                    #),

                    html.Div(
                    [
                        #dbc.Button("Open Offcanvas", id="open-offcanvas", n_clicks=0),
                        dbc.Offcanvas(
                            html.P(
                                "This is the content of the Offcanvas. "
                                "Close it by clicking on the close button, or "
                                "the backdrop."
                            ),
                            id="offcanvas",
                            title="Title",
                            is_open=False,
                            placement = "bottom"
                        ),
                    ]
                    )


                    
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

            
                                        


            

            #dcc.Graph(figure=fig, id='graph_r_11'),

           
           
            ]
            )


        ]),#divisao_1
        dmc.Space(h=50),
    ]
    ),#className="p-xl-5", 
    id =  "modulo_content_3",
    #style = {'display':'none',}
    
    )




    return modulo