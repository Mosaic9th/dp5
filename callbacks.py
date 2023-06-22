#dash
from dash import Input, Output, callback, html, ctx, State
#from dash_extensions.enrich import Dash, Input, Output, html
from dash.exceptions import PreventUpdate

#plotly
import plotly.graph_objs as go

import plotly.express as px

#dash-bootstrap-components
import dash_bootstrap_components as dbc

#dash-bootstrap-templates

#dash_mantine_components

#dash-iconify

#modulos

#paginas

#callbacks/layouts

#outros
import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import numpy as np
from datetime import date

import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') 

# importando a lista dos códigos das ações
carteira_ibov_bruta = pd.read_csv('assets/dados/parametros_ibov/dados_ibov.csv')
codigos_lista = carteira_ibov_bruta['Código'].values.tolist()
codigos_lista = sorted(codigos_lista)
ibov_tabela = carteira_ibov_bruta[['Código', 'Ação', 'Setor']] 

# mes e ano final
today = datetime.now()
first = today.replace(day=1)
last = first - timedelta(days=1)
last_month = last.month
year_ = last.year

#funções útes
def trunc_datetime(someDate):
    return someDate.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

from cfd import (cadastro_firebase, login_firebase, validar_email, validar_senha, refresh_email, reenviar_email_confirmacao, refresh_autenticacao, refefinir_senha,
                dividendos_cut, envio_email
                )

# importando a amplitudes dos meses
amplitude_mes = pd.read_csv('assets/dados/parametros_ibov/amplitude_mes.csv')

# cores_theme
primary = 'rgb(55,90,127)'
secondary = 'rgb(68,68,68)'
success = 'rgb(0,188,140)'
danger = 'rgb(231,76,60)'
warning = 'rgb(243,156,18)'
info = 'rgb(52,152,219)'
light = 'rgb(173,181,189)'
dark = 'rgb(48,48,48)'

# cores
cor1 = 'rgb(15,181,174)'
cor2 = 'rgb(64,70,202)'
cor3 = 'rgb(246,133,17)'
cor4 = 'rgb(222,61,130)'
cor5 = 'rgb(126,132,250)'
cor6 = 'rgb(114,224,106)'
cor7 = 'rgb(20,122,243)'
cor8 = 'rgb(115,38,211)'
cor9 = 'rgb(232,198,0)'
cor10 = 'rgb(203,93,0)'
cor11 = 'rgb(0,143,93)'
cor12 = 'rgb(188,233,49)'

#lista_cores_12 = [turquoise, summer_sky, azul, magenta, slate_blue, rosybrown,  darkgoldenrod, bege, yellow, lavender, darkgrey, atlantis]

lista_cores_12 = [cor1,cor2,cor3,cor4,cor5,cor6,cor7,cor8,cor9,cor10,cor11,cor12]
#################################################################
#CALLBACKS START ################################################
#################################################################



#alert_benchmark
@callback(

    [
    Output ("danger_btc", "is_open"),
    Output ("danger_btc", "children"),
    ],
    [
    Input('dropdown_benchmarks', 'value'),
    Input('dia_inicial', 'children'),
    Input('dropdown_mes_inicio', 'value'),
    Input('dropdown_ano_inicio', 'value'),
    ]

)

def alert_benchmark(dropdown_benchmarks, dia_inicial, dropdown_mes_inicio, dropdown_ano_inicio):
    
    if 'Bitcoin' in dropdown_benchmarks:

        btc_hist = pd.read_csv('assets/dados/benchmarks/Bitcoin.csv')
        
        btc_hist['Date'] = pd.to_datetime(btc_hist['Date'])

        data_btc = btc_hist['Date'].iloc[0]

        data_selecionada = date(int(dropdown_ano_inicio), int(dropdown_mes_inicio), int(dia_inicial))


        if data_selecionada < data_btc:

            is_open = True
            danger = (html.I(className="bi bi-x-octagon-fill me-4", ), 'Para escolher o ativo Bitcoin como comparativo, o mês/ano inicial deve ser no mínimo ' + str(data_btc.month) + '/' + str(data_btc.year) + '.')

        else:

            is_open = False
            danger = None

    else:
        is_open = False
        danger = None

      
    return is_open, danger

  




# selected_stocks_data
@callback(
    [
    Output ('selected_stocks_data', 'data'),
    Output ("danger_dropdown_codigos_ativos_zerado", "is_open"),
    Output ("danger_dropdown_codigos_ativos", "is_open"),
    Output('graph', 'figure'),
    Output ("danger_data_inicial_1", "is_open"),
    Output ('danger_data_inicial_1', 'children'),
    Output ("danger_data_final_1", "is_open"),
    Output ("danger_data_final_2", "is_open"),
    Output ("danger_data_inicial_fora", "is_open"),
    Output ("danger_data_inicial_fora", 'children'),
    Output ("dia_inicial", 'children'),
    Output ("dia_final", 'children'),
    ],
    [
    Input('dropdown_codigos_ativos', 'value'),
    Input('dropdown_mes_inicio', 'value'),
    Input('dropdown_ano_inicio', 'value'),
    Input('dropdown_mes_fim', 'value'),
    Input('dropdown_ano_fim', 'value'),
    ]
)

def selected_stocks_data (codigos_ativos, mes_inicio, ano_inicio, mes_fim, ano_fim):

    if len (codigos_ativos) > 0:

        codigos_ativos.sort()

        #print('!!!!!!!!!!!!!!!!!!!!!!!')
        grafico = go.Figure()


        mes_ano_inicio_selecionado = None

        mes_ano_inicio = ano_inicio + '-' + mes_inicio
        mes_ano_inicio = datetime.strptime(mes_ano_inicio, '%Y-%m')
        mes_ano_inicio = trunc_datetime(mes_ano_inicio)

        mes_ano_fim = ano_fim + '-' + mes_fim
        mes_ano_fim = datetime.strptime(mes_ano_fim, '%Y-%m')
        mes_ano_fim = trunc_datetime(mes_ano_fim)

        max_mes_ano_inicio =  today - relativedelta(months=1)
        max_mes_ano_inicio = trunc_datetime(max_mes_ano_inicio)

        mes_ano_inicio_str = str(mes_ano_inicio)
        mes_ano_inicio_str = mes_ano_inicio_str[:7]

        from  modulos.modulos_home.modulo_content_1 import last_month as lm1, year_ as y1
        ly1 = y1 -10 
        

        if int(mes_inicio) < lm1 and int(ano_inicio) == ly1 or int(ano_inicio) <= (ly1 -1):     
            is_open_1 = True
            danger1 = (html.I(className="bi bi-x-octagon-fill me-4", ), 'Mês/ano inicial não pode ser menor que ' + str(lm1) + '/' + str(ly1) + '.')
        else: 
            is_open_1 = False
            danger1 = None

        if mes_ano_fim <= mes_ano_inicio:
            is_open_2 = True
        else: 
            is_open_2 = False

        if mes_ano_fim > max_mes_ano_inicio:
            is_open_3 = True
        else: 
            is_open_3 = False


        try: 
            mes_ano_inicio_selecionado = amplitude_mes.loc[amplitude_mes['ano_mes_fim'].isin([mes_ano_inicio_str])].reset_index(drop=True)['amplitude_fim'][0]
            mes_ano_inicio_selecionado = str(mes_ano_inicio_selecionado)
            mes_ano_inicio_selecionado = datetime.strptime(mes_ano_inicio_selecionado, '%Y-%m-%d')
            mes_ano_fim_str = str(mes_ano_fim )
            mes_ano_fim_str  = mes_ano_fim_str [:7]      
            dia_inicial = str(mes_ano_inicio_selecionado.day)
        except:
            dia_inicial = ''
            mes_ano_inicio_selecionado = None

        try: 
            mes_ano_fim_selecionado = amplitude_mes.loc[amplitude_mes['ano_mes_fim'].isin([mes_ano_fim_str])].reset_index(drop=True)['amplitude_fim'][0]
            mes_ano_fim_selecionado = str(mes_ano_fim_selecionado)
            mes_ano_fim_selecionado = datetime.strptime(mes_ano_fim_selecionado, '%Y-%m-%d')
            dia_final = str(mes_ano_fim_selecionado.day)

            #print (dia_final)
        except:
            dia_final = ''
            mes_ano_fim_selecionado = None
            #print ('nao foi dia_final')
        
        if len (codigos_ativos) > 12:
            is_open_0 = True
        else:
            is_open_0 = False

        n = 0
        todos = pd.DataFrame([])

        for i in codigos_ativos:
            
            ativos_to_read =  codigos_ativos[0+n]
            hist_ativo = pd.read_csv('assets/dados/stocks/'+ ativos_to_read +'.csv')
            n = n+1

            hist_ativo['Date'] = pd.to_datetime(hist_ativo['Date'])
            hist_ativo.set_index('Date', inplace=True)
            hist_ativo = hist_ativo.rename(columns={'Adj Close': ativos_to_read})

            todos = pd.concat([todos, hist_ativo], axis=1)
            todos = todos.dropna(axis=0)


        data_inicial_todos = todos.first_valid_index()
            
        if mes_ano_inicio_selecionado < data_inicial_todos:
            is_open_4 = True
            danger4 = (html.I(className="bi bi-x-octagon-fill me-4", ), 'Um ou mais ativos selecionados não possuem histórico suficiente; mes/ano não pode ser menor que ' + str(data_inicial_todos.month) +'/' + str(data_inicial_todos.year) + '.')
           
        else: 
            is_open_4 = False
            danger4 = None          

        mes_ano_inicio_selecionado = str(mes_ano_inicio_selecionado)

        try:
            todos = todos [mes_ano_inicio_selecionado: mes_ano_fim_selecionado]
        except:
            todos = todos
            
        
        

        grafico = go.Figure()

        n = 0

        if len(codigos_ativos)<=12:
            for i in todos:
                col_name = i

                grafico.add_trace(go.Scatter(x=todos.index, y=todos[i],
                                    mode='lines', # 'lines' or 'markers'
                                    name=col_name,
                                    line_color = lista_cores_12[n]                            
                                    ))
                n = n +1
        else:
            pass  
        #grafico.update_layout(margin=dict(l=30, r=30, t=30, b=30),paper_bgcolor='rgba(0,0,0,0)' ) 

        

        grafico.update_layout(
        margin=dict(l=50, r=50, t=50, b=50),
        paper_bgcolor='rgba(0,0,0,0)', 
        title="PREÇO DE FECHAMENTO AJUSTADO (DIÁRIO):",
        xaxis={'title': 'DATA','fixedrange':True},
        yaxis={'title': 'VALOR (R$)','fixedrange':True},
        showlegend=True
        
    )

        grafico.update_yaxes(
            dict(tickformat=".2f")
        )
        grafico.update_xaxes(
        rangeslider_visible=False,
        tickformatstops = [

        dict(dtickrange=[None, None], value="%d/%m/%Y"),
    ]
    )
        
        todos = todos.to_json(orient ='index')
            
        return todos, False, is_open_0, grafico, is_open_1, danger1, is_open_2, is_open_3, is_open_4, danger4, dia_inicial, dia_final
    
    else:
        grafico = go.Figure()
        return None, True, None, grafico, None, None, None, None, None, None, None, None

# limitando_valor_investimento_inicial
@callback(
    
    Output("danger_investimento_inicial", "is_open"),
    Input("investimento_inicial","value"),
)

def limitando_valor_investimento_inicial (value):

    if value is not None:

        if 100 <= int(value) <= 1000000000:
            return False
        else:
            return True

    else:
        return True

# limitando_valor_aporte_mensal
@callback(
    
    Output("danger_aporte_mensal", "is_open"),
    [
    Input("valor_aporte_mensal","value"),
    Input("checklist_mensal","value"),
    ]
)

def limitando_valor_aporte_mensal (aporte, check_list):

    if aporte is not None:
  
        if 50 <= int(aporte) <= 1000000000 :
            return False

        else:
            if len (check_list) > 0:
                return True
            else: 
                return False
   
    else: 
        
        if len (check_list) > 0:
            return True
        else: 
            return False


#disable_personalisar_peso
@callback(
    Output("checklist_alocado", "value"),
    Input("dropdown_codigos_ativos","value"),
)

def disable_personalisar_peso (dropdown_codigos_ativos):

    if len (dropdown_codigos_ativos) <= 1:
        return []
    else:
        raise PreventUpdate


#opcao_callapse
@callback(

    [
    Output('collapse_checklist_dividendos_2', 'is_open'),
    Output('collapse_aporte_mensal', 'is_open'),
    ],

    [
    Input("checklist_dividendos", 'value'),
    Input("checklist_mensal","value")
    ]

)

def opcao_callapse(checklist_dividendos, checklist_mensal):

    collapse_checklist_dividendos_2 = False
    collapse_aporte_mensal = False

    if len(checklist_dividendos) > 0:
        collapse_checklist_dividendos_2  = True



    if len(checklist_mensal) > 0:
        collapse_aporte_mensal =  True

    else: 
        pass

    return collapse_checklist_dividendos_2, collapse_aporte_mensal

# exibir_grafico e tabela
@callback(
    [
    Output ("div_spinner_grafico", "style"),
    Output ("div_graph", "style"),
    Output ("div_spinner_tabela", "style"),
    Output ("div_table", "style"),
    Output("disable_rodar_2", 'data'),
    ],
    [
    Input ("danger_dropdown_codigos_ativos_zerado", "is_open"),
    Input ("danger_dropdown_codigos_ativos", "is_open"),
    Input ("danger_data_inicial_1", "is_open"),
    Input ("danger_data_final_1", "is_open"),
    Input ("danger_data_final_2", "is_open"),
    Input ("danger_data_inicial_fora", "is_open"),
    Input ("danger_btc", "is_open"),
    Input ("danger_investimento_inicial", "is_open"),
    Input ("danger_aporte_mensal", "is_open"),
    
    
    ]
)

def exibir_grafico(danger_1, danger_2, danger_3, danger_4, danger_5, danger_6, danger_7, danger_8, danger_9):

    if danger_1 ==  danger_2 == danger_3 ==  danger_4 == danger_5 ==  danger_6  == danger_7 == danger_8 == danger_9 == False:
        #prosseguir
        return {'display': 'none'}, {'display': 'block'},{'display': 'none'}, {'display': 'block'}, False

    else:
        #corrigir
        return {'display': 'block'}, {'display': 'none'}, {'display': 'block'}, {'display': 'none'}, True


# preenchendo_tabela
@callback(

    [

    Output ('c0', 'children'),
    Output ('c1', 'children'),
    Output ('c2', 'children'),
    Output ('c3', 'children'),
    Output ('c4', 'children'),
    Output ('c5', 'children'),
    Output ('c6', 'children'),
    Output ('c7', 'children'),
    Output ('c8', 'children'),
    Output ('c9', 'children'),
    Output ('c10', 'children'),
    Output ('c11', 'children'),

    Output ('a0', 'children'),
    Output ('a1', 'children'),
    Output ('a2', 'children'),
    Output ('a3', 'children'),
    Output ('a4', 'children'),
    Output ('a5', 'children'),
    Output ('a6', 'children'),
    Output ('a7', 'children'),
    Output ('a8', 'children'),
    Output ('a9', 'children'),
    Output ('a10', 'children'),
    Output ('a11', 'children'),

    Output ('s0', 'children'),
    Output ('s1', 'children'),
    Output ('s2', 'children'),
    Output ('s3', 'children'),
    Output ('s4', 'children'),
    Output ('s5', 'children'),
    Output ('s6', 'children'),
    Output ('s7', 'children'),
    Output ('s8', 'children'),
    Output ('s9', 'children'),
    Output ('s10', 'children'),
    Output ('s11', 'children'),

    Output ('row0', 'style'),
    Output ('row1', 'style'),
    Output ('row2', 'style'),
    Output ('row3', 'style'),
    Output ('row4', 'style'),
    Output ('row5', 'style'),
    Output ('row6', 'style'),
    Output ('row7', 'style'),
    Output ('row8', 'style'),
    Output ('row9', 'style'),
    Output ('row10', 'style'),
    Output ('row11', 'style'),
    Output('div_checklist_alocado', 'style')
    ],

    Input("dropdown_codigos_ativos", "value"),
    
    ) 

def preenchendo_tabela (value):

    if len(value) >0:

        value.sort()


    if 0 ==0:
        
        if len (value) == 0:
            return (
            
            None, None, None, None, None, None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None, None, None, None, None,
            {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'},
            {'display':'none'}
            )

        else: 
            
            
   
            try:
                a0 = ibov_tabela.loc[ibov_tabela['Código'] == value[0]].iloc[0]['Ação']
                s0 = ibov_tabela.loc[ibov_tabela['Código'] == value[0]].iloc[0]['Setor']
            except:
                pass
            try:
                a1 = ibov_tabela.loc[ibov_tabela['Código'] == value[1]].iloc[0]['Ação']
                s1 = ibov_tabela.loc[ibov_tabela['Código'] == value[1]].iloc[0]['Setor']
            except:
                pass
            try:
                a2 = ibov_tabela.loc[ibov_tabela['Código'] == value[2]].iloc[0]['Ação']
                s2 = ibov_tabela.loc[ibov_tabela['Código'] == value[2]].iloc[0]['Setor']
            except:
                pass
            try:
                a3 = ibov_tabela.loc[ibov_tabela['Código'] == value[3]].iloc[0]['Ação']
                s3 = ibov_tabela.loc[ibov_tabela['Código'] == value[3]].iloc[0]['Setor']
            except:
                pass
            try:
                a4 = ibov_tabela.loc[ibov_tabela['Código'] == value[4]].iloc[0]['Ação']
                s4 = ibov_tabela.loc[ibov_tabela['Código'] == value[4]].iloc[0]['Setor']
            except:
                pass
            try:
                a5 = ibov_tabela.loc[ibov_tabela['Código'] == value[5]].iloc[0]['Ação']
                s5 = ibov_tabela.loc[ibov_tabela['Código'] == value[5]].iloc[0]['Setor']
            except:
                pass
            try:
                a6 = ibov_tabela.loc[ibov_tabela['Código'] == value[6]].iloc[0]['Ação']
                s6 = ibov_tabela.loc[ibov_tabela['Código'] == value[6]].iloc[0]['Setor']
            except:
                pass
            try:
                a7 = ibov_tabela.loc[ibov_tabela['Código'] == value[7]].iloc[0]['Ação']
                s7 = ibov_tabela.loc[ibov_tabela['Código'] == value[7]].iloc[0]['Setor']
            except:
                pass
            try:
                a8 = ibov_tabela.loc[ibov_tabela['Código'] == value[8]].iloc[0]['Ação']
                s8 = ibov_tabela.loc[ibov_tabela['Código'] == value[8]].iloc[0]['Setor']
            except:
                pass
            try:
                a9 = ibov_tabela.loc[ibov_tabela['Código'] == value[9]].iloc[0]['Ação']
                s9 = ibov_tabela.loc[ibov_tabela['Código'] == value[9]].iloc[0]['Setor']
            except:
                pass
            try:
                a10 = ibov_tabela.loc[ibov_tabela['Código'] == value[10]].iloc[0]['Ação']
                s10 = ibov_tabela.loc[ibov_tabela['Código'] == value[10]].iloc[0]['Setor']
            except:
                pass
            try:
                a11 = ibov_tabela.loc[ibov_tabela['Código'] == value[11]].iloc[0]['Ação']
                s11 = ibov_tabela.loc[ibov_tabela['Código'] == value[11]].iloc[0]['Setor']
            except:
                pass

            if len (value) == 1:

                return (
                
                value[0], None, None, None, None, None, None, None, None, None, None, None,
                a0, None, None, None, None, None, None, None, None, None, None, None,
                s0, None, None, None, None, None, None, None, None, None, None, None,
                {'display': 'table-row'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'},
                {'display':'none'}
                )
            
            if len (value) == 2:
                return (
                
                value[0], value[1], None, None, None, None, None, None, None, None, None, None,
                a0, a1, None, None, None, None, None, None, None, None, None, None,
                s0, s1, None, None, None, None, None, None, None, None, None, None,
                {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'},
                {'display':'block'}
                )

            if len (value) == 3:
                    
                return (
                
                value[0], value[1], value[2], None, None, None, None, None, None, None, None, None,
                a0, a1, a2, None, None, None, None, None, None, None, None, None,
                s0, s1, s2, None, None, None, None, None, None, None, None, None,
                {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'},
                {'display':'block'}
                )

            if len (value) == 4:
                    
                return (
                
                value[0], value[1], value[2], value[3], None, None, None, None, None, None, None, None,
                a0, a1, a2, a3, None, None, None, None, None, None, None, None,
                s0, s1, s2, s3, None, None, None, None, None, None, None, None,
                {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'},
                {'display':'block'}
                )

            if len (value) == 5:
                    
                return (
                
                value[0], value[1], value[2], value[3], value[4], None, None, None, None, None, None, None,
                a0, a1, a2, a3, a4, None, None, None, None, None, None, None,
                s0, s1, s2, s3, s4, None, None, None, None, None, None, None,
                {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'},
                {'display':'block'}
                )

            if len (value) == 6:
                    
                return (
                
                value[0], value[1], value[2], value[3], value[4], value[5], None, None, None, None, None, None,
                a0, a1, a2, a3, a4, a5, None, None, None, None, None, None,
                s0, s1, s2, s3, s4, s5, None, None, None, None, None, None,
                {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'},
                {'display':'block'}
                )

            if len (value) == 7:
                    
                return (
                
                value[0], value[1], value[2], value[3], value[4], value[5], value[6], None, None, None, None, None,
                a0, a1, a2, a3, a4, a5, a6, None, None, None, None, None,
                s0, s1, s2, s3, s4, s5, s6, None, None, None, None, None,
                {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'},
                {'display':'block'}
                )

            if len (value) == 8:
                    
                return (
                
                value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], None, None, None, None,
                a0, a1, a2, a3, a4, a5, a6, a7, None, None, None, None,
                s0, s1, s2, s3, s4, s5, s6, s7, None, None, None, None,
                {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'},
                {'display':'block'}
                )

            if len (value) == 9:
                    
                return (
                
                value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8], None, None, None,
                a0, a1, a2, a3, a4, a5, a6, a7, a8, None, None, None,
                s0, s1, s2, s3, s4, s5, s6, s7, s8, None, None, None,
                {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'},
                {'display':'block'}
                )

            if len (value) == 10:
                    
                return (
                
                value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8], value[9], None, None,
                a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, None, None,
                s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, None, None,
                {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'none'}, {'display': 'none'},
                {'display':'block'}
                )

            if len (value) == 11:
                    
                return (
                
                value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8], value[9], value[10], None,
                a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, None,
                s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, None,
                {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'none'},
                {'display':'block'}
                )

            if len (value) == 12:
                    
                return ( 
                
                value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8], value[9], value[10], value[11],
                a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11,
                s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11,
                {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'}, {'display': 'table-row'},
                {'display':'block'}
                )

            if len (value) > 12:
                
                raise PreventUpdate

# soma
@callback(

    [
    Output('soma', 'children'),
    Output('soma', 'className'),

    ],
    [
    Input ("checklist_alocado", "value"),

    Input('p0', 'value'),
    Input('p1', 'value'),
    Input('p2', 'value'),
    Input('p3', 'value'),
    Input('p4', 'value'),
    Input('p5', 'value'),
    Input('p6', 'value'),
    Input('p7', 'value'),
    Input('p8', 'value'),
    Input('p9', 'value'),
    Input('p10', 'value'),
    Input('p11', 'value'),

    Input('pb0', 'value'),
    Input('pb1', 'value'),
    Input('pb2', 'value'),
    Input('pb3', 'value'),
    Input('pb4', 'value'),
    Input('pb5', 'value'),
    Input('pb6', 'value'),
    Input('pb7', 'value'),
    Input('pb8', 'value'),
    Input('pb9', 'value'),
    Input('pb10', 'value'),
    Input('pb11', 'value'),

    Input("dropdown_codigos_ativos", "value"),
    
    ]
    ) 

def soma (checklist_alocado, value0, value1,value2, value3, value4,value5, value6, value7, value8, value9, value10, value11, value0b, value1b,value2b, value3b, value4b,value5b, value6b, value7b, value8b, value9b, value10b, value11b, value):

    somatorio = [0]
    classe = None

    if len (value) == 0:
        return ('Total: 0 %', None,
        )

    else:

        if len(checklist_alocado)> 0:

            if value0b and value1b and value2b and value3b and value4b and value5b and value6b and value7b and value8b and value9b and value10b and value11b is not None:
    
                if len (value) == 1:
                    somatorio = round(float(value0b),2)
                    
                elif len (value) == 2:     
                    somatorio = round(float(value0b) + float(value1b),2)
        
                elif len (value) == 3:
                    somatorio = round(float(value0b) + float(value1b) + float(value2b),2)
    
                elif len (value) == 4:      
                    somatorio = round(float(value0b) + float(value1b) + float(value2b) + float(value3b),2)

                elif len (value) == 5:                
                    somatorio = round(float(value0b) + float(value1b) + float(value2b) + float(value3b) + float(value4b),2)

                elif len (value) == 6:            
                    somatorio = round(float(value0b) + float(value1b) + float(value2b) + float(value3b) + float(value4b) + float(value5b),2)

                elif len (value) == 7:             
                    somatorio = round(float(value0b) + float(value1b) + float(value2b) + float(value3b) + float(value4b) + float(value5b) + float(value6b),2)

                elif len (value) == 8:               
                    somatorio = round(float(value0b) + float(value1b) + float(value2b) + float(value3b) + float(value4b) + float(value5b) + float(value6b) + float(value7b),2)

                elif len (value) == 9:              
                    somatorio = round(float(value0b) + float(value1b) + float(value2b) + float(value3b) + float(value4b) + float(value5b) + float(value6b) + float(value7b) + float(value8b),2)

                elif len (value) == 10:                   
                    somatorio = round(float(value0b) + float(value1b) + float(value2b) + float(value3b) + float(value4b) + float(value5b) + float(value6b) + float(value7b) + float(value8b) + float(value9b),2)

                elif len (value) == 11:                
                    somatorio = round(float(value0b) + float(value1b) + float(value2b) + float(value3b) + float(value4b) + float(value5b) + float(value6b) + float(value7b) + float(value8b) + float(value9b) + float(value10b),2)

                elif len (value) == 12:                    
                    somatorio = round(float(value0b) + float(value1b) + float(value2b) + float(value3b) + float(value4b) + float(value5b) + float(value6b) + float(value7b) + float(value8b) + float(value9b) + float(value10b) + float(value11b),2)

                elif len (value) > 12:             
                    raise PreventUpdate

                if somatorio == 100:
                    classe = 'text-success'
                
                elif somatorio < 100:
                    classe = 'text-danger'

                elif somatorio > 100:
                    classe = 'text-danger'
                
                somatorio = "Total: " + str(somatorio) + ' %'

                return (somatorio, classe,
                )
            else:

                raise PreventUpdate
        
        else: 
        

            if value0 and value1 and value2 and value3 and value4 and value5 and value6 and value7 and value8 and value9 and value10 and value11 is not None:
    
                if len (value) == 1:
                    somatorio = round(float(value0),2)
                    
                elif len (value) == 2:     
                    somatorio = round(float(value0) + float(value1),2)
        
                elif len (value) == 3:
                    somatorio = round(float(value0) + float(value1) + float(value2),2)
    
                elif len (value) == 4:      
                    somatorio = round(float(value0) + float(value1) + float(value2) + float(value3),2)

                elif len (value) == 5:                
                    somatorio = round(float(value0) + float(value1) + float(value2) + float(value3) + float(value4),2)

                elif len (value) == 6:            
                    somatorio = round(float(value0) + float(value1) + float(value2) + float(value3) + float(value4) + float(value5),2)

                elif len (value) == 7:             
                    somatorio = round(float(value0) + float(value1) + float(value2) + float(value3) + float(value4) + float(value5) + float(value6),2)

                elif len (value) == 8:               
                    somatorio = round(float(value0) + float(value1) + float(value2) + float(value3) + float(value4) + float(value5) + float(value6) + float(value7),2)

                elif len (value) == 9:              
                    somatorio = round(float(value0) + float(value1) + float(value2) + float(value3) + float(value4) + float(value5) + float(value6) + float(value7) + float(value8),2)

                elif len (value) == 10:                   
                    somatorio = round(float(value0) + float(value1) + float(value2) + float(value3) + float(value4) + float(value5) + float(value6) + float(value7) + float(value8) + float(value9),2)

                elif len (value) == 11:                
                    somatorio = round(float(value0) + float(value1) + float(value2) + float(value3) + float(value4) + float(value5) + float(value6) + float(value7) + float(value8) + float(value9) + float(value10),2)

                elif len (value) == 12:                    
                    somatorio = round(float(value0) + float(value1) + float(value2) + float(value3) + float(value4) + float(value5) + float(value6) + float(value7) + float(value8) + float(value9) + float(value10) + float(value11),2)

                elif len (value) > 12:             
                    raise PreventUpdate

                if somatorio == 100:
                    classe = 'text-success'
                
                elif somatorio < 100:
                    classe = 'text-danger'

                elif somatorio > 100:
                    classe = 'text-danger'
                
                somatorio = "Total: " + str(somatorio) + ' %'

                return (somatorio, classe,
                )
            else:

                raise PreventUpdate

@callback(

    [
    Output('p0', 'value'),
    Output('p1', 'value'),
    Output('p2', 'value'),
    Output('p3', 'value'),
    Output('p4', 'value'),
    Output('p5', 'value'),
    Output('p6', 'value'),
    Output('p7', 'value'),
    Output('p8', 'value'),
    Output('p9', 'value'),
    Output('p10', 'value'),
    Output('p11', 'value'),

    Output('p0', 'style'),
    Output('p1', 'style'),
    Output('p2', 'style'),
    Output('p3', 'style'),
    Output('p4', 'style'),
    Output('p5', 'style'),
    Output('p6', 'style'),
    Output('p7', 'style'),
    Output('p8', 'style'),
    Output('p9', 'style'),
    Output('p10', 'style'),
    Output('p11', 'style'),

    Output('pb0', 'style'),
    Output('pb1', 'style'),
    Output('pb2', 'style'),
    Output('pb3', 'style'),
    Output('pb4', 'style'),
    Output('pb5', 'style'),
    Output('pb6', 'style'),
    Output('pb7', 'style'),
    Output('pb8', 'style'),
    Output('pb9', 'style'),
    Output('pb10', 'style'),
    Output('pb11', 'style'),


    ],

    [
    Input ("checklist_alocado", "value"),
    Input("dropdown_codigos_ativos", "value"),  
    ]

)

def open_porcentagem (value, len_ativos):

    vis = {'display':'block'}
    inv = {'display':'none'}
    if len (value) > 0:

        if len(len_ativos) == 0:
            raise PreventUpdate

        if len(len_ativos) == 1:
            return (
            '100', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            #True, True, True, True, True, True, True, True, True, True, True, True,
            inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv,
            vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis
            )

        if len(len_ativos) == 2:   
            return (
            '50', '50', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            #False, False, True, True, True, True, True, True, True, True, True, True,
            inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv,
            vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis
            )

        if len(len_ativos) == 3:  
            return (
            '33.34', '33.33', '33.33', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            #False, False, False, True, True, True, True, True, True, True, True, True,
            inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv,
            vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis
            )
        if len(len_ativos) == 4:    
            return (
            '25', '25', '25', '25', '0', '0', '0', '0', '0', '0', '0', '0',
            #False, False, False, False, True, True, True, True, True, True, True, True,
            inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv,
            vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis
            )
        if len(len_ativos) == 5:    
            return (
            '20', '20', '20', '20', '20', '0', '0', '0', '0', '0', '0', '0',
            #False, False, False, False, False, True, True, True, True, True, True, True,
            inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv,
            vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis
            )
        
        if len(len_ativos) == 6:   
            return (
            '16.67', '16.67', '16.67', '16.67', '16.66', '16.66', '0', '0', '0', '0', '0', '0',
            #False, False, False, False, False, False, True, True, True, True, True, True,
            inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv,
            vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis
            )
        
        if len(len_ativos) == 7: 
            return (
            '14.29', '14.29', '14.29', '14.29', '14.28', '14.28', '14.28', '0', '0', '0', '0', '0',
            #False, False, False, False, False, False, False, True, True, True, True, True,
            inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv,
            vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis
            )
        if len(len_ativos) == 8:  
            return (
            '12.5', '12.5', '12.5', '12.5', '12.5', '12.5', '12.5', '12.5', '0', '0', '0', '0',
            #False, False, False, False, False, False, False, False, True, True, True, True,
            inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv,
            vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis
            )
        if len(len_ativos) == 9:
            return (
            '11.12', '11.11', '11.11', '11.11', '11.11', '11.11', '11.11', '11.11', '11.11', '0', '0', '0',
            #False, False, False, False, False, False, False, False, False, True, True, True,
            inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv,
            vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis
            )
        
        if len(len_ativos) == 10:     
            return (
            '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '0', '0',
            #False, False, False, False, False, False, False, False, False, False, True, True,
            inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv,
            vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis
            )
        
        if len(len_ativos) == 11:    
            return (
            '9.1', '9.09', '9.09', '9.09', '9.09', '9.09', '9.09', '9.09', '9.09', '9.09', '9.09', '0',
            #False, False, False, False, False, False, False, False, False, False, False, True,
            inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv,
            vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis
            )

        if len(len_ativos) == 12:     
            return (
            '8.34', '8.34', '8.34', '8.34', '8.33', '8.33', '8.33', '8.33', '8.33', '8.33', '8.33', '8.33',
            #False, False, False, False, False, False, False, False, False, False, False, False,
            inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv,
            vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis
            )
        if len(len_ativos) > 12:
            return (
            '8.34', '8.34', '8.34', '8.34', '8.33', '8.33', '8.33', '8.33', '8.33', '8.33', '8.33', '8.33',
            #False, False, False, False, False, False, False, False, False, False, False, False,
            inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv,
            vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis
            )
    
    else:

        #print('else')

        if len(len_ativos) == 0:
            raise PreventUpdate

        if len(len_ativos) == 1:
            return (
            '100', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            #True, True, True, True, True, True, True, True, True, True, True, True,
            vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis,
            inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv
            )

        if len(len_ativos) == 2:
            return (
            '50', '50', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            #True, True, True, True, True, True, True, True, True, True, True, True,
            vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis,
            inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv
            )

        if len(len_ativos) == 3:  
            return (
            '33.34', '33.33', '33.33', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            #True, True, True, True, True, True, True, True, True, True, True, True,
            vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis,
            inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv
            )

        if len(len_ativos) == 4:   
            return (
            '25', '25', '25', '25', '0', '0', '0', '0', '0', '0', '0', '0',
            #True, True, True, True, True, True, True, True, True, True, True, True,
            vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis,
            inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv
            )

        if len(len_ativos) == 5:   
            return (
            '20', '20', '20', '20', '20', '0', '0', '0', '0', '0', '0', '0',
            #True, True, True, True, True, True, True, True, True, True, True, True,
            vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis,
            inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv
            )
        
        if len(len_ativos) == 6:   
            return (
            '16.67', '16.67', '16.67', '16.67', '16.66', '16.66', '0', '0', '0', '0', '0', '0',
            #True, True, True, True, True, True, True, True, True, True, True, True,
            vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis,
            inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv
            )
        
        if len(len_ativos) == 7:  
            return (
            '14.29', '14.29', '14.29', '14.29', '14.28', '14.28', '14.28', '0', '0', '0', '0', '0',
            #True, True, True, True, True, True, True, True, True, True, True, True,
            vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis,
            inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv
            )

        if len(len_ativos) == 8:  
            return (
            '12.5', '12.5', '12.5', '12.5', '12.5', '12.5', '12.5', '12.5', '0', '0', '0', '0',
            #True, True, True, True, True, True, True, True, True, True, True, True,
            vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis,
            inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv
            )

        if len(len_ativos) == 9:  
            return (
            '11.12', '11.11', '11.11', '11.11', '11.11', '11.11', '11.11', '11.11', '11.11', '0', '0', '0',
            #True, True, True, True, True, True, True, True, True, True, True, True,
            vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis,
            inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv
            )
        
        if len(len_ativos) == 10:  
            return (
            '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '0', '0',
            #True, True, True, True, True, True, True, True, True, True, True, True,
            vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis,
            inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv
            )
        
        
        if len(len_ativos) == 11:  
            return (
            '9.1', '9.09', '9.09', '9.09', '9.09', '9.09', '9.09', '9.09', '9.09', '9.09', '9.09', '0',
            #True, True, True, True, True, True, True, True, True, True, True, True,
            vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis,
            inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv
            )

        if len(len_ativos) == 12:  
            return (
            '8.34', '8.34', '8.34', '8.34', '8.33', '8.33', '8.33', '8.33', '8.33', '8.33', '8.33', '8.33',
            #True, True, True, True, True, True, True, True, True, True, True, True,
            vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis,
            inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv
            )
        
        if len(len_ativos) > 12:
            return (
            '8.34', '8.34', '8.34', '8.34', '8.33', '8.33', '8.33', '8.33', '8.33', '8.33', '8.33', '8.33',
            #True, True, True, True, True, True, True, True, True, True, True, True,
            vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis, vis,
            inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv
            )

@callback(

    [
    Output ("div_spinner_grafico2", "style"),
    Output ("div_graph2", "style"),
    Output ("div_spinner_grafico3", "style"),
    Output ("div_graph3", "style"),
    Output("disable_rodar_3", 'data'),
    ],
    [
    Input('soma', 'children'),
    Input ("danger_dropdown_codigos_ativos_zerado", "is_open"),
    Input ("danger_dropdown_codigos_ativos", "is_open"),
    Input ("danger_data_inicial_1", "is_open"),
    Input ("danger_data_final_1", "is_open"),
    Input ("danger_data_final_2", "is_open"),
    Input ("danger_data_inicial_fora", "is_open"),
    Input ("danger_btc", "is_open"),
    Input ("danger_investimento_inicial", "is_open"),
    Input ("danger_aporte_mensal", "is_open"),
    ]
    
)    

def exibir_outros_graficos(soma,danger_1, danger_2, danger_3, danger_4, danger_5, danger_6, danger_7, danger_8, danger_9):

    if soma is not None:
        soma = float(soma.translate({ord(i): None for i in 'Total:%'}))
        
        if soma == 100 and danger_1 == danger_2 == danger_3 == danger_4 == danger_5 == danger_6 == danger_7 == danger_8 == danger_9  == False:
            #prosseguir
            return {'display': 'none'}, {'display': 'block'},{'display': 'none'}, {'display': 'block'}, False
            
        else:
            #corrigir
            return {'display': 'block'}, {'display': 'none'}, {'display': 'block'}, {'display': 'none'}, True

    #else:
        #raise PreventUpdate

#grafico_setor
@callback(
    Output('graph_setor', 'figure'),
    [
    Input('dropdown_codigos_ativos', 'value'),
    Input ("checklist_alocado", "value"),
    
    Input ('p0', 'value'),
    Input ('p1', 'value'),
    Input ('p2', 'value'),
    Input ('p3', 'value'),
    Input ('p4', 'value'),
    Input ('p5', 'value'),
    Input ('p6', 'value'),
    Input ('p7', 'value'),
    Input ('p8', 'value'),
    Input ('p9', 'value'),
    Input ('p10', 'value'),
    Input ('p11', 'value'),

    Input ('pb0', 'value'),
    Input ('pb1', 'value'),
    Input ('pb2', 'value'),
    Input ('pb3', 'value'),
    Input ('pb4', 'value'),
    Input ('pb5', 'value'),
    Input ('pb6', 'value'),
    Input ('pb7', 'value'),
    Input ('pb8', 'value'),
    Input ('pb9', 'value'),
    Input ('pb10', 'value'),
    Input ('pb11', 'value'),


    Input ('s0', 'children'),
    Input ('s1', 'children'),
    Input ('s2', 'children'),
    Input ('s3', 'children'),
    Input ('s4', 'children'),
    Input ('s5', 'children'),
    Input ('s6', 'children'),
    Input ('s7', 'children'),
    Input ('s8', 'children'),
    Input ('s9', 'children'),
    Input ('s10', 'children'),
    Input ('s11', 'children'),
    ]

)

def grafico_setor(dropdown_codigos_ativos, checklist_alocado, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, pb0, pb1, pb2, pb3, pb4, pb5, pb6, pb7, pb8, pb9, pb10, pb11, s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11):

    if p0 and p1 and p2 and p3 and p4 and p5 and p6 and p7 and p8 and p9 and p10 and p11 and pb0 and pb1 and pb2 and pb3 and pb4 and pb5 and pb6 and pb7 and pb8 and pb9 and pb10 and pb11 is not None:

        df_setor=pd.DataFrame([])

        if len(checklist_alocado) > 0:

            pb0 = float(pb0)    
            pb1 = float(pb1)
            pb2 = float(pb2)
            pb3 = float(pb3)
            pb4 = float(pb4)
            pb5 = float(pb5)
            pb6 = float(pb6)
            pb7 = float(pb7)
            pb8 = float(pb8)
            pb9 = float(pb9)
            pb10 = float(pb10)
            pb11 = float(pb11)

            if len (dropdown_codigos_ativos) == 0:

                dict0 = [{'name':None,'value':0}]
                dict1 = [{'name':None,'value':0}]
                dict2 = [{'name':None,'value':0}]
                dict3 = [{'name':None,'value':0}]
                dict4 = [{'name':None,'value':0}]
                dict5 = [{'name':None,'value':0}]
                dict6 = [{'name':None,'value':0}]
                dict7 = [{'name':None,'value':0}]
                dict8 = [{'name':None,'value':0}]
                dict9 = [{'name':None,'value':0}]
                dict10 = [{'name':None,'value':0}]
                dict11 = [{'name':None,'value':0}]

            if len (dropdown_codigos_ativos) == 1:

                dict0 = [{'name':s0,'value':pb0}]
                dict1 = [{'name':None,'value':0}]
                dict2 = [{'name':None,'value':0}]
                dict3 = [{'name':None,'value':0}]
                dict4 = [{'name':None,'value':0}]
                dict5 = [{'name':None,'value':0}]
                dict6 = [{'name':None,'value':0}]
                dict7 = [{'name':None,'value':0}]
                dict8 = [{'name':None,'value':0}]
                dict9 = [{'name':None,'value':0}]
                dict10 = [{'name':None,'value':0}]
                dict11 = [{'name':None,'value':0}]
    
            if len (dropdown_codigos_ativos) == 2:
                dict0 = [{'name':s0,'value':pb0}]
                dict1 = [{'name':s1,'value':pb1}]
                dict2 = [{'name':None,'value':0}]
                dict3 = [{'name':None,'value':0}]
                dict4 = [{'name':None,'value':0}]
                dict5 = [{'name':None,'value':0}]
                dict6 = [{'name':None,'value':0}]
                dict7 = [{'name':None,'value':0}]
                dict8 = [{'name':None,'value':0}]
                dict9 = [{'name':None,'value':0}]
                dict10 = [{'name':None,'value':0}]
                dict11 = [{'name':None,'value':0}]

            if len (dropdown_codigos_ativos) == 3:

                dict0 = [{'name':s0,'value':pb0}]
                dict1 = [{'name':s1,'value':pb1}]
                dict2 = [{'name':s2,'value':pb2}]
                dict3 = [{'name':None,'value':0}]
                dict4 = [{'name':None,'value':0}]
                dict5 = [{'name':None,'value':0}]
                dict6 = [{'name':None,'value':0}]
                dict7 = [{'name':None,'value':0}]
                dict8 = [{'name':None,'value':0}]
                dict9 = [{'name':None,'value':0}]
                dict10 = [{'name':None,'value':0}]
                dict11 = [{'name':None,'value':0}]

            if len (dropdown_codigos_ativos) == 4:

                dict0 = [{'name':s0,'value':pb0}]
                dict1 = [{'name':s1,'value':pb1}]
                dict2 = [{'name':s2,'value':pb2}]
                dict3 = [{'name':s3,'value':pb3}]
                dict4 = [{'name':None,'value':0}]
                dict5 = [{'name':None,'value':0}]
                dict6 = [{'name':None,'value':0}]
                dict7 = [{'name':None,'value':0}]
                dict8 = [{'name':None,'value':0}]
                dict9 = [{'name':None,'value':0}]
                dict10 = [{'name':None,'value':0}]
                dict11 = [{'name':None,'value':0}]

            if len (dropdown_codigos_ativos) == 5:

                dict0 = [{'name':s0,'value':pb0}]
                dict1 = [{'name':s1,'value':pb1}]
                dict2 = [{'name':s2,'value':pb2}]
                dict3 = [{'name':s3,'value':pb3}]
                dict4 = [{'name':s4,'value':pb4}]
                dict5 = [{'name':None,'value':0}]
                dict6 = [{'name':None,'value':0}]
                dict7 = [{'name':None,'value':0}]
                dict8 = [{'name':None,'value':0}]
                dict9 = [{'name':None,'value':0}]
                dict10 = [{'name':None,'value':0}]
                dict11 = [{'name':None,'value':0}]

            if len (dropdown_codigos_ativos) == 6:

                dict0 = [{'name':s0,'value':pb0}]
                dict1 = [{'name':s1,'value':pb1}]
                dict2 = [{'name':s2,'value':pb2}]
                dict3 = [{'name':s3,'value':pb3}]
                dict4 = [{'name':s4,'value':pb4}]
                dict5 = [{'name':s5,'value':pb5}]
                dict6 = [{'name':None,'value':0}]
                dict7 = [{'name':None,'value':0}]
                dict8 = [{'name':None,'value':0}]
                dict9 = [{'name':None,'value':0}]
                dict10 = [{'name':None,'value':0}]
                dict11 = [{'name':None,'value':0}]

            if len (dropdown_codigos_ativos) == 7:

                dict0 = [{'name':s0,'value':pb0}]
                dict1 = [{'name':s1,'value':pb1}]
                dict2 = [{'name':s2,'value':pb2}]
                dict3 = [{'name':s3,'value':pb3}]
                dict4 = [{'name':s4,'value':pb4}]
                dict5 = [{'name':s5,'value':pb5}]
                dict6 = [{'name':s6,'value':pb6}]
                dict7 = [{'name':None,'value':0}]
                dict8 = [{'name':None,'value':0}]
                dict9 = [{'name':None,'value':0}]
                dict10 = [{'name':None,'value':0}]
                dict11 = [{'name':None,'value':0}]

            if len (dropdown_codigos_ativos) == 8:

                dict0 = [{'name':s0,'value':pb0}]
                dict1 = [{'name':s1,'value':pb1}]
                dict2 = [{'name':s2,'value':pb2}]
                dict3 = [{'name':s3,'value':pb3}]
                dict4 = [{'name':s4,'value':pb4}]
                dict5 = [{'name':s5,'value':pb5}]
                dict6 = [{'name':s6,'value':pb6}]
                dict7 = [{'name':s7,'value':pb7}]
                dict8 = [{'name':None,'value':0}]
                dict9 = [{'name':None,'value':0}]
                dict10 = [{'name':None,'value':0}]
                dict11 = [{'name':None,'value':0}]

            if len (dropdown_codigos_ativos) == 9:

                dict0 = [{'name':s0,'value':pb0}]
                dict1 = [{'name':s1,'value':pb1}]
                dict2 = [{'name':s2,'value':pb2}]
                dict3 = [{'name':s3,'value':pb3}]
                dict4 = [{'name':s4,'value':pb4}]
                dict5 = [{'name':s5,'value':pb5}]
                dict6 = [{'name':s6,'value':pb6}]
                dict7 = [{'name':s7,'value':pb7}]
                dict8 = [{'name':s8,'value':pb8}]
                dict9 = [{'name':None,'value':0}]
                dict10 = [{'name':None,'value':0}]
                dict11 = [{'name':None,'value':0}]


            if len (dropdown_codigos_ativos) == 10:

                dict0 = [{'name':s0,'value':pb0}]
                dict1 = [{'name':s1,'value':pb1}]
                dict2 = [{'name':s2,'value':pb2}]
                dict3 = [{'name':s3,'value':pb3}]
                dict4 = [{'name':s4,'value':pb4}]
                dict5 = [{'name':s5,'value':pb5}]
                dict6 = [{'name':s6,'value':pb6}]
                dict7 = [{'name':s7,'value':pb7}]
                dict8 = [{'name':s8,'value':pb8}]
                dict9 = [{'name':s9,'value':pb9}]
                dict10 = [{'name':None,'value':0}]
                dict11 = [{'name':None,'value':0}]

            if len (dropdown_codigos_ativos) == 11:

                dict0 = [{'name':s0,'value':pb0}]
                dict1 = [{'name':s1,'value':pb1}]
                dict2 = [{'name':s2,'value':pb2}]
                dict3 = [{'name':s3,'value':pb3}]
                dict4 = [{'name':s4,'value':pb4}]
                dict5 = [{'name':s5,'value':pb5}]
                dict6 = [{'name':s6,'value':pb6}]
                dict7 = [{'name':s7,'value':pb7}]
                dict8 = [{'name':s8,'value':pb8}]
                dict9 = [{'name':s9,'value':pb9}]
                dict10 = [{'name':s10,'value':pb10}]
                dict11 = [{'name':None,'value':0}]

            if len (dropdown_codigos_ativos) >= 12:

                dict0 = [{'name':s0,'value':pb0}]
                dict1 = [{'name':s1,'value':pb1}]
                dict2 = [{'name':s2,'value':pb2}]
                dict3 = [{'name':s3,'value':pb3}]
                dict4 = [{'name':s4,'value':pb4}]
                dict5 = [{'name':s5,'value':pb5}]
                dict6 = [{'name':s6,'value':pb6}]
                dict7 = [{'name':s7,'value':pb7}]
                dict8 = [{'name':s8,'value':pb8}]
                dict9 = [{'name':s9,'value':pb9}]
                dict10 = [{'name':s10,'value':pb10}]
                dict11 = [{'name':s11,'value':pb11}]

        else:

            p0 = float(p0)
            p1 = float(p1)
            p2 = float(p2)
            p3 = float(p3)
            p4 = float(p4)
            p5 = float(p5)
            p6 = float(p6)
            p7 = float(p7)
            p8 = float(p8)
            p9 = float(p9)
            p10 = float(p10)
            p11 = float(p11)

            dict0 = [{'name':s0,'value':p0}]
            dict1 = [{'name':s1,'value':p1}]
            dict2 = [{'name':s2,'value':p2}]
            dict3 = [{'name':s3,'value':p3}]
            dict4 = [{'name':s4,'value':p4}]
            dict5 = [{'name':s5,'value':p5}]
            dict6 = [{'name':s6,'value':p6}]
            dict7 = [{'name':s7,'value':p7}]
            dict8 = [{'name':s8,'value':p8}]
            dict9 = [{'name':s9,'value':p9}]
            dict10 = [{'name':s10,'value':p10}]
            dict11 = [{'name':s11,'value':p11}]
        
        names = set([k['name'] for k in dict0+dict1+dict2+dict3+dict4+dict5+dict6+dict7+dict8+dict9+dict10+dict11])
        dc = []
        for name in names:
            temp_val = []
            for dict_ in dict0+dict1+dict2+dict3+dict4+dict5+dict6+dict7+dict8+dict9+dict10+dict11:
                if dict_['name'] == name:
                    temp_val.append(dict_['value'])
            dc.append({'name': name, 'value' : sum(temp_val)})

        df_setor=pd.DataFrame(dc)
        df_setor = df_setor[df_setor.value != 0.0]

        df_setor['colors'] = lista_cores_12[0:len(df_setor)]

        df_setor = df_setor.sort_values('name').reset_index(drop=True)

        #print('df_setor')
        #print(df_setor)

        grafico = go.Figure(data=[go.Pie(labels=df_setor.name, values=df_setor.value, hoverinfo="label+percent", hole=.3 )], layout_showlegend=True,)
        grafico.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=50, r=50, t=50, b=50),
                              title="PERCENTUAL ALOCADO POR SETOR ECONÔMICO:",
                              )

        grafico.update_traces(
                  marker=dict(colors=df_setor['colors'], ))

        #print('3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333')
        #print(df_setor)
    
        return grafico 
    
    else: 
        raise PreventUpdate

#grafico_acao
@callback(
    Output('graph_acoes', 'figure'),
    [
    Input('dropdown_codigos_ativos', 'value'),
    Input ("checklist_alocado", "value"),
    
    Input ('p0', 'value'),
    Input ('p1', 'value'),
    Input ('p2', 'value'),
    Input ('p3', 'value'),
    Input ('p4', 'value'),
    Input ('p5', 'value'),
    Input ('p6', 'value'),
    Input ('p7', 'value'),
    Input ('p8', 'value'),
    Input ('p9', 'value'),
    Input ('p10', 'value'),
    Input ('p11', 'value'),

    Input ('pb0', 'value'),
    Input ('pb1', 'value'),
    Input ('pb2', 'value'),
    Input ('pb3', 'value'),
    Input ('pb4', 'value'),
    Input ('pb5', 'value'),
    Input ('pb6', 'value'),
    Input ('pb7', 'value'),
    Input ('pb8', 'value'),
    Input ('pb9', 'value'),
    Input ('pb10', 'value'),
    Input ('pb11', 'value'),

    Input ('c0', 'children'),
    Input ('c1', 'children'),
    Input ('c2', 'children'),
    Input ('c3', 'children'),
    Input ('c4', 'children'),
    Input ('c5', 'children'),
    Input ('c6', 'children'),
    Input ('c7', 'children'),
    Input ('c8', 'children'),
    Input ('c9', 'children'),
    Input ('c10', 'children'),
    Input ('c11', 'children'),
    ]

)


def grafico_acao(dropdown_codigos_ativos, checklist_alocado, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, pb0, pb1, pb2, pb3, pb4, pb5, pb6, pb7, pb8, pb9, pb10, pb11, c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11):

    if p0 and p1 and p2 and p3 and p4 and p5 and p6 and p7 and p8 and p9 and p10 and p11 and pb0 and pb1 and pb2 and pb3 and pb4 and pb5 and pb6 and pb7 and pb8 and pb9 and pb10 and pb11 is not None:

        df_acao=pd.DataFrame([])
        
        if len(checklist_alocado) > 0:

            pb0 = float(pb0)    
            pb1 = float(pb1)
            pb2 = float(pb2)
            pb3 = float(pb3)
            pb4 = float(pb4)
            pb5 = float(pb5)
            pb6 = float(pb6)
            pb7 = float(pb7)
            pb8 = float(pb8)
            pb9 = float(pb9)
            pb10 = float(pb10)
            pb11 = float(pb11)


            if len (dropdown_codigos_ativos) == 0:

                dict0 = [{'name':None,'value':0}]
                dict1 = [{'name':None,'value':0}]
                dict2 = [{'name':None,'value':0}]
                dict3 = [{'name':None,'value':0}]
                dict4 = [{'name':None,'value':0}]
                dict5 = [{'name':None,'value':0}]
                dict6 = [{'name':None,'value':0}]
                dict7 = [{'name':None,'value':0}]
                dict8 = [{'name':None,'value':0}]
                dict9 = [{'name':None,'value':0}]
                dict10 = [{'name':None,'value':0}]
                dict11 = [{'name':None,'value':0}]

            if len (dropdown_codigos_ativos) == 1:

                dict0 = [{'name':c0,'value':pb0}]
                dict1 = [{'name':None,'value':0}]
                dict2 = [{'name':None,'value':0}]
                dict3 = [{'name':None,'value':0}]
                dict4 = [{'name':None,'value':0}]
                dict5 = [{'name':None,'value':0}]
                dict6 = [{'name':None,'value':0}]
                dict7 = [{'name':None,'value':0}]
                dict8 = [{'name':None,'value':0}]
                dict9 = [{'name':None,'value':0}]
                dict10 = [{'name':None,'value':0}]
                dict11 = [{'name':None,'value':0}]
    
            if len (dropdown_codigos_ativos) == 2:
                dict0 = [{'name':c0,'value':pb0}]
                dict1 = [{'name':c1,'value':pb1}]
                dict2 = [{'name':None,'value':0}]
                dict3 = [{'name':None,'value':0}]
                dict4 = [{'name':None,'value':0}]
                dict5 = [{'name':None,'value':0}]
                dict6 = [{'name':None,'value':0}]
                dict7 = [{'name':None,'value':0}]
                dict8 = [{'name':None,'value':0}]
                dict9 = [{'name':None,'value':0}]
                dict10 = [{'name':None,'value':0}]
                dict11 = [{'name':None,'value':0}]

            if len (dropdown_codigos_ativos) == 3:

                dict0 = [{'name':c0,'value':pb0}]
                dict1 = [{'name':c1,'value':pb1}]
                dict2 = [{'name':c2,'value':pb2}]
                dict3 = [{'name':None,'value':0}]
                dict4 = [{'name':None,'value':0}]
                dict5 = [{'name':None,'value':0}]
                dict6 = [{'name':None,'value':0}]
                dict7 = [{'name':None,'value':0}]
                dict8 = [{'name':None,'value':0}]
                dict9 = [{'name':None,'value':0}]
                dict10 = [{'name':None,'value':0}]
                dict11 = [{'name':None,'value':0}]

            if len (dropdown_codigos_ativos) == 4:

                dict0 = [{'name':c0,'value':pb0}]
                dict1 = [{'name':c1,'value':pb1}]
                dict2 = [{'name':c2,'value':pb2}]
                dict3 = [{'name':c3,'value':pb3}]
                dict4 = [{'name':None,'value':0}]
                dict5 = [{'name':None,'value':0}]
                dict6 = [{'name':None,'value':0}]
                dict7 = [{'name':None,'value':0}]
                dict8 = [{'name':None,'value':0}]
                dict9 = [{'name':None,'value':0}]
                dict10 = [{'name':None,'value':0}]
                dict11 = [{'name':None,'value':0}]

            if len (dropdown_codigos_ativos) == 5:

                dict0 = [{'name':c0,'value':pb0}]
                dict1 = [{'name':c1,'value':pb1}]
                dict2 = [{'name':c2,'value':pb2}]
                dict3 = [{'name':c3,'value':pb3}]
                dict4 = [{'name':c4,'value':pb4}]
                dict5 = [{'name':None,'value':0}]
                dict6 = [{'name':None,'value':0}]
                dict7 = [{'name':None,'value':0}]
                dict8 = [{'name':None,'value':0}]
                dict9 = [{'name':None,'value':0}]
                dict10 = [{'name':None,'value':0}]
                dict11 = [{'name':None,'value':0}]

            if len (dropdown_codigos_ativos) == 6:

                dict0 = [{'name':c0,'value':pb0}]
                dict1 = [{'name':c1,'value':pb1}]
                dict2 = [{'name':c2,'value':pb2}]
                dict3 = [{'name':c3,'value':pb3}]
                dict4 = [{'name':c4,'value':pb4}]
                dict5 = [{'name':c5,'value':pb5}]
                dict6 = [{'name':None,'value':0}]
                dict7 = [{'name':None,'value':0}]
                dict8 = [{'name':None,'value':0}]
                dict9 = [{'name':None,'value':0}]
                dict10 = [{'name':None,'value':0}]
                dict11 = [{'name':None,'value':0}]

            if len (dropdown_codigos_ativos) == 7:

                dict0 = [{'name':c0,'value':pb0}]
                dict1 = [{'name':c1,'value':pb1}]
                dict2 = [{'name':c2,'value':pb2}]
                dict3 = [{'name':c3,'value':pb3}]
                dict4 = [{'name':c4,'value':pb4}]
                dict5 = [{'name':c5,'value':pb5}]
                dict6 = [{'name':c6,'value':pb6}]
                dict7 = [{'name':None,'value':0}]
                dict8 = [{'name':None,'value':0}]
                dict9 = [{'name':None,'value':0}]
                dict10 = [{'name':None,'value':0}]
                dict11 = [{'name':None,'value':0}]

            if len (dropdown_codigos_ativos) == 8:

                dict0 = [{'name':c0,'value':pb0}]
                dict1 = [{'name':c1,'value':pb1}]
                dict2 = [{'name':c2,'value':pb2}]
                dict3 = [{'name':c3,'value':pb3}]
                dict4 = [{'name':c4,'value':pb4}]
                dict5 = [{'name':c5,'value':pb5}]
                dict6 = [{'name':c6,'value':pb6}]
                dict7 = [{'name':c7,'value':pb7}]
                dict8 = [{'name':None,'value':0}]
                dict9 = [{'name':None,'value':0}]
                dict10 = [{'name':None,'value':0}]
                dict11 = [{'name':None,'value':0}]

            if len (dropdown_codigos_ativos) == 9:

                dict0 = [{'name':c0,'value':pb0}]
                dict1 = [{'name':c1,'value':pb1}]
                dict2 = [{'name':c2,'value':pb2}]
                dict3 = [{'name':c3,'value':pb3}]
                dict4 = [{'name':c4,'value':pb4}]
                dict5 = [{'name':c5,'value':pb5}]
                dict6 = [{'name':c6,'value':pb6}]
                dict7 = [{'name':c7,'value':pb7}]
                dict8 = [{'name':c8,'value':pb8}]
                dict9 = [{'name':None,'value':0}]
                dict10 = [{'name':None,'value':0}]
                dict11 = [{'name':None,'value':0}]


            if len (dropdown_codigos_ativos) == 10:

                dict0 = [{'name':c0,'value':pb0}]
                dict1 = [{'name':c1,'value':pb1}]
                dict2 = [{'name':c2,'value':pb2}]
                dict3 = [{'name':c3,'value':pb3}]
                dict4 = [{'name':c4,'value':pb4}]
                dict5 = [{'name':c5,'value':pb5}]
                dict6 = [{'name':c6,'value':pb6}]
                dict7 = [{'name':c7,'value':pb7}]
                dict8 = [{'name':c8,'value':pb8}]
                dict9 = [{'name':c9,'value':pb9}]
                dict10 = [{'name':None,'value':0}]
                dict11 = [{'name':None,'value':0}]

            if len (dropdown_codigos_ativos) == 11:

                dict0 = [{'name':c0,'value':pb0}]
                dict1 = [{'name':c1,'value':pb1}]
                dict2 = [{'name':c2,'value':pb2}]
                dict3 = [{'name':c3,'value':pb3}]
                dict4 = [{'name':c4,'value':pb4}]
                dict5 = [{'name':c5,'value':pb5}]
                dict6 = [{'name':c6,'value':pb6}]
                dict7 = [{'name':c7,'value':pb7}]
                dict8 = [{'name':c8,'value':pb8}]
                dict9 = [{'name':c9,'value':pb9}]
                dict10 = [{'name':c10,'value':pb10}]
                dict11 = [{'name':None,'value':0}]

            if len (dropdown_codigos_ativos) >= 12:

                dict0 = [{'name':c0,'value':pb0}]
                dict1 = [{'name':c1,'value':pb1}]
                dict2 = [{'name':c2,'value':pb2}]
                dict3 = [{'name':c3,'value':pb3}]
                dict4 = [{'name':c4,'value':pb4}]
                dict5 = [{'name':c5,'value':pb5}]
                dict6 = [{'name':c6,'value':pb6}]
                dict7 = [{'name':c7,'value':pb7}]
                dict8 = [{'name':c8,'value':pb8}]
                dict9 = [{'name':c9,'value':pb9}]
                dict10 = [{'name':c10,'value':pb10}]
                dict11 = [{'name':c11,'value':pb11}]


        else:

            p0 = float(p0)
            p1 = float(p1)
            p2 = float(p2)
            p3 = float(p3)
            p4 = float(p4)
            p5 = float(p5)
            p6 = float(p6)
            p7 = float(p7)
            p8 = float(p8)
            p9 = float(p9)
            p10 = float(p10)
            p11 = float(p11)

            dict0 = [{'name':c0,'value':p0}]
            dict1 = [{'name':c1,'value':p1}]
            dict2 = [{'name':c2,'value':p2}]
            dict3 = [{'name':c3,'value':p3}]
            dict4 = [{'name':c4,'value':p4}]
            dict5 = [{'name':c5,'value':p5}]
            dict6 = [{'name':c6,'value':p6}]
            dict7 = [{'name':c7,'value':p7}]
            dict8 = [{'name':c8,'value':p8}]
            dict9 = [{'name':c9,'value':p9}]
            dict10 = [{'name':c10,'value':p10}]
            dict11 = [{'name':c11,'value':p11}]
        
        names = set([k['name'] for k in dict0+dict1+dict2+dict3+dict4+dict5+dict6+dict7+dict8+dict9+dict10+dict11])
        dc = []
        for name in names:
            temp_val = []
            for dict_ in dict0+dict1+dict2+dict3+dict4+dict5+dict6+dict7+dict8+dict9+dict10+dict11:
                if dict_['name'] == name:
                    temp_val.append(dict_['value'])
            dc.append({'name': name, 'value' : sum(temp_val)})

        df_acao=pd.DataFrame(dc)
        df_acao = df_acao[df_acao.value != 0.0]

        df_acao = df_acao.sort_values('name').reset_index(drop=True)
        
        df_acao['colors'] = lista_cores_12[0:len(df_acao)]

  
        

        #print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$(((((((((((((((((((()))))))))))))))))))))')

        #print(df_acao)

        grafico = go.Figure(data=[go.Pie(labels=df_acao.name, values=df_acao.value, hoverinfo="label+percent", hole=.3 ), ], layout_showlegend=True,)
        grafico.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=50, r=50, t=50, b=50),
                              title="PERCENTUAL ALOCADO POR AÇÃO:",
                              )
       
        grafico.update_traces(
                  marker=dict(colors=df_acao['colors']))
        #print('!!!!!!!!!ddsds!!!!!!!!!!!!!!')
        return grafico 
    
    else: 
        
        raise PreventUpdate


#################################################################
#CALLBACKS CADASTROS ############################################
#################################################################

# exibir botao certo
@callback(

    [
    Output("btn_ainda_nao_logou", "style"), # nao logado
    Output("btn_rodar", "style"), # logado e verificado
    Output("btn_ainda_nao_verificou_email", "style"), # logado mas não verificado
    
    ],

    [
    Input('dados_perfil', 'data'),
    Input('dados_email_verificado', 'data'),
    Input("url", "pathname"),
    ]

)

def exibir_botao_certo(dados_perfil, dados_email_verificado, url):

    
    if url == '/':

        print('dados_email_verificado', dados_email_verificado)
        # logado
        if dados_perfil[0] != 'Visitante':

            # verificado
            if dados_email_verificado == True or dados_perfil[2] == True:


                return {'display' : 'none'},  {'display' : 'inline', 'width':'260px'}, {'display' : 'none'}

       
            # nao verificado
            elif dados_email_verificado == False or dados_perfil[2] == False:

                return  {'display' : 'none'}, {'display' : 'none'}, {'display' : 'inline', 'width':'260px'}        
        #não logado
        else:

            return {'display' : 'inline', 'width':'260px'}, {'display' : 'none'}, {'display' : 'none'}

    else:

        raise PreventUpdate

#refresh_email_verificado
@callback(

    Output("dados_email_verificado", "data"),
    
    [
    Input('local', 'data'),
    Input("dados_perfil", "data"),
    ]

)

def refresh_email_verificado(data, dados_perfil):

    if data:

        if data ['clicks'] > 0:
            
            if dados_perfil[3] is not None and dados_perfil[2] is not True:

                RefreshToken = dados_perfil[3]
                Token = dados_perfil[4]
                refresh = refresh_email(RefreshToken, Token)

                print('verificação', refresh[2] )

                #return  refresh[2]
                return refresh[2]

            else: 
                print('verificação false')
                return False
        
        else: 
            raise PreventUpdate

     
    raise PreventUpdate

# exibir relatorio
@callback(

    Output("relatorio_graphs", "style"),

    Input('btn_rodar', 'n_clicks')

)

def exibir_relatorio(n_clicks):#(dados_perfil, dados_email_verificado, url):

    if n_clicks > 0:

        return {'display' : 'block'}

    else:

        return {'display' : 'none'}


# exibir validar email
@callback(

    Output("div_validacao", "style"),
    Input('btn_ainda_nao_verificou_email', 'n_clicks')

)

def exibir_validar_email(n_clicks):#(dados_perfil, dados_email_verificado, url):


    if n_clicks > 0:

        return {'display' : 'block'}

    else:

        return {'display' : 'none'}

# exibir um ou outro

@callback(

    [
    Output("container_valide_seu_email", "style"), 
    Output("container_logar_novamente", "style"), 
    
    ],

    [
    #Input ("btn_ainda_nao_verificou_email", 'n_clicks'),
    Input('local', 'modified_timestamp'),
    State('local', 'data'),

    ]
)

def on_data(ts, data):

    #div_validar_email_maior
    #div_logar_novamente_email_maior

    if data is not None:

        if data['clicks'] <=3:
        
            return {'display' : 'block'}, {'display' : 'none'}

        else:

            return {'display' : 'none'}, {'display' : 'block'}
    
    else:
        return {'display' : 'block'}, {'display' : 'none'}

    #else: 
    
 




#CALLBACKS RENDER PAGES END ################################################


# ativar_botao_redefinir
@callback(

    Output("botao_redefinir", "disabled"),
    Input("redeninir_email", "value"),
    
)

def ativar_botao_redefinir(redeninir_email):

    if redeninir_email != '':

        return False

    else:
        return True

#refefinir_senha_form


@callback(
    [
    Output("danger_refefinir_senha", "is_open"),
    Output("danger_refefinir_senha", "children"),
    Output("success_refefinir_senha", "is_open"),
    Output("success_refefinir_senha", "children"),
    Output('login_link', 'style')
    ],
    [
    Input ("botao_redefinir", "n_clicks"),
    Input ("redeninir_email", "value")
    ]
)

def refefinir_senha_form(botao_redefinir, redeninir_email):

    triggered_id = ctx.triggered_id

    email = str(redeninir_email)

    danger_refefinir_senha_children = None
    success_refefinir_senha_children = None
    login_link = {'display' : 'none'}

    if triggered_id == 'botao_redefinir':

        #print(email)

        email_no_formato_valido = validar_email(email)

        if email_no_formato_valido == True:

            redefinir = refefinir_senha(email)

            if redefinir[0] == True:

                success_refefinir_senha_children = html.I(className="bi bi-check-circle-fill me-4"),"E-mail de redefinição de senha enviado!"

                login_link = {'display' : 'block'}

                return False, danger_refefinir_senha_children, True, success_refefinir_senha_children, login_link

            else:

                if redefinir[1] == 'RESET_PASSWORD_EXCEED_LIMIT':
                    danger_refefinir_senha_children = html.I(className="bi bi-x-octagon-fill me-4", ),"Envio de e-mails de redefinição excedeu o limite."

                else:

                    danger_refefinir_senha_children = html.I(className="bi bi-x-octagon-fill me-4", ),"Erro no processamento, tente novamente mais tarde."

                return True,danger_refefinir_senha_children, False, success_refefinir_senha_children, login_link

        else:

            danger_refefinir_senha_children = html.I(className="bi bi-x-octagon-fill me-4", ),"E-mail inválido."
                
            return True,danger_refefinir_senha_children, False, success_refefinir_senha_children, login_link



    else:

        raise PreventUpdate

# ativar_botao_cadastrar
@callback(

    Output("btn_cadastrar", "disabled"),
    [
    Input("cadastro_nome", "value"),
    Input("cadastro_email", "value"),
    Input("cadastro_password_1", "value"),
    Input("cadastro_password_2", "value"),
    Input("checklist_termos", "value"),

    ]
)

def ativar_botao_cadastrar(username, email, password_1, password_2, checklist_termos):

    if len (checklist_termos) >0:
        checklist_termos = checklist_termos[-1]
    else:
        checklist_termos =0

    if username != '' and  email!= '' and password_1 != '' and  password_2 != '' and checklist_termos == 1:

        print(type(checklist_termos))
        return False

    else:
        return True


##### CADASTRO

@callback(
    
    [
    Output("dados_perfil_temp_1", "data"),
    Output("dados_path_temp_1", "data"),
    Output("danger_cadastro_invalido", "is_open"),
    Output("danger_cadastro_invalido", "children"),
    Output("danger_cadastro_email_invalido", "is_open"),
    Output("danger_cadastro_password_2_senhas_diferentes", "is_open"),
    Output("danger_cadastro_password_formato" , "is_open"),
    Output("danger_cadastro_password_espaco", "is_open"),
    Output("danger_cadastro_caracteres", "is_open"),
    Output("danger_cadastro_caracteres", "children"),


    ],
    [
    Input("btn_cadastrar", "n_clicks"),
    Input("cadastro_nome", "value"),
    Input("cadastro_email", "value"),
    Input("cadastro_password_1", "value"),
    Input("cadastro_password_2", "value"),
    ]
)
def cadastro_cad (n_btn_cadastrar, username, email, password_1, password_2):

    triggered_id = ctx.triggered_id

    username = str(username)
    email = str(email)
    password_1 = str(password_1)
    password_2 = str(password_2)

    caminho = '/'
    danger_cadastro_email_invalido_is_open= False
    danger_cadastro_password_2_senhas_diferentes_is_open = False
    danger_cadastro_invalido_children = None
    danger_cadastro_password_formato_is_open = False
    danger_cadastro_password_espaco_is_open = False
    danger_cadastro_caracteres_is_open = False
    danger_cadastro_caracteres_children = None

    if triggered_id == 'btn_cadastrar':

        email_no_formato_valido = validar_email(email)
        senha_no_formato_valido = validar_senha (password_1, password_2)

        if password_1 == password_2 and password_1[0] == ' ' or password_1[-1] == ' ':
            tem_espaco = True
        else:
            tem_espaco = False

        if password_1 == password_2 and len (password_1) > 100:
            n_caracteres_superior_ao_limite = True
        else:
            n_caracteres_superior_ao_limite = False

        if password_1 == password_2 and len (password_1) < 8:
            n_caracteres_inferior_ao_limite = True
        else:
            n_caracteres_inferior_ao_limite = False

        if email_no_formato_valido == True and senha_no_formato_valido == True and tem_espaco == False and password_1 == password_2 and n_caracteres_superior_ao_limite == False and n_caracteres_inferior_ao_limite == False:

            form = cadastro_firebase(email, password_1, username)

            #usuario_criado[0], email_veririficacao_enviado[1], usuario_autenticado[2], cadastro_criado[3], username[4], email[5], email_verificado[6], error_message[7], RefreshToken[8], Token[9]

            if form[0] == form[1] == form[2] == form[3] == True and form[7] == None:
                #perfil = username[4], email[5], email_verificado[6], RefreshToken[8], Token[9]
                dados_perfil_temp_1 = form[4], form[5], form[6], form[8], form[9]
                caminho = '/'
                danger_cadastro_invalido_is_open = False
        
            else:
                if str(form[7]) == 'EMAIL_EXISTS':
                    #print("Já existe um cadastro com esse e-mail.")
                    danger_cadastro_invalido_children = html.I(className="bi bi-x-octagon-fill me-4", ),"Já existe um cadastro com esse e-mail."

                else:
                    #print(form[7])
                    danger_cadastro_invalido_children = html.I(className="bi bi-x-octagon-fill me-4", ),"Erro na conexão com o banco de dados, por favor refaça o cadastro."
                
                dados_perfil_temp_1 = 'Visitante', None, None, None, None
                caminho = None
                danger_cadastro_invalido_is_open = True
                      
        else: 
             
            if email_no_formato_valido == False:
                danger_cadastro_email_invalido_is_open=True
                #print('email inválido') 

            if senha_no_formato_valido == False:
                danger_cadastro_password_formato_is_open = True

            if password_1 != password_2:

                danger_cadastro_password_2_senhas_diferentes_is_open =True

            if tem_espaco == True:
                danger_cadastro_password_espaco_is_open = True

            if n_caracteres_superior_ao_limite == True:

                danger_cadastro_caracteres_is_open = True
                danger_cadastro_caracteres_children = html.I(className="bi bi-x-octagon-fill me-4", ),"Use 100 caracteres ou menos para sua senha."

            if n_caracteres_inferior_ao_limite == True:

                danger_cadastro_caracteres_is_open = True
                danger_cadastro_caracteres_children = html.I(className="bi bi-x-octagon-fill me-4", ),"Use 8 caracteres ou mais para sua senha"


            dados_perfil_temp_1 = 'Visitante', None, None, None, None
            caminho = None
            danger_cadastro_invalido_is_open = False

        return (dados_perfil_temp_1, caminho, danger_cadastro_invalido_is_open,  danger_cadastro_invalido_children, danger_cadastro_email_invalido_is_open, 
        danger_cadastro_password_2_senhas_diferentes_is_open, danger_cadastro_password_formato_is_open, danger_cadastro_password_espaco_is_open,
        danger_cadastro_caracteres_is_open, danger_cadastro_caracteres_children
        )

    else:
        raise PreventUpdate

# ativar_botao_entrar
@callback(

    Output("botao_login", "disabled"),
    [
    Input("login_email", "value"),
    Input("login_password", "value"),
    ]
)

def ativar_botao_cadastrar(email, password):

    if email!= '' and password != '':

        return False

    else:
        return True
##### LOGIN
@callback(
    [
    Output("dados_perfil_temp_2", "data"),
    Output("dados_path_temp_2", "data"),
    Output('danger_email_senha_invalido', 'is_open'),
    Output('danger_email_senha_invalido', 'children'),
    ],
    [
    Input("botao_login", "n_clicks"),
    Input("login_email", "value"),
    Input("login_password", "value"),
    ]
    
)

def login(botao_login, email_login, password_login):

    triggered_id = ctx.triggered_id



    if triggered_id == 'botao_login':

        login_form = login_firebase(email_login, password_login) #usuario_autenticado[0], bd_conectado[1], username[2], email[3], email_verificado[4], idToken[5], error_message[6], Token[7]
            

        if login_form[0] == login_form[1] == True:
            #perfil = username[3], email[4], email_verificado[4], RefreshToken[5], Token[7]
            dados_perfil_temp_2 = login_form[2], login_form[3], login_form[4], login_form[5], login_form[7]
            caminho = '/'
            is_open_danger = False 
            mensagem_danger = None

        else:
                                
            if login_form[0] == False:

                if str(login_form[6]) == "TOO_MANY_ATTEMPTS_TRY_LATER : Access to this account has been temporarily disabled due to many failed login attempts. You can immediately restore it by resetting your password or you can try again later.":

                    mensagem_danger = (html.I(className="bi bi-x-octagon-fill me-4", ), "Número de tentativas excedido. Você pode redefinir a sua senha ou tentar novamente mais tarde.")

                else: 

                    mensagem_danger = (html.I(className="bi bi-x-octagon-fill me-4", ), "Campo e-mail e/ou senha inválido(s).")

                dados_perfil_temp_2 = 'Visitante', None, None, None, None
                caminho = None
                is_open_danger= True 

            else:


                dados_perfil_temp_2 = 'Visitante', None, None, None, None
                caminho = None
                is_open_danger = True 
                mensagem_danger =  (html.I(className="bi bi-x-octagon-fill me-4", ), "Sem conexão com banco de dados, tente novamente mais tarde.")
              
        return  dados_perfil_temp_2, caminho, is_open_danger, mensagem_danger

    else: 
        raise PreventUpdate

#sair1
@callback(
    [
    Output('dados_perfil_temp_3', 'data'),
    Output('dados_path_temp_3','data'),
    ],

    #[
    Input('menu_sair', 'n_clicks'),
    #Input('btn_logar_novamente_email_maior', 'n_clicks'),
    #]
)
    
def click_menu(n_clicks):

    if n_clicks:

        return ('Visitante', None, None, None, None), '/'
    
    #elif n_clicks_2:

        #return ('Visitante', None, None, None, None), '/login'

   

    raise PreventUpdate

#sair2
@callback(
    [
    Output('dados_perfil_temp_4', 'data'),
    Output('dados_path_temp_4','data'),
    ],

    #[
    #Input('menu_sair', 'n_clicks'),
    Input('btn_logar_novamente_email_maior', 'n_clicks'),
    #]
)
    
def click_menu(n_clicks):

    if n_clicks:

        print(n_clicks)
        return ('Visitante', None, None, None, None), '/login'
    
    #elif n_clicks_2:

        #return ('Visitante', None, None, None, None), '/login'

   

    raise PreventUpdate


#reenviar_email_verificacao
@callback(

    Output("success_reenvio_email_verificacao_1", "is_open"),
    Output("danger_reenvio_email_verificacao_1", "is_open"),
    Output("danger_reenvio_email_verificacao_1", "children"),
    Output("success_reenvio_email_verificacao_2", "is_open"),
    Output("danger_reenvio_email_verificacao_2", "is_open"),
    Output("danger_reenvio_email_verificacao_2", "children"),

    [
    Input ('btn_reenvio_email_confirmacao', 'n_clicks'),
    #Input("url", "pathname"),
    Input("dados_perfil", "data"),
    ]
)

def reenviar_email_verificacao(n_clicks, dados_perfil):

    triggered_id = ctx.triggered_id


    success_reenvio_email_verificacao_is_open_1 = False
    danger_reenvio_email_verificacao_is_open_1 = False
    danger_reenvio_email_verificacao_children_1 = None

    success_reenvio_email_verificacao_is_open_2 = False
    danger_reenvio_email_verificacao_is_open_2 = False
    danger_reenvio_email_verificacao_children_2 = None

    if triggered_id == "btn_reenvio_email_confirmacao":
        #print(n_clicks, url)
        envio = reenviar_email_confirmacao(dados_perfil[4])
        

        if envio[0] == True:

            success_reenvio_email_verificacao_is_open_1 = True
            success_reenvio_email_verificacao_is_open_2 = True

        else: 
            
            if envio[1] == 'TOO_MANY_ATTEMPTS_TRY_LATER':

                danger_reenvio_email_verificacao_children_1 = html.I(className="bi bi-x-octagon-fill me-4", ), "Quantidade de envios excedida, tente novamente mais tarde."
                danger_reenvio_email_verificacao_children_2 = html.I(className="bi bi-x-octagon-fill me-4", ), "Quantidade de envios excedida, tente novamente mais tarde."

            else: 

                danger_reenvio_email_verificacao_children_1 = html.I(className="bi bi-x-octagon-fill me-4", ), "Autenticação expirada, refaça o login e tente novamente." 
                danger_reenvio_email_verificacao_children_2 = html.I(className="bi bi-x-octagon-fill me-4", ), "Autenticação expirada, refaça o login e tente novamente." 

            danger_reenvio_email_verificacao_is_open_1 = True
            danger_reenvio_email_verificacao_is_open_2 = True

        return success_reenvio_email_verificacao_is_open_1, danger_reenvio_email_verificacao_is_open_1, danger_reenvio_email_verificacao_children_1, success_reenvio_email_verificacao_is_open_2, danger_reenvio_email_verificacao_is_open_2, danger_reenvio_email_verificacao_children_2
        
    else:
            
        raise PreventUpdate
    

# n_clicks_email_de_confirmacao

@callback(

    Output('local', 'data'),
    Input('local-button', 'n_clicks'),
    State('local', 'data')

)

def on_click(n_clicks, data):

    if n_clicks > 0:

  
        data = data or {'clicks': 0}

        data['clicks'] = data['clicks'] + 1

        print(data)
        return data
    
    else:

        raise PreventUpdate


#refresh_perfil
@callback(

    Output("dados_refresh", "data"),
    Input("url", "pathname"),
    Input("dados_perfil", "data"),
    
)
def refresh_perfil(url, dados_perfil):

    triggered_id = ctx.triggered_id

    if triggered_id == "url":
        #print('url: ', url)
        
        if dados_perfil[3] is not None:
            #print('dados_perfil[3]: ', dados_perfil[3])


            RefreshToken = dados_perfil[3]
            refresh = refresh_autenticacao(RefreshToken)

            print (refresh)
            ##print(refresh[0])
            #return refresh[0]
            return refresh
        
        else:

            raise PreventUpdate
    raise PreventUpdate

#perfil_temp_para_perfil
@callback(

    Output("dados_perfil", "data"),
    
    Input("dados_perfil_temp_1", "data"),
    Input("dados_perfil_temp_2", "data"),
    Input("dados_perfil_temp_3", "data"),
    Input("dados_perfil_temp_4", "data"),
   
    prevent_initial_call=True
    
)
def perfil_temp_para_perfil_1 (dados_perfil_temp_1, dados_perfil_temp_2, dados_perfil_temp_3, dados_perfil_temp_4):

    triggered_id = ctx.triggered_id

    if triggered_id == 'dados_perfil_temp_1':
        
        return dados_perfil_temp_1

    elif triggered_id == 'dados_perfil_temp_2':

        return dados_perfil_temp_2

    elif triggered_id == 'dados_perfil_temp_3':

        return dados_perfil_temp_3

    elif triggered_id == 'dados_perfil_temp_4':

        return dados_perfil_temp_4
    
    raise PreventUpdate

#perfil
@callback(
    
    Output("visitante", "children"),
   
    [
    Input("dados_perfil", "data"),
    Input("visitante", "children")
    ]
)

def perfil (dados_perfil, visitante):

    retorno = 'Olá, ' + dados_perfil[0] + '!'
    return retorno


    
#path_temp_para_path
@callback(

    Output("dados_path", "data"),
    
    Input("dados_path_temp_1", "data"),
    Input("dados_path_temp_2", "data"),
    Input("dados_path_temp_3", "data"),
    Input("dados_path_temp_4", "data"),
    Input("dados_path_temp_5", "data"),
    Input("dados_path_temp_6", "data"),
    prevent_initial_call=True
    
)
def perfil_temp_para_perfil_1 (dados_path_temp_1, dados_path_temp_2, dados_path_temp_3, dados_path_temp_4, dados_path_temp_5, dados_path_temp_6):

    triggered_id = ctx.triggered_id

    if triggered_id == 'dados_path_temp_1':

        return dados_path_temp_1

    elif triggered_id == 'dados_path_temp_2':

        return dados_path_temp_2

    elif triggered_id == 'dados_path_temp_3':

        return dados_path_temp_3
    
    elif triggered_id == 'dados_path_temp_4':

        return dados_path_temp_4

    elif triggered_id == 'dados_path_temp_5':

        return dados_path_temp_5
    
    elif triggered_id == 'dados_path_temp_6':

        return dados_path_temp_6

    raise PreventUpdate



#logado_ou_nao
@callback(

    [
    Output('menu_logado', 'style'),
    Output('menu_deslogado', 'style'),
    ],
    Input("dados_perfil", "data")
)

def logado_ou_nao(dados_perfil):

    if dados_perfil [0] == 'Visitante' and dados_perfil [1] == None and dados_perfil [2] == None and dados_perfil [3] == None:
        return {'display': 'none'}, None
    else:
        return None, {'display': 'none'}


#redirect
@callback(

    Output("url", "pathname"),
    Input("dados_path", "data"),
    
    prevent_initial_call=True
)

def redirect(dados_path):

    if dados_path != None:

        print(55555555555555555555555555555555555555555555555555555555555555555555555)
        return dados_path

    else: 

        raise PreventUpdate
    

#redirect quando logado
#/login
#/redefinir-senha
#/criar-conta

@callback(

    Output("dados_path_temp_5", "data"),

    [
    Input("url", "pathname"),
    Input("dados_perfil", "data"),
    ]

)

def redirect_quando_logado(url, dados_perfil):

    if dados_perfil != ['Visitante', None, None, None, None]:

        if url == '/login' or url == '/redefinir-senha' or url == '/criar-conta':

            return '/'
        
        else: 

            return None

    raise PreventUpdate

#redirect quando deslogado
#/minha-conta
#/contato
#/lgpd

@callback(

    Output("dados_path_temp_6", "data"),
    [
    Input("url", "pathname"),
    Input("dados_perfil", "data"),
    ]

)

def redirect_quando_deslogado(url, dados_perfil):

    if dados_perfil == ['Visitante', None, None, None, None]:

        if url == '/minha-conta' or url == '/contato' or url == '/lgpd':

            return '/login'
        
        else: 

            return None

    raise PreventUpdate



#####################################################
######## EMAIL ######################################
#####################################################


#habilitar_btn_envio_contato
@callback(

    
    Output ("botao_enviar_contato", "disabled"),

    [
    Input ("dropdown_contato", "value"),
    Input ("mensagem_contato", "value"),
    Input ("botao_enviar_contato", "n_clicks"),
    ]
)

def habilitar_btn_envio_contato(dropdown_contato, mensagem_contato, botao_enviar_contato):

    if dropdown_contato is not None and mensagem_contato != '' and  botao_enviar_contato == 0:

        return False
    else:

        return True
   
#botao_enviar_contato_data
@callback(

    Output ('botao_enviar_contato_data', 'data'),

    [
    Input ("botao_enviar_contato", "n_clicks"),
    Input ("danger_contato", "is_open"),
    Input ("success_contato", "is_open"),
    ],
)

def enviar_contato_data(botao_enviar_contato, danger_contato, success_contato):

    if botao_enviar_contato >0 and  success_contato is False or botao_enviar_contato >0 and  danger_contato is False :
        return True

    else:
        return False

#botao_voltar
@callback(
        
    Output('div_contato_botao_voltar', 'style'),

    [
    Input ("danger_contato", "is_open"),
    Input ("success_contato", "is_open"),
    ],
)

def botao_voltar(danger_contato, success_contato):

    if danger_contato is True or success_contato is True:

        return {'display': 'block'}

    else: 

        return {'display': 'none'}


@callback(

    [
    Output ("danger_contato", "is_open"),
    Output ("success_contato", "is_open"),
    Output ("success_contato", "children"),   
    ],

    [
    Input ("dropdown_contato", "value"),
    Input ("mensagem_contato", "value"),
    Input ("botao_enviar_contato_data", "data"),
    Input ("dados_perfil", "data"),
    ]
)

def email(dropdown_contato, mensagem_contato, botao_enviar_contato, dados_perfil):

    triggered_id = ctx.triggered_id
    protocolo = 'protocolo'

    if triggered_id == "botao_enviar_contato_data":

        danger_contato_is_open = False
        success_contato_is_open = False
        success_contato_children = None

        eemail = envio_email(dados_perfil[0], dados_perfil[1], dropdown_contato, mensagem_contato, 'contato', protocolo)

        if eemail[0] == False:

            danger_contato_is_open = False

        if eemail[0] == True:

            success_contato_is_open = True
            success_contato_children = html.I(className="bi bi-check-circle-fill me-4", ), "Contato enviado com sucesso! Protocolo n. " + protocolo + "."

        print(eemail[0], eemail[1])

        return danger_contato_is_open, success_contato_is_open, success_contato_children
    
    else:

        raise PreventUpdate


@callback(

    [
    Output ('dropdown_contato', "disabled"),
    Output ('mensagem_contato', "disabled"),
    ],

    Input ("botao_enviar_contato", "n_clicks"),
    
)

def disable(botao_enviar_contato):

    triggered_id = ctx.triggered_id

    if triggered_id == "botao_enviar_contato":

        return True, True
    
    else:

        raise PreventUpdate


#spinner_contato

@callback(
    
    Output('div_contato_spinner', 'style'),

    [
    Input ('botao_enviar_contato', 'n_clicks'),
    Input ("danger_contato", "is_open"),
    Input ("success_contato", "is_open"),
    ]

)

def spinner_contato(botao_enviar_contato, danger_contato, success_contato):
    
    triggered_id = ctx.triggered_id

    mostrar = {'display':'none'}

    if triggered_id  == 'botao_enviar_contato':

        mostrar = {'display':'block'}

    if triggered_id  == 'danger_contato':

        if danger_contato == True:

            mostrar = {'display':'none'}
        
        else: 

            mostrar = {'display':'none'}

    if triggered_id  == 'success_contato':

        if success_contato == True:

            mostrar = {'display':'none'}
        
        else: 

            mostrar = {'display':'none'}

    return mostrar

    
    
#####################################################
######## FIM EMAIL ##################################
#####################################################

#####################################################
######## LGPD ######################################
#####################################################


#habilitar_btn_envio_lgpd
@callback(

    
    Output ("botao_enviar_lgpd", "disabled"),

    [
    Input ("dropdown_lgpd", "value"),
    Input ("mensagem_lgpd", "value"),
    Input ("botao_enviar_lgpd", "n_clicks"),
    ]
)

def habilitar_btn_envio_lgpd(dropdown_lgpd, mensagem_lgpd, botao_enviar_lgpd):

    if dropdown_lgpd is not None and mensagem_lgpd != '' and  botao_enviar_lgpd == 0:

        return False
    else:

        return True
   
#botao_enviar_lgpd_data
@callback(

    Output ('botao_enviar_lgpd_data', 'data'),

    [
    Input ("botao_enviar_lgpd", "n_clicks"),
    Input ("danger_lgpd", "is_open"),
    Input ("success_lgpd", "is_open"),
    ],
)

def enviar_lgpd_data(botao_enviar_lgpd, danger_lgpd, success_lgpd):

    if botao_enviar_lgpd >0 and  success_lgpd is False or  botao_enviar_lgpd >0 and  danger_lgpd is False:
        return True

    else:
        return False

#botao_voltar
@callback(
        
    Output('div_lgpd_botao_voltar', 'style'),

    [
    Input ("danger_lgpd", "is_open"),
    Input ("success_lgpd", "is_open"),
    ],
)

def botao_voltar(danger_lgpd, success_lgpd):

    if danger_lgpd is True or success_lgpd is True:

        return {'display': 'block'}

    else: 

        return {'display': 'none'}


@callback(

    [
    Output ("danger_lgpd", "is_open"),
    Output ("success_lgpd", "is_open"),
    Output ("success_lgpd", "children"),   
    ],

    [
    Input ("dropdown_lgpd", "value"),
    Input ("mensagem_lgpd", "value"),
    Input ("botao_enviar_lgpd_data", "data"),
    Input ("dados_perfil", "data"),
    ]
)

def email_lgpd(dropdown_lgpd, mensagem_lgpd, botao_enviar_lgpd, dados_perfil):

    triggered_id = ctx.triggered_id
    protocolo = 'protocolo'

    if triggered_id == "botao_enviar_lgpd_data":

        danger_lgpd_is_open = False
        success_lgpd_is_open = False
        success_lgpd_children = None

        eemail = envio_email(dados_perfil[0], dados_perfil[1], dropdown_lgpd, mensagem_lgpd, 'lgpd', protocolo)

        if eemail[0] == False:

            danger_lgpd_is_open = False

        if eemail[0] == True:

            success_lgpd_is_open = True
            success_lgpd_children = html.I(className="bi bi-check-circle-fill me-4", ), "Contato enviado com sucesso! Protocolo n. " + protocolo + "."

        print(eemail[0], eemail[1])

        return danger_lgpd_is_open, success_lgpd_is_open, success_lgpd_children
    
    else:

        raise PreventUpdate


@callback(

    [
    Output ('dropdown_lgpd', "disabled"),
    Output ('mensagem_lgpd', "disabled"),
    ],

    Input ("botao_enviar_lgpd", "n_clicks"),
    
)

def disable(botao_enviar_lgpd):

    triggered_id = ctx.triggered_id

    if triggered_id == "botao_enviar_lgpd":

        return True, True
    
    else:

        raise PreventUpdate


#spinner_lgpd

@callback(
    
    Output('div_lgpd_spinner', 'style'),

    [
    Input ('botao_enviar_lgpd', 'n_clicks'),
    Input ("danger_lgpd", "is_open"),
    Input ("success_lgpd", "is_open"),
    ]

)

def spinner_contato(botao_enviar_lgpd, danger_lgpd, success_lgpd):
    
    triggered_id = ctx.triggered_id

    mostrar = {'display':'none'}

    if triggered_id  == 'botao_enviar_lgpd':

        mostrar = {'display':'block'}

    if triggered_id  == 'danger_lgpd':

        if danger_lgpd == True:

            mostrar = {'display':'none'}
        
        else: 

            mostrar = {'display':'none'}

    if triggered_id  == 'success_lgpd':

        if success_lgpd == True:

            mostrar = {'display':'none'}
        
        else: 

            mostrar = {'display':'none'}

    return mostrar

    
    
#####################################################
######## FIM LGPD ##################################
#####################################################



#####################################################
######## RELATORIO ##################################
#####################################################

#passando dados para os stores do relatorio

@callback(

    [
    Output ('dropdown_codigos_ativos_data', 'data'),
    Output ('data_inicial_data', 'data'),
    Output ('data_final_data', 'data'),
    Output ('aportes_data', 'data'),
    Output ('dropdown_benchmarks_data', 'data'),
    Output ('checklist_alocado_data', 'data'),
    Output ('p_data', 'data'),
    Output ('pb_data', 'data'),
    Output ('dividendos_data', 'data'),
    Output ("exibir_relatorio", "data")
    ],

    [
    Input ("btn_rodar", "n_clicks"),
    Input ("dropdown_codigos_ativos", "value"),
    Input ("dia_inicial", "children"),
    Input ("dropdown_mes_inicio", "value"),
    Input ("dropdown_ano_inicio", "value"),
    Input ("dia_final", "children"),
    Input ("dropdown_mes_fim", "value"),
    Input ("dropdown_ano_fim", "value"),
    Input ("investimento_inicial", "value"),
    Input ("checklist_mensal", "value"),
    Input ("valor_aporte_mensal", "value"),
    Input ("checklist_dividendos", "value"),
    Input ("checklist_dividendos_2", "value"),
    Input ("dropdown_benchmarks", "value"),

    Input ("checklist_alocado", "value"),

    Input('p0', 'value'),
    Input('p1', 'value'),
    Input('p2', 'value'),
    Input('p3', 'value'),
    Input('p4', 'value'),
    Input('p5', 'value'),
    Input('p6', 'value'),
    Input('p7', 'value'),
    Input('p8', 'value'),
    Input('p9', 'value'),
    Input('p10', 'value'),
    Input('p11', 'value'),

    Input('pb0', 'value'),
    Input('pb1', 'value'),
    Input('pb2', 'value'),
    Input('pb3', 'value'),
    Input('pb4', 'value'),
    Input('pb5', 'value'),
    Input('pb6', 'value'),
    Input('pb7', 'value'),
    Input('pb8', 'value'),
    Input('pb9', 'value'),
    Input('pb10', 'value'),
    Input('pb11', 'value'),

    ]
)

def dados_relatorio (btn_rodar, dropdown_codigos_ativos, 
        dia_inicial, dropdown_mes_inicio, dropdown_ano_inicio, 
        dia_final, dropdown_mes_fim, dropdown_ano_fim, 
        investimento_inicial, checklist_mensal, valor_aporte_mensal, checklist_dividendos, checklist_dividendos_2,
        dropdown_benchmarks,
        checklist_alocado,
        p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, 
        pb0, pb1, pb2, pb3, pb4, pb5, pb6, pb7, pb8, pb9, pb10, pb11
        ):

    triggered_id = ctx.triggered_id

    if triggered_id == "btn_rodar":

    

        #print('dropdown_codigos_ativos: ', dropdown_codigos_ativos)
        #print('dropdown_codigos_ativos_type: ', type(dropdown_codigos_ativos))
        #<class 'list'>

        #print('dia_inicial: ', dia_inicial)
        #print('dia_inicial_type: ', type(dia_inicial))
        #<class 'str'>

        #print('dropdown_mes_inicio: ', dropdown_mes_inicio)
        #print('dropdown_mes_inicio_type: ', type(dropdown_mes_inicio))
        #<class 'str'>

        #print('dropdown_ano_inicio: ', dropdown_ano_inicio)
        #print('dropdown_ano_inicio_type: ', type(dropdown_ano_inicio))
        #<class 'str'>

        #print('dia_final: ', dia_final)
        #print('dia_final_type: ', type(dia_final))
        #<class 'str'>

        #print('dropdown_mes_fim: ', dropdown_mes_fim)
        #print('dropdown_mes_fim_type: ', type(dropdown_mes_fim))
        #<class 'str'>

        #print('dropdown_ano_fim: ', dropdown_ano_fim)
        #print('dropdown_ano_fim_type: ', type(dropdown_ano_fim))
        #<class 'str'>

        #print('investimento_inicial: ', investimento_inicial)
        #print('investimento_inicial_type: ', type(investimento_inicial))
        #<class 'str'>

        #print('checklist_mensal: ', checklist_mensal)
        #print('checklist_mensal_type: ', type(checklist_mensal))
        #<class 'list'>

        #print('valor_aporte_mensal: ', valor_aporte_mensal)
        #print('valor_aporte_mensal_type: ', type(valor_aporte_mensal))
        #<class 'str'>

        #print('checklist_dividendos: ', checklist_dividendos)
        #print('checklist_dividendos_type: ', type(checklist_dividendos))
        #<class 'list'>

        #print('dropdown_benchmarks: ', dropdown_benchmarks)
        #print('dropdown_benchmarks_type: ', type(dropdown_benchmarks))
        #<class 'list'>


        #dropdown_codigos_ativos, 
        #dia_inicial, dropdown_mes_inicio, dropdown_ano_inicio, 
        #dia_final, dropdown_mes_fim, dropdown_ano_fim, 
        #investimento_inicial, checklist_mensal, valor_aporte_mensal, checklist_dividendos, 
        # dropdown_benchmarks,
        #p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, 
        #pb0, pb1, pb2, pb3, pb4, pb5, pb6, pb7, pb8, pb9, pb10, pb11

        if len (checklist_mensal) > 0:
            checklist_mensal_str = str(checklist_mensal[0])
        else: 
            checklist_mensal_str = '0'
        
        if len (checklist_dividendos) > 0:
            checklist_dividendos_str = str(checklist_dividendos[0])
        else: 
            checklist_dividendos_str = '0'

        if len (checklist_dividendos_2) > 0:
            checklist_dividendos_2_str = str(checklist_dividendos_2[0])
        else: 
            checklist_dividendos_2_str = '0'
        
        if len (checklist_alocado) > 0:
            checklist_alocado_str = str(checklist_alocado[0])
        else: 
            checklist_alocado_str = '0'


        #rodar função para pegar as colunas de dividendos
        data_i = str(dropdown_ano_inicio) + '-' + str(dropdown_mes_inicio) + '-' + str(dia_inicial)
        data_f =str(dropdown_ano_fim) + '-' + str(dropdown_mes_fim) + '-' + str(dia_final)
        dividendos = dividendos_cut(dropdown_codigos_ativos, data_i, data_f)
        
        
        
        return (dropdown_codigos_ativos,
        [dia_inicial, dropdown_mes_inicio, dropdown_ano_inicio],
        [dia_final, dropdown_mes_fim, dropdown_ano_fim],
        [investimento_inicial, checklist_mensal_str, valor_aporte_mensal, checklist_dividendos_str, checklist_dividendos_2_str],
        dropdown_benchmarks,
        checklist_alocado_str,
        [float(p0), float(p1), float(p2), float(p3), float(p4), float(p5), float(p6), float(p7), float(p8), float(p9), float(p10), float(p11)],
        [float(pb0), float(pb1), float(pb2), float(pb3), float(pb4), float(pb5), float(pb6), float(pb7), float(pb8), float(pb9), float(pb10), float(pb11)],
        dividendos,
        1
        )

    else:

        raise PreventUpdate
    


#stores_disable_botao_rodar

@callback(

    Output('disable_rodar', 'data'),
   
    [
    Input('disable_rodar_1', 'data'),
    Input('disable_rodar_2', 'data'),
    Input('disable_rodar_3', 'data'),
    #Input("dados_path", "data"),
    ]
)

def stores_disable_botao_rodar(disable_rodar_1, disable_rodar_2, disable_rodar_3):

    #if dados_path:
        #return Fals

    triggered_id = ctx.triggered_id

    print(disable_rodar_1, disable_rodar_2, disable_rodar_3)

    if triggered_id == 'disable_rodar_1':

        print('trigou 1')

        return disable_rodar_1

    
    if triggered_id == 'disable_rodar_2':

        print('trigou 2')

        if disable_rodar_3 == disable_rodar_2:

            return disable_rodar_3
        else:

            return disable_rodar_3
            

    if triggered_id == 'disable_rodar_3':

        print('trigou 3')

        return disable_rodar_3
    

 

    else:

        raise PreventUpdate
    
#disable_botao_rodar
@callback(

    [
    Output("btn_ainda_nao_logou", 'disabled'),
    Output("btn_rodar", 'disabled'),
    Output("btn_ainda_nao_verificou_email", 'disabled'),
    ],

    Input('disable_rodar', 'data'),
)

def disable_botao_rodar(disable_rodar):

    if disable_rodar == True:

        return True, True, True
    
    else: 

        return False, False, False

#exibir_relatorio e bloquear o resto

@callback(

    [
    Output("exibir", "style"),
    Output("disable_rodar_1", 'data'),
    Output('dropdown_codigos_ativos', 'disabled'),
    Output('dropdown_mes_inicio', 'disabled'),
    Output('dropdown_ano_inicio', 'disabled'),
    Output('dropdown_mes_fim', 'disabled'),
    Output('dropdown_ano_fim', 'disabled'),
    Output("investimento_inicial", 'disabled'),
    Output("valor_aporte_mensal", 'disabled'),
    Output("dropdown_benchmarks", 'disabled'),
    Output("checklist_mensal",'options'),
    Output("checklist_dividendos",'options'),
    Output("checklist_dividendos_2",'options'),
    Output("checklist_alocado", 'style'),

    Output('pb0', 'disabled'),
    Output('pb1', 'disabled'),
    Output('pb2', 'disabled'),
    Output('pb3', 'disabled'),
    Output('pb4', 'disabled'),
    Output('pb5', 'disabled'),
    Output('pb6', 'disabled'),
    Output('pb7', 'disabled'),
    Output('pb8', 'disabled'),
    Output('pb9', 'disabled'),
    Output('pb10', 'disabled'),
    Output('pb11', 'disabled'),
    
    ],

    [
    Input('exibir_relatorio', 'data'),
    Input ('aportes_data', 'data'),#[investimento_inicial, checklist_mensal_str, valor_aporte_mensal, checklist_dividendos_str, checklist_dividendos_2_str],

    ]
)

def exibir_relatorio(exibir_relatorio, aportes_data):

    print(exibir_relatorio, '$%$%%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    #print(aportes_data)
    if aportes_data[1] == '1':
        um = '  SIM'
    else:
        um = '  NÃO'

    if aportes_data[3] == '1':
        dois = '  SIM'
    else:
        dois = '  NÃO'

    if aportes_data[4] == '1':
        tres = '  SIM'
    else:
        tres = '  NÃO'

    if exibir_relatorio == 1:
        

        return (
        {"display":"block"}, True, True, True, True, True, True, True, True, True, 
        [{"label": "Realizar novos aportes mensais:" + um, "value": aportes_data[1] ,"disabled": True}], [{"label": "Considerar dividendos:" + dois, "value": aportes_data[3], "disabled": True}], [{"label": "Reinvestir dividendos:" + tres, "value": aportes_data[4], "disabled": True}], {"display":"none"}, 
        True, True, True, True, True, True, True, True, True, True, True, True,
        
        )
    else:

        raise PreventUpdate
        
   
        

@callback(

    [
    Output('grafico_1f', 'figure'),
    Output('grafico_2f', 'figure'),
    Output('grafico_3f', 'figure'),
    Output('grafico_4f', 'figure'),
    Output('grafico_5f', 'figure'),
    Output('grafico_6f', 'figure'),
    Output('grafico_7f', 'figure'),
    Output('grafico_8f', 'figure'),

    Output('leg_1', 'children'),
    Output('leg_2', 'children'),
    Output('leg_3', 'figure'),
    Output('leg_4', 'figure'),
    Output('rmi_txt', 'children'),
    Output('emi_txt', 'children'),
    Output('melhor_acao', 'children'),
    Output('pior_acao', 'children'),
    Output('melhor_setor', 'children'),
    Output('pior_setor', 'children'),

    #Output('table_rel', 'children')

    ],

    [
    Input ('dropdown_codigos_ativos_data', 'data'),
    Input ('data_inicial_data', 'data'),
    Input ('data_final_data', 'data'),
    Input ('aportes_data', 'data'),
    Input ('dropdown_benchmarks_data', 'data'),
    Input ('checklist_alocado_data', 'data'),
    Input ('p_data', 'data'),
    Input ('pb_data', 'data'),
    Input ('dividendos_data', 'data'),
    Input ('selected_stocks_data', 'data'),
    ]

)

def revendo_graficos(dropdown_codigos_ativos_data, data_inicial_data, data_final_data, aportes_data, dropdown_benchmarks_data, checklist_alocado_data, p_data, pb_data, dividendos_data, selected_stocks_data):

    ##### preparando
    if len (dropdown_codigos_ativos_data) > 0:
    
        dropdown_codigos_ativos_data.sort()

        selected_stocks_data = pd.read_json(selected_stocks_data, orient ='index')
        dividendos_data = pd.read_json(dividendos_data, orient ='index')

        p_data = p_data[:len(dropdown_codigos_ativos_data)]
        pb_data = pb_data[:len(dropdown_codigos_ativos_data)]

        if checklist_alocado_data == '1':
            px = pb_data
        else: 
            px = p_data


        #criação do df com o close, dividendos e peso das ações escolhidas
        df_acoes = pd.DataFrame([])
        n=0

        for i in dropdown_codigos_ativos_data:

            selected_stocks_data [i+ "close"] = selected_stocks_data[i]

            try:
                dividendos_data [i+ "dividends"] = dividendos_data[i]
            except:
                dividendos_data [i+ "dividends"] = 0

            selected_stocks_data[i+ 'p'] = px[n]/100

            df_to_concat = pd.concat([selected_stocks_data [i+ "close"] , dividendos_data [i+ "dividends"], selected_stocks_data[i+ 'p']], axis=1)
            
            df_acoes = pd.concat([df_acoes , df_to_concat], axis=1) 
            df_acoes.fillna(0)

            n = n +1

        #print(df_acoes)

        amplitude_mes = pd.read_csv('assets/dados/parametros_ibov/amplitude_mes.csv')

        amplitude_mes['amplitude_fim'] = pd.to_datetime(amplitude_mes['amplitude_fim'] )

        amplitude_mes['index'] = amplitude_mes['amplitude_fim']
        amplitude_mes.set_index('index', inplace=True)

        data_inicial = str(data_inicial_data[2] + '-' +  data_inicial_data[1] + '-' + data_inicial_data[0])
        data_final = str(data_final_data[2] + '-' +  data_final_data[1] + '-' + data_final_data[0])

        amplitude_mes = amplitude_mes [data_inicial: data_final]

        #investimento_inicial, checklist_mensal, valor_aporte_mensal, checklist_dividendos, checklist_dividendos_2
        if aportes_data[1] == '1':

            amplitude_mes['aporte'] = float(aportes_data[2])

        else: 

            amplitude_mes['aporte'] = 0
        
        amplitude_mes = amplitude_mes['aporte']

        total_rel = pd.concat([df_acoes , amplitude_mes], axis=1) 
        
        total_rel['aporte'][0] = float(aportes_data[0])
        total_rel['aporte'][-1] = 0

        #(total_rel)

        ########## quant_acoes
        quant_acoes_list_df = []
        for i in dropdown_codigos_ativos_data:

            total_rel [i + "quant_acoes"] = total_rel ['aporte'] * total_rel [i + "p"] / total_rel [i + "close"]
            total_rel = total_rel.fillna(0)
            quant_acoes_list = total_rel[i + "quant_acoes"].values.tolist()

            for j in quant_acoes_list:

                if len(quant_acoes_list_df) == 0:
                    quant_acoes_list_df.append(j)

                else:
                    quant_acoes_list_df.append(j + quant_acoes_list_df[-1])       

            total_rel[i + "quant_acoes"] = quant_acoes_list_df
            quant_acoes_list_df = []

    ########## quant_acoes_dividendos
        quant_acoes_dividendos_list_df = []
        for i in dropdown_codigos_ativos_data:
            total_rel = total_rel.replace(0, np.nan)

            total_rel [i + "quant_acoes_dividendos"] = total_rel [i + 'dividends'] * total_rel [i + "quant_acoes"] / total_rel [i + "close"]

            total_rel = total_rel.fillna(0)

            quant_acoes_dividendos_list = total_rel[i + "quant_acoes_dividendos"].values.tolist()

            for j in quant_acoes_dividendos_list:

                if len(quant_acoes_dividendos_list_df) == 0:

                    quant_acoes_dividendos_list_df.append(j)

                else:

                    quant_acoes_dividendos_list_df.append(j + quant_acoes_dividendos_list_df[-1])
            

            total_rel[i + "quant_acoes_dividendos"] = quant_acoes_dividendos_list_df
            quant_acoes_dividendos_list_df = []

        ########## retorno_diario_dividendos
        pagamento_dividendos_list_df = []
        for i in dropdown_codigos_ativos_data:
            
            total_rel = total_rel.replace(0, np.nan)

            total_rel [i + 'pagamento_dividendos'] = total_rel [i + 'dividends'] * total_rel [i + "quant_acoes"]

            total_rel = total_rel.fillna(0)
            
            pagamento_dividendos_list = total_rel [i + 'pagamento_dividendos'].values.tolist()

            for j in pagamento_dividendos_list:

                if len(pagamento_dividendos_list_df) == 0:

                    pagamento_dividendos_list_df.append(j)

                else:

                    pagamento_dividendos_list_df.append(j + pagamento_dividendos_list_df[-1])
            

            total_rel[i + "pagamento_dividendos"] = pagamento_dividendos_list_df
            pagamento_dividendos_list_df = []

        ########## soma_aportes
        soma_aportes_list_df = []
        soma_aportes_list = total_rel ['aporte'].values.tolist()

        for j in soma_aportes_list:

            if len(soma_aportes_list_df) == 0:

                soma_aportes_list_df.append(j)

            else:

                soma_aportes_list_df.append(j + soma_aportes_list_df[-1])
            
        total_rel["soma_aportes"] = soma_aportes_list_df


        ########## opcoes em relação aos dividendos para calcular valor em ações
        if aportes_data[3] == '0':
            
            for i in dropdown_codigos_ativos_data:
                total_rel [i] = total_rel [i + 'close'] * total_rel [i + "quant_acoes"]  # não considerar dividendos
        else: 
            if aportes_data[4] == '0':
            
                for i in dropdown_codigos_ativos_data:
                    total_rel [i] = total_rel [i + 'close'] * total_rel [i + "quant_acoes"]  + total_rel [i + 'pagamento_dividendos'] # considerar dividendos, mas não reinvestir

            else:
                
                for i in dropdown_codigos_ativos_data:
                    total_rel [i] = total_rel [i + 'close'] * total_rel [i + "quant_acoes"]  + total_rel [i + 'close'] * total_rel [i + "quant_acoes_dividendos"] # reinvestir dividendos

        #print('total_rel')
        #print(total_rel)


        ######### soma_dividendos_cada_acao
        lista_acao = []
        lista_dividendos = []
        for i in dropdown_codigos_ativos_data:

            lista_acao.append(i)
            lista_dividendos.append(round(total_rel[i+'pagamento_dividendos'].iloc[-1], 2))
            
        dividendos = pd.DataFrame([])
        dividendos['acao'] = lista_acao
        dividendos['dividendos'] = lista_dividendos

        #print('dividendos')
        #print(dividendos)

        ######### soma_aportes_cada_acao
        aportes = pd.DataFrame([])

        for i in dropdown_codigos_ativos_data:

            aportes[i] = round(total_rel["soma_aportes"] * total_rel[i+"p"],2)

        ######### soma_aportes_carteira 
        aportes['Carteira'] = aportes[dropdown_codigos_ativos_data].sum(axis=1)

        #('aportes')
        #print(aportes)


        ######### valor_cada_acao
        valor = pd.DataFrame([])
        
        valor = round(total_rel[dropdown_codigos_ativos_data],2)

        valor['Carteira'] = valor[dropdown_codigos_ativos_data].sum(axis=1)

        #print('valor')
        #print(valor)

        ######### rendimento_cada_acao
        rendimentos = pd.DataFrame([])

        for i in dropdown_codigos_ativos_data:

            rendimentos[i] = round(total_rel[i],2)- round((total_rel["soma_aportes"] * total_rel[i+"p"] ),2)

        ######### retorno_carteira
        rendimentos['Carteira'] = rendimentos[dropdown_codigos_ativos_data].sum(axis=1)

        #print('rendimentos')
        #print(rendimentos)

        ######### rentabilidade_cada_acao
        rentabilidade = pd.DataFrame([])

        for i in dropdown_codigos_ativos_data:

            rentabilidade[i] =  round(rendimentos[i] *100 / aportes[i], 2)

        rentabilidade['Carteira'] = round(rendimentos['Carteira'] *100 / aportes['Carteira'], 2)

        #print('rentabilidade')
        #print(rentabilidade)

        #####################################

        ########## total de aportes
        total_aportado_valor = round(aportes['Carteira'].iloc[-1], 2)
        #print('total_aportado: ', total_aportado_valor)
        ########## valor_da_carteira
        valor_da_carteira_valor = round(valor['Carteira'].iloc[-1], 2)
        #print('valor_da_carteira: ', valor_da_carteira_valor)
        ########## rendimento
        rendimento_valor = round(rendimentos['Carteira'].iloc[-1], 2)
        #print('rendimento: ', rendimento_valor)
        ########## rentabilidade
        rentabilidade_valor = round(rentabilidade['Carteira'].iloc[-1], 2)
        #print('rentabilidade: ', rentabilidade_valor)
        ##########
        rendimento_inicio = round(rendimentos['Carteira'].iloc[0], 2)
        rendimento_fim = round(rendimentos['Carteira'].iloc[-1], 2)
        ##########
        elevacao_max_inicio = rentabilidade['Carteira'].max()
        rebaixamento_max_inicio = rentabilidade['Carteira'].min()
        rebaixamento_max = 0

        
        ##########

        #####################################

        ######### aportes_setor
        df_setor = pd.DataFrame([])

        ##print(retornos[dropdown_codigos_ativos_data])

        df_setor ['acoes'] = dropdown_codigos_ativos_data

    
        df_setor['aportes'] = aportes[dropdown_codigos_ativos_data].iloc[-1].tolist()
        df_setor ['rendimentos'] = rendimentos[dropdown_codigos_ativos_data].iloc[-1].tolist()
        df_setor ['rentabilidade'] = rentabilidade[dropdown_codigos_ativos_data].iloc[-1].tolist()



        df_setor["color"] = np.where(df_setor['rendimentos']<0, danger, success)
        #print('df_setor')
        #print(df_setor)


        #setor_rendimento

        try:
            dict0 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[0]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[0]].iloc[0]['rendimentos'] }]
            soma_dicts = dict0
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        try:
            dict1 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[1]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[1]].iloc[0]['rendimentos'] }]
            soma_dicts = dict0+dict1
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        try:
            dict2 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[2]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[2]].iloc[0]['rendimentos'] }]
            soma_dicts = dict0+dict1+dict2
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        try:
            dict3 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[3]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[3]].iloc[0]['rendimentos'] }]
            soma_dicts = dict0+dict1+dict2+dict3
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        try:
            dict4 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[4]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[4]].iloc[0]['rendimentos'] }]
            soma_dicts = dict0+dict1+dict2+dict3+dict4
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        try:
            dict5 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[5]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[5]].iloc[0]['rendimentos'] }]
            soma_dicts = dict0+dict1+dict2+dict3+dict4+dict5
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        try:
            dict6 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[6]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[6]].iloc[0]['rendimentos'] }]
            soma_dicts = dict0+dict1+dict2+dict3+dict4+dict5+dict6
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        try:
            dict7 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[7]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[7]].iloc[0]['rendimentos'] }]
            soma_dicts = dict0+dict1+dict2+dict3+dict4+dict5+dict6+dict7
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        try:
            dict8 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[8]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[8]].iloc[0]['rendimento'] }]
            soma_dicts = dict0+dict1+dict2+dict3+dict4+dict5+dict6+dict7+dict8
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        try:
            dict9 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[9]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[9]].iloc[0]['rendimentos'] }]
            soma_dicts = dict0+dict1+dict2+dict3+dict4+dict5+dict6+dict7+dict8+dict9
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        try:
            dict10 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[10]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[10]].iloc[0]['rendimentos'] }]
            soma_dicts = dict0+dict1+dict2+dict3+dict4+dict5+dict6+dict7+dict8+dict9+dict10
            names = set([k['name'] for k in soma_dicts])
        except:
            pass
            
        try:
            dict11 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[11]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[11]].iloc[0]['rendimentos'] }]
            soma_dicts = dict0+dict1+dict2+dict3+dict4+dict5+dict6+dict7+dict8+dict9+dict10+dict11
            names = set([k['name'] for k in soma_dicts])
        except:
            pass
        
        dcx_rendimento = []
        for name in names:
            temp_val = []
            #for dict_ in soma_dicts = dict0+dict1+dict2+dict3+dict4+dict5+dict6+dict7+dict8+dict9+dict10+dict11:
            for dict_ in soma_dicts:
                if dict_['name'] == name:
                    temp_val.append(dict_['value'])
            dcx_rendimento.append({'name': name, 'value' : sum(temp_val)})

        dcx_rendimento_setor=pd.DataFrame(dcx_rendimento)
        dcx_rendimento_setor = dcx_rendimento_setor[dcx_rendimento_setor.value != 0.0]

        dcx_rendimento_setor.rename(columns = {'name':'setor', 'value':'rendimento'}, inplace = True)

        dcx_rendimento_setor["color"] = np.where(dcx_rendimento_setor['rendimento']<0, danger, success)

        dcx_rendimento_setor = dcx_rendimento_setor.sort_values('setor').reset_index(drop=True)
        

        #print('dcx_rendimento_setor')
        #print(dcx_rendimento_setor)

        #setor_rentabilidade

        try:
            dict0 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[0]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[0]].iloc[0]['rentabilidade'] }]
            soma_dicts = dict0
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        try:
            dict1 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[1]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[1]].iloc[0]['rentabilidade'] }]
            soma_dicts = dict0+dict1
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        try:
            dict2 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[2]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[2]].iloc[0]['rentabilidade'] }]
            soma_dicts = dict0+dict1+dict2
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        try:
            dict3 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[3]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[3]].iloc[0]['rentabilidade'] }]
            soma_dicts = dict0+dict1+dict2+dict3
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        try:
            dict4 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[4]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[4]].iloc[0]['rentabilidade'] }]
            soma_dicts = dict0+dict1+dict2+dict3+dict4
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        try:
            dict5 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[5]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[5]].iloc[0]['rentabilidade'] }]
            soma_dicts = dict0+dict1+dict2+dict3+dict4+dict5
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        try:
            dict6 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[6]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[6]].iloc[0]['rentabilidade'] }]
            soma_dicts = dict0+dict1+dict2+dict3+dict4+dict5+dict6
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        try:
            dict7 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[7]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[7]].iloc[0]['rentabilidade'] }]
            soma_dicts = dict0+dict1+dict2+dict3+dict4+dict5+dict6+dict7
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        try:
            dict8 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[8]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[8]].iloc[0]['rentabilidade'] }]
            soma_dicts = dict0+dict1+dict2+dict3+dict4+dict5+dict6+dict7+dict8
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        try:
            dict9 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[9]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[9]].iloc[0]['rentabilidade'] }]
            soma_dicts = dict0+dict1+dict2+dict3+dict4+dict5+dict6+dict7+dict8+dict9
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        try:
            dict10 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[10]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[10]].iloc[0]['rentabilidade'] }]
            soma_dicts = dict0+dict1+dict2+dict3+dict4+dict5+dict6+dict7+dict8+dict9+dict10
            names = set([k['name'] for k in soma_dicts])
        except:
            pass
            
        try:
            dict11 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[11]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[11]].iloc[0]['rentabilidade'] }]
            soma_dicts = dict0+dict1+dict2+dict3+dict4+dict5+dict6+dict7+dict8+dict9+dict10+dict11
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        
        dcx_rentabilidade = []
        for name in names:
            temp_val = []
            #for dict_ in soma_dicts = dict0+dict1+dict2+dict3+dict4+dict5+dict6+dict7+dict8+dict9+dict10+dict11:
            for dict_ in soma_dicts:
                if dict_['name'] == name:
                    temp_val.append(dict_['value'])
            dcx_rentabilidade.append({'name': name, 'value' : sum(temp_val)})

        dcx_rentabilidade_setor=pd.DataFrame(dcx_rentabilidade)
        dcx_rentabilidade_setor = dcx_rentabilidade_setor[dcx_rentabilidade_setor.value != 0.0]

        dcx_rentabilidade_setor.rename(columns = {'name':'setor', 'value':'rentabilidade'}, inplace = True)

        dcx_rentabilidade_setor["color"] = np.where(dcx_rentabilidade_setor['rentabilidade']<0, danger, success)

        dcx_rentabilidade_setor.sort_values('setor').reset_index(drop=True)

        #print('dcx_rentabilidade_setor')
        #print(dcx_rentabilidade_setor)


        #setor_aporte

        try:
            dict0 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[0]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[0]].iloc[0]['aportes'] }]
            soma_dicts = dict0
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        try:
            dict1 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[1]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[1]].iloc[0]['aportes'] }]
            soma_dicts = dict0+dict1
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        try:
            dict2 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[2]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[2]].iloc[0]['aportes'] }]
            soma_dicts = dict0+dict1+dict2
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        try:
            dict3 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[3]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[3]].iloc[0]['aportes'] }]
            soma_dicts = dict0+dict1+dict2+dict3
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        try:
            dict4 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[4]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[4]].iloc[0]['aportes'] }]
            soma_dicts = dict0+dict1+dict2+dict3+dict4
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        try:
            dict5 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[5]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[5]].iloc[0]['aportes'] }]
            soma_dicts = dict0+dict1+dict2+dict3+dict4+dict5
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        try:
            dict6 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[6]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[6]].iloc[0]['aportes'] }]
            soma_dicts = dict0+dict1+dict2+dict3+dict4+dict5+dict6
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        try:
            dict7 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[7]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[7]].iloc[0]['aportes'] }]
            soma_dicts = dict0+dict1+dict2+dict3+dict4+dict5+dict6+dict7
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        try:
            dict8 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[8]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[8]].iloc[0]['aportes'] }]
            soma_dicts = dict0+dict1+dict2+dict3+dict4+dict5+dict6+dict7+dict8
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        try:
            dict9 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[9]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[9]].iloc[0]['aportes'] }]
            soma_dicts = dict0+dict1+dict2+dict3+dict4+dict5+dict6+dict7+dict8+dict9
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        try:
            dict10 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[10]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[10]].iloc[0]['aportes'] }]
            soma_dicts = dict0+dict1+dict2+dict3+dict4+dict5+dict6+dict7+dict8+dict9+dict10
            names = set([k['name'] for k in soma_dicts])
        except:
            pass
            
        try:
            dict11 = [{'name':ibov_tabela.loc[ibov_tabela['Código'] == dropdown_codigos_ativos_data[11]].iloc[0]['Setor'], 'value':df_setor.loc[df_setor['acoes'] == dropdown_codigos_ativos_data[11]].iloc[0]['aportes'] }]
            soma_dicts = dict0+dict1+dict2+dict3+dict4+dict5+dict6+dict7+dict8+dict9+dict10+dict11
            names = set([k['name'] for k in soma_dicts])
        except:
            pass

        
        dcx_aporte = []
        for name in names:
            temp_val = []
            #for dict_ in soma_dicts = dict0+dict1+dict2+dict3+dict4+dict5+dict6+dict7+dict8+dict9+dict10+dict11:
            for dict_ in soma_dicts:
                if dict_['name'] == name:
                    temp_val.append(dict_['value'])
            dcx_aporte.append({'name': name, 'value' : sum(temp_val)})

        dcx_aporte_setor=pd.DataFrame(dcx_aporte)
        dcx_aporte_setor = dcx_aporte_setor[dcx_aporte_setor.value != 0.0]

        dcx_aporte_setor.rename(columns = {'name':'setor', 'value':'aporte'}, inplace = True)

        dcx_aporte_setor["color"] = warning

        dcx_aporte_setor.sort_values('setor').reset_index(drop=True)

        #print('dcx_aporte_setor')
        #print(dcx_aporte_setor)



        
        
        ######### benchmarks
        df_bench = pd.read_csv('assets/dados/benchmarks/Ibovespa.csv')
        df_bench['Date'] = pd.to_datetime(df_bench['Date'])
        df_bench.set_index('Date', inplace=True)
        
        n = 0
        for i  in dropdown_benchmarks_data:

            if i == 'Ibovespa':
                n = n+1

            else:
                
                bench_to_read =  dropdown_benchmarks_data[0+n]
                hist_bench = pd.read_csv('assets/dados/benchmarks/'+ bench_to_read +'.csv')
                n = n+1

                hist_bench['Date'] = pd.to_datetime(hist_bench['Date'])
                hist_bench.set_index('Date', inplace=True)
    
                df_bench = pd.concat([df_bench, hist_bench], axis=1)
                df_bench = df_bench.dropna(axis=0)

        df_bench = df_bench[dropdown_benchmarks_data]

        df_bench = df_bench [data_inicial: data_final]
        
        total_rel_b = pd.concat([df_bench , amplitude_mes], axis=1) 
        
        total_rel_b['aporte'][0] = float(aportes_data[0])
        total_rel_b['aporte'][-1] = 0

        
        # corrigindo o CDI
        if 'CDI' in dropdown_benchmarks_data:

            total_rel_b['CDI'] = total_rel_b['CDI'] - total_rel_b['CDI'].iloc[0]

        #print('total_rel_b')
        #print(total_rel_b)


        ######### quant_acoes_bench
        quant_acoes_list_df = []
        for i in dropdown_benchmarks_data:


            total_rel_b [i + "quant_acoes"] = total_rel_b ['aporte'] / total_rel_b [i]
            total_rel_b = total_rel_b.fillna(0)
            quant_acoes_list = total_rel_b[i + "quant_acoes"].values.tolist()

            for j in quant_acoes_list:

                if len(quant_acoes_list_df) == 0:
                    quant_acoes_list_df.append(j)

                else:
                    quant_acoes_list_df.append(j + quant_acoes_list_df[-1])       

            total_rel_b[i + "quant_acoes"] = quant_acoes_list_df
            quant_acoes_list_df = []
            


        ######### soma_aportes_bench
        soma_aportes_list_df = []
        soma_aportes_list = total_rel_b ['aporte'].values.tolist()

        for j in soma_aportes_list:

            if len(soma_aportes_list_df) == 0:

                soma_aportes_list_df.append(j)

            else:

                soma_aportes_list_df.append(j + soma_aportes_list_df[-1])
            
        total_rel_b["soma_aportes"] = soma_aportes_list_df
    

        ######### rendimento benchmarks
        for i in dropdown_benchmarks_data:

            if i != 'CDI':
                total_rel_b ['rendimento' + i] = round(total_rel_b [i] * total_rel_b [i + "quant_acoes"], 2)  # não considerar dividendos

            else: 
                total_rel_b ['rendimento' + i] = total_rel_b [i] * total_rel_b["soma_aportes"]/100 + total_rel_b["soma_aportes"]


        #print(total_rel_b)


        ######### rendimento_de_cada_bench
        valor_bench = pd.DataFrame([])

        for i in dropdown_benchmarks_data:

            valor_bench[i] = round(total_rel_b ['rendimento' + i], 2)

        #print('valor_bench')
        #print(valor_bench)

        ######### rentabilidade_cada_bench
        rentabilidade_bench = pd.DataFrame([])

        for i in dropdown_benchmarks_data:

            rentabilidade_bench[i] =  round((valor_bench[i] *100 / total_rel_b['soma_aportes']) - 100, 2)

        #rentabilidade['Carteira'] = round(rendimentos['Carteira'] *100 / aportes['Carteira'], 2)

        #print('rentabilidade_bench')
        #print(rentabilidade_bench)


        #print(rendimentos['Carteira'])
        

        rentabilidade_final = pd.DataFrame([])

        lista_ativos = dropdown_benchmarks_data
        lista_ativos.insert(0, 'Carteira')
        lista_rentabilidade = []

        for i in dropdown_benchmarks_data:

            if i != 'Carteira':

                lista_rentabilidade.append(rentabilidade_bench[i].iloc[-1])

            else:

                lista_rentabilidade.append(rentabilidade_valor)

        rentabilidade_final ['ativos'] = lista_ativos
        rentabilidade_final ['rentabilidade'] = lista_rentabilidade

        rentabilidade_final["color"] = np.where(rentabilidade_final ['rentabilidade']<0, danger, success)

        #print('rentabilidade_final')
        #print(rentabilidade_final)



        ##########drawdown

        picos_carteira = rendimentos['Carteira'].cummax()
        #print('picos_carteira')
        #print(picos_carteira)
        
        drawdown = (rendimentos['Carteira']-picos_carteira )/picos_carteira
        #print('drawdown')
        #print(drawdown)

        #https://www.youtube.com/watch?v=_LhK6aX35IM
        #https://www.youtube.com/watch?v=6jsDvbIbiVo
        max_ddw = drawdown.min()
        max_ddw = round(max_ddw*100, 2)
        #print('max_ddw')
        #print(max_ddw*100)


        #melhor ação
        #print('melhor ação')
        melhor_acao = rentabilidade[dropdown_codigos_ativos_data].iloc[-1].max()
        lst_melhor_acao = []
        #print('')

        for i in dropdown_codigos_ativos_data:

            if rentabilidade[i].iloc[-1] == melhor_acao:
                lst_melhor_acao.append(i)
            else:
                pass
        lst_melhor_acao  = ', '.join(lst_melhor_acao )
                
        #print(lst_melhor_acao)

        #pior ação
        #print('pior ação')
        pior_acao = rentabilidade[dropdown_codigos_ativos_data].iloc[-1].min()
        lst_pior_acao = []
        #print('')

        for i in dropdown_codigos_ativos_data:

            if rentabilidade[i].iloc[-1] == pior_acao:
                lst_pior_acao.append(i)
            else:
                pass
        lst_pior_acao  = ', '.join(lst_pior_acao )
                
        #print(lst_pior_acao)


        #melhor setor
        #print('melhor setor')
        melhor_setor = dcx_rentabilidade_setor['rentabilidade'].max()
        lst_melhor_setor = []
        #print(melhor_setor)

        for index, row in dcx_rentabilidade_setor.iterrows():

            if row[1] == melhor_setor:
                lst_melhor_setor.append(row[0])

        lst_melhor_setor  = ', '.join(lst_melhor_setor)

        #print(lst_melhor_setor)


        #pior setor
        #print('pior setor')
        pior_setor = dcx_rentabilidade_setor['rentabilidade'].min()
        lst_pior_setor = []
        #print(pior_setor)

        for index, row in dcx_rentabilidade_setor.iterrows():

            if row[1] == pior_setor:
                lst_pior_setor.append(row[0])

        lst_pior_setor  = ', '.join(lst_pior_setor)

        #print(lst_pior_setor)

  
    
        ########## Grafico_1 HISTÓRICO DO RENDIMENTO DA CARTEIRA
        grafico_1 = go.Figure()

        grafico_1.add_trace(go.Scatter(x=rendimentos.index, y=rendimentos['Carteira'],fill='tozeroy',
            mode='lines', # 'lines' or 'markers'
            #line_color='rgb(52,152,219)',
            name='Carteira',
            ))
        
        grafico_1.update_layout(
            margin=dict(l=50, r=50, t=50, b=50),
            #autosize=False,
            #width=500,
            #height=600,
            paper_bgcolor='rgba(0,0,0,0)', 
            title="HISTÓRICO DO RENDIMENTO DA CARTEIRA:",
            xaxis={'title': 'DATA','fixedrange':True},
            yaxis={'title': 'VALOR (R$)','fixedrange':True}
            
        )

        if rendimento_fim >= rendimento_inicio:
            grafico_1.update_traces(fill='tozeroy',line={'color':success})
        else:
            grafico_1.update_traces(fill='tozeroy',line={'color':danger})

        grafico_1.update_yaxes(
            dict(tickformat=".2f")
        )

        grafico_1.update_xaxes(
        rangeslider_visible=False,
        tickformatstops = [
            dict(dtickrange=[None, None], value="%d/%m/%Y"),
        ]
        )

        ########## Grafico_2 HISTÓRICO DA VALORIZAÇÃO DA CARTEIRA VS APORTES REALIZADOS:
        grafico_2 = go.Figure()

        grafico_2.add_trace(go.Scatter(x=valor.index, y=valor['Carteira'],fill='tozeroy',
            mode='lines', # 'lines' or 'markers'
            line_color=info,
            name='Carteira',
            ))
        
        grafico_2.add_trace(go.Scatter(x=aportes.index, y=aportes['Carteira'],
            mode='lines', # 'lines' or 'markers'
            line_color=warning,
            name='Aportes',
            ))
        
        grafico_2.update_layout(
            margin=dict(l=50, r=50, t=50, b=50),
            #autosize=False,
            #width=500,
            #height=600,
            paper_bgcolor='rgba(0,0,0,0)', 
            title="HISTÓRICO DA VALORIZAÇÃO DA CARTEIRA VS APORTES:",
            xaxis={'title': 'DATA','fixedrange':True},
            yaxis={'title': 'VALOR (R$)','fixedrange':True}
            
        )

        grafico_2.update_yaxes(
            dict(tickformat=".2f")
        )

        grafico_2.update_xaxes(
        rangeslider_visible=False,
        tickformatstops = [
            dict(dtickrange=[None, None], value="%d/%m/%Y"),
        ]
        )

        ########## Grafico_3 RENDIMENTO VS APORTES POR AÇÃO:
        grafico_3 = go.Figure()

        grafico_3.add_trace(go.Bar(
        x = df_setor ['acoes'],
        y =df_setor['aportes'],
        name='Aportes',
        marker = {'color': warning })
        )

        grafico_3.add_trace(go.Bar(
        x = df_setor ['acoes'],
        y =df_setor ['rendimentos'],
        name='Rendimento',
        marker_color=df_setor['color']
        )
        )
        
        
        grafico_3.update_layout(
            margin=dict(l=50, r=50, t=50, b=50),
            paper_bgcolor='rgba(0,0,0,0)', 
            title="APORTES VS RENDIMENTO POR AÇÃO:",
            xaxis={'title': 'AÇÃO','fixedrange':True},
            yaxis={'title': 'VALOR (R$)','fixedrange':True},
            showlegend=False
            
        )

        grafico_3.update_yaxes(
            dict(tickformat=".2f")
        )

        grafico_3.update_xaxes(
        rangeslider_visible=False,
        tickformatstops = [
            dict(dtickrange=[None, None], value="%d/%m/%Y"),
        ]
        )

        ########## Grafico_4 RENTABILIDADE POR AÇÃO:
        grafico_4 = go.Figure()

        
        grafico_4.add_trace(go.Bar(
        x = df_setor ['acoes'],
        y =df_setor['rentabilidade'],
        name='Rentabilidade',
        marker_color=df_setor['color'])
        )
        

        grafico_4.update_layout(
            margin=dict(l=50, r=50, t=50, b=50),
            paper_bgcolor='rgba(0,0,0,0)', 
            title="RENTABILIDADE POR AÇÃO:",
            xaxis={'title': 'AÇÃO','fixedrange':True},
            yaxis={'title': 'PERCENTUAL (%)','fixedrange':True},
            showlegend=False
            
        )

        grafico_4.update_yaxes(
            dict(tickformat=".2f")
        )

        grafico_4.update_xaxes(
        rangeslider_visible=False,
        tickformatstops = [
            dict(dtickrange=[None, None], value="%d/%m/%Y"),
        ]
        )


        ########## Grafico_5 RENTABILIDADE POR SETOR ECONÔMICO:
        grafico_5 = go.Figure()

        
        grafico_5.add_trace(go.Bar(
        x = dcx_rentabilidade_setor ['setor'],
        y =dcx_rentabilidade_setor['rentabilidade'],
        name='Rentabilidade',
        marker_color=dcx_rentabilidade_setor['color'])
        )
        

        grafico_5.update_layout(
            margin=dict(l=50, r=50, t=50, b=50),
            paper_bgcolor='rgba(0,0,0,0)', 
            title="RENTABILIDADE POR SETOR ECONÔMICO:",
            xaxis={'title': 'SETOR','fixedrange':True},
            yaxis={'title': 'PERCENTUAL (%)','fixedrange':True},
            showlegend=False
            
        )

        grafico_5.update_yaxes(
            dict(tickformat=".2f")
        )

        grafico_5.update_xaxes(
        rangeslider_visible=False,
        tickformatstops = [
            dict(dtickrange=[None, None], value="%d/%m/%Y"),
        ]
        )

        ########## Grafico_6 SOMATÓRIO DOS DIVIDENDOS RECEBIDOS POR AÇÃO:
        grafico_6 = go.Figure()

        
        grafico_6.add_trace(go.Bar(
        x = dividendos ['acao'],
        y =dividendos['dividendos'],
        name='Dividendos',
        marker_color=lista_cores_12
        )
        )

        grafico_6.update_layout(
            margin=dict(l=50, r=50, t=50, b=50),
            paper_bgcolor='rgba(0,0,0,0)', 
            title="SOMATÓRIO DOS DIVIDENDOS RECEBIDOS POR AÇÃO:",
            xaxis={'title': 'AÇÃO','fixedrange':True},
            yaxis={'title': 'VALOR (R$)','fixedrange':True},
            showlegend=False
            
        )

        grafico_6.update_yaxes(
            dict(tickformat=".2f")
        )

        grafico_6.update_xaxes(
        rangeslider_visible=False,
        tickformatstops = [
            dict(dtickrange=[None, None], value="%d/%m/%Y"),
        ]
        )

        ########## Grafico_7 HISTÓRICO DA RENDABILIDADE DA CARTEIRA VS BENCHMARK(S)::
        grafico_7 = go.Figure()

        grafico_7.add_trace(go.Scatter(x=rentabilidade.index, y=rentabilidade['Carteira'],fill='tozeroy',
            mode='lines', # 'lines' or 'markers'
            name='Carteira',
            ))
        
        if rentabilidade['Carteira'].iloc[-1] >= 0:
            grafico_7.update_traces(fill='tozeroy',line={'color':success})
        else:
            grafico_7.update_traces(fill='tozeroy',line={'color':danger})
        
        grafico_7.update_layout(
            margin=dict(l=50, r=50, t=50, b=50),
            #autosize=False,
            #width=500,
            #height=600,
            paper_bgcolor='rgba(0,0,0,0)', 
            title="HISTÓRICO DA RENDABILIDADE DA CARTEIRA VS BENCHMARK(S):",
            xaxis={'title': 'DATA','fixedrange':True},
            yaxis={'title': 'PORCENTAGEM (%)','fixedrange':True},
            showlegend=True
            
        )

        grafico_7.update_yaxes(
            dict(tickformat=".2f")
        )

        grafico_7.update_xaxes(
        rangeslider_visible=False,
        tickformatstops = [
            dict(dtickrange=[None, None], value="%d/%m/%Y"),
        ]
        )
        
        for i in dropdown_benchmarks_data:
            
            if i == 'Ibovespa':
                grafico_7.add_trace(go.Scatter(x=rentabilidade_bench.index, y=rentabilidade_bench[i],
                    mode='lines', # 'lines' or 'markers'
                    name='Ibovespa',
                    line_color= cor9,
                    ))

            if i == 'CDI':
                grafico_7.add_trace(go.Scatter(x=rentabilidade_bench.index, y=rentabilidade_bench[i],
                    mode='lines', # 'lines' or 'markers'
                    name='CDI',
                    line_color= cor3,
                    ))
                
            #if i == 'IFIX':
                #grafico_7.add_trace(go.Scatter(x=rentabilidade_bench.index, y=rentabilidade_bench[i],
                    #mode='lines', # 'lines' or 'markers'
                    #name='IFIX',
                    #line_color= cor5,
                    #))
                
            if i == 'Dólar Ptax':
                grafico_7.add_trace(go.Scatter(x=rentabilidade_bench.index, y=rentabilidade_bench[i],
                    mode='lines', # 'lines' or 'markers'
                    name='Dólar Ptax',
                    line_color= cor7,
                    ))
                
            if i == 'Bitcoin':
                grafico_7.add_trace(go.Scatter(x=rentabilidade_bench.index, y=rentabilidade_bench[i],
                    mode='lines', # 'lines' or 'markers'
                    name='Bitcoin',
                    line_color= cor4,
                    ))
            else:

                pass
        

        ########## Grafico_8 HISTÓRICO DA RENDABILIDADE DA CARTEIRA VS BENCHMARK(S)::
        grafico_8 = go.Figure()



        for i in rentabilidade_final ['ativos']:

            print('i')
            print(i)
        
        grafico_8.add_trace(go.Bar(
        x = rentabilidade_final ['ativos'],
        y = rentabilidade_final['rentabilidade'],
        name='Rentabilidade',
        marker_color=rentabilidade_final["color"],
        #marker_pattern_shape="x",
        #marker_line_color="black",
        #color=cor4,
        marker=dict(pattern_fillmode='overlay', line_color=rentabilidade_final["color"],line_width=1 )#, pattern_fillmode="overlay")#line_color=rentabilidade_final["color"],line_width=2
    
        ),
        ),

        print('rentabilidade_final')
        print(rentabilidade_final)
        

        #grafico_8.update_traces(
        #    marker=dict(color="white", line_color="black", pattern_fillmode="replace")
        #),
        
        

        grafico_8.update_layout(
            margin=dict(l=50, r=50, t=50, b=50),
            paper_bgcolor='rgba(0,0,0,0)', 
            title="RENTABILIDADE DA CARTEIRA VS BENCHMARK(S):",
            xaxis={'title': 'ATIVO','fixedrange':True},
            yaxis={'title': 'PORCENTAGEM (%)','fixedrange':True},
            showlegend=False
            
        )

        grafico_8.update_yaxes(
            dict(tickformat=".2f")
        )

        grafico_8.update_xaxes(
        rangeslider_visible=False,
        tickformatstops = [
            dict(dtickrange=[None, None], value="%d/%m/%Y"),
        ]
        )
        

        ########## Relatório

        leg_1 = 'R$ {:.2f}'.format(valor_da_carteira_valor)#.replace(".", ",")

        leg_2 = 'R$ {:.2f}'.format(total_aportado_valor)#.replace(".", ",")

        leg_3 = go.Figure()
        leg_3 = go.Figure(go.Indicator(
            mode="delta",
            value=rendimento_fim,
            delta={'reference': rendimento_inicio, 'valueformat':'.2f', "prefix": " R$ "},
           
            ))

        leg_3.update_traces(delta_font = {'size':16})
        leg_3.update_layout(height=20,paper_bgcolor='rgba(0,0,0,0)', )

        if rendimento_fim >= rendimento_inicio:
            leg_3.update_traces(delta_increasing_color=success)
        elif rendimento_fim < rendimento_inicio:
            leg_3.update_traces(delta_increasing_color=danger)


        leg_4 = go.Figure()
        leg_4 = go.Figure(go.Indicator(
            mode="delta",
            value=rentabilidade_valor,
            delta={'reference': 0, 'valueformat':'.2f', "prefix": " ", "suffix": " %"}
            ))

        leg_4.update_traces(delta_font = {'size':16})
        leg_4.update_layout(height=20,paper_bgcolor='rgba(0,0,0,0)', )

        if rentabilidade_valor >= 0:
            leg_4.update_traces(delta_increasing_color=success)
        elif rentabilidade_valor < 0:
            leg_4.update_traces(delta_increasing_color=danger)


        rmi_txt = '{:.2f} %'.format(rebaixamento_max_inicio)

        emi_txt = '{:.2f} %'.format(elevacao_max_inicio)

        melhor_acao = lst_melhor_acao

        pior_acao = lst_pior_acao


        #print(lst_melhor_acao)

        ########## tabela_rel

        ########## CAGR

        #print(data_inicial)
        #print(data_final)

        vf = 1980.0 #valor final
        vi = 1000 #valor inicial
        t = 6.0

        CAGR = (vf/vi)**(1/t)-1


        
        
        dv_lista=[]
        for i in lista_ativos:

            if i != 'Carteira':

                dv_lista.append(rentabilidade_bench[i].std())

            else:

                dv_lista.append(rendimentos['Carteira'].std())


        df_table = pd.DataFrame([])

        df_table['ATIVO'] = rentabilidade_final['ativos']

        df_table['DESVIO PADRÃO'] = dv_lista
        df_table['DESVIO PADRÃO'] = df_table['DESVIO PADRÃO'].map('{:.2f} %'.format)

        df_table['RENTABILIDADE'] = rentabilidade_final['rentabilidade'].map('{:.2f} %'.format)
        
        


        
        table_rel = html.Div( 
                dbc.Table.from_dataframe(df_table, striped=True, bordered=True, hover=True, style = {'text-align':'center', 'background-color':'#222222'})
                )

            
        #print(rebaixamento_max_inicio) 
        return grafico_1, grafico_2, grafico_3, grafico_4, grafico_5, grafico_6, grafico_7, grafico_8, leg_1, leg_2, leg_3, leg_4, rmi_txt, emi_txt, lst_melhor_acao, lst_pior_acao, lst_melhor_setor, lst_pior_setor
    
    else: 
        raise PreventUpdate


#não exibir cards especificos

@callback(

    [
    Output('row_dividendos', 'style'),
    Output('row_benchmarks_1', 'style'),
    Output('row_benchmarks_2', 'style'),
    ],
    [
    Input ('aportes_data', 'data'),
    Input ('dropdown_benchmarks_data', 'data'),
    ]
)

def cards_especificos(aportes_data, dropdown_benchmarks_data):

    print(aportes_data[3])
    print(dropdown_benchmarks_data)

    style_row_dividendos = {}
    style_row_benchmarks_1 = {}
    style_row_benchmarks_2 = {}


    if aportes_data[3] == '0':

        style_row_dividendos = {"display": "none"}
   
    if dropdown_benchmarks_data == []:

        style_row_benchmarks_1 = {"display": "none"}
        style_row_benchmarks_2 = {"display": "none"}

    else:
        pass
    return style_row_dividendos, style_row_benchmarks_1, style_row_benchmarks_2

