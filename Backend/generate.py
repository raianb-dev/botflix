import json

class generate():
    def __init__(self, session):
        self.session = session

    # Gerar username/ usernumber
    def username(self) -> str:
        url = "https://painel.mastertv.xyz/src/ajax/Customers.ajax.php"
        payload = {
            "input": "username",
            "AjaxFile": "Customers",
            "AjaxAction": "changeUserOrPass"
        }
        headers = {
            'authority': 'painel.mastertv.xyz',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': f'PHPSESSID={self.session.cookies.get("PHPSESSID")}',
            'dnt': '1',
            'origin': 'https://painel.mastertv.xyz',
            'pragma': 'no-cache',
            'referer': 'https://painel.mastertv.xyz/panel.php?page=customers/form',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }

        response = self.session.post(url, headers=headers, data=payload)

        if response.status_code == 200:
            response_data = json.loads(response.text)  # Obtenha o conteúdo da resposta como texto
            pwd = response_data['form']['#CustomerForm']['username']
            print("Gerando usuário")
            return pwd
        else:
            return "Falha na solicitação de username"

    # Gerar password
    def password(self) -> str:
        url = "https://painel.mastertv.xyz/src/ajax/Customers.ajax.php"
        payload = {
            "input": "password",
            "AjaxFile": "Customers",
            "AjaxAction": "changeUserOrPass"
        }
        headers = {
            'authority': 'painel.mastertv.xyz',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': f'PHPSESSID={self.session.cookies.get("PHPSESSID")}',
            'dnt': '1',
            'origin': 'https://painel.mastertv.xyz',
            'pragma': 'no-cache',
            'referer': 'https://painel.mastertv.xyz/panel.php?page=customers/form',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }

        response = self.session.post(url, headers=headers, data=payload)

        if response.status_code == 200:
            response_data = json.loads(response.text)  # Obtenha o conteúdo da resposta como texto
            pwd = response_data['form']['#CustomerForm']['password']
            print("Gerando senha")
            return pwd
        else:
            return "Falha na solicitação de password"
