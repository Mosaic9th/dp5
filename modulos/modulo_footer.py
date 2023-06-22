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

#callbacks / layouts

#outros


def create_modulo_footer():
    
    modulo = html.Div(
    
        dbc.Container(
        [
            html.Div(
            [

                dbc.Row(
                [

                    dbc.Col(
                    [  
                        dmc.Space(h=40),
                        html.H5("Institucional", className="text-success p-3 mb-2", ),
                        dbc.Row(dmc.Anchor(dbc.Button("Quem Somos", color="link"), href="/quem-somos"), style = {'width':'100%', 'margin-left': '0px', 'padding-left': '10px' }),
                        dbc.Row(dmc.Anchor(dbc.Button("Política de Privacidade", color="link"), href="/politica-de-privacidade"), style = {'width':'100%', 'margin-left': '0px', 'padding-left': '10px' }),
                        dbc.Row(dmc.Anchor(dbc.Button("Termos de Uso", color="link"), href="/termos-de-uso"), style = {'width':'100%', 'margin-left': '0px', 'padding-left': '10px' }),
                        dmc.Space(h=40), 
                    ], id = 'col_ft_1',
                    md=4,
                    style={
                        'border-right': 'thin white solid',
                        'border-left': 'thin white solid',
                        #'height':'250px',
                        'text-align': 'center'
                    }
                    ),

                    
                        
                    dbc.Col(
                    [
                        dmc.Space(h=40),
                        dbc.Row(html.H5("Fale Conosco",className="text-success p-3 mb-2", ),),
                        dbc.Row(dmc.Anchor(dbc.Button("Entre em Contato", color="link"), href="/contato"), style = {'width':'100%', 'margin-left': '0px', 'padding-left': '10px' }),
                        dbc.Row(dmc.Anchor(dbc.Button("Atendimento LGPD", color="link"), href="/lgpd"), style = {'width':'100%', 'margin-left': '0px', 'padding-left': '10px' }),
                        dmc.Space(h=40), 
                    
                    ],id = 'col_ft_2',
                    md=4,
                    style={
                        #'border-right': 'thin white solid',
                        #'border-left': 'thin white solid',
                        #'height':'250px',
                        'text-align': 'center'
                    }
                    ),

                    dbc.Col(
                
                    [
                        dmc.Space(h=40), 
                        dbc.Row(html.H5("Minha Conta",className="text-success p-3 mb-2", ),),
                        dbc.Row(dmc.Anchor(dbc.Button("Minha Conta", color="link"), href="/minha-conta"), style = {'width':'100%', 'margin-left': '0px', 'padding-left': '10px' }),
                        dbc.Row(dmc.Anchor(dbc.Button("Criar Conta", color="link"), href="/criar-conta"), style = {'width':'100%', 'margin-left': '0px', 'padding-left': '10px' }),
                        dbc.Row(dmc.Anchor(dbc.Button("Fazer Login", color="link"), href="/login"), style = {'width':'100%', 'margin-left': '0px', 'padding-left': '10px' }),
                        
                        
                        dmc.Space(h=40), 
                    
            
                    ],id = 'col_ft_3',
                    md=4, 
                    style={
                        'border-right': 'thin white solid',
                        'border-left': 'thin white solid',
                        #'height':'250px',
                        'text-align': 'center'
                    }
                
                        
                    ),
      
                ],
                ),

            ], className="p-3",
        ),

    ], 
    ),style={'background-color': '#303030',
             #'display': 'inline-block', 
             'vertical-align': 'bottom',
             #'height': '260px',

            }, 
    id = "modulo_footer"
    
)


    return modulo