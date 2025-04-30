from db import db
from flask_login import UserMixin
from datetime import datetime



class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)



class Vaga(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)


class Candidatura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    vaga_id = db.Column(db.Integer, db.ForeignKey('vaga.id'), nullable=False)
    data_candidatura = db.Column(db.DateTime, default=datetime.utcnow)

    usuario = db.relationship('Usuario', backref='candidaturas')
    vaga = db.relationship('Vaga', backref='candidaturas')
