import os
from flask import Flask, render_template, redirect, request, url_for, session, send_file
from .auth import login, logout
from .gerar_pdf import GerarPDf
from datetime import date

app = Flask(__name__)
app.secret_key = "d2e90a70c44d53aae0f1284548aa62a08a9fa786d28fbfb5c0a6c6ea4163acbe"

@app.route("/", methods=["GET", "POST"])
def rota_login():    
  if request.method == "POST":
        usuario, senha = request.form.get("usuario"), request.form.get("senha")
        if login(usuario, senha):
            session["logado"] = True
            session["usuario"] = usuario
            return render_template("index.html")
    
  return render_template("login.html")
  
    
    
@app.route("/logout", methods=["POST", "GET"])
def rota_logout():
    logout()
    session.clear()
    return redirect(url_for("rota_login"))

@app.route("/index")
def index():
    if not session.get("logado"):
        return redirect(url_for("rota_login"))
    
    return render_template("index.html")


@app.route("/gerar-pdf", methods=["GET", "POST"])
def gerar_pdf():
    if not session.get("logado"):
       return redirect(url_for('rota_login'))

    if request.method == "POST":
        pdf = GerarPDf(request.form.get("aluno"))

        ano_serie = request.form.get("ano-serie")
        motivo = request.form.get("motivo")
        professor = request.form.get("professor")
        disciplina = request.form.get("disciplina")
        
        caminho_pdf = pdf.gerar(ano_serie, motivo, professor, disciplina)       
        return send_file(
            caminho_pdf,
            as_attachment=True,
            download_name=os.path.basename(caminho_pdf)
        )

    return render_template("index.html")


if __name__ == "__main__":
      app.run(debug=True, host="0.0.0.0", port=5000)