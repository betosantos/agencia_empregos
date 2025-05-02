import os
from flask import Flask, render_template
from db import db
from models import Usuario
from dotenv import load_dotenv

load_dotenv()  # carrega variáveis do .env

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)



@app.route('/')
def index():    
    return render_template('index.html')



if __name__ == '__main__':
    with app.app_context():
        #db.drop_all()    # Apaga todas as tabelas
        db.create_all()
        print("Tabelas apagadas e recriadas com sucesso!")
    app.run(debug=True)
else:
    with app.app_context():
        #db.drop_all()    # Apaga todas as tabelas
        db.create_all()
        print("Tabelas apagadas e recriadas com sucesso!")