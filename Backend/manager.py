import os
from generate import generate
from create_iptv import save_customer
import pickle
import json
from send import ManangerWa

class create():

    def user(self, client_name, client_cel):

        # Verificar se o arquivo existe
        if os.path.exists("session.pkl"):
            # Remover o arquivo se ele existir
            os.remove("session.pkl")

        # Criar o arquivo executando o comando "python session.py"
        os.system("python session.py")

        # Carregar a sessão do arquivo
        with open('session.pkl', 'rb') as file:
            session = pickle.load(file)

        # Criar uma instância da classe Generate
        generate_instance = generate(session)

        # Gerar usuário e senha
        user = generate_instance.username()
        passw = generate_instance.password()

        # Fazer a requisição para salvar o cliente
        username = f"{user}"
        password = f"{passw}"
        max_connections = 4
        months = 1
        reseller_notes = f"{client_name}"

        result = save_customer(username, password, max_connections, months, reseller_notes)
        print(result)

        result = json.loads(result)
        # Extraindo  o id da string de resposta e armazenando-a
        id_value = result['ajax'][0]['AjaxData'].split('=')[-1]

        # salvando resposta para enviar no whatsapp
        from modal import modal_show
        save_info = modal_show(modal_show,id_value)

        # enviando o modal via whastapp
        manager = ManangerWa()
        manager.send(mensage=save_info, number=f'{client_cel}')
        return 'Usuário Criado'

