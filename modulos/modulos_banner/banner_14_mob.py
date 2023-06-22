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


def banner_14_mob():

    modulo = html.Div(
    [


        html.A(
            href="https://coinext.com.br/index.html?aff=338911",
            children=[
                #html.Img(src=r'assets/banners/coinext_300x300.gif', width="250x", height="250px", 
                #className="p-3 mb-2 text-md-center",
                #),
                ]
            ),

    ], 
    id = 'banner_14_mob',
    style={
        #'text-align': 'center'
        }
    ),

    return modulo

