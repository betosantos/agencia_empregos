from db import db


class Usuario(db.Model):
    __tablename__ = 'usuario'  # Nome fixo, minúsculo
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    