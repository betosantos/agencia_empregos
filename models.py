from db import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'  # Nome fixo, minúsculo
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    

class Vaga(db.Model):
    __tablename__ = 'vagas'  # Nome fixo, minúsculo
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String, nullable=False)
    descricao = db.Column(db.Text, nullable=True)
