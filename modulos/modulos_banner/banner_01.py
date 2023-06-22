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
import pandas as pd 

from cfd import banners

result_banners = banners()

banner_01_file = result_banners[0]
banner_01_link = result_banners[1]

def banner_01():

    
        
    modulo = html.Div(
    [

        
        
        html.A(
            href= banner_01_link,
            children=[
                html.Img(src=r"assets/banners/" + banner_01_file),
                ]
            ),

    ], 
    id = 'banner_01',
    style={
        #'text-align': 'center'
        }
    ),

    return modulo

