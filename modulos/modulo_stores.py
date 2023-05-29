#dash
from dash import dcc, html

#plotly

#dash-bootstrap-components

#dash-bootstrap-templates

#dash_mantine_components

#dash-iconify

#modulos

#paginas

#callbacks/layouts

#outros



def create_modulo_stores():
    
    modulo = html.Div(
    [ 
        #cadastro
        dcc.Store(id='dados_perfil', data= ['Visitante', None, None, None, None], storage_type='local'), #'local', or 'session'
        dcc.Store(id='dados_perfil_temp_1', data= ['Visitante', None, None, None, None], storage_type='memory'), #'local', or 'session'
        dcc.Store(id='dados_perfil_temp_2', data= ['Visitante', None, None, None, None], storage_type='memory'), #'local', or 'session'
        dcc.Store(id='dados_perfil_temp_3', data= ['Visitante', None, None, None, None], storage_type='memory'), #'local', or 'session'
        dcc.Store(id='dados_perfil_temp_4', data= ['Visitante', None, None, None, None], storage_type='memory'), #'local', or 'session'
   
        dcc.Store(id='dados_email_verificado', data= False, storage_type='local'), #'local', or 'session'

        dcc.Store(id='dados_refresh', data= ['Visitante', None, None, None, None], storage_type='local'), #'local', or 'session

        dcc.Store(id='dados_path', data= None, storage_type='memory'), #'local', or 'session'
        dcc.Store(id='dados_path_temp_1', data= None, storage_type='memory'), #'local', or 'session'
        dcc.Store(id='dados_path_temp_2', data= None, storage_type='memory'), #'local', or 'session'
        dcc.Store(id='dados_path_temp_3', data= None, storage_type='memory'), #'local', or 'session'
        dcc.Store(id='dados_path_temp_4', data= None, storage_type='memory'), #'local', or 'session'
        dcc.Store(id='dados_path_temp_5', data= None, storage_type='memory'), #'local', or 'session'
        dcc.Store(id='dados_path_temp_6', data= None, storage_type='memory'), #'local', or 'session'

        #preenchimentos

        dcc.Store(id='selected_stocks_data', data=[], storage_type='local'), #'local', or 'session'

        #dropdown_codigos_ativos
        dcc.Store(id='dropdown_codigos_ativos_data', data= [], storage_type='local'), #'local', or 'session'
        
        #dia_inicial, dropdown_mes_inicio, dropdown_ano_inicio, 
        dcc.Store(id='data_inicial_data', data= None, storage_type='local'), #'local', or 'session'
        
        #dia_final, dropdown_mes_fim, dropdown_ano_fim, 
        dcc.Store(id='data_final_data', data= None, storage_type='local'), #'local', or 'session'

        #investimento_inicial, checklist_mensal, valor_aporte_mensal, checklist_dividendos, 
        dcc.Store(id='aportes_data', data= None, storage_type='local'), #'local', or 'session'

        #dropdown_benchmarks
        dcc.Store(id='dropdown_benchmarks_data', data= None, storage_type='local'), #'local', or 'session'

        #checklist_alocado
        dcc.Store(id='checklist_alocado_data', data= None, storage_type='local'), #'local', or 'session'

        #p
        dcc.Store(id='p_data', data= None, storage_type='local'), #'local', or 'session'

        #pb
        dcc.Store(id='pb_data', data= None, storage_type='local'), #'local', or 'session'
    
        #dividendos
        dcc.Store(id='dividendos_data', data= None, storage_type='local'), #'local', or 'session'
    
        
        #exibir_relatorio
        dcc.Store(id='exibir_relatorio', data= 0, storage_type='local'), #'local', or 'session'

        #local
        dcc.Store(id='local', storage_type='local'),

        #disable botao rodar
        dcc.Store(id='disable_rodar', data= False, storage_type='local'),
        dcc.Store(id='disable_rodar_1', data= False, storage_type='memory'),
        dcc.Store(id='disable_rodar_2', data= False, storage_type='memory'),
        dcc.Store(id='disable_rodar_3', data= False, storage_type='memory'),
        dcc.Store(id='disable_rodar_4', data= False, storage_type='memory'),

        #email
        dcc.Store(id='botao_enviar_contato_data', data= False, storage_type='memory'),

        #lgpd
        dcc.Store(id='botao_enviar_lgpd_data', data= False, storage_type='memory'),

   
    ], id = 'modulo_stores'
    )
    
    return modulo