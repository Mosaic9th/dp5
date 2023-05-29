#dash
from dash import html

#plotly

#dash-bootstrap-components

#dash-bootstrap-templates

#dash_mantine_components

#dash-iconify

#modulos
from modulos.modulo_lgpd_form import create_modulo_lgpd_form
modulo_lgpd_form = create_modulo_lgpd_form()

#paginas

#callbacks/layouts

#outros


def create_pagina_lgpd():

    pagina = html.Div(

    [
        
        modulo_lgpd_form

    ], id = 'pagina_lgpd',
    style= {'min-height': '80vh',
            'background-color': '#ffffff'}
    )

    return pagina

