import pyrebase
import requests
import json
import re
import pandas as pd
import yagmail

def cadastro_firebase(email, password, username):

    #usuario_criado = email_veririficacao_enviado = login_realizado = cadastro_criado = email_ja_verificado = None

    email_verificado = None
    user = None
    error_message = None
    RefreshToken = None
    Token = None

    config = {
        "apiKey": "AIzaSyDT1ZNID1TUzRrxg15g0oRdqKkSdeam9d0",
        "authDomain": "mosaicdownloader.firebaseapp.com",
        "databaseURL": "https://mosaicdownloader-default-rtdb.firebaseio.com",
        "projectId": "mosaicdownloader",
        "storageBucket": "mosaicdownloader.appspot.com",
        "messagingSenderId": "675662442195",
        "appId": "1:675662442195:web:2896f369f400238fbf6e26",
        "measurementId": "G-DDFHB17KY9"
    }

    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    db = firebase.database()

    try:
        user = auth.create_user_with_email_and_password(email, password)
        usuario_criado =  True
        RefreshToken = user['refreshToken']
        Token = user['idToken']

    except requests.exceptions.HTTPError as error:
        error_message = error.args[1]
        error_message = json.loads(error_message)['error']['message']
        print(error_message)
        usuario_criado =  False
        auth = None
        RefreshToken = None
        Token = None
    
    if user is not None:
        try:
            auth.send_email_verification(user['idToken'])
            email_veririficacao_enviado = True

        except requests.exceptions.HTTPError as error:
            error_message = error.args[1]
            error_message = json.loads(error_message)['error']['message']
            print(error_message)
            email_veririficacao_enviado = False
            
            #deletar usuario
            auth.delete_user_account(user['idToken'])
            
    else:
        email_veririficacao_enviado = False
        RefreshToken = None
        Token = None
    
    if user is not None:
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            info = auth.get_account_info(user['idToken'])
            email_verificado = (info['users'][0]['emailVerified'])
            localId = (info['users'][0]['localId'])
            email = (info['users'][0]['email'])

            usuario_autenticado = True
            email_verificado = email_verificado

        except requests.exceptions.HTTPError as error:
            error_message = error.args[1]
            error_message = json.loads(error_message)['error']['message']
            usuario_autenticado = False
            RefreshToken = None
            Token = None

            #deletar usuario
            auth.delete_user_account(user['idToken'])
    else:
        usuario_autenticado = False
    
    if user is not None:
        try: 
            #criando cadastro
            data = {'username': username, 'email': email, 'id': localId, 'emailVerified': email_verificado}
            db.child("users").child(localId).set(data,user['idToken'])
            cadastro_criado= True

        except requests.exceptions.HTTPError as error:
            error_message = error.args[1]
            error_message = json.loads(error_message)['error']['message']
            print(error_message) 
            cadastro_criado = False
            RefreshToken= None
            Token = None

            #deletar usuario
            auth.delete_user_account(user['idToken'])
    else:

        cadastro_criado = False
                
    #print(usuario_criado, email_veririficacao_enviado, login_realizado, cadastro_criado, email_ja_verificado)
    return usuario_criado, email_veririficacao_enviado, usuario_autenticado, cadastro_criado, username, email, email_verificado, error_message, RefreshToken, Token

    #perfil = username[4], email[5], email_verificado[6], RefreshToken[8], Token[9]

def login_firebase (email_login, password_login):

    user = None
    usuario_autenticado = False
    bd_conectado = False
    username = 'visitante'
    email = None
    email_verificado = None
    error_message = None

    RefreshToken = None
    Token = None

    config = {
        "apiKey": "AIzaSyDT1ZNID1TUzRrxg15g0oRdqKkSdeam9d0",
        "authDomain": "mosaicdownloader.firebaseapp.com",
        "databaseURL": "https://mosaicdownloader-default-rtdb.firebaseio.com",
        "projectId": "mosaicdownloader",
        "storageBucket": "mosaicdownloader.appspot.com",
        "messagingSenderId": "675662442195",
        "appId": "1:675662442195:web:2896f369f400238fbf6e26",
        "measurementId": "G-DDFHB17KY9"
    }

    
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    db = firebase.database()
    
    try:
        user = auth.sign_in_with_email_and_password(str(email_login,), str(password_login))
        usuario_autenticado = True
        RefreshToken = user['refreshToken']
        Token = user['idToken']

    except requests.exceptions.HTTPError as error:
        
        usuario_autenticado = False
        error_message = error.args[1]
        error_message = json.loads(error_message)['error']['message']
        print(error_message)
    
    if user is not None:
        try:
            info = auth.get_account_info(user['idToken'])
            bd_conectado = True
            email_verificado = (info['users'][0]['emailVerified'])
            email = (info['users'][0]['email'])

            localId = (info['users'][0]['localId'])
            user_data = db.child("users").child(localId).get(user['idToken'])

            perfil_keys = list(user_data.val().keys())
            perfil_values = list(user_data.val().values())

            perfil_dicionario = dict(zip (perfil_keys, perfil_values))

            username = perfil_dicionario['username']

            
            
        except requests.exceptions.HTTPError as error:
            
            #print('falha na conexão com o banco de dados')
            bd_conectado = False
            error_message = error.args[1]
            error_message = json.loads(error_message)['error']['message']
            print(error_message)
    
        
    return usuario_autenticado, bd_conectado, username, email, email_verificado, RefreshToken, error_message, Token
    #perfil = username[3], email[4], email_verificado[4], RefreshToken[5], Token[7]



def refresh_email (RefreshToken, Token):

    config = {
        "apiKey": "AIzaSyDT1ZNID1TUzRrxg15g0oRdqKkSdeam9d0",
        "authDomain": "mosaicdownloader.firebaseapp.com",
        "databaseURL": "https://mosaicdownloader-default-rtdb.firebaseio.com",
        "projectId": "mosaicdownloader",
        "storageBucket": "mosaicdownloader.appspot.com",
        "messagingSenderId": "675662442195",
        "appId": "1:675662442195:web:2896f369f400238fbf6e26",
        "measurementId": "G-DDFHB17KY9"
    }
    
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    auth = firebase.auth()

    try:
        user = auth.refresh(RefreshToken)

        
        info = auth.get_account_info(Token)
        email_verificado = (info['users'][0]['emailVerified'])
        email = (info['users'][0]['email'])
    

        localId = (info['users'][0]['localId'])
        user_data = db.child("users").child(localId).get(Token)

        perfil_keys = list(user_data.val().keys())
        perfil_values = list(user_data.val().values())

        perfil_dicionario = dict(zip (perfil_keys, perfil_values))

        username = perfil_dicionario['username']

        return username, email, email_verificado, RefreshToken, Token
        
    except requests.exceptions.HTTPError as error:
        print(error)


def refresh_autenticacao (RefreshToken):

    config = {
        "apiKey": "AIzaSyDT1ZNID1TUzRrxg15g0oRdqKkSdeam9d0",
        "authDomain": "mosaicdownloader.firebaseapp.com",
        "databaseURL": "https://mosaicdownloader-default-rtdb.firebaseio.com",
        "projectId": "mosaicdownloader",
        "storageBucket": "mosaicdownloader.appspot.com",
        "messagingSenderId": "675662442195",
        "appId": "1:675662442195:web:2896f369f400238fbf6e26",
        "measurementId": "G-DDFHB17KY9"
    }
    
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()

    try:
        user = auth.refresh(RefreshToken)

        return True
        
    except requests.exceptions.HTTPError as error:
       return False



def reenviar_email_confirmacao (Token):

    config = {
        "apiKey": "AIzaSyDT1ZNID1TUzRrxg15g0oRdqKkSdeam9d0",
        "authDomain": "mosaicdownloader.firebaseapp.com",
        "databaseURL": "https://mosaicdownloader-default-rtdb.firebaseio.com",
        "projectId": "mosaicdownloader",
        "storageBucket": "mosaicdownloader.appspot.com",
        "messagingSenderId": "675662442195",
        "appId": "1:675662442195:web:2896f369f400238fbf6e26",
        "measurementId": "G-DDFHB17KY9"
    }
    
    print('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()


    error_message = None

    try:
        auth.send_email_verification(Token)
        email_veririficacao_enviado = True

    except requests.exceptions.HTTPError as error:
        error_message = error.args[1]
        error_message = json.loads(error_message)['error']['message']
        print(error_message)
        email_veririficacao_enviado = False

    return email_veririficacao_enviado, error_message


def refefinir_senha(email):

    config = {
        "apiKey": "AIzaSyDT1ZNID1TUzRrxg15g0oRdqKkSdeam9d0",
        "authDomain": "mosaicdownloader.firebaseapp.com",
        "databaseURL": "https://mosaicdownloader-default-rtdb.firebaseio.com",
        "projectId": "mosaicdownloader",
        "storageBucket": "mosaicdownloader.appspot.com",
        "messagingSenderId": "675662442195",
        "appId": "1:675662442195:web:2896f369f400238fbf6e26",
        "measurementId": "G-DDFHB17KY9"
    }
    
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()

    error_message = None

    try:

        reenvio = auth.send_password_reset_email(email)
        return True, error_message

    except requests.exceptions.HTTPError as error:
        error_message = error.args[1]
        error_message = json.loads(error_message)['error']['message']
        print(error_message)
        
        return False, error_message


def validar_email(email):

    pat = "^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z\.a-zA-Z]"
   
    if(re.search(pat,email)):  
        return True
          
    else:  
        return False


def validar_senha(senha_1, senha_2):

    pat = "[a-zA-Z0-9,.\-|;!_?]*"
   
    if(re.search(pat,senha_1)) and (re.search(pat,senha_2)):  
        return True
          
    else:  
        return False



###############

#dividendos_cut
def dividendos_cut(codigos_ativos, data_inicial, data_final):

    n = 0
    dividendos = pd.DataFrame([])

    for i in codigos_ativos:
            
        ativos_to_read =  codigos_ativos[0+n]
        try:
        #if pd.read_csv('dados/dividends/'+ ativos_to_read +'.csv'):

            hist_dividendos = pd.read_csv('dados/dividends/'+ ativos_to_read +'.csv')
            hist_dividendos['Date'] = pd.to_datetime(hist_dividendos['Date'])
            hist_dividendos.set_index('Date', inplace=True)
            hist_dividendos = hist_dividendos.rename(columns={'Adj Dividends': ativos_to_read})
            dividendos = pd.concat([dividendos, hist_dividendos], axis=1)
            dividendos = dividendos [data_inicial: data_final]
            
            #print(i, 'print dividendos!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            #print(dividendos)
            #dividendos = dividendos.to_json(orient ='index')
            
        except:
        #else:
            
            #print(i,'não tem dividendos!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            #dividendos = dividendos.to_json(orient ='index')
            pass


        n = n + 1
        
    print( 'p9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999')
    print(dividendos)
    dividendos = dividendos.to_json(orient ='index')
       
    return dividendos


#email
###############

def envio_email(user_name, user_email, assunto, mensagem, tipo_contato, protocolo):

    user_1 = 'backtestportfolio@gmail.com'
    app_password_1 = 'lpcwblwkzfzcrnfm'
    to_1 = 'backtestportfolio.contato@gmail.com'


    subject_1 = 'BP ' + tipo_contato + ' ' + protocolo
    content_1 = [tipo_contato, assunto, protocolo, mensagem, user_name, user_email]

    user_2 = 'backtestportfolio.contato@gmail.com'
    app_password_2 = 'amvjdjjgdqrfnotu '
    to_2 = user_email

    subject_2 = 'BP ' + tipo_contato + ' ' + protocolo
    content_2 = [tipo_contato, assunto, protocolo, mensagem, user_name, user_email]

    retorno_1 = False
    retorno_2 = False

    try:
        with yagmail.SMTP(user_1, app_password_1) as yag:
            yag.send(to_1, subject_1, content_1)
        
        retorno_1 = True

        

    except:

        pass

    if retorno_1 == True:

        try:
            with yagmail.SMTP(user_2, app_password_2) as yag:
                yag.send(to_2, subject_2, content_2)
            
            retorno_2 = True


        except:

            pass

    return retorno_1, retorno_2
