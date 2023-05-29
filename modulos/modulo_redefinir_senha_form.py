#dash
import dash_bootstrap_components as dbc
from dash import html

#plotly

#dash-bootstrap-components

#dash-bootstrap-templates

#dash_mantine_components
import dash_mantine_components as dmc

#dash-iconify
from dash_iconify import DashIconify

#paginas

#modulos

#callbacks / layouts

#outros



email_redefinir = html.Div(

    [
        dmc.Space(h=30),
        dbc.Label("E-mail:", html_for="example-email"),
        dmc.TextInput(
            placeholder="Digite seu e-mail cadastrado",
            icon=DashIconify(icon="ic:round-alternate-email"),
            id="redeninir_email"
        )
    ],
    className="mb-3",
)


botao_redefinir = html.Div(
    [
        

        dmc.Space(h=30),

        html.Div(
            dbc.Button(
                "REDEFINIR SENHA", id="botao_redefinir", className="me-2", color="success", outline=True, n_clicks=0, disabled = True), className="d-grid gap-2",
            ),

        
        dmc.Space(h=30),
        dbc.Alert(
        [
            
            html.I(className="bi bi-check-circle-fill me-4", 
            ), 
        ],
        color="danger",
        className="d-flex align-items-center",
        id= "danger_refefinir_senha",
        is_open = False,  
        ),
        
        dbc.Alert(
        [
            
            html.I(className="bi bi-check-circle-fill me-4", 
            ), 
        ],
        color="success",
        className="d-flex align-items-center",
        id= "success_refefinir_senha",
        is_open = False,  
        ),
        dmc.Space(h=5),

        html.Div(
        [
        dmc.Anchor(dbc.Button("Fazer login.", color="link"), href="/login"),
        dmc.Space(h=25), 
        ], style = {'display':'none'}, id = 'login_link'
        ),
              

        
    ]
)

form = dbc.Form([email_redefinir , botao_redefinir])


def create_modulo_redefinir_senha_form():

    modulo = html.Div(
    
        dbc.Container(
        [
            html.Div(
            [

                dbc.Row(
                [
                    dmc.Space(h=50),
                    html.H3("Redefinir Senha", style = {'text-align': 'center'},className="text-primary", ), 
                    dmc.Space(h=30),
                    dbc.Col(
                    
                        dbc.Card(
                            dbc.CardBody(
                                form
                            ),
                        color="dark", inverse=True
                        ),
                    style = {'max-width' : '460px'}
                    ),
                    dmc.Space(h=50),

                ], className ='row d-flex justify-content-center'
                )
            ]
            )
        ]
        ), id = 'modulo_redefinir_senha_form', style={'background-color': '#ffffff'}, 
    )

    return modulo