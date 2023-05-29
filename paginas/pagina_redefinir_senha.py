#dash
from dash import html

#plotly

#dash-bootstrap-components

#dash-bootstrap-templates

#dash_mantine_components

#dash-iconify

#modulos
from modulos.modulo_redefinir_senha_form import create_modulo_redefinir_senha_form
modulo_redefinir_senha_form = create_modulo_redefinir_senha_form()

#paginas

#callbacks/layouts

#outros


def create_pagina_redefinir_senha():

    pagina = html.Div(

    [
        
        modulo_redefinir_senha_form

    ], id = 'pagina_redefinir_senha_form',
    style= {'min-height': '80vh',
            'background-color': '#ffffff'}


    )

    return pagina

