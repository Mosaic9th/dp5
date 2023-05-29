#dash
from dash import html

#plotly

#dash-bootstrap-components

#dash-bootstrap-templates

#dash_mantine_components

#dash-iconify

#modulos
from modulos.modulo_cadastro_form import create_modulo_cadastro_form
modulo_cadastro_form = create_modulo_cadastro_form()

#paginas

#callbacks/layouts

#outros


def create_pagina_criar_conta():

    pagina = html.Div(

    [
        
        modulo_cadastro_form

    ], id = 'pagina_criar_conta',
    style= {'min-height': '80vh',
            'background-color': '#ffffff'}

    )

    return pagina

