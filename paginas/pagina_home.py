#dash
from dash import html

#plotly

#dash-bootstrap-components

#dash-bootstrap-templates

#dash_mantine_components

#dash-iconify

#modulos
from modulos.modulos_home.modulo_header import create_modulo_header
modulo_header = create_modulo_header()
from modulos.modulos_home.modulo_content_1 import create_modulo_content_1
modulo_content_1 = create_modulo_content_1()
from modulos.modulos_home.modulo_content_2 import create_modulo_content_2
modulo_content_2 = create_modulo_content_2()
from modulos.modulos_home.modulo_content_3 import create_modulo_content_3
modulo_content_3 = create_modulo_content_3()

from modulos.modulos_relatorio.modulo_backtest import create_modulo_backtest
modulo_backtest = create_modulo_backtest()

#paginas

#callbacks/layouts

#outros


def create_pagina_home():

    pagina = html.Div(

    [
        modulo_header,
        modulo_content_1,
        modulo_content_2,
        modulo_content_3,
        modulo_backtest

    ], id = 'pagina_home'
    )

    return pagina

