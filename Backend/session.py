from auth.login import Login

# Criar uma instância da classe Login
login = Login()

# Verificar se a sessão já existe em um arquivo
session_file = 'session.pkl'
try:
    session = login.load_session(session_file)
    print("Sessão carregada do arquivo.")
except FileNotFoundError:
    # Obter uma nova sessão
    status_code, session_id, session = login.get_session()
    login.save_session(session, session_file)
    print("Nova sessão criada e salva no arquivo.")

# Continuar usando a sessão para outras requisições...
