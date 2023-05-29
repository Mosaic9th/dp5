#dash
import dash_bootstrap_components as dbc
from dash import html, dcc

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



assunto = html.Div(

    [
        dmc.Space(h=30),
        dbc.Label("Assunto:"),
        dcc.Dropdown(
            options = ['Dúvida', 'Sugestão', 'Reclamação', 'Outro'],
            id = 'dropdown_lgpd',
            multi=False,
            placeholder="Selecione o assunto",
        ),
    ],
    className="mb-3",
)
mensagem = html.Div(
    [
    #dmc.Space(h=20),
    dmc.Textarea(
  
        placeholder="Digite sua mensagem...",
        autosize=True,
        minRows=4,
        maxRows=6,
        id = 'mensagem_lgpd'
    ),
    
    ],
    className="mb-3",
)

botao_contato = html.Div(
    [
        

        dmc.Space(h=30),

        html.Div(
            dbc.Button(
                "ENVIAR", id="botao_enviar_lgpd",  color="success", outline=True, n_clicks=0, disabled = True
            ), className="d-grid gap-2",
        ),

        
        # inserir alerts!!!!!!!!!!!!!!!!!
        
        dmc.Space(h=25),
        
        html.Div(

            [ 
            dbc.Alert(
            [
                html.I(className="bi bi-x-octagon-fill me-4"
                ), "Houve um erro inesperado. Por favor, tente mais tarde.",
            ],
            color="danger",
            className="d-flex align-items-center",
            id= "danger_lgpd",
            is_open = False
            ),
        ]),

        html.Div(
            [ 
            dbc.Alert(
            [
                #html.I(className="bi bi-check-circle-fill me-4", 
                #), "Contato enviado com sucesso!", 
            ],
            color="success",
            className="d-flex align-items-center",
            id= "success_lgpd",
            is_open = False,  

            ),

            

            dmc.Space(h=25),  
        ]),
        


        html.Div(
    
            html.Div(
        
            [
    
                dbc.Button(
                    "VOLTAR", id="botao_voltar_lgpd",  color="info", outline=True, n_clicks=0, disabled = False, href = '/' 
                ),

                dmc.Space(h=25), 
    
            ],className="d-grid gap-2", 
            ),id = 'div_lgpd_botao_voltar', style={'display':'none'}
        ),
        
        html.Div(
    
            html.Div(
        
            [
                
                html.Div(
                    
                    dbc.Spinner(spinner_style={"width": "30px", "height": "30px"},color="info", id = "spinner_lgpd_voltar", ),
                    className= 'text-md-center',
                ),  
                

                dmc.Space(h=25), 
                
            ], className="d-grid gap-2", 
            ),
        id = 'div_lgpd_spinner', style={'display':'none'}

        )
    ]
)

form = dbc.Form([assunto, mensagem, botao_contato])


def create_modulo_lgpd_form():

    modulo = html.Div(
    
        dbc.Container(
        [
            html.Div(
            [

                dbc.Row(
                [
                    dmc.Space(h=50),
                    html.H3("Contato LGPD", style = {'text-align': 'center'},className="text-primary", ), 
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
        ), id = 'modulo_lgpd_form', style={'background-color': '#ffffff'}, 
    )

    return modulo