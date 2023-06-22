#dash
from dash import html

#plotly

#dash-bootstrap-components
import dash_bootstrap_components as dbc

#dash-bootstrap-templates

#dash_mantine_components
import dash_mantine_components as dmc

#dash-iconify
from dash_iconify import DashIconify

#modulos

#paginas

#callbacks/layouts

#outros



def create_modulo_navbar():
    
    modulo =  html.Div(

        [

        dbc.Container(
        [

            html.Div(
            [
                
                dbc.Row(
                [
                    dbc.Col(
                    [

                        dmc.Space(h=15),
                        html.Img(src=r'assets/images/icon_mosaic.png', width="30x", height="30px", ),
                        dbc.NavbarBrand("backtest.zone", className="ms-2")

                        
                        

                    ], 
                    ),

                    dbc.Col(
                    [
                       
                        
                        html.Div(
                        [
                            dmc.Menu(
                            [
                                
                                dmc.MenuTarget(
                                    
                                    dmc.Button(children = '', id= 'visitante', variant="subtle", color = "violet", leftIcon=DashIconify(icon="mdi:user"),),
                                
                                ),


                                ###

                                dmc.MenuDropdown(
                                [

                                    html.Div(
                                    [
                                    dmc.MenuItem(
                                        "Minha Conta",
                                        href='/minha-conta',
                                        id = 'menu_minha_conta',
                                        icon=DashIconify(icon="carbon:user-profile"),
                                    ),
                                                        
                                    dmc.Button(
                                        "Sair",
                                        variant="outline",
                                        leftIcon=DashIconify(icon="ri:logout-circle-line"),
                                        color='red',
                                        fullWidth=True,
                                        id = 'menu_sair',
                                        style = {'display':'flex'}
                                    ),
                                    ], id = 'menu_logado'               
                                    ),

                                    html.Div(
                                    [
                                    dmc.MenuItem(
                                        "Entrar",
                                        href='/login',
                                        id = 'menu_entrar',
                                        icon=DashIconify(icon="ri:login-circle-line"),
                                    ),

                                    dmc.MenuItem(
                                        "Criar Conta",
                                        href='/criar-conta',
                                        id = 'menu_cadastro',
                                        icon=DashIconify(icon="mdi:subscriptions"),
                                    ),
                                    
                                    dmc.MenuItem(
                                        "Esqueci Minha Senha",
                                        href='/redefinir-senha',
                                        id = 'menu_redefinir_senha',
                                        icon=DashIconify(icon="mdi:forgot-password"),
                                    ),
                                    ],id = 'menu_deslogado' 
                                    ),
                                                                        
                                ], id = 'menu_navbar'
                                ),
                                ###


                            ], style={
                                #'border': 'thin grey solid',
                                'height':'60px'
                                },

                            transition="rotate-top",
                            transitionDuration=150,
                            position='bottom-end'
                        
                            
                            ),

                        ], className= "d-flex justify-content-end",
                        style={
                                #'border': 'thin grey solid',
                                },
                        ),

                    ], 
                    ),

                ]
                ),
                
            ], style = {'height':'60px',
                        #'display': 'flex',
                        #'justify-content': 'center',
                        #'align-items': 'center',
                        },
            ),


            
        ]
        ),

        dbc.Container(
        [
            html.Div(
            [

            html.Div(
            [
                dbc.Col(
                [
                    
                    html.Img(src=r'assets/images/icon_mosaic.png', width="30x", height="30px", ),
                    dbc.NavbarBrand("backtest.zone", className="ms-2")
                ]
                ),

                

                dbc.Col(
                [
                    dmc.Space(h=12),
                    html.Div(
                    [
                        
                        dmc.Text(id="menu-text", mb="md"),
                        dmc.Menu(
                        [
                            
                            #dmc.MenuTarget(dmc.Button(children = '', id= 'visitante', variant="subtle", color = "violet", leftIcon=DashIconify(icon="mdi:user"),)),
                                         
                            dmc.MenuDropdown(
                            [
                                dmc.MenuItem(
                                    "Minha Conta",
                                    href='/minha-conta',
                                    #id = 'menu_minha_conta',
                                    icon=DashIconify(icon="carbon:user-profile"),
                                ),
                                                    
                                dmc.Button(
                                    "Sair",
                                    variant="outline",
                                    leftIcon=DashIconify(icon="ri:logout-circle-line"),
                                    color='red',
                                    fullWidth=True,
                                    #id = 'menu_sair',
                                    style = {'display':'flex'}
                                ),
                                                    
                            ], #id = 'menu_logado',
                                            
                            ),
                            
                            dmc.MenuDropdown(
                            [
                                dmc.MenuItem(
                                    "Entrar",
                                    href='/login',
                                    #id = 'menu_entrar',
                                    icon=DashIconify(icon="ri:login-circle-line"),
                                ),

                                dmc.MenuItem(
                                    "Criar Conta",
                                    href='/criar-conta',
                                    #id = 'menu_cadastro',
                                    icon=DashIconify(icon="mdi:subscriptions"),
                                ),
                                
                                dmc.MenuItem(
                                    "Esqueci Minha Senha",
                                    href='/redefinir-senha',
                                    #id = 'menu_redefinir_senha',
                                    icon=DashIconify(icon="mdi:forgot-password"),
                                ),
                                                                        
                            ], #id = 'menu_deslogado'
                            ),
                            
                            
                        ],transition="rotate-top",
                        transitionDuration=150,
                        position='left-end'
                        ),
                        
                    ], #style = {'text-align' : 'right'},
                        className= "d-flex justify-content-end"
                    ),
                ],
                )

            ], #align="center",
            id = 'nav_div',
            style = {'height' : '60px', 
                     #'border': 'thin grey solid',
                    }
                        
            ),

            ],style = {'height' : '60px', 
                     #'border': 'thin grey solid',
                    }
            ),
              
        ], style = {'display' : 'none'}
        )#,id = 'modulo_navbar_b'
        ],id = "modulo_navbar"
    )
    

    return modulo