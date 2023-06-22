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

import dash_dangerously_set_inner_html



def create_modulo_quem_somos():

    modulo = html.Div(
    
        dbc.Container(
        [
            html.Div(
            [

                dbc.Row(
                [
                    dmc.Space(h=50),
                    html.H3("Quem Somos", style = {'text-align': 'center'},className="text-primary", ), 
                    dmc.Space(h=30),
                    
                    
                ], className ='row d-flex justify-content-center'
                ),

                #dmc.Space(h=50),

                dbc.Row(
                [
                    html.Div(
                    
                        dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                            
                            <p>
                                <h5 color="#222222" align="justify">
                                    
                                    O site <strong>backtest.zone</strong> disponibiliza uma ferramenta criada para permitir que voc&ecirc; simule uma <strong>carteira de a&ccedil;&otilde;es</strong> utilizando-se dos 
                                    <strong>dados hist&oacute;ricos</strong> dos principais pap&eacute;is negociados no Brasil.

                                <h5>
                            </p>

                            <p>
                                 <h5 color="#222222" align="justify">

                                    Funciona assim: <strong>voc&ecirc; escolhe as a&ccedil;&otilde;es</strong>, <strong>configura a simula&ccedil;&atilde;o</strong> e <strong>gera os resultados</strong>. Da&iacute; voc&ecirc; pode analisar 
                                    os riscos a que est&aacute; sujeito e os retornos que pode auferir se, de fato, decidir aplicar dinheiro de verdade. Ou seja, voc&ecirc; pode fazer o 
                                    <strong>backtest do seu portf&oacute;lio</strong> antes de tomar qualquer decis&atilde;o que ponha seu patrim&ocirc;nio em jogo.

                                <h5>
                            </p>
                            
                            <p>
                                <h5 color="#222222" align="justify">
                                    
                                    &Eacute; claro que resultados passados n&atilde;o implicam resultados futuros, tendo em vista in&uacute;meros fatores que se alteram rapidamende e 
                                    mudam completamente o panorama do mercado. Por essa raz&atilde;o, n&atilde;o recomendamos qualquer forma de investimento a voc&ecirc;, deixando isso a 
                                    cargo dos an&aacute;listas profissionais. O que fazemos &eacute; entregar uma boa ferramenta para lhe ajudar a investir de forma consciente, cuidando 
                                    dos riscos inerentes a essa atividade.

                                <h5>
                            </p>
                        
                        '''),className="text-primary text-secondary p-3 mb-3",
                        style={'text-indent': '100px',
                               #'padding-left':'100px',
                               #'padding-right':'100px',
                               }
                        
                        
       
                
                    ),
                ],style={
                    'padding-left':'100px',
                    'padding-right':'100px',
                }
                ),
            dmc.Space(h=100),
            ]
            )
        ]
        ), id = 'modulo_contato_form', style={'background-color': '#ffffff'}, 
    )

    return modulo