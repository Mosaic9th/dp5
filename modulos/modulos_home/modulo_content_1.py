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
from modulos.modulos_banner.banner_02 import banner_02
from modulos.modulos_banner.banner_03 import banner_03
from modulos.modulos_banner.banner_04 import banner_04


from modulos.modulos_banner.banner_02_mob import banner_02_mob
from modulos.modulos_banner.banner_04_mob import banner_04_mob


#callbacks / layouts

#outros
import pandas as pd
from datetime import datetime, timedelta

# importando a lista dos códigos das ações
carteira_ibov_bruta = pd.read_csv('assets/dados/parametros_ibov/dados_ibov.csv')
codigos_lista = carteira_ibov_bruta['Código'].values.tolist()
codigos_lista = sorted(codigos_lista)
ibov_tabela = carteira_ibov_bruta[['Código', 'Ação', 'Setor']] 

# mes e ano final
today = datetime.now()
first = today.replace(day=1)
last = first - timedelta(days=1)
last_month = last.month
year_ = last.year


test_keys = ["label", "value"]
test_values = []
lista_dict = []

anos_list = list(range(year_-10, year_+1))

for i in anos_list:

    test_values.append(str(i))
    test_values.append(str(i))
    res = {}
    for key in test_keys:
        for value in test_values:
            res[key] = value
            test_values.remove(value)
            break
    test_values=[]

    lista_dict.append(res)


def create_modulo_content_1():
    
    modulo  = html.Div(
    
    dbc.Container(
    [
        html.Div(
        [
            dmc.Space(h=50), 

            html.Div(
                html.H3("Configure sua carteira:", className="p-3 mb-2 text-md-center"),
                style={
                    'text-align': 'center',
                },
            ),

            dmc.Space(h=10),

            dbc.Row(
            [
                dbc.Col(
                [ 
                    

                    #div_composicao
                    html.Div(
                    [
                        #card_composicao
                        dbc.Card(
                        [
                            dmc.Space(h=10),
                            dbc.CardHeader("COMPOSIÇÃO DA CARTEIRA:", style={"background-color": "#222222", 'border':'none'}),
                            dbc.CardBody([
                                dbc.FormText("Selecione até 12 ações para montar sua carteira:"),
                                ################# dropdown_codigos_ativos_data
                                dcc.Dropdown(                           
                                    options = codigos_lista,
                                    value =['PETR3'],
                                    id = 'dropdown_codigos_ativos',
                                    multi=True,
                                    placeholder="Selecione ou digite o código",
                                    persistence = True,
                                    persistence_type = 'session'
                                ),
                            
                                html.Div(children=[
                                    dbc.Alert(
                                    [
                                        html.I(className="bi bi-x-octagon-fill me-4"),
                                        "Selecione no máximo 12 ações.",
                                    ],
                                    color="danger",
                                    className="d-flex align-items-center",
                                    id= "danger_dropdown_codigos_ativos",
                                    is_open = False,
                                    ),
                                    dbc.Alert(
                                    [
                                        html.I(className="bi bi-x-octagon-fill me-4", 
                                        ), "Você precisa escolher ao menos uma ação.", 
                                    ],
                                    color="danger",
                                    className="d-flex align-items-center",
                                    id= "danger_dropdown_codigos_ativos_zerado",
                                    is_open = False,  
                                    ),
                        
                                ],
                                style={"padding-top": "10px",}
                                ),
                            ],
                            ),
                        ],style={"background-color": "#222222", 'border': 'thin #333333 solid',}
                        ),#fim_card_composicao
                    ]
                    ),#fim_div_composicao

                    
                    #dmc.Space(h=10),
                    #banner_2
                    html.Div(
                    [
                        html.Div(
                            dmc.Text("PUBLICIDADE", size="xs", color="gray",align="center"),
                        style = {'height':'20px',
                        'margin-top':'15px',
                        #'text-align': 'center'
                        },
                        id = 'banner_2_p', 
                        
                        ),
                        html.Div(
                            banner_02(),
                        style={             
                        #'text-align': 'center',
                        'height':'100px',

                        },       
                        id = 'banner_2', 
                        ),
    
                        dmc.Space(h=20),

                    ], id = 'div_content_banner_2', 
                    ),

                    #banner_2_mobile
                    html.Div(
                    [
                        html.Div(
                            dmc.Text("PUBLICIDADE", size="xs", color="gray",align="center"),
                        style = {'height':'20px',
                        'margin-top':'15px',
                                                },
                        id = 'banner_2_p_mobile', 
                        
                        ),
                        html.Div(
                            banner_02_mob(),
                        style={             
                        
                        'height':'300px',
                        },       
                        id = 'banner_2_mobile', 
                        ),
    
                        dmc.Space(h=20),

                    ], id = 'div_content_banner_2_mobile', 
                    style={'display':'none'}
                    ),
                   
                   

                    dmc.Space(h=10),

                    #div_periodo
                    html.Div(
                    [
                    dbc.Card(
                    [
                        dmc.Space(h=10),
                        dbc.CardHeader("PERÍODO:", style={"background-color": "#222222", 'border':'none'}),
                        

                        dbc.CardBody([

                            dbc.Row([

                        dbc.Col([

                            html.Div(
                            [   
                                dbc.FormText("Dia inicial:"),
                                html.H6(children = '31',className="p-2 mb-2", id = "dia_inicial" )
                            ],
                            
                            ),
    
                        ], md=4, ),

                        dbc.Col([

                            html.Div(
                            [   
                                dbc.FormText("Mês inicial:"),
                                dcc.Dropdown(
                                    options=[
                                    {'label': 'janeiro', 'value': '1'},
                                    {'label': 'fevereiro', 'value': '2'},
                                    {'label': 'março', 'value': '3'},
                                    {'label': 'abril', 'value': '4'},
                                    {'label': 'maio', 'value': '5'},
                                    {'label': 'junho', 'value': '6'},
                                    {'label': 'julho', 'value': '7'},
                                    {'label': 'agosto', 'value': '8'},
                                    {'label': 'setembro', 'value': '9'},
                                    {'label': 'outubro', 'value': '10'},
                                    {'label': 'novembro', 'value': '11'},
                                    {'label': 'dezembro', 'value': '12'},
                                    ],
                                    id = 'dropdown_mes_inicio',
                                    placeholder="Selecione o mês inicial",
                                    value = str(last_month),
                                    clearable=False,
                                    persistence = True,
                                    persistence_type = 'session'
                                ),
                            ],
                            #className="p-2 mb-2"
                            ),
    
                        ], md=4, ),
                    

                                                
                        dbc.Col([

                            html.Div(
                            [   
                                dbc.FormText("Ano inicial:"),
                                dcc.Dropdown(
                                    options=lista_dict,
                                    id = 'dropdown_ano_inicio',
                                    placeholder="Selecione o ano inicial",
                                    value = str(year_-10),
                                    clearable=False,
                                    persistence = True,
                                    persistence_type = 'session'
                                ),
                            ],
                            #className="p-2 mb-2"
                            ),

                            
                        ], md=4,),

                        
                    html.Div(children=
                    [
                        dbc.Alert(
                        [
                            html.I(className="bi bi-x-octagon-fill me-4", 
                            ), "danger_data_inicial_1.",
                        ],
                        color="danger",
                        id= "danger_data_inicial_1",
                        is_open = False,      
                        ),
                        dbc.Alert(
                        [
                            html.I(className="bi bi-x-octagon-fill me-4", 
                            ), "danger_data_inicial_1.",
                        ],
                        color="danger",
                        className="d-flex align-items-center",
                        id= "danger_data_inicial_fora",
                        is_open = False,
                                
                        ),
                    ],
                    style={"padding-top": "15px",}
                    ),

                    ],
                    ), 

                    dbc.Row([

                        dbc.Col([

                            html.Div(
                            [   
                                dbc.FormText("Dia final:"),
                                html.H6(children = '31',className="p-2 mb-2", id = "dia_final" )
                            ],
                            
                            ),
    
                        ], md=4, ),
                    
                        
                        dbc.Col([

                            html.Div(
                            [   
                                dbc.FormText("Mês final:"),
                                dcc.Dropdown(
                                    options=[
                                    {'label': 'janeiro', 'value': '1'},
                                    {'label': 'fevereiro', 'value': '2'},
                                    {'label': 'março', 'value': '3'},
                                    {'label': 'abril', 'value': '4'},
                                    {'label': 'maio', 'value': '5'},
                                    {'label': 'junho', 'value': '6'},
                                    {'label': 'julho', 'value': '7'},
                                    {'label': 'agosto', 'value': '8'},
                                    {'label': 'setembro', 'value': '9'},
                                    {'label': 'outubro', 'value': '10'},
                                    {'label': 'novembro', 'value': '11'},
                                    {'label': 'dezembro', 'value': '12'},
                                    ],
                                    value = str(last_month),
                                    id = 'dropdown_mes_fim',
                                    placeholder="Selecione o mês final",
                                    clearable=False,
                                    persistence = True,
                                    persistence_type = 'session'
                                ),
                            ],
                            #className="p-2 mb-2"
                            ),
    
                        ], md=4, ),

                                                
                        dbc.Col([

                            html.Div(
                            [   
                                dbc.FormText("Ano final:"),
                                dcc.Dropdown(
                                    options = lista_dict,
                                    id = 'dropdown_ano_fim',
                                    placeholder="Selecione o ano final",
                                    value= str(year_),
                                    clearable=False,
                                    persistence = True,
                                    persistence_type = 'session'
                                ),
                            ],
                            #className="p-2 mb-2"
                            ),

                            
                        ], md=4, ),

                        
                    html.Div(children=
                    [
                        dbc.Alert(
                        [
                            html.I(className="bi bi-x-octagon-fill me-4", 
                            ), "A data final deve ser maior que a data inicial.",
                        ],
                        color="danger",
                        className="d-flex align-items-center",
                        id= "danger_data_final_1",
                        is_open = False,
                        ),
                        dbc.Alert(
                        [
                            html.I(className="bi bi-x-octagon-fill me-4", 
                            ), "O mês/ano final não deve ser igual ou maior que mês/ano atual.",
                        ],
                        color="danger",
                        className="d-flex align-items-center",
                        id= "danger_data_final_2",
                        is_open = False,         
                        ),
                    ],
                    style={"padding-top": "15px",}
                    ),
                
                    ],#style={'border': 'thin #fff solid',}
                    ),

                        ]),
                        
                    ], style={"background-color": "#222222", 'border': 'thin #333333 solid',}
                    )

                    ]
                    ),

                    dmc.Space(h=20),

                    #div_investimento
                    html.Div(
                    [
                        #card_investimento
                        dbc.Card(
                        [
                            dmc.Space(h=10),
                            dbc.CardHeader("INVESTIMENTO:", 
                                style={
                                    "background-color": "#222222", 
                                    'border':'none'
                                }
                            ),                        
                            dbc.CardBody(
                            [
                                dbc.FormText("Digite o valor de investimento inicial (mín. R$ 100,00):"),
                                dbc.InputGroup(
                                    [    
                                    dbc.InputGroupText("R$"),
                                    dbc.Input(placeholder="", type="number", min=100, max=1000000000, value= '1000',step=1,id="investimento_inicial", persistence = True, persistence_type = 'session'),
                                    dbc.InputGroupText(",00"),            
                                    ],
                                    className="mb-3",),
                                html.Div(
                                    [ 
                                    dbc.Alert(
                                        [
                                        html.I(className="bi bi-x-octagon-fill me-4"
                                        ), "O valor inicial deve estar entre R$ 100,00 e R$ 1.000.000.000,00.",
                                        ],
                                        color="danger",
                                        className="d-flex align-items-center",
                                        id= "danger_investimento_inicial",
                                        is_open = False
                                        ),
                                    ]),
                                html.Div(
                                    [ 
                                    dmc.Space(h=10),
                                    dbc.Checklist(
                                        options=[
                                            {"label": "Realizar novos aportes mensais", "value": 1},
                                        ],
                                        value=[],
                                        inline=True,
                                        switch=True,
                                        id= "checklist_mensal",
                                        persistence = True,
                                        persistence_type = 'session',
                                    ),
                                ],
                                ),
                                dbc.Collapse(
                                    html.Div(
                                    [
                                        dbc.FormText("Digite o valor dos aportes mensais (mín. R$ 50,00):"),
                                        dbc.InputGroup(
                                        [    
                                            dbc.InputGroupText("R$"),
                                            dbc.Input(placeholder="", type="number",  min=50, max=1000000000, value= '500',step=1,id="valor_aporte_mensal", persistence = True, persistence_type = 'session'),
                                            dbc.InputGroupText(",00"),            
                                        ],
                                        className="mb-3",),
                                
                                    ],id="investimento_mensal", style={"padding-top": "10px", "padding-bottom": "0px"}
                                    ),
                                    id="collapse_aporte_mensal",
                                    is_open=False,
                                ),
                                html.Div(
                                [ 
                                    dbc.Alert(
                                    [
                                        html.I(className="bi bi-x-octagon-fill me-4"
                                        ), "O valor deve estar entre R$ 100,00 e R$ 1.000.000.000,00.",
                                    ],
                                    color="danger",
                                    className="d-flex align-items-center",
                                    id= "danger_aporte_mensal",
                                    is_open = False
                                    ),
                                ],
                                ),
                            ]
                            ),
                        ], style={"background-color": "#222222", 'border': 'thin #333333 solid',}
                        ),#fim_card_investimento
                    ],
                    ),#fim_div_investimento

                    dmc.Space(h=20),

                    #div_dividendos
                    html.Div(
                    [
                        #card_dividendos 
                        dbc.Card(
                        [
                            dmc.Space(h=10),
                            dbc.CardHeader("DIVIDENDOS:", 
                                style={
                                    "background-color": "#222222", 
                                    'border':'none'
                                }
                            ),
                            dbc.CardBody(
                            [
                                dbc.Checklist(
                                    options=[
                                        {"label": "Considerar dividendos", "value": 1},
                                    ],
                                    value=[],
                                    inline=True,
                                    switch=True,
                                    id= "checklist_dividendos",
                                    persistence = True,
                                    persistence_type = 'session'
                                    ),
                                dbc.Collapse(
                                    html.Div(
                                    [
                                        dmc.Space(h=10),
                                        dbc.Checklist(
                                            options=[
                                                {"label": "Reinvestir dividendos", "value": 1},
                                            ],
                                            value=[],
                                            inline=True,
                                            switch=True,
                                            id= "checklist_dividendos_2",
                                            persistence = True,
                                            persistence_type = 'session'
                                        ),
                                    ]
                                    ),
                                id="collapse_checklist_dividendos_2",
                                is_open=False,
                                ),
                            ],
                            ),

                        ], style={"background-color": "#222222", 'border': 'thin #333333 solid',}
                        ),#fim_card_dividendos 
                    ], 
                    ),#fim_div_dividendos

                    dmc.Space(h=20),
                    
                    #div_benchmark(s)
                    html.Div(
                    [
                        #card_benchmark(s) 
                        dbc.Card(
                        [
                            dmc.Space(h=10),
                            dbc.CardHeader("BENCHMARK(S):", 
                                style={
                                    "background-color": "#222222", 'border':'none'
                                    }
                                    ),
                            dbc.CardBody([
                                dbc.FormText("Selecione até 4 ativos para comparação de performance:"),
                                dcc.Dropdown(                           
                                    options = ['Ibovespa', 'CDI', 'Dólar Ptax', 'Bitcoin'],
                                    value =['Ibovespa'],
                                    id = 'dropdown_benchmarks',
                                    multi=True,
                                    placeholder="Selecione",
                                    persistence = True,
                                    persistence_type = 'session'
                                ),
                                html.Div(children=[
                                    dmc.Space(h=10), 
                                    dbc.Alert(
                                    [    
                                    ],color="danger",
                                    className="d-flex align-items-center",
                                    id= "danger_btc",
                                    is_open = False,
                                    ),
                                ],
                                ),
                            ], 
                            ),   
                        ],style={"background-color": "#222222", 'border': 'thin #333333 solid'}  
                        ),#fim_card_benchmark(s)   
                    ],               
                    ),#fim_div_benchmark(s)   

                ], md=5, id='configuracao'
                ),
                #

                dbc.Col(    
                [                      
                                                                    
                    html.Div(
        
                    [

                        html.Div([
                            dbc.Card([

                                dbc.CardBody([
                                    html.Div([
                                        dmc.Space(h=15),
                                        dcc.Graph( id='graph', config = {'displaylogo': False, 'displayModeBar': False},
                                            figure = go.Figure(layout = Layout(paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=50, r=50, t=50, b=50))),
                                        ),
                                    ],   
                                    ), 
                                ], 
                                ),
                                
                            ],id = 'card_div_graph', color="dark",
                            ),

                        ],id = "div_graph",style={"display":"none"}
                        ),

                        html.Div([
                            dbc.Card([

                                dbc.CardBody([
                                    html.Div(
                                    [   
                                        dmc.Space(h=180),
                                        dbc.Spinner(spinner_style={"width": "100px", "height": "100px"},color="info", id = "spinner_grafico"),
                                        dmc.Space(h=180),
                                    ], #style = {"max-height": "480px"}
                                    ),
                                ],#style = {"max-height": "480px"},

                                ),
                            ],id = 'card_div_spinner_grafico', color="dark", style = {"height": "500px"},
                            ),

                        ],id ="div_spinner_grafico"
                        ),
                    
                    #banner_3
                    html.Div(
                    [
                        #dmc.Space(h=30),
                        html.Div(
                            dmc.Text("PUBLICIDADE", size="xs", color="gray",align="center"),
                        style = {'height':'20px',
                        'margin-top':'30px',
                        'text-align': 'center'
                        },
                        id = 'banner_3_p', 
                        
                        ),
                        html.Div(
                            banner_03(),
                        style={             
                        'text-align': 'center',
                        'height':'540px',
                        #'width': '480px',
                        },       
                        id = 'banner_3', 
                        ),
    
                        

                    ], id = 'div_content_banner_3', 
                    #style={    
                    #'text-align': 'center'
                #}    
                    

                    ),
                        #banner_2
                        #dmc.Space(h=50),
                      
                                   
                    ],
                    ),
                ],
                md=7, id='col_graph',
                style={    
                    'text-align': 'center'
                }    
                ),
            ],className="gx-5",
            ),
            

            

                    #banner_4
                    html.Div(
                    [
                        html.Div(
                            dmc.Text("PUBLICIDADE", size="xs", color="gray",align="center"),
                        style = {'height':'20px',
                        'margin-top':'30px',
                        },
                        id = 'banner_4_p', 
                        ),
                        html.Div(
                            banner_04(),
                        style={             
                        'height':'250px',
                        },       
                        id = 'banner_4', 
                        ),
                ], id = 'div_content_banner_4', 
                ),

                #banner_4_mobile
                    html.Div(
                    [
                        html.Div(
                            dmc.Text("PUBLICIDADE", size="xs", color="gray",align="center"),
                        style = {'height':'20px',
                        'margin-top':'30px',
                                                },
                        id = 'banner_4_p_mobile', 
                        
                        ),
                        html.Div(
                            banner_04_mob(),
                        style={             
                        
                        'height':'300px',
                        },       
                        id = 'banner_4_mobile', 
                        ),
    
                        dmc.Space(h=20),

                    ], id = 'div_content_banner_4_mobile', 
                    style = {'display': 'none'}
                    ),


            
            
            dmc.Space(h=50),
        
        ],
         style={
        #'border': 'thin grey solid',
        }
        ),

    
    ], 
    ), id = 'modulo_content_1',
    
    )
    
    return modulo