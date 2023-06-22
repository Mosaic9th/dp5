#https://blog.betrybe.com/tecnologia/err-connection-reset-como-resolver/

#dash
from dash import Dash, dcc, html, Input, Output, callback

#plotly

#dash-bootstrap-components
import dash_bootstrap_components as dbc

#dash-bootstrap-templates
from dash_bootstrap_templates import load_figure_template

#dash_mantine_components

#dash-iconify

#paginas

#modulos
from modulos.modulo_stores import create_modulo_stores
modulo_stores = create_modulo_stores()
from modulos.modulo_navbar import create_modulo_navbar
modulo_navbar = create_modulo_navbar()
from modulos.modulo_footer import create_modulo_footer
modulo_footer = create_modulo_footer()
from modulos.modulo_footer_b import create_modulo_footer_b
modulo_footer_b = create_modulo_footer_b()

#callbacks / layouts
import callbacks
from layouts import layout_home, layout_login, layout_criar_conta, layout_redefinir_senha, layout_contato, layout_lgpd, layout_minha_conta, layout_politica_de_privacidade, layout_termos_de_uso, layout_quem_somos, layout_documentacao, layout_404



#outros


# This loads the "flatly" themed figure template from dash-bootstrap-templates library,
load_figure_template("darkly")

app = Dash(__name__, suppress_callback_exceptions=True,
            external_stylesheets=[dbc.themes.DARKLY, dbc.icons.BOOTSTRAP],
            meta_tags=[{'name': 'viewport',
                       'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.9, minimum-scale=0.5,'}],
            )

server = app.server

app.layout = html.Div([
     modulo_stores,
     dcc.Location(id='url', refresh=False),
     modulo_navbar,
     html.Div(id='page-content', style= {'min-height': '80vh'}),

     html.Div(
     [
     modulo_footer,
     modulo_footer_b,
     ]
     )
    
])

@callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):

     if pathname == '/':
          return layout_home
     elif pathname == '/login':
          return layout_login
     elif pathname == '/criar-conta':
          return layout_criar_conta
     elif pathname == '/redefinir-senha':
          return layout_redefinir_senha
     elif pathname == '/contato':
          return layout_contato
     elif pathname == '/lgpd':
          return layout_lgpd
     elif pathname == '/minha-conta':
          return layout_minha_conta
     elif pathname == '/politica-de-privacidade':
          return layout_politica_de_privacidade 
     elif pathname == '/termos-de-uso':
          return layout_termos_de_uso
     elif pathname == '/quem-somos':
          return layout_quem_somos
     elif pathname == '/documentacao':
          return layout_documentacao
     else:
          return layout_404

if __name__ == '__main__':
    app.run_server(debug=True)