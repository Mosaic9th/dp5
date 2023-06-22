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


def uolplay_actionpay_336x280():

    modulo = html.Div(
    [

        #dmc.Space(h=10), 
        html.A(
            #href="http://trafficcost.ru/647e51332bfa810af07df422/st/bn",
            children=[
                html.Img(src=r'assets/banners/uolplay_actionpay_336x280.gif', width="336px", height="280px", 
                ),
                ]
            ),
        #dmc.Space(h=10), 
    ], 
    id = 'uolplay_actionpay_336x280',
    #style={
        #'text-align': 'center'
        #}
    ),

    return modulo

