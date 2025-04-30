from flask import Flask, render_template, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from dotenv import load_dotenv
import os

from db import db
from models import Usuario, Vaga, Candidatura

# Carrega variáveis do .env
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

# Inicializa banco e login
db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))


@app.route('/')
def index():
    vagas = Vaga.query.all()
    return render_template('index.html', vagas=vagas)

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

@app.route('/vaga/<int:vaga_id>')
def detalhes_vaga(vaga_id):
    vaga = Vaga.query.get_or_404(vaga_id)
    return render_template('detalhes_vaga.html', vaga=vaga)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
