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

#callbacks / layouts

#outros
import pandas as pd
from datetime import datetime, timedelta

# importando a lista dos códigos das ações
carteira_ibov_bruta = pd.read_csv('dados/parametros_ibov/dados_ibov.csv')
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

            html.H3("Configure sua carteira:", className="p-4 mb-4 text-md-center", style = {'text-align': 'center'}, id = "config_cart"), 
            dmc.Space(h=10),

            dbc.Row(
            [

                dbc.Col(
                    [
                   
                    dmc.Space(h=20),

                    html.Div(
                        [                        
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
                    ],

                    ),

                    html.Div(children=[
                        dbc.Alert(
                        [
                            html.I(className="bi bi-x-octagon-fill me-4"),
                            "Selecione no máximo doze ações.",
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

                    html.Div(
                        [

                        dmc.Space(h=10), 
                        html.Img(src=r'assets/images/banner.png', width="480x", height="320px", 
                            className="p-3 mb-2 text-md-center",
                            style={
                                'maxWidth': '100%',
                                'maxHeight': '100%',
                            },
                        ),

                        dmc.Space(h=10), 
                        ],style = {'text-align': 'center'}
                    ),

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






                    
                    ],#style={"padding-top": "10px", "padding-bottom": "10px"}
                    ), 
                    #

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

                            
                        ], md=4,),

                        
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


                    html.Div(
                        [
                        
                        dbc.FormText("Digite o valor de investimento inicial (mín. R$ 100,00):"),
                       

                        dbc.InputGroup(
                            [    
                            dbc.InputGroupText("R$"),
                            dbc.Input(placeholder="", type="number", min=100, max=1000000000, value= '1000',step=1,id="investimento_inicial", persistence = True, persistence_type = 'session'),
                            dbc.InputGroupText(",00"),            
                            ],
                            className="mb-3",),
                        
                        ],#style={"padding-top": "10px", "padding-bottom": "0px"}
                        ),

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
                            #id="switches-inline-input",
                            inline=True,
                            switch=True,
                            id= "checklist_mensal",
                            persistence = True,
                            persistence_type = 'session',
                            
                            
                            
                            
                            ),
                        ],#style={"padding-top": "10px", "padding-bottom": "10px"}
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
                        ]),

                    html.Div(
                        [
                        dmc.Space(h=10),
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
                        
                        

                        ] ,style={"padding-top": "10px", "padding-bottom": "30px"}
                        ),
                    
                    
                    html.Div(
                    
                    [
                        html.H6("Comparar rentabilidade da carteira com (benchmarks):", style={"padding-top": "10px", "padding-bottom": "10px"}),

                        dcc.Dropdown(                           
                            options = ['Ibovespa', 'CDI', 'Dólar Ptax', 'Bitcoin'],
                            value =['Ibovespa'],
                            id = 'dropdown_benchmarks',
                            multi=True,
                            placeholder="Selecione",
                            persistence = True,
                            persistence_type = 'session'
                          
                        ),

                        dmc.Space(h=10),

                        html.Div(children=[
                        dbc.Alert(
                        [
                            
                        ],
                        color="danger",
                        className="d-flex align-items-center",
                        id= "danger_btc",
                        is_open = False,
                        ),
                        ]
                        ),
                        
                        
                    ], style={"padding-bottom": "30px"}
                    ),

                    
                    
                    ],
                    ),
                    
                    ],
                    md=5, 
                    style={

                    },
                ),

                dbc.Col(
                
                [                      
                                                                    
                    html.Div(children=[

                        html.Div([

                            dbc.Card([
                                
                                dbc.CardBody([
                                    html.Div([
                                        dmc.Space(h=15),
                                        #html.H5("Preço de Fechamento Ajustado (Diário):", className="card-title"),
                                        dcc.Graph( id='graph', config = {'displaylogo': False, 'displayModeBar': False},
                                            figure = go.Figure(layout = Layout(paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=50, r=50, t=50, b=50))),
                                        ),],
                                        id = "div_graph",
                                        style={"display":"none"}
                                        
                                    ),
                                    html.Div(
                                        dbc.Spinner(spinner_style={"width": "100px", "height": "100px"},color="info", id = "spinner_grafico"),
                                    id ="div_spinner_grafico", style = {"max-height": "500px", "padding-top": "200px"} ),
                            
                                ], 
                                ),
                                
                            ],color="dark", inverse=True, style = {"max-height": "600px","min-height": "500px"}
                            ),

                        ],
                        #style={"overflow-x": "scroll",},
                        className="p-2 mb-2 ",
                        
                        ),
                        html.Div(
                            html.Img(src=r'assets/images/banner.png', width="750px", height="300px", 
                                className="p-3 mb-2",
                                style={
                                    'maxWidth': '100%',
                                    'maxHeight': '100%',
                                },
                            ),className="p-3 mb-2 "
                        ),
                            
                            
                    ],
                    style={'maxWidth': '100%',},
                    className="p-3 mb-2",
                    id = 'div_certa',
                    
                    ),
                    ],
                    md=7, 
                    style={
                        
                        'text-align': 'center'
                        }    
                ),
            ],
            ),
        
        ],
        #className="p-xl-5",
        ),
    html.Hr(),
    ], 
    ), id = 'modulo_content_1'
)


    return modulo