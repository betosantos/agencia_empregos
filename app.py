from flask import Flask, render_template, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from dotenv import load_dotenv
import os

from db import db
from models import Usuario, Vaga, Candidatura

# Carrega variáveis do .env
load_dotenv()

app = Flask(__name__)

# Inicializa banco e login
db.init_app(app)


@app.route('/')
def index():    
    return render_template('index.html')

@app.route('/login')
def login():
    usuario = Usuario.query.first()
    login_user(usuario)
    flash("Login realizado com sucesso!", "success")
    return redirect(url_for('index'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout efetuado com sucesso!", "info")
    return redirect(url_for('index'))



if __name__ == '__main__':    
    app.run(debug=True)
