#dash
import dash_bootstrap_components as dbc
from dash import html, dcc

#plotly

#dash-bootstrap-components

#dash-bootstrap-templates

#dash_mantine_components
import dash_mantine_components as dmc

#dash-iconify
from dash_iconify import DashIconify

#paginas

#modulos

#callbacks / layouts

#outros



def create_modulo_quem_somos():

    modulo = html.Div(
    
        dbc.Container(
        [
            html.Div(
            [

                dbc.Row(
                [
                    dmc.Space(h=50),
                    html.H3("Quem Somos", style = {'text-align': 'center'},className="text-primary", ), 
                    dmc.Space(h=30),
                    
                    
                ], className ='row d-flex justify-content-center'
                ),

                dmc.Space(h=50),

                dbc.Row(
                [
                    #texto
                ]
                )
            ]
            )
        ]
        ), id = 'modulo_contato_form', style={'background-color': '#ffffff'}, 
    )

    return modulo