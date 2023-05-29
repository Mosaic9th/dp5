#dash
from dash import html

#plotly

#dash-bootstrap-components

#dash-bootstrap-templates

#dash_mantine_components

#dash-iconify

#modulos
from modulos.modulo_contato_form import create_modulo_contato_form
modulo_contato_form = create_modulo_contato_form()

#paginas

#callbacks/layouts

#outros


def create_pagina_contato():

    pagina = html.Div(

    [
        
        modulo_contato_form

    ], id = 'pagina_contato',
    style= {'min-height': '80vh',
            'background-color': '#ffffff'}
    )

    return pagina

