import pickle

with open('session.pkl', 'rb') as file:
    session = pickle.load(file)


def save_customer(username, password, max_connections, months, reseller_notes) -> str:
        url = "https://painel.mastertv.xyz/src/ajax/Customers.ajax.php"
        headers = {
        'authority': 'painel.mastertv.xyz',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'cookie': f'PHPSESSID={session.cookies.get("PHPSESSID")}',
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
        files=[

        ]
        data = {
        'AjaxFile': 'Customers',
        'AjaxAction': 'save',
        'id': '',
        'type': 'iptv',
        'username': username,
        'password': password,
        'max_connections': max_connections,
        'months': months,
        'bouquet[]': ['1', '2', '3', '4'],  # Adicione todos os valores desejados como elementos da lista
        'reseller_notes': reseller_notes
        }
        print(session.cookies.get("PHPSESSID"))
        response = session.post(url, headers=headers, data=data)
        if response.status_code == 200:
            return response.text
        else:
            return "Falha na solicitação de salvar o cliente"

