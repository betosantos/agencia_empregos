import os
from flask import Flask, render_template
from db import db
from models import Usuario
from dotenv import load_dotenv

load_dotenv()  # carrega variáveis do .env

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://agencia_empregos_user:QRYDPIqYwF4TF9VgL9Ss8PKGASkN3fsr@dpg-d0abvjp5pdvs73ckhntg-a.oregon-postgres.render.com/agencia_empregos"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)



@app.route('/')
def index():    
    return render_template('index.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
else:
    with app.app_context():
        db.create_all()