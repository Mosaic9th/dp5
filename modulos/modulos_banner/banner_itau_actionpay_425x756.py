#dash
import dash_bootstrap_components as dbc
from dash import html

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


def itau_actionpay_425x756():

    modulo = html.Div(
    [

        #dmc.Space(h=10), 
        html.A(
            href="http://trafficcost.ru/647ca0752bfa816a1f2c3b32/st/bn",
            children=[
                html.Img(src=r'assets/banners/itau_actionpay_425x756.jpg', width="400px", height="711px", 
                #className="p-3 mb-2 text-md-center",
                ),
                ]
            ),
        #dmc.Space(h=10), 
    ], 
    id = 'itau_actionpay_425x756',
    style={
        'text-align': 'center'
        }
    ),

    return modulo

