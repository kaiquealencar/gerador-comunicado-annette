from flask import   session, flash, get_flashed_messages

USUARIO = "annette"
SENHA = "irma@annette"

def login(usuario, senha):
    if usuario == USUARIO and senha == SENHA:
        session["logado"] = True
        return True
    else:
        flash("Usuário ou senha incorretos!", "danger")
        return False
        
def logout():
    session.pop("logado", None)
    