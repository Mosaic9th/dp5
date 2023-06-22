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


def mcboot_actionpay_468x60():

    modulo = html.Div(
    [

        dmc.Space(h=10), 
        html.A(
            #href="http://trafficcost.ru/647f9d382bfa8150c25478c3/st/bn",
            children=[
                html.Img(src=r'assets/banners/mcboot_actionpay_468x60.jpg', width="468x", height="60px", 
                #className="p-3 mb-2 text-md-center",
                ),
                ]
            ),
        dmc.Space(h=10), 
    ], 
    id = 'mcboot_actionpay_468x60',
    style={
        'text-align': 'center'
        }
    ),

    return modulo

