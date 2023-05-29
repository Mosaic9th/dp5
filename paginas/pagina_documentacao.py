#dash
from dash import html

#plotly

#dash-bootstrap-components

#dash-bootstrap-templates

#dash_mantine_components

#dash-iconify

#modulos
#from modulos.modulo_login_form import create_modulo_login_form
#modulo_login_form = create_modulo_login_form()

#paginas

#callbacks/layouts

#outros


def create_pagina_documentacao():

    pagina = html.Div(

    [
        
        #modulo_login_form

    ], id = 'pagina_documentacao',
    style= {'min-height': '80vh',
            'background-color': '#ffffff'}
    )

    return pagina

