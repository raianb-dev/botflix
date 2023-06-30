import requests
import json
import pickle

# Carregar a sessão do arquivo
with open('session.pkl', 'rb') as file:
    session = pickle.load(file)

def modal_show(self, id_value):
    self.id_value = id_value 
    url = "https://painel.mastertv.xyz/src/ajax/Customers.ajax.php"

    payload = f'AjaxFile=Customers&AjaxAction=modalShow&id={id_value}'
    headers = {
        'authority': 'painel.mastertv.xyz',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
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

    response = requests.request("POST", url, headers=headers, data=payload)

    # Extrai as informações desejadas do JSON
    json_data = response.json()
    modal_body = json_data['content']['#ModalBody']
    links = modal_body.split('\n')
    info = {}

    # Verifica cada linha do conteúdo
    for line in links:
        if line.startswith("*Link:") or line.startswith("*Link2:"):
            link_type, link = line.split(":")[0].strip(), line.split(":")[1].strip()
            info[link_type] = link
        elif line.startswith("*Usuário:"):
            info["Usuário"] = line.split(":")[1].strip()
        elif line.startswith("*Senha:"):
            info["Senha"] = line.split(":")[1].strip()

    # Constrói a resposta formatada
    response_text = f"Usuário: {info['Usuário']}\nSenha: {info['Senha']}\n\nXCIPTV:\nURL: http://dns.mastertv.xyz\nUsuário: {info['Usuário']}\nSenha: {info['Senha']}\n\nIPTV SMARTERS:\nUsuário: {info['Usuário']}\nSenha: {info['Senha']}\nURL: http://ddsw.xyz:80\n\nDNS V2 STB / SmartUp: 162.212.156.184\nDNS V3 STB / SmartUp: 162.212.156.139\nUsuário: {info['Usuário']}\nSenha: {info['Senha']}\n\nWEBPLAYER:\nLink: {info.get('Link', '')}\nLink2: {info.get('Link2', '')}\nUsuário: {info['Usuário']}\nSenha: {info['Senha']}\n\nLinks encurtados:\nhttp://e.mastertv.xyz/I620P9\nhttp://e.mastertv.xyz/Xp4ogD\nhttp://e.mastertv.xyz/oPpblp"

    return response_text
