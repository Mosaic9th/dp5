#dash
from dash import html

#plotly

#dash-bootstrap-components

#dash-bootstrap-templates

#dash_mantine_components

#dash-iconify

#modulos
from modulos.modulo_quem_somos import create_modulo_quem_somos
modulo_quem_somos = create_modulo_quem_somos()

#paginas

#callbacks/layouts

#outros


def create_pagina_quem_somos():

    pagina = html.Div(

    [
        
        modulo_quem_somos

    ], id = 'pagina_quem_somos',
    style= {'min-height': '80vh',
            'background-color': '#ffffff'}
    )

    return pagina

