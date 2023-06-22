#dash
from dash import dcc, html

#plotly

#dash-bootstrap-components
import dash_bootstrap_components as dbc

#dash-bootstrap-templates

#dash_mantine_components

#dash-iconify

#modulos

#paginas
from paginas.pagina_home import create_pagina_home
pagina_home = create_pagina_home ()

from paginas.pagina_login import create_pagina_login
pagina_login = create_pagina_login ()

from paginas.pagina_criar_conta import create_pagina_criar_conta
pagina_criar_conta = create_pagina_criar_conta ()

from paginas.pagina_redefinir_senha import create_pagina_redefinir_senha
pagina_redefinir_senha = create_pagina_redefinir_senha ()

from paginas.pagina_contato import create_pagina_contato
pagina_contato = create_pagina_contato ()

from paginas.pagina_lgpd import create_pagina_lgpd
pagina_lgpd = create_pagina_lgpd ()

from paginas.pagina_minha_conta import create_pagina_minha_conta
pagina_minha_conta = create_pagina_minha_conta ()

from paginas.pagina_politica_de_privacidade import create_pagina_politica_de_privacidade
pagina_politica_de_privacidade = create_pagina_politica_de_privacidade ()

from paginas.pagina_termos_de_uso import create_pagina_termos_de_uso
pagina_termos_de_uso = create_pagina_termos_de_uso ()

from paginas.pagina_quem_somos import create_pagina_quem_somos
pagina_quem_somos = create_pagina_quem_somos ()

from paginas.pagina_documentacao import create_pagina_documentacao
pagina_documentacao = create_pagina_documentacao ()

from paginas.pagina_404 import create_pagina_404
pagina_404 = create_pagina_404 ()


#callbacks/layouts

#outros


layout_home = html.Div(

[
    pagina_home
],  

)


layout_login = html.Div([
    pagina_login
])

layout_criar_conta = html.Div([
    pagina_criar_conta
])

layout_redefinir_senha = html.Div([
    pagina_redefinir_senha
])

layout_contato = html.Div([
    pagina_contato
])

layout_lgpd = html.Div([
    pagina_lgpd
])

layout_minha_conta = html.Div([
    pagina_minha_conta
])

layout_politica_de_privacidade = html.Div([
    pagina_politica_de_privacidade
])

layout_termos_de_uso = html.Div([
    pagina_termos_de_uso
])

layout_quem_somos = html.Div([
    pagina_quem_somos
])

layout_documentacao = html.Div([
    pagina_documentacao
])

layout_404 = html.Div([
    pagina_404
])


