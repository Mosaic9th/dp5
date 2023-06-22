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


def novomanto_actionpay_720x300():

    modulo = html.Div(
    [

        #dmc.Space(h=10), 
        html.A(
            href="http://trafficcost.ru/647f9d382bfa8150c25478c3/st/bn",
            children=[
                html.Img(src=r'assets/banners/quintoandar_480x466.jpg', width="480px", height="480px", 
                #className="p-3 mb-2 text-md-center",
                ),
                ]
            ),
        #dmc.Space(h=10), 
    ], 
    id = 'quintoandar_480x466',
    style={
        'text-align': 'center'
        }
    ),

    return modulo

