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


def uolplay_1200x628():

    modulo = html.Div(
    [

        #dmc.Space(h=10), 
        html.A(
            href="http://trafficcost.ru/647e51332bfa810af07df422/st/bn",
            children=[
                html.Img(src=r'assets/banners/uolplay_actionpay_1200x628.jpg', width="1200x", height="628px", 
                ),
                ]
            ),
        #dmc.Space(h=10), 
    ], 
    id = 'uolplay_1200x628',
    #style={
        #'text-align': 'center'
        #}
    ),

    return modulo

