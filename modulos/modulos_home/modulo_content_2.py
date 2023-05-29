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

# TABELA #

p0 = dbc.InputGroup(
    [    
    dbc.Input(placeholder="", type="number", value= '0', min=0.01, max=99.99, step=0.01,id ='p0', disabled = True,),
    dbc.Input(placeholder="", type="number", value= '0.01', min=0.01, max=99.99, step=0.01,id ='pb0', disabled = False, persistence = True, persistence_type = 'session',),
    dbc.InputGroupText("%"),            
    ],
    #className="mb-3",
    style = {'min-width':'150px'}
    ), 

p1 = dbc.InputGroup(
    [    
    dbc.Input(placeholder="", type="number", value= '0', min=0.01, max=99.99, step=0.01,id ='p1', disabled = True,),
    dbc.Input(placeholder="", type="number", value= '0.01', min=0.01, max=99.99, step=0.01,id ='pb1', disabled = False, persistence = True, persistence_type = 'session', ),
    dbc.InputGroupText("%"),            
    ],
    #className="mb-3",
    style = {'min-width':'150px'}
    ), 


p2 = dbc.InputGroup(
    [    
    dbc.Input(placeholder="", type="number", value= '0', min=0.01, max=99.99, step=0.01,id ='p2', disabled = True, ),
    dbc.Input(placeholder="", type="number", value= '0.01', min=0.01, max=99.99, step=0.01,id ='pb2', disabled = False, persistence = True, persistence_type = 'session', ),
    dbc.InputGroupText("%"),            
    ],
    #className="mb-3",
    style = {'min-width':'150px'}
    ),  

p3 = dbc.InputGroup(
    [    
    dbc.Input(placeholder="", type="number", value= '0', min=0.01, max=99.99, step=0.01,id ='p3', disabled = True, ),
    dbc.Input(placeholder="", type="number", value= '0.01', min=0.01, max=99.99, step=0.01,id ='pb3', disabled = False, persistence = True, persistence_type = 'session', ),
    dbc.InputGroupText("%"),            
    ],
    #className="mb-3",
    style = {'min-width':'150px'}
    ), 

p4 = dbc.InputGroup(
    [    
    dbc.Input(placeholder="", type="number", value= '0', min=0.01, max=99.99, step=0.01,id ='p4', disabled = True, ),
    dbc.Input(placeholder="", type="number", value= '0.01', min=0.01, max=99.99, step=0.01,id ='pb4', disabled = False, persistence = True, persistence_type = 'session', ),
    dbc.InputGroupText("%"),            
    ],
    #className="mb-3",
    style = {'min-width':'150px'}
    ),

p5 = dbc.InputGroup(
    [    
    dbc.Input(placeholder="", type="number", value= '0', min=0.01, max=99.99, step=0.01,id ='p5', disabled = True, ),
    dbc.Input(placeholder="", type="number", value= '0.01', min=0.01, max=99.99, step=0.01,id ='pb5', disabled = False, persistence = True, persistence_type = 'session', ),
    dbc.InputGroupText("%"),            
    ],
    #className="mb-3",
    style = {'min-width':'150px'}
    ),    

p6 = dbc.InputGroup(
    [    
    dbc.Input(placeholder="", type="number", value= '0', min=0.01, max=99.99, step=0.01,id ='p6', disabled = True, ),
    dbc.Input(placeholder="", type="number", value= '0.01',min=0.01, max=99.99, step=0.01,id ='pb6', disabled = False, persistence = True, persistence_type = 'session', ),
    dbc.InputGroupText("%"),            
    ],
    #className="mb-3",
    style = {'min-width':'150px'}
    ),     

p7 = dbc.InputGroup(
    [    
    dbc.Input(placeholder="", type="number", value= '0', min=0.01, max=99.99, step=0.01,id ='p7', disabled = True, ),
    dbc.Input(placeholder="", type="number", value= '0.01', min=0.01, max=99.99, step=0.01,id ='pb7', disabled = False, persistence = True, persistence_type = 'session', ),
    dbc.InputGroupText("%"),            
    ],
    #className="mb-3",
    style = {'min-width':'150px'}
    ),   

p8 = dbc.InputGroup(
    [    
    dbc.Input(placeholder="", type="number", value= '0', min=0.01, max=99.99, step=0.01,id ='p8', disabled = True, ),
    dbc.Input(placeholder="", type="number", value= '0.01', min=0.01, max=99.99, step=0.01,id ='pb8', disabled = False, persistence = True, persistence_type = 'session', ),
    dbc.InputGroupText("%"),            
    ],
    #className="mb-3",
    style = {'min-width':'150px'}
    ),   

p9 = dbc.InputGroup(
    [    
    dbc.Input(placeholder="", type="number", value= '0', min=0.01, max=99.99, step=0.01,id ='p9', disabled = True, ),
    dbc.Input(placeholder="", type="number", value= '0.01', min=0.01, max=99.99, step=0.01,id ='pb9', disabled = False, persistence = True, persistence_type = 'session', ),
    dbc.InputGroupText("%"),            
    ],
    #className="mb-3",
    style = {'min-width':'150px'}
    ),  

p10 = dbc.InputGroup(
    [    
    dbc.Input(placeholder="", type="number", value= '0', min=0.01, max=99.99, step=0.01,id ='p10', disabled = True, ),
    dbc.Input(placeholder="", type="number", value= '0.01', min=0.01, max=99.99, step=0.01,id ='pb10', disabled = False, persistence = True, persistence_type = 'session', ),
    dbc.InputGroupText("%"),            
    ],
    #className="mb-3",
    style = {'min-width':'150px'}
    ),   

p11 = dbc.InputGroup(
    [    
    dbc.Input(placeholder="", type="number", value= '0', min=0.01, max=99.99, step=0.01,id ='p11', disabled = True, ),
    dbc.Input(placeholder="", type="number", value= '0.01', min=0.01, max=99.99, step=0.01,id ='pb11', disabled = False, persistence = True, persistence_type = 'session', ),
    dbc.InputGroupText("%"),            
    ],
    #className="mb-3",
    style = {'min-width':'150px'}
    ),

row0 = html.Tr([html.Td('1'), html.Td(id='c0'), html.Td(id='a0'), html.Td(id='s0'), html.Td(p0)], id = 'row0', style = {'display': 'none'})
row1 = html.Tr([html.Td('2'), html.Td(id='c1'), html.Td(id='a1'), html.Td(id='s1'), html.Td(p1)], id = 'row1', style = {'display': 'none'})
row2 = html.Tr([html.Td('3'), html.Td(id='c2'), html.Td(id='a2'), html.Td(id='s2'), html.Td(p2)], id = 'row2', style = {'display': 'none'})
row3 = html.Tr([html.Td('4'), html.Td(id='c3'), html.Td(id='a3'), html.Td(id='s3'), html.Td(p3)], id = 'row3', style = {'display': 'none'})
row4 = html.Tr([html.Td('5'), html.Td(id='c4'), html.Td(id='a4'), html.Td(id='s4'), html.Td(p4)], id = 'row4', style = {'display': 'none'})
row5 = html.Tr([html.Td('6'), html.Td(id='c5'), html.Td(id='a5'), html.Td(id='s5'), html.Td(p5)], id = 'row5', style = {'display': 'none'})
row6 = html.Tr([html.Td('7'), html.Td(id='c6'), html.Td(id='a6'), html.Td(id='s6'), html.Td(p6)], id = 'row6', style = {'display': 'none'})
row7 = html.Tr([html.Td('8'), html.Td(id='c7'), html.Td(id='a7'), html.Td(id='s7'), html.Td(p7)], id = 'row7', style = {'display': 'none'})
row8 = html.Tr([html.Td('9'), html.Td(id='c8'), html.Td(id='a8'), html.Td(id='s8'), html.Td(p8)], id = 'row8', style = {'display': 'none'})
row9 = html.Tr([html.Td('10'), html.Td(id='c9'), html.Td(id='a9'), html.Td(id='s9'), html.Td(p9)], id = 'row9', style = {'display': 'none'})
row10 = html.Tr([html.Td('11'), html.Td(id='c10'), html.Td(id='a10'), html.Td(id='s10'), html.Td(p10)], id = 'row10', style = {'display': 'none'})
row11 = html.Tr([html.Td('12'), html.Td(id='c11'), html.Td(id='a11'), html.Td(id='s11'), html.Td(p11)], id = 'row11', style = {'display': 'none'})


body_lista = [row0, row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11]

table_header = [
            html.Thead(html.Tr([html.Th("Quant."), html.Th("Código"), html.Th("Ação"), html.Th("Setor"), html.Th(['Peso do Ativo', html.H6(id = 'soma', className="text-primary" ),])]))
            ]
        
table_body = [html.Tbody(body_lista)]

table = html.Div( children =dbc.Table(table_header + table_body, striped=False, bordered=True, hover=True, responsive= False,color="dark"), id='table', style = {'text-align':'center'})

# TABELA END #


def create_modulo_content_2():
    
    modulo = html.Div(
    
    dbc.Container(
    [
        html.Div(
        [

            dbc.Row(
            [
                html.Div(
                [
                    dmc.Space(h=20),
                    html.H3("Configure o peso de cada ativo na carteira:", className="p-3 mb-3 text-md-center"),
                    dmc.Space(h=30),
                    html.Div(table, id ="div_tabela", style = {'text-align':'center'} ),
                    html.Div(
                    dbc.Spinner(spinner_style={"width": "100px", "height": "100px"},color="info", id = "spinner_tabela"),
                    id ="div_spinner_tabela", className="p-2 mb-2 text-md-center", 
                    ),

                    html.Div(
                    [
                        dbc.Checklist(
                            options=[
                            {"label": "Personalizar peso de cada ação", "value": 1},
                            ],
                            value=[],
                            inline=True,
                            switch=True,
                            id= "checklist_alocado",
                            persistence = True,
                            persistence_type = 'session',
                        ),
                    ], style = {'display':'none'}, id = "div_checklist_alocado"
                    ),
                
                ],#className="p-2 mb-2 ", 
                id= 'div_table',  
                ), 

            ],  
            ),

        ],
        #className="p-xl-5",
        ),

    ], 
    ),
    id =  "modulo_content_2",
    #style={'display':'none'},   
)


    return modulo