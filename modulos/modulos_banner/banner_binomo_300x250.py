#dash
import dash_bootstrap_components as dbc
from dash import html

#plotly

#dash-bootstrap-components

#dash-bootstrap-templates

#dash_mantine_components
import dash_mantine_components as dmc

#dash-iconify

#paginas

#modulos

#callbacks / layouts

#outros



def binomo_300x250():

    modulo = html.Div(
    [

        html.A(
            href="https://binomo.com/pt?a=bdeb91b43e01",
            children=[
                html.Img(src=r'assets/banners/binomo_300x250.png', width="300x", height="250px", 
                ),
                ]
            ),

    ], 
    id = 'binomo_300x250',
    ),

    return modulo

