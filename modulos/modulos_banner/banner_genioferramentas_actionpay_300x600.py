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


def genioferramentas_actionpay_300x600():

    modulo = html.Div(
    [

        #dmc.Badge("PUBLICIDADE", variant="dot"), 
        html.A(
            href="http://trafficcost.ru/647fa4572bfa81724c0524e8/st/bn",
            children=[
                html.Img(src=r'assets/banners/genioferramentas_actionpay_300x600.jpg', width="300px", height="600px", 
                #className="p-3 mb-2 text-md-center",
                ),
                ]
            ),
        #dmc.Space(h=10), 
    ], 
    id = 'genioferramentas_actionpay_300x600',
    #style={
        #'text-align': 'right'
        #}
    ),

    return modulo

