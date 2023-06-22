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


def amazon_prime_750x400():

    modulo = html.Div(
    [

        html.A(
            #href="https://coinext.com.br/index.html?aff=338911",
            children=[
                html.Img(src=r'assets/banners/amazon_prime_750x400.png', width="750x", height="400px", 
                #className="p-3 mb-2 text-md-center",
                ),
                ]
            ),
    ], 
    id = 'amazon_prime_750x400',
    style={
        #'text-align': 'center'
        }
    ),

    return modulo

