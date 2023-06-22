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

#paginas

#modulos

#callbacks / layouts

#outros


def create_modulo_footer_b():
    
    modulo = html.Div(
    
        dbc.Container(
        [
            html.Div(
            [

                dbc.Row(
                [
                    
                    dmc.Space(h=40),
                    dbc.Col(
                    [
                        html.Img(src=r'assets/images/icon_mosaic.png', width="100x", height="100px", ),
                        dmc.Space(h=5),
                        html.H4("backtest.zone", className="text-dark ms-2"),
                                
                    
                    ], md = 4,
                    style= {
                        'text-align':'center',
                    }

                    ),

                    dbc.Col(
                    [
                        dmc.Space(h=30),

                        dbc.Row(
                        [   
                            dbc.Col(
                            
                                DashIconify(
                                    icon="ps:youtube",
                                    width=50,
                                    height=50,
                                    rotate=0,
                                    color = "#222222"
                                    #flip="horizontal",
                                ),
                            ),
                        
                            dbc.Col(
                            
                                DashIconify(
                                    icon="ant-design:instagram-filled",
                                    width=50,
                                    height=50,
                                    rotate=0,
                                    color = "#222222"
                                    #flip="horizontal",
                                ),
                            ),

                            dbc.Col(
                            
                            
                                DashIconify(
                                    icon="simple-icons:medium",
                                    width=50,
                                    height=50,
                                    rotate=0,
                                    color = "#222222"
                                    #flip="horizontal",
                                ),
                            ),

                            
                        ]
                        ),

                    ], md = 8,
                    style= {
                        'text-align':'center',
                        #'display': 'flex',
                        #'justify-content': 'space-between',
                    }

                    ),

                dmc.Space(h=20),
                html.H6("2023 | Todos os Direitos Reservados. Segurança e Privacidade.", className="text-dark ms-2",style= {'text-align':'center',}
                ),
                dmc.Space(h=20),
                ],
                ),

            ], className="p-3",
        ),

    ], 
    ),style={'background-color': '#ebe9eb',
             #'display': 'inline-block', 
             'vertical-align': 'bottom',
             #'height': '260px',

            }, 
    id = "modulo_footer_b"
    
)


    return modulo