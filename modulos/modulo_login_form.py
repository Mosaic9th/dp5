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



email_login = html.Div(

    [
        dmc.Space(h=30),
        dbc.Label("E-mail:", html_for="example-email"),
        dmc.TextInput(
            placeholder="Digite seu e-mail",
            icon=DashIconify(icon="ic:round-alternate-email"),
            id= 'login_email'
        )
    ],
    className="mb-3",
)
password_login = html.Div(
    [
    dbc.Label("Senha:"),
    dmc.PasswordInput(
        #label="Didite sua senha:",
        #style={"width": 300},
        placeholder="Digite sua senha",
        icon=DashIconify(icon="bi:shield-lock"),
        id= 'login_password'
    ),
    
    ],
    className="mb-3",
)

botao_login = html.Div(
    [
        

        dmc.Space(h=30),

        html.Div(
            dbc.Button(
                "ENTRAR", id="botao_login", className="me-2", color="success", outline=True, n_clicks=0, disabled = True), className="d-grid gap-2",
            ),

        
        dmc.Space(h=30),

        #alerts
        dbc.Alert(
        [
            
            html.I(className="bi bi-check-circle-fill me-4", 
            ), 
        ],
        color="danger",
        className="d-flex align-items-center",
        id= "danger_email_senha_invalido",
        is_open = False,  
        ),
        #

        dmc.Space(h=5),

        html.Div(
        dmc.Anchor(dbc.Button("Esqueceu a senha?", color="link"), href="/redefinir-senha"),
        ),
        html.Div(
        #dmc.Anchor(dbc.Button("Ainda não tem cadastro?", color="link"), href="/criar-conta"),
        dmc.Anchor(dbc.Button("Ainda não tem cadastro?", color="link"), href="/criar-conta"),
        ),
        dmc.Space(h=25),       

        
    ]
)

form = dbc.Form([email_login, password_login, botao_login])


def create_modulo_login_form():

    modulo = html.Div(
    
        dbc.Container(
        [
            html.Div(
            [

                dbc.Row(
                [
                    dmc.Space(h=50),
                    html.H3("Login", style = {'text-align': 'center'},className="text-primary", ), 
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
        ), id = 'modulo_login_form', style={'background-color': '#ffffff'}, 
    )

    return modulo