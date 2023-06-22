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


def banner_uolplay_actionpay_728x90():

    modulo = html.Div(
    [

        #dmc.Space(h=10), 
        html.A(
            #href="http://trafficcost.ru/647f96642bfa811cd81de27e/st/bn",
            children=[
                html.Img(src=r'assets/banners/uolplay_actionpay_728x90.gif', width="728px", height="90px", 
                #className="p-3 mb-2 text-md-center",
                ),
                ],
                
            ),
        #dmc.Space(h=10), 
    ], 
    id = 'uolplay_actionpay_728x90',
    style={
        'text-align': 'center'
        }
    ),

    return modulo

