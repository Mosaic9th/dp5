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



nome_cadastro = html.Div(
    [
        dmc.Space(h=30),
        dbc.Label("Nome:"),
        dmc.TextInput(
            #label="Your Email",
            #style={"width": 200},
            placeholder="Digite seu nome",
            #icon=DashIconify(icon="ic:round-alternate-email"),
            id="cadastro_nome"
        ),
        
        
    ],
    className="mb-3",
)

email_cadastro = html.Div(
    [
        dbc.Label("E-mail:"),
        dmc.TextInput(
            placeholder="Digite seu e-mail",
            icon=DashIconify(icon="ic:round-alternate-email"),
            id="cadastro_email"
        ),

    ],
    className="mb-3",
)
password_cadastro_1 = html.Div(
    [
        dbc.Label("Senha:"),
        dmc.PasswordInput(
            placeholder="Digite uma senha",
            icon=DashIconify(icon="bi:shield-lock"),
            id= 'cadastro_password_1'
        ),
        dmc.Space(h=10),
        dbc.FormText(
            "Use oito ou mais caracteres com uma combinação de letras, números e símbolos.", className = 'justify-content-center'
        ),
        
    ],
    className="mb-3",
)

password_cadastro_2 = html.Div(
    [
        dbc.Label("Repita a senha:"),
        dmc.PasswordInput(
            placeholder="Repita a senha",
            icon=DashIconify(icon="bi:shield-lock"),
            id= 'cadastro_password_2'
        ),


    ],
    className="mb-3",
)



botao_cadastrar = html.Div(
    [
        dmc.Space(h=20),

       dbc.Checklist(
                options=[
                {"label": "Li e concordo com os TERMOS DE USO e com a POLÍTICA DE PRIVACIDADE.", "value": 1},
                ],
                value=[],
                inline=False,
                switch=False,
                id= "checklist_termos",
                #persistence = True,
                #persistence_type = 'session'

                ),
        dmc.Space(h=10),

        html.Div([
        dmc.Anchor(dbc.Button("Termos de Uso", color="link"), href="/termos-de-uso",),
        dmc.Anchor(dbc.Button("Política de Privacidade", color="link"), href="/politica-de-privacidade",),
        ], style = {'text-align': 'center'}
        ),
        dmc.Space(h=30),

        html.Div(
            dbc.Button(
                "CADASTRAR", id="btn_cadastrar", className="me-2", color="success", outline=True, n_clicks=0, disabled = True), className="d-grid gap-2",
            ),
        dmc.Space(h=30),
    
        #alerts
        dbc.Alert(
        color="danger",
        className="d-flex align-items-center",
        id= "danger_cadastro_invalido",
        is_open = False,  
        ),

        dbc.Alert(
        [
            html.I(className="bi bi-x-octagon-fill me-4", ), "E-mail inválido." 
        ],
        color="danger",
        className="d-flex align-items-center",
        id= "danger_cadastro_email_invalido",
        is_open = False,  
        ),

        dbc.Alert(
        [
            html.I(className="bi bi-x-octagon-fill me-4", ), "As duas senhas informadas devem ser idênticas." 
        ],
        color="danger",
        className="d-flex align-items-center",
        id= "danger_cadastro_password_2_senhas_diferentes",
        is_open = False,  
        ),

        dbc.Alert(
        [
            html.I(className="bi bi-x-octagon-fill me-4", ), "As duas senhas informadas devem ser idênticas." 
        ],
        color="danger",
        className="d-flex align-items-center",
        id= "danger_cadastro_password_2_senhas_diferentes",
        is_open = False,  
        ),

        dbc.Alert(
        [
            html.I(className="bi bi-x-octagon-fill me-4", ), "Ao criar a senha, use apenas letras, números e caracteres de pontuação comuns."
        ],
        color="danger",
        className="d-flex align-items-center",
        id= "danger_cadastro_password_formato",
        is_open = False,  
        ),

        dbc.Alert(
        [
            html.I(className="bi bi-x-octagon-fill me-4", ), "A senha não pode começar ou terminar com um espaço em branco."
        ],
        color="danger",
        className="d-flex align-items-center",
        id= "danger_cadastro_password_espaco",
        is_open = False,  
        ),

        dbc.Alert(
        color="danger",
        className="d-flex align-items-center",
        id= "danger_cadastro_caracteres",
        is_open = False,  
        ),
    

        dmc.Space(h=5),
        
        dmc.Anchor(dbc.Button("Já tem cadastro?", color="link"), href="/login"),

        dmc.Space(h=25),
    ]
)
form = dbc.Form([nome_cadastro, email_cadastro, password_cadastro_1, password_cadastro_2, botao_cadastrar])

def create_modulo_cadastro_form():

    modulo = html.Div(
    
        dbc.Container(
        [
            html.Div(
            [

                dbc.Row(
                [
                    dmc.Space(h=50),
                    html.H3("Criar Conta", style = {'text-align': 'center'},className="text-primary", ), 
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
        ), id = 'modulo_cadastro_form', style={'background-color': '#ffffff'}, 
    )

    return modulo