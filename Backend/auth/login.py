import requests
import pickle

class Login:
    def get_session(self):
        # Criar uma sessão
        session = requests.Session()

        # URL e payload do login
        login_url = "https://painel.mastertv.xyz/src/ajax/Login.ajax.php"
        login_payload = {
            "AjaxFile": "Login",
            "AjaxAction": "ExeLogin",
            "username": "raianpbstudio@gmail.com",
            "password": "bm@23"
        }

        # Headers da requisição de login
        login_headers = {
            'authority': 'painel.mastertv.xyz',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://painel.mastertv.xyz',
            'pragma': 'no-cache',
            'referer': 'https://painel.mastertv.xyz/index.php?exe=logoff',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }

        # Fazer a requisição de login
        login_response = session.post(login_url, headers=login_headers, data=login_payload)

        # Verificar se o login foi bem-sucedido
        if login_response.status_code == 200:
            # O cookie será automaticamente armazenado na sessão
            # Você pode fazer outras requisições usando a mesma sessão
            
            # Imprimir o ID da sessão do cookie
            session_id = session.cookies.get('PHPSESSID')
            print("ID da Sessão:", session_id)
        else:
            print("Falha no login")

        return login_response.status_code, session_id, session

    def save_session(self, session, session_file):
        with open(session_file, 'wb') as file:
            pickle.dump(session, file)

    def load_session(self, session_file):
        with open(session_file, 'rb') as file:
            session = pickle.load(file)
        return session
