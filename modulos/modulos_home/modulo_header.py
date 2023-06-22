#dash
from dash import html

#plotly

#dash-bootstrap-components
import dash_bootstrap_components as dbc

#dash-bootstrap-templates

#dash_mantine_components
import dash_mantine_components as dmc

#dash-iconify

#paginas

#modulos

from modulos.modulos_banner.banner_01 import banner_01


#callbacks / layouts

#outros

def create_modulo_header():
    
    modulo = html.Div(
    

    dbc.Container(

    [
        dmc.Space(h=50), 
        html.Div(
        [

            dbc.Row(
            [

                dbc.Col(
                    html.Div(
                    [
                        dbc.Row(
                        [
                        html.H1(("Monte sua carteira de ações"),
                        className="text-primary p-3 mb-2",
                        ),
                    
                        html.H5(("Escolha as melhores ações, faça o backtest e, com apenas alguns cliques, obtenha informações valiosas para tomar a melhor decisão na hora de investir."),
                        className="text-secondary p-3 mb-2 ",   
                        ),

                        dmc.Space(h=20), 
                        
                        dbc.Button("Documentação", id="btn_docs", n_clicks=0, href='/documentacao', color="primary", outline=True, className="p-3 mb-2 ", style = {'width':'260px'}),
                        ], className= "d-flex justify-content-center"
                        ),

                        dmc.Space(h=30),
                    ],
                    #className="p-2 mb-2 ",  
                    style={
                        #'border': 'thin grey solid',
                        'text-align': 'center',
                        'min-height':'260px',
                        }
                    ),
                    md=8, id='col_monte_carteira',
                  
                ),
                        
                dbc.Col(
                    [
                    #dmc.Space(h=15),
                    
                    #banner_1
                    html.Div(
                    [
                        #dmc.Space(h=30),
                        html.Div(
                            dmc.Text("PUBLICIDADE", size="xs", color="gray",align="center"),
                        style = {'height':'20px',
                        'margin-top':'25px',
                        'text-align': 'center'
                        },
                        id = 'banner_1_p', 
                        
                        ),
                        html.Div(
                            banner_01(),
                            #dmc.Space(h=30),

                        style={             
                        'text-align': 'center',
                        'height':'250x',
                        #'width': '300px',
                        },       
                        id = 'banner_1', 
                        ),
    
                        

                    ], id = 'div_content_banner_1', 
                    #style={    
                    #'text-align': 'center'
                #}    
                    

                    ),
                    #html.Div(
                        #coinext_300x300(),
                           #style={
                            #'border': 'thin grey solid',
                            #'height':'250px',
                            #'text-align': 'right'
                            #}, id= 'div_bn_0'
                    #),
                    dmc.Space(h=50),
                    ],md=4, id='col_banner_0',

                ),

            ],className="gx-5",
            ),

        ], style={
        #'border': 'thin grey solid',
        }

        ),
        dmc.Space(h=20), 
     
    ], 
    ),style={'background-color': '#ffffff'}, 
    id = 'modulo_header'
    
)


    return modulo