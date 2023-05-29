#dash
from dash import html

#plotly

#dash-bootstrap-components

#dash-bootstrap-templates

#dash_mantine_components

#dash-iconify

#modulos
from modulos.modulos_relatorio.modulo_content_r_1 import create_modulo_content_r_1
modulo_content_r_1 = create_modulo_content_r_1()

#paginas

#callbacks/layouts

#outros


def create_pagina_relatorio():

    pagina = html.Div(

    [
        
        #modulo_content_r_1

    ], id = 'pagina_relatorio'
    )

    return pagina

